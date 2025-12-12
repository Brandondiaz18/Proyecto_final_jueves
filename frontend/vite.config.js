import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";
import fs from "fs";
import path from "path";

// Fix para Vercel: forzar permisos de ejecución en vite.js
try {
  const vitePath = path.resolve("node_modules/vite/bin/vite.js");
  fs.chmodSync(vitePath, 0o755);
  console.log("✓ Permisos corregidos para vite.js");
} catch (err) {
  console.warn("⚠ No se pudo corregir permisos vite.js (esto es normal si se ejecuta localmente)");
}

export default defineConfig({
  plugins: [react()],
});
