import type { APIRoute, GetStaticPaths } from 'astro';
import { getCollection } from 'astro:content';
import satori from 'satori';
import { Resvg } from '@resvg/resvg-js';
import { readFileSync } from 'node:fs';
import { join } from 'node:path';

let fontRegular: Buffer | undefined;
let fontBold: Buffer | undefined;
let fontCyrillicRegular: Buffer | undefined;
let fontCyrillicBold: Buffer | undefined;

function getFont(pkg: string, filename: string): Buffer {
  return readFileSync(join(process.cwd(), `node_modules/@fontsource/${pkg}/files`, filename));
}

export const getStaticPaths: GetStaticPaths = async () => {
  const posts = await getCollection('posts');
  return posts.map(post => {
    const [cat, locale, slug] = post.id.split('/');
    return {
      params: { slug: `${locale}/${cat}/${slug}` },
      props: { post },
    };
  });
};

const W = 1200;
const H = 630;
const PAD = 56;

export const GET: APIRoute = async ({ props }) => {
  fontRegular        ??= getFont('space-mono',      'space-mono-latin-400-normal.woff');
  fontBold           ??= getFont('space-mono',      'space-mono-latin-700-normal.woff');
  fontCyrillicRegular ??= getFont('noto-sans-mono', 'noto-sans-mono-cyrillic-400-normal.woff');
  fontCyrillicBold    ??= getFont('noto-sans-mono', 'noto-sans-mono-cyrillic-700-normal.woff');

  const { post } = props;

  const rawLines = (post.body ?? '')
    .split('\n')
    .map((l: string) => (l.length > 88 ? l.slice(0, 85) + '…' : l));

  // Drop leading blank lines
  while (rawLines.length > 0 && rawLines[0].trim() === '') rawLines.shift();
  const lines = rawLines.slice(0, 18);

  const lineNodes = (lines.length > 0 ? lines : [post.data.description]).map(
    (line: string) => ({
      type: 'div',
      props: {
        style: {
          display: 'flex',
          color: /^#{1,3}\s/.test(line)
            ? '#ede9dc'
            : line.startsWith('```') || line.startsWith('---')
            ? '#555'
            : '#888',
          fontWeight: /^#{1,3}\s/.test(line) ? 700 : 400,
          fontSize: 14,
          lineHeight: 1.65,
        },
        children: line || '\u00a0',
      },
    })
  );

  const tree = {
    type: 'div',
    props: {
      style: {
        display: 'flex',
        flexDirection: 'column',
        width: W,
        height: H,
        backgroundColor: '#1c1c1a',
        padding: `${PAD}px`,
        fontFamily: '"Space Mono", "Noto Mono"',
      },
      children: [
        // {
        //   type: 'div',
        //   props: {
        //     style: {
        //       display: 'flex',
        //       fontSize: 12,
        //       color: '#444',
        //       letterSpacing: '0.08em',
        //       marginBottom: 28,
        //     },
        //     children: 'python sucks >_',
        //   },
        // },
        // {
        //   type: 'div',
        //   props: {
        //     style: {
        //       display: 'flex',
        //       fontSize: 26,
        //       fontWeight: 700,
        //       color: '#ede9dc',
        //       lineHeight: 1.2,
        //       letterSpacing: '-0.01em',
        //       marginBottom: 28,
        //     },
        //     children: post.data.title,
        //   },
        // },
        {
          type: 'div',
          props: {
            style: {
              display: 'flex',
              flexDirection: 'column',
              flex: 1,
              borderTop: '1px solid #2e2e2a',
              paddingTop: 24,
              overflow: 'hidden',
            },
            children: lineNodes,
          },
        },
      ],
    },
  };

  const svg = await satori(tree as Parameters<typeof satori>[0], {
    width: W,
    height: H,
    fonts: [
      { name: 'Space Mono', data: fontRegular,         weight: 400, style: 'normal' },
      { name: 'Space Mono', data: fontBold,             weight: 700, style: 'normal' },
      { name: 'Noto Mono',  data: fontCyrillicRegular!, weight: 400, style: 'normal' },
      { name: 'Noto Mono',  data: fontCyrillicBold!,    weight: 700, style: 'normal' },
    ],
  });

  const png = new Resvg(svg, { fitTo: { mode: 'width', value: W } })
    .render()
    .asPng();

  return new Response(png, {
    headers: { 'Content-Type': 'image/png' },
  });
};
