import express from 'express';
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const app = express();
const PORT = 3000;

const SITE_DIR = fs.existsSync('/home/z/my-project/download/loja-do-cabo-site')
  ? '/home/z/my-project/download/loja-do-cabo-site'
  : path.join(__dirname, 'public');

const ZIP_PATH = fs.existsSync('/home/z/my-project/download/loja-do-cabo-site.zip')
  ? '/home/z/my-project/download/loja-do-cabo-site.zip'
  : path.join(__dirname, 'public', 'loja-do-cabo-site.zip');

// Direct download route for the Netlify deployment ZIP
app.get(['/loja-do-cabo-site.zip', '/download/loja-do-cabo-site.zip'], (_req, res) => {
  if (fs.existsSync(ZIP_PATH)) {
    res.setHeader('Content-Type', 'application/zip');
    res.setHeader('Content-Disposition', 'attachment; filename="loja-do-cabo-site.zip"');
    return res.sendFile(ZIP_PATH);
  }
  res.status(404).send('ZIP file not found');
});

// Serve HTML pages with a convenient floating ZIP download widget in preview mode
app.use((req, res, next) => {
  if (req.method !== 'GET') return next();
  const cleanPath = req.path.split('?')[0];
  let candidate = '';
  if (cleanPath.endsWith('/')) {
    candidate = path.join(SITE_DIR, cleanPath, 'index.html');
  } else if (cleanPath.endsWith('.html')) {
    candidate = path.join(SITE_DIR, cleanPath);
  } else if (!path.extname(cleanPath)) {
    const dirIndex = path.join(SITE_DIR, cleanPath, 'index.html');
    if (fs.existsSync(dirIndex)) {
      candidate = dirIndex;
    }
  }

  if (candidate && fs.existsSync(candidate)) {
    let html = fs.readFileSync(candidate, 'utf-8');
    const downloadBar = `
  <!-- Preview Download Floating Button -->
  <div id="netlify-zip-bar" style="position:fixed;bottom:16px;right:16px;z-index:9999;background:#12131C;border:1px solid rgba(245,185,66,0.45);border-radius:12px;padding:10px 16px;box-shadow:0 12px 30px rgba(0,0,0,0.65);display:flex;align-items:center;gap:12px;font-family:'Outfit',sans-serif;">
    <a href="/loja-do-cabo-site.zip" download="loja-do-cabo-site.zip" style="background:linear-gradient(135deg,#F5B942,#FF8A00);color:#0B0B10;font-weight:700;font-size:13px;padding:8px 14px;border-radius:8px;text-decoration:none;white-space:nowrap;">
      Baixar loja-do-cabo-site.zip (Netlify)
    </a>
    <button onclick="document.getElementById('netlify-zip-bar').remove()" aria-label="Fechar barra de download" style="background:transparent;border:none;color:#858A9E;cursor:pointer;font-size:16px;line-height:1;padding:4px;">×</button>
  </div>`;
    if (html.includes('</body>')) {
      html = html.replace('</body>', `${downloadBar}\n</body>`);
    }
    res.setHeader('Content-Type', 'text/html; charset=utf-8');
    return res.status(200).send(html);
  }
  next();
});

// Serve static assets (img/*.webp, img/*.png, sitemap.xml, robots.txt, etc.)
app.use(express.static(SITE_DIR));
app.use(express.static(path.join(__dirname, 'public')));

app.listen(PORT, '0.0.0.0', () => {
  console.log(`Loja do Cabo static server running at http://0.0.0.0:${PORT}`);
});
