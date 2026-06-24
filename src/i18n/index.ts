import ru from './ru';
import en from './en';

const dict = { ru, en };

export type Locale = 'ru' | 'en';

export function useTranslations(locale: Locale) {
  return function t(key: keyof typeof ru): string {
    return dict[locale]?.[key] ?? ru[key];
  };
}
