# Sosialisturin

Føroysk tíðinda- og ástøðisútgáva bygd við Astro.

## Menning

```bash
npm install
npm run dev
```

## Innihald

Greinar liggja í `src/content/posts/` sum Markdown. Frontmatter stýrir heiti, lýsing, dagfesting, kategori, høvundi, miðlaslóð og øðrum. Kategorier: `Tíðindi`, `Ástøði`, `Video`, `Ljóð`.

## Útgáva

GitHub Actions byggir og sendir síðuna til GitHub Pages, tá broytingar verða lagdar á `main`. Í repository settings skal **Pages → Source** vera **GitHub Actions**.
