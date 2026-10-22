import rss from '@astrojs/rss';
import {getCollection} from 'astro:content';
import early from '../data/early-access.json';

export async function GET(context) {
  const posts = await getCollection('posts');
  const publishedSlugs = new Set(posts.map(p => p.id.replace(/\.(md|mdx)$/, '')));
  const locked = early.filter(item => !publishedSlugs.has(item.slug) && new Date(item.releaseAt).getTime() > Date.now());
  const items = [
    ...posts.map(p => ({
      title: p.data.title,
      description: p.data.description,
      pubDate: p.data.date,
      link: `/grein/${p.id.replace(/\.(md|mdx)$/, '')}/`
    })),
    ...locked.map(item => ({
      title: item.title,
      description: item.description || item.title,
      pubDate: new Date(new Date(item.releaseAt).getTime() - 30 * 24 * 60 * 60 * 1000),
      link: `/grein/${item.slug}/`,
      customData: '<media:content xmlns:media="http://search.yahoo.com/mrss/" url="https://sosialistur.info/patreon-preview.png" medium="image" type="image/png" />'
    }))
  ].sort((a, b) => b.pubDate - a.pubDate);
  return rss({title:'Sosialisturin',description:'Føroysk tíðindi, greining og ástøði.',site:context.site,items});
}
