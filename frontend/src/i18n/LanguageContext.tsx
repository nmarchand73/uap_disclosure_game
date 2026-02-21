import { createContext, useContext, useState, useCallback, useEffect, type ReactNode } from "react";
import { getStoredLang, setStoredLang, t, type Lang } from "./strings";

type LanguageContextValue = {
  lang: Lang;
  setLang: (l: Lang) => void;
  t: (key: string) => string;
};

const LanguageContext = createContext<LanguageContextValue | null>(null);

export function LanguageProvider({ children }: { children: ReactNode }) {
  const [lang, setLangState] = useState<Lang>(getStoredLang);

  const setLang = useCallback((l: Lang) => {
    setStoredLang(l);
    setLangState(l);
  }, []);

  useEffect(() => {
    setLangState(getStoredLang());
  }, []);

  const value: LanguageContextValue = {
    lang,
    setLang,
    t: (key: string) => t(lang, key),
  };

  return <LanguageContext.Provider value={value}>{children}</LanguageContext.Provider>;
}

export function useLanguage(): LanguageContextValue {
  const ctx = useContext(LanguageContext);
  if (!ctx) throw new Error("useLanguage must be used within LanguageProvider");
  return ctx;
}
