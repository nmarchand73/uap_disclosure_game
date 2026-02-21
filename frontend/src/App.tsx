import { BrowserRouter, Routes, Route } from "react-router-dom";
import { LanguageProvider } from "./i18n/LanguageContext";
import Lobby from "./features/lobby/Lobby";
import Game from "./features/game/Game";

const routerFuture = {
  v7_startTransition: true,
  v7_relativeSplatPath: true,
} as const;

function App() {
  return (
    <LanguageProvider>
      <BrowserRouter future={routerFuture}>
        <Routes>
          <Route path="/" element={<Lobby />} />
          <Route path="/game/:gameId" element={<Game />} />
        </Routes>
      </BrowserRouter>
    </LanguageProvider>
  );
}

export default App;
