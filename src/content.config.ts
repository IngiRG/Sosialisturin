import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';
const posts=defineCollection({loader:glob({pattern:'**/*.{md,mdx}',base:'./src/content/posts'}),schema:z.object({title:z.string(),description:z.string(),date:z.coerce.date(),category:z.enum(['Tíðindi','Ástøði','Poddvarp']),section:z.string().optional(),author:z.string().default('Sosialisturin'),featured:z.boolean().default(false),image:z.string().optional(),mediaUrl:z.string().optional(),duration:z.string().optional(),tags:z.array(z.string()).default([])})});
export const collections={posts};