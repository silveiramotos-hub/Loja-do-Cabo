import fs from 'fs';
import path from 'path';
import test from 'node:test';
import assert from 'node:assert/strict';

const SITE_DIR = '/home/z/my-project/download/loja-do-cabo-site';
const ZIP_PATH = '/home/z/my-project/download/loja-do-cabo-site.zip';

const EXPECTED_HTML_PATHS = [
  'index.html',
  'blog/index.html',
  'tada-power/index.html',
  'tadamaxx/index.html',
  'erectus-plus/index.html',
  'erectus-retard/index.html',
  'erectus-caps-turbo/index.html',
  'madeirada/index.html',
  'testosterona-natural-mitos-e-verdades/index.html',
  'respiracao-para-durar-mais-na-cama/index.html',
  'exercicios-de-kegel-masculino/index.html',
  'minerais-para-potencia-masculina/index.html',
  'aminoacidos-para-erecao/index.html',
  'alimentos-vasodilatadores-para-erecao/index.html',
  'combinacao-de-valeriana-e-damiana-controle-da-ejaculacao-precoce/index.html',
  'como-usar-pomada-anestesica-para-ejaculacao-precoce/index.html',
  'quanto-tempo-dura-uma-relacao-normal/index.html',
];

test('All 17 HTML routes and ZIP archive exist', () => {
  assert.equal(fs.existsSync(ZIP_PATH), true, 'loja-do-cabo-site.zip must exist');
  assert.ok(fs.statSync(ZIP_PATH).size > 200000, 'ZIP should be populated');

  for (const rel of EXPECTED_HTML_PATHS) {
    const full = path.join(SITE_DIR, rel);
    assert.equal(fs.existsSync(full), true, `Missing HTML file: ${rel}`);
  }
});

test('Hero uses lifestyle couple image, 0 Express/10-caps kits, and Braip checkouts + official sites exist', () => {
  const home = fs.readFileSync(path.join(SITE_DIR, 'index.html'), 'utf-8');
  assert.ok(home.includes('/img/hero-casal-estilo-vida.webp'), 'Hero must use lifestyle couple WebP image');
  assert.ok(home.includes('/img/hero-casal-estilo-vida.png'), 'Hero must use lifestyle couple PNG fallback');

  // Official external sites
  assert.ok(home.includes('https://tadapower.com.br/'));
  assert.ok(home.includes('https://tadamaxx.com/'));
  assert.ok(home.includes('https://erectusplus.com.br/'));
  assert.ok(home.includes('https://erectusturbo.com/'));
  assert.ok(home.includes('https://madeirada.com.br/'));

  // Official Braip checkout links
  const expectedBraipLinks = [
    'https://ev.braip.com/checkout/plapredn/che14zvv',
    'https://ev.braip.com/checkout/plalvlxe/chepmkvz',
    'https://ev.braip.com/checkout/pla48l1v/chedd8lj',
    'https://ev.braip.com/checkout/plagyn2m/che16g1v',
    'https://ev.braip.com/checkout/plalv6lk/cheejgxk',
    'https://ev.braip.com/checkout/pla04zqy/ched6vg7',
  ];
  for (const braip of expectedBraipLinks) {
    assert.ok(home.includes(braip), `Home missing Braip checkout: ${braip}`);
  }

  // Zero 10-capsule Express kits in any HTML file
  for (const rel of EXPECTED_HTML_PATHS) {
    const content = fs.readFileSync(path.join(SITE_DIR, rel), 'utf-8');
    assert.equal(/10\s*c[áa]psulas/i.test(content), false, `${rel} still mentions 10 cápsulas`);
    assert.equal(/(?:\(Express\)|TadaMaxx\s+Express|Madeirada\s+Express|Kit\s+Express)/i.test(content), false, `${rel} still mentions Express kit`);
  }
});

test('Meta Pixel, google-site-verification, WebP <picture> and 0 Chinese chars in all HTML files', () => {
  const cjkRegex = /[\u4e00-\u9fff\u3400-\u4dbf\u3040-\u30ff\uac00-\ud7af]/;

  for (const rel of EXPECTED_HTML_PATHS) {
    const content = fs.readFileSync(path.join(SITE_DIR, rel), 'utf-8');

    assert.ok(content.includes("fbq('init', 'SEU_PIXEL_ID')"), `${rel} missing fbq init`);
    assert.ok(content.includes("fbq('track', 'PageView')"), `${rel} missing PageView`);
    assert.ok(content.includes('a[href*="wa.me"]'), `${rel} missing wa.me selector`);
    assert.ok(content.includes("fbq('track', 'Contact')"), `${rel} missing Contact event`);
    assert.ok(content.includes("fbq('track', 'InitiateCheckout')"), `${rel} missing InitiateCheckout event`);
    assert.ok(content.includes('name="google-site-verification"'), `${rel} missing google-site-verification`);
    assert.ok(content.includes('<picture>'), `${rel} missing <picture> tag`);
    assert.ok(content.includes('type="image/webp"'), `${rel} missing image/webp source`);
    assert.ok(content.includes('loading="lazy"'), `${rel} missing loading="lazy"`);
    assert.ok(content.includes('/testosterona-natural-mitos-e-verdades/'), `${rel} missing link to testosterona post`);
    assert.ok(content.includes('/respiracao-para-durar-mais-na-cama/'), `${rel} missing link to respiracao post`);
    assert.equal(cjkRegex.test(content), false, `${rel} contains unexpected CJK characters`);
  }
});

test('JSON-LD Store on Home, Product on 6 products, FAQPage on 9 blog articles', () => {
  const home = fs.readFileSync(path.join(SITE_DIR, 'index.html'), 'utf-8');
  assert.ok(home.includes('"@type": "Store"'));
  assert.ok(home.includes('+5571983821218'));

  const products = ['tada-power', 'tadamaxx', 'erectus-plus', 'erectus-retard', 'erectus-caps-turbo', 'madeirada'];
  for (const p of products) {
    const html = fs.readFileSync(path.join(SITE_DIR, p, 'index.html'), 'utf-8');
    assert.ok(html.includes('"@type": "Product"'), `${p} missing Product JSON-LD`);
    assert.ok(html.includes('"priceCurrency": "BRL"'), `${p} missing BRL currency`);
    assert.ok(html.includes('"price": "PRECO_AQUI"'), `${p} missing PRECO_AQUI placeholder`);
    assert.ok(html.includes('https://schema.org/InStock'), `${p} missing InStock`);
    assert.ok(html.includes('https://ev.braip.com/checkout/'), `${p} missing Braip checkout link`);
  }

  const articles = EXPECTED_HTML_PATHS.slice(8);
  assert.equal(articles.length, 9);
  for (const a of articles) {
    const html = fs.readFileSync(path.join(SITE_DIR, a), 'utf-8');
    assert.ok(html.includes('"@type": "FAQPage"'), `${a} missing FAQPage JSON-LD`);
  }
});

test('sitemap.xml and robots.txt are valid and complete', () => {
  const sitemap = fs.readFileSync(path.join(SITE_DIR, 'sitemap.xml'), 'utf-8');
  assert.ok(sitemap.includes('https://lojadocabo.com/'));
  assert.ok(sitemap.includes('https://lojadocabo.com/blog/'));
  assert.ok(sitemap.includes('https://lojadocabo.com/testosterona-natural-mitos-e-verdades/'));
  assert.ok(sitemap.includes('https://lojadocabo.com/respiracao-para-durar-mais-na-cama/'));
  const locCount = (sitemap.match(/<loc>/g) || []).length;
  assert.equal(locCount, 17, 'sitemap.xml must contain all 17 canonical URLs');

  const robots = fs.readFileSync(path.join(SITE_DIR, 'robots.txt'), 'utf-8');
  assert.ok(robots.includes('User-agent: *'));
  assert.ok(robots.includes('Allow: /'));
  assert.ok(robots.includes('Sitemap: https://lojadocabo.com/sitemap.xml'));
});
