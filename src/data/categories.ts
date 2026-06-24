export const CATEGORIES: Record<string, Record<string, string>> = {
  'python-inside': {
    ru: 'Внутри Python',
    en: 'Inside Python',
  },
};

export function getCategoryLabel(slug: string | null | undefined, locale = 'ru'): string {
  if (!slug) return locale === 'ru' ? 'Без категории' : 'Uncategorized';
  return CATEGORIES[slug]?.[locale] ?? CATEGORIES[slug]?.ru ?? slug;
}

export function getPostCategory(postId: string): string | null {
  const i = postId.indexOf('/');
  return i !== -1 ? postId.slice(0, i) : null;
}
