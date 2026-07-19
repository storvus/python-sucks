import { getCollection } from 'astro:content'

export const CATEGORIES: Record<string, Record<string, string>> = {
  'python-inside': {
    ru: 'Внутри Python',
    en: 'Inside Python',
  },
  'learn-python': {
    ru: 'Учим Python',
    en: 'Learn Python',
  },
};

const HIDDEN_CATEGORIES = [
  'gists'
]

export function getCategoryLabel(slug: string | null | undefined, locale = 'ru'): string {
  if (!slug) return locale === 'ru' ? 'Без категории' : 'Uncategorized';
  return CATEGORIES[slug]?.[locale] ?? CATEGORIES[slug]?.ru ?? slug;
}

export function getPostCategory(postId: string): string | null {
  const i = postId.indexOf('/');
  return i !== -1 ? postId.slice(0, i) : null;
}

export async function getVisiblePosts(locale: string) {
  return (await getCollection('posts'))
    .filter(p => p.id.split('/')[1] === locale && !HIDDEN_CATEGORIES.includes(getPostCategory(p.id)))
    .sort((a, b) => b.data.pubDate.valueOf() - a.data.pubDate.valueOf());
}
