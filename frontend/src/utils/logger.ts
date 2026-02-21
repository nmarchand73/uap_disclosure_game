/**
 * App logger: level-based console output with optional context.
 * In production, debug logs are no-op unless VITE_LOG_LEVEL=debug.
 */
const LOG_LEVELS = ["debug", "info", "warn", "error"] as const;
type LogLevel = (typeof LOG_LEVELS)[number];

const envLevel = (import.meta.env.VITE_LOG_LEVEL as string)?.toLowerCase() ?? "";
const defaultLevel: LogLevel = import.meta.env.DEV ? "debug" : "info";
const effectiveLevel = LOG_LEVELS.includes(envLevel as LogLevel) ? (envLevel as LogLevel) : defaultLevel;
const minLevelIndex = LOG_LEVELS.indexOf(effectiveLevel);

function shouldLog(level: LogLevel): boolean {
  const idx = LOG_LEVELS.indexOf(level);
  return idx >= 0 && idx >= minLevelIndex;
}

function timestamp(): string {
  const now = new Date();
  return now.toTimeString().slice(0, 8);
}

function formatMessage(level: string, message: string, context?: Record<string, unknown>): string {
  const prefix = `[${timestamp()}] [${level.toUpperCase()}]`;
  if (context && Object.keys(context).length > 0) {
    try {
      return `${prefix} ${message} ${JSON.stringify(context)}`;
    } catch {
      return `${prefix} ${message}`;
    }
  }
  return `${prefix} ${message}`;
}

function createLogger(namespace: string) {
  return {
    debug(message: string, context?: Record<string, unknown>): void {
      if (!shouldLog("debug")) return;
      const msg = formatMessage("debug", `[${namespace}] ${message}`, context);
      console.debug(msg);
    },
    info(message: string, context?: Record<string, unknown>): void {
      if (!shouldLog("info")) return;
      const msg = formatMessage("info", `[${namespace}] ${message}`, context);
      console.info(msg);
    },
    warn(message: string, context?: Record<string, unknown>): void {
      if (!shouldLog("warn")) return;
      const msg = formatMessage("warn", `[${namespace}] ${message}`, context);
      console.warn(msg);
    },
    error(message: string, context?: Record<string, unknown>): void {
      if (!shouldLog("error")) return;
      const msg = formatMessage("error", `[${namespace}] ${message}`, context);
      console.error(msg);
    },
  };
}

export type AppLogger = ReturnType<typeof createLogger>;

export function getLogger(namespace: string): AppLogger {
  return createLogger(namespace);
}

export const logger = getLogger("app");
