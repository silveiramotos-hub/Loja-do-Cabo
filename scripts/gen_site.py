#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Master generator for Loja do Cabo static website (lojadocabo.com).
Builds:
- /index.html (Store JSON-LD, lifestyle couple Hero image, 6 products with Braip checkouts & official sites, blog highlights)
- 6 product pages (/tada-power/, /tadamaxx/, /erectus-plus/, /erectus-retard/, /erectus-caps-turbo/, /madeirada/)
  with Product JSON-LD (priceCurrency BRL, price PRECO_AQUI, InStock), Braip checkouts (no 10-caps Express), and official site links
- /blog/index.html with all 9 articles
- 9 blog article pages (including the 2 new posts from Task 3) with FAQPage JSON-LD
- /sitemap.xml (home, /blog/, 6 products, 9 articles)
- /robots.txt
- Packages /home/z/my-project/download/loja-do-cabo-site.zip and copies to /app/applet/public/
"""

import os
import json
import shutil
import zipfile
from typing import Dict, Any

from post_template import (
    SITE_DOMAIN,
    WHATSAPP_NUMBER,
    WHATSAPP_DISPLAY,
    INSTAGRAM_URL,
    PRODUCTS,
    BLOG_ARTICLES,
    META_PIXEL_HEAD,
    META_PIXEL_BODY_END,
    SHARED_CSS,
    picture_tag,
    render_header,
    render_footer,
)
from gen_new_posts import build_testosterona_post, build_respiracao_post
from gen_existing_posts import build_existing_posts


def build_home_page() -> str:
    store_jsonld = json.dumps(
        {
            "@context": "https://schema.org",
            "@type": "Store",
            "name": "Loja do Cabo",
            "legalName": "Loja do Cabo Ltda",
            "description": "Loja especializada em suplementos naturais e fórmulas avançadas para desempenho, potência e vitalidade masculina no Brasil.",
            "url": f"{SITE_DOMAIN}/",
            "telephone": f"+{WHATSAPP_NUMBER}",
            "image": f"{SITE_DOMAIN}/img/logo-loja-do-cabo.png",
            "priceRange": "$$",
            "address": {
                "@type": "PostalAddress",
                "addressLocality": "Salvador",
                "addressRegion": "BA",
                "addressCountry": "BR"
            },
            "sameAs": [
                INSTAGRAM_URL
            ]
        },
        ensure_ascii=False,
        indent=2
    )

    wa_hero = f"https://wa.me/{WHATSAPP_NUMBER}?text=Ol%C3%A1%21%20Vim%20pelo%20site%20da%20Loja%20do%20Cabo%20e%20quero%20uma%20indica%C3%A7%C3%A3o%20para%20o%20meu%20perfil."

    product_cards = []
    for p in PRODUCTS:
        pic = picture_tag(p["img"], f"{p['name']} - Loja do Cabo", width=p["width"], height=p["height"], lazy=True)
        kit_buttons = "\n".join(
            f"""              <a href="{k['url']}" target="_blank" rel="noopener" class="btn-kit-braip btn-buy" data-checkout="true">
                <span>{k['label']}</span>
                <span class="kit-cta">Comprar na Braip →</span>
              </a>"""
            for k in p["kits"]
        )
        product_cards.append(f"""        <article class="surface-card">
          <div>
            <a href="/{p['slug']}/" class="product-img-wrap" aria-label="Ver detalhes do {p['name']}">
              {pic}
            </a>
            <div class="meta-line" style="margin-bottom: 8px;">
              <span>{p["badge"]}</span>
              <span class="meta-sep">·</span>
              <span>Frete Grátis</span>
            </div>
            <h3 style="font-size: 1.4rem; font-weight: 800; margin-bottom: 6px;">
              <a href="/{p['slug']}/">{p["name"]}</a>
            </h3>
            <p style="color: var(--gold-start); font-size: 0.9rem; font-weight: 600; margin-bottom: 10px;">
              {p["tagline"]}
            </p>
            <p style="color: var(--text-secondary); font-size: 0.9rem; margin-bottom: 12px;">
              {p["subtitle"]}
            </p>
            <p style="color: var(--text-muted); font-size: 0.8125rem; margin-bottom: 14px;">
              <strong style="color: var(--text-primary);">Fórmula:</strong> {p["formula"]}
            </p>
            <div class="kit-list" aria-label="Checkouts Braip do {p['name']}">
{kit_buttons}
            </div>
          </div>
          <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin-top: 8px;">
            <a href="{p['external_url']}" target="_blank" rel="noopener" class="btn-gold btn-buy" data-checkout="true" style="padding: 10px 12px; font-size: 0.84rem;">
              Site Oficial ↗
            </a>
            <a href="/{p['slug']}/" class="btn-outline" style="padding: 10px 12px; font-size: 0.84rem;">
              Ver Ficha →
            </a>
          </div>
        </article>""")

    products_html = "\n".join(product_cards)

    # Show top 6 blog articles on home (starting with the 2 new ones)
    blog_cards = []
    for a in BLOG_ARTICLES[:6]:
        blog_cards.append(f"""        <article class="surface-card">
          <div>
            <div class="meta-line" style="margin-bottom: 10px;">
              <span>{a["category"]}</span>
              <span class="meta-sep">·</span>
              <span>{a["read_time"]}</span>
            </div>
            <h3 style="font-size: 1.15rem; font-weight: 700; margin-bottom: 10px;">
              <a href="/{a['slug']}/">{a["title"]}</a>
            </h3>
            <p style="color: var(--text-secondary); font-size: 0.9rem; margin-bottom: 18px;">
              {a["excerpt"]}
            </p>
          </div>
          <a href="/{a['slug']}/" style="color: var(--gold-start); font-weight: 600; font-size: 0.9rem;">
            Ler guia completo →
          </a>
        </article>""")
    blog_html = "\n".join(blog_cards)

    # Hero image: Couple / Lifestyle / Vitality instead of TadaMaxx bottle
    hero_pic = picture_tag(
        "hero-casal-estilo-vida",
        "Casal em sintonia — Qualidade de vida, vitalidade e desempenho masculino com a Loja do Cabo",
        width=800,
        height=600,
        lazy=False,
        img_class="hero-lifestyle-img"
    )
    discreta_pic = picture_tag("embalagem-discreta", "Embalagem 100% Discreta Loja do Cabo", width=343, height=374, lazy=True)
    garantia_pic = picture_tag("garantia-30-dias", "Garantia de Qualidade Loja do Cabo", width=375, height=375, lazy=True)

    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Loja do Cabo — Suplementos Naturais para Desempenho e Potência Masculina</title>
  <meta name="description" content="Potência, firmeza e controle masculino em cada fase da vida. Conheça Tada Power, TadaMaxx, Erectus Plus, Erectus Retard, Erectus Caps Turbo e Madeirada com frete grátis." />
  <link rel="canonical" href="{SITE_DOMAIN}/" />
  <meta property="og:type" content="website" />
  <meta property="og:title" content="Loja do Cabo — Suplementos Naturais para Desempenho Masculino" />
  <meta property="og:description" content="Fórmulas exclusivas para vigor, ereção firme e controle ejaculatório. Envio 100% discreto e frete grátis para todo o Brasil." />
  <meta property="og:url" content="{SITE_DOMAIN}/" />
  <meta property="og:site_name" content="Loja do Cabo" />
  <meta property="og:image" content="{SITE_DOMAIN}/img/hero-casal-estilo-vida.png" />
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="Loja do Cabo — Potência e Vitalidade Masculina" />
  <meta name="twitter:description" content="Fórmulas exclusivas para vigor, ereção firme e controle ejaculatório com frete grátis." />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Outfit:wght@600;700;800&display=swap" rel="stylesheet" />
  <script type="application/ld+json">
{store_jsonld}
  </script>
{META_PIXEL_HEAD}
  <style>
{SHARED_CSS}
    .hero-section {{
      padding: 64px 0 72px;
      border-bottom: 1px solid var(--border-subtle);
      background: radial-gradient(circle at 80% 20%, rgba(245, 185, 66, 0.08), transparent 45%);
    }}
    .hero-grid {{
      display: grid;
      grid-template-columns: 1.2fr 1fr;
      gap: 48px;
      align-items: center;
    }}
    .hero-headline {{
      font-size: clamp(2.25rem, 4.2vw, 3.6rem);
      font-weight: 800;
      margin-bottom: 20px;
      color: var(--text-primary);
    }}
    .hero-accent {{
      background: linear-gradient(135deg, var(--gold-start), var(--gold-end));
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }}
    .hero-lifestyle-card {{
      background: var(--bg-surface);
      border: 1px solid var(--border-gold);
      border-radius: 18px;
      padding: 16px;
      overflow: hidden;
    }}
    .hero-lifestyle-img {{
      width: 100%;
      height: auto;
      aspect-ratio: 4 / 3;
      object-fit: cover;
      border-radius: 12px;
      margin-bottom: 14px;
    }}
    .kpi-strip {{
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 20px;
      margin-top: 48px;
      padding-top: 32px;
      border-top: 1px solid var(--border-subtle);
    }}
    .kpi-item strong {{
      display: block;
      font-family: 'Outfit', sans-serif;
      font-size: 1.5rem;
      font-weight: 800;
      color: var(--gold-start);
      font-variant-numeric: tabular-nums;
    }}
    .kpi-item span {{
      font-size: 0.85rem;
      color: var(--text-secondary);
    }}
    @media (max-width: 960px) {{
      .hero-grid {{ grid-template-columns: 1fr; }}
      .kpi-strip {{ grid-template-columns: repeat(2, 1fr); }}
    }}
  </style>
</head>
<body>
{render_header()}
  <main>
    <section class="hero-section">
      <div class="container">
        <div class="hero-grid">
          <div>
            <span class="kicker">LOJA DO CABO LTDA · QUALIDADE DE VIDA E CONFIANÇA MASCULINA</span>
            <h1 class="hero-headline">
              Potência, Firmeza e <span class="hero-accent">Vigor Masculino</span> para Cada Fase da Vida
            </h1>
            <p style="font-size: 1.125rem; color: var(--text-secondary); margin-bottom: 28px; max-width: 62ch;">
              Fórmulas exclusivas em cápsulas desenvolvidas sob medida para jovens, adultos de 40+, 50+ e 60+ que buscam ereções firmes,
              controle do tempo na cama e sintonia plena na vida a dois. Compra 100% segura via <strong>Braip</strong> com <strong>Frete Grátis</strong> e embalagem discreta.
            </p>
            <div style="display: flex; flex-wrap: wrap; gap: 14px;">
              <a href="#catalogo" class="btn-gold">
                Escolher Meu Suplemento
              </a>
              <a href="{wa_hero}" target="_blank" rel="noopener" class="btn-whatsapp">
                Atendimento Sigiloso ({WHATSAPP_DISPLAY})
              </a>
            </div>
          </div>
          <div class="hero-lifestyle-card">
            {hero_pic}
            <p class="meta-line" style="justify-content: center;">
              <span>Sintonia & Vitalidade</span>
              <span class="meta-sep">·</span>
              <span>Checkout Seguro Braip</span>
              <span class="meta-sep">·</span>
              <span>Sigilo Total</span>
            </p>
          </div>
        </div>

        <div class="kpi-strip">
          <div class="kpi-item">
            <strong>6 Fórmulas</strong>
            <span>Dosagens específicas de 3 mg a 20 mg + ativos naturais</span>
          </div>
          <div class="kpi-item">
            <strong>Até 36 Horas</strong>
            <span>Janela de resposta ativa com firmeza e segurança</span>
          </div>
          <div class="kpi-item">
            <strong>100% Discreto</strong>
            <span>Caixa parda sem identificação externa de conteúdo</span>
          </div>
          <div class="kpi-item">
            <strong>Frete Grátis</strong>
            <span>Entrega rastreada para todos os estados do Brasil</span>
          </div>
        </div>
      </div>
    </section>

    <section id="catalogo" style="padding: 72px 0; border-bottom: 1px solid var(--border-subtle);">
      <div class="container">
        <div style="max-width: 760px; margin-bottom: 44px;">
          <span class="kicker">CATÁLOGO OFICIAL E CHECKOUTS BRAIP</span>
          <h2 style="font-size: clamp(1.8rem, 3vw, 2.5rem); font-weight: 800; margin-bottom: 12px;">
            Escolha Seu Tratamento (30, 60, 90 ou 120 Cápsulas)
          </h2>
          <p style="color: var(--text-secondary);">
            Clique diretamente no kit desejado para ir ao checkout oficial da Braip com frete grátis, ou acesse o site oficial de cada produto.
          </p>
        </div>

        <div class="grid-3">
{products_html}
        </div>
      </div>
    </section>

    <section style="padding: 72px 0; border-bottom: 1px solid var(--border-subtle);">
      <div class="container">
        <div class="grid-2" style="align-items: center;">
          <div>
            <span class="kicker">COMPRA SEGURA NA BRAIP E ENVIO SIGILOSO</span>
            <h2 style="font-size: clamp(1.75rem, 2.8vw, 2.3rem); font-weight: 800; margin-bottom: 16px;">
              Discrição Absoluta da Saída do Estoque Até as Suas Mãos
            </h2>
            <p style="color: var(--text-secondary); margin-bottom: 18px;">
              Sabemos que a sua privacidade vem em primeiro lugar. Todos os pedidos realizados nos checkouts oficiais da Braip são despachados
              em caixas pardas lacradas, sem logotipos chamativos e sem qualquer menção a suplementos sexuais na etiqueta de transporte.
            </p>
            <ul style="color: var(--text-secondary); padding-left: 20px; display: grid; gap: 10px; margin-bottom: 24px;">
              <li><strong>Checkout 100% Seguro na Braip</strong> (Pix, Cartão em até 12x ou Boleto);</li>
              <li><strong>Frete Grátis para todo o Brasil</strong> em todos os kits de 30, 60, 90 e 120 cápsulas;</li>
              <li><strong>Atendimento humano e direto</strong> pelo WhatsApp oficial {WHATSAPP_DISPLAY};</li>
              <li><strong>Garantia de satisfação e autenticidade</strong> direto da Loja do Cabo Ltda.</li>
            </ul>
            <a href="{wa_hero}" target="_blank" rel="noopener" class="btn-whatsapp">
              Falar com Especialista no WhatsApp
            </a>
          </div>
          <div class="grid-2" style="gap: 20px;">
            <div class="surface-card" style="align-items: center; text-align: center;">
              <div style="max-width: 180px; margin: 0 auto 14px;">
                {discreta_pic}
              </div>
              <h3 style="font-size: 1.05rem; font-weight: 700; margin-bottom: 6px;">Embalagem 100% Discreta</h3>
              <p style="font-size: 0.85rem; color: var(--text-secondary);">Ninguém sabe o que tem dentro do pacote além de você.</p>
            </div>
            <div class="surface-card" style="align-items: center; text-align: center;">
              <div style="max-width: 180px; margin: 0 auto 14px;">
                {garantia_pic}
              </div>
              <h3 style="font-size: 1.05rem; font-weight: 700; margin-bottom: 6px;">Qualidade Garantida</h3>
              <p style="font-size: 0.85rem; color: var(--text-secondary);">Fórmulas originais Loja do Cabo Ltda com checkout oficial Braip.</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section style="padding: 72px 0;">
      <div class="container">
        <div style="display: flex; flex-wrap: wrap; justify-content: space-between; align-items: flex-end; gap: 20px; margin-bottom: 40px;">
          <div>
            <span class="kicker">CONTEÚDO CIENTÍFICO E PRÁTICO</span>
            <h2 style="font-size: clamp(1.8rem, 3vw, 2.4rem); font-weight: 800;">
              Últimos Guias do Blog Loja do Cabo
            </h2>
          </div>
          <a href="/blog/" class="btn-outline">Ver Todos os 9 Artigos →</a>
        </div>
        <div class="grid-3">
{blog_html}
        </div>
      </div>
    </section>
  </main>
{render_footer()}
{META_PIXEL_BODY_END}
</body>
</html>
"""


def build_product_page(product: Dict[str, Any]) -> str:
    slug = product["slug"]
    canonical = f"{SITE_DOMAIN}/{slug}/"
    prod_jsonld = json.dumps(
        {
            "@context": "https://schema.org",
            "@type": "Product",
            "name": product["name"],
            "description": product["subtitle"],
            "image": [
                f"{SITE_DOMAIN}/img/{product['img']}.png",
                f"{SITE_DOMAIN}/img/{product['img']}.webp"
            ],
            "brand": {
                "@type": "Brand",
                "name": "Loja do Cabo"
            },
            "offers": {
                "@type": "Offer",
                "url": product["default_checkout_url"],
                "priceCurrency": "BRL",
                "price": "PRECO_AQUI",
                "availability": "https://schema.org/InStock",
                "seller": {
                    "@type": "Organization",
                    "name": "Loja do Cabo Ltda"
                }
            }
        },
        ensure_ascii=False,
        indent=2
    )

    hero_pic = picture_tag(
        product["img"],
        f"{product['name']} - Suplemento Masculino Loja do Cabo",
        width=product["width"],
        height=product["height"],
        lazy=False
    )

    highlights_html = "\n".join(
        f'              <li><strong>✓</strong> {h}</li>'
        for h in product["highlights"]
    )

    caps_cards = []
    for k in product["kits"]:
        caps_cards.append(f"""          <div class="surface-card" style="padding: 24px;">
            <div>
              <span class="kicker">CHECKOUT OFICIAL BRAIP · FRETE GRÁTIS</span>
              <h3 style="font-size: 1.3rem; font-weight: 800; margin-bottom: 6px;">{product["name"]} — {k["caps"]}</h3>
              <p style="font-family: 'Outfit', sans-serif; font-size: 1.45rem; font-weight: 800; color: var(--gold-start); margin-bottom: 10px; font-variant-numeric: tabular-nums;">
                {k["price"]}
              </p>
              <p style="font-size: 0.875rem; color: var(--text-secondary); margin-bottom: 18px;">
                Pagamento 100% seguro via Braip (Pix, Cartão ou Boleto) + Envio imediato em embalagem discreta.
              </p>
            </div>
            <a href="{k['url']}" target="_blank" rel="noopener" class="btn-gold btn-buy" data-checkout="true" style="width: 100%;">
              Comprar {k["caps"]} na Braip →
            </a>
          </div>""")
    caps_html = "\n".join(caps_cards)

    faq_html = "\n".join(
        f"""        <div class="faq-item">
          <h3 class="faq-q">{item["q"]}</h3>
          <p class="faq-a">{item["a"]}</p>
        </div>"""
        for item in product["faq"]
    )

    other_products = [p for p in PRODUCTS if p["slug"] != slug][:3]
    other_html = "\n".join(
        f"""        <article class="surface-card">
          <div>
            <a href="/{op['slug']}/" class="product-img-wrap">
              {picture_tag(op['img'], op['name'], width=op['width'], height=op['height'], lazy=True)}
            </a>
            <h3 style="font-size: 1.2rem; font-weight: 700; margin-bottom: 6px;"><a href="/{op['slug']}/">{op["name"]}</a></h3>
            <p style="color: var(--text-secondary); font-size: 0.88rem; margin-bottom: 16px;">{op["subtitle"]}</p>
          </div>
          <div style="display: grid; gap: 8px;">
            <a href="{op['default_checkout_url']}" target="_blank" rel="noopener" class="btn-gold btn-buy" data-checkout="true" style="width: 100%; padding: 10px 14px; font-size: 0.88rem;">Comprar na Braip →</a>
            <a href="/{op['slug']}/" class="btn-outline" style="width: 100%; padding: 9px 14px; font-size: 0.85rem;">Conhecer {op["name"]}</a>
          </div>
        </article>"""
        for op in other_products
    )

    wa_main = f"https://wa.me/{WHATSAPP_NUMBER}?text=Ol%C3%A1%21%20Estou%20na%20p%C3%A1gina%20do%20{product['name']}%20e%20tenho%20uma%20d%C3%BAvida."

    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{product["name"]} — {product["tagline"]} | Loja do Cabo</title>
  <meta name="description" content="{product['subtitle']} Compre {product['name']} original no checkout oficial da Braip com frete grátis e envio discreto." />
  <link rel="canonical" href="{canonical}" />
  <meta property="og:type" content="product" />
  <meta property="og:title" content="{product['name']} — {product['tagline']} | Loja do Cabo" />
  <meta property="og:description" content="{product['subtitle']}" />
  <meta property="og:url" content="{canonical}" />
  <meta property="og:site_name" content="Loja do Cabo" />
  <meta property="og:image" content="{SITE_DOMAIN}/img/{product['img']}.png" />
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="{product['name']} | Loja do Cabo" />
  <meta name="twitter:description" content="{product['subtitle']}" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Outfit:wght@600;700;800&display=swap" rel="stylesheet" />
  <script type="application/ld+json">
{prod_jsonld}
  </script>
{META_PIXEL_HEAD}
  <style>
{SHARED_CSS}
    .pdp-grid {{
      display: grid;
      grid-template-columns: 0.95fr 1.15fr;
      gap: 48px;
      align-items: start;
      padding: 56px 0;
      border-bottom: 1px solid var(--border-subtle);
    }}
    .pdp-highlights {{
      list-style: none;
      display: grid;
      gap: 10px;
      margin: 22px 0 28px;
      color: var(--text-secondary);
    }}
    .pdp-highlights strong {{ color: var(--gold-start); margin-right: 6px; }}
    @media (max-width: 900px) {{
      .pdp-grid {{ grid-template-columns: 1fr; }}
    }}
  </style>
</head>
<body>
{render_header()}
  <main class="container">
    <section class="pdp-grid">
      <div class="surface-card" style="padding: 28px; align-items: center;">
        <div style="max-width: 440px; width: 100%; margin: 0 auto;">
          {hero_pic}
        </div>
      </div>
      <div>
        <div class="meta-line" style="margin-bottom: 10px;">
          <a href="/" style="color: var(--gold-start);">Catálogo Loja do Cabo</a>
          <span class="meta-sep">·</span>
          <span>{product["badge"]}</span>
          <span class="meta-sep">·</span>
          <span>Checkout Oficial Braip</span>
        </div>
        <h1 style="font-size: clamp(2.1rem, 3.8vw, 3rem); font-weight: 800; margin-bottom: 10px;">
          {product["name"]}
        </h1>
        <p style="font-size: 1.2rem; color: var(--gold-start); font-weight: 700; margin-bottom: 16px;">
          {product["tagline"]}
        </p>
        <p style="color: var(--text-secondary); font-size: 1.02rem; margin-bottom: 18px;">
          {product["description_long"]}
        </p>

        <div class="tip-box" style="margin: 20px 0;">
          <span class="tip-box-title">Composição e Indicação Principal</span>
          <p style="font-size: 0.92rem; color: var(--text-secondary); margin-bottom: 6px;">
            <strong>Fórmula Ativa:</strong> {product["formula"]}
          </p>
          <p style="font-size: 0.92rem; color: var(--text-secondary); margin-bottom: 0;">
            <strong>Indicação:</strong> {product["indication"]}
          </p>
        </div>

        <ul class="pdp-highlights">
{highlights_html}
        </ul>

        <div style="display: flex; flex-wrap: wrap; gap: 12px; margin-bottom: 16px;">
          <a href="#apresentacoes" class="btn-gold">
            Escolher Kit e Comprar na Braip
          </a>
          <a href="{product['external_url']}" target="_blank" rel="noopener" class="btn-outline">
            Visitar Site Oficial ({product["name"]}) ↗
          </a>
          <a href="{wa_main}" target="_blank" rel="noopener" class="btn-whatsapp">
            Tirar Dúvidas ({WHATSAPP_DISPLAY})
          </a>
        </div>
        <p class="meta-line">
          <span>Frete Grátis Brasil</span>
          <span class="meta-sep">·</span>
          <span>Embalagem Discreta</span>
          <span class="meta-sep">·</span>
          <span>Pagamento Seguro Braip</span>
        </p>
      </div>
    </section>

    <section id="apresentacoes" style="padding: 56px 0; border-bottom: 1px solid var(--border-subtle);">
      <span class="kicker">CHECKOUT OFICIAL BRAIP</span>
      <h2 style="font-size: 1.85rem; font-weight: 800; margin-bottom: 12px;">
        Escolha o Seu Tratamento {product["name"]} com Frete Grátis
      </h2>
      <p style="color: var(--text-secondary); margin-bottom: 28px;">
        Clique no kit desejado abaixo para ir diretamente ao checkout seguro da Braip:
      </p>
      <div class="grid-3">
{caps_html}
      </div>
    </section>

    <section style="padding: 56px 0; border-bottom: 1px solid var(--border-subtle);">
      <div class="grid-2">
        <div>
          <span class="kicker">MODO DE USO SEGURO</span>
          <h2 style="font-size: 1.65rem; font-weight: 800; margin-bottom: 14px;">Como Utilizar o {product["name"]}</h2>
          <p style="color: var(--text-secondary); margin-bottom: 16px;">
            {product["how_to_use"]}
          </p>
          <p style="color: var(--text-secondary);">
            Para potencializar ainda mais seus resultados a longo prazo, confira nossos guias gratuitos sobre
            <a href="/testosterona-natural-mitos-e-verdades/" style="color: var(--gold-start); text-decoration: underline;">testosterona natural</a>,
            <a href="/respiracao-para-durar-mais-na-cama/" style="color: var(--gold-start); text-decoration: underline;">técnicas de respiração</a> e
            <a href="/exercicios-de-kegel-masculino/" style="color: var(--gold-start); text-decoration: underline;">exercícios de Kegel masculino</a>.
          </p>
        </div>
        <div>
          <span class="kicker">DÚVIDAS FREQUENTES</span>
          <h2 style="font-size: 1.65rem; font-weight: 800; margin-bottom: 14px;">Perguntas Sobre o {product["name"]}</h2>
          <div>
{faq_html}
          </div>
        </div>
      </div>
    </section>

    <section style="padding: 56px 0;">
      <h2 style="font-size: 1.65rem; font-weight: 800; margin-bottom: 24px;">Outras Fórmulas da Loja do Cabo</h2>
      <div class="grid-3">
{other_html}
      </div>
    </section>
  </main>
{render_footer()}
{META_PIXEL_BODY_END}
</body>
</html>
"""


def build_blog_index() -> str:
    canonical = f"{SITE_DOMAIN}/blog/"
    cards = []
    for a in BLOG_ARTICLES:
        prod = next((p for p in PRODUCTS if p["slug"] == a["cta_product_slug"]), PRODUCTS[0])
        pic = picture_tag(prod["img"], a["title"], width=prod["width"], height=prod["height"], lazy=True)
        new_label = ' <span class="meta-sep">·</span> <strong style="color: var(--gold-start);">Novo</strong>' if a.get("is_new") else ""
        cards.append(f"""        <article class="surface-card">
          <div>
            <a href="/{a['slug']}/" class="product-img-wrap" style="aspect-ratio: 16 / 10; margin-bottom: 18px;">
              {pic}
            </a>
            <div class="meta-line" style="margin-bottom: 10px;">
              <span>{a["category"]}</span>
              <span class="meta-sep">·</span>
              <span>{a["read_time"]}</span>{new_label}
            </div>
            <h2 style="font-size: 1.22rem; font-weight: 700; margin-bottom: 10px;">
              <a href="/{a['slug']}/">{a["title"]}</a>
            </h2>
            <p style="color: var(--text-secondary); font-size: 0.9rem; margin-bottom: 18px;">
              {a["excerpt"]}
            </p>
          </div>
          <a href="/{a['slug']}/" style="color: var(--gold-start); font-weight: 600; font-size: 0.92rem;">
            Ler artigo completo →
          </a>
        </article>""")

    cards_html = "\n".join(cards)

    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Blog Loja do Cabo — Guias de Desempenho, Testosterona e Saúde Masculina</title>
  <meta name="description" content="Artigos científicos e práticos sobre testosterona natural, técnicas de respiração para durar mais, exercícios de Kegel, minerais, aminoácidos e vigor masculino." />
  <link rel="canonical" href="{canonical}" />
  <meta property="og:type" content="website" />
  <meta property="og:title" content="Blog Loja do Cabo — Saúde e Desempenho Masculino" />
  <meta property="og:description" content="Confira nossos 9 guias completos sobre potência, controle ejaculatório, nutrição vasodilatadora e saúde hormonal." />
  <meta property="og:url" content="{canonical}" />
  <meta property="og:site_name" content="Loja do Cabo" />
  <meta property="og:image" content="{SITE_DOMAIN}/img/logo-loja-do-cabo.png" />
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="Blog Loja do Cabo — Saúde e Desempenho Masculino" />
  <meta name="twitter:description" content="9 guias completos sobre potência, controle ejaculatório e saúde hormonal." />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Outfit:wght@600;700;800&display=swap" rel="stylesheet" />
{META_PIXEL_HEAD}
  <style>{SHARED_CSS}</style>
</head>
<body>
{render_header()}
  <main class="container" style="padding-top: 56px;">
    <header style="max-width: 760px; margin-bottom: 48px;">
      <span class="kicker">CENTRAL DE CONHECIMENTO MASCULINO · 9 ARTIGOS COMPLETOS</span>
      <h1 style="font-size: clamp(2.1rem, 3.8vw, 3rem); font-weight: 800; margin-bottom: 14px;">
        Blog Loja do Cabo: Ciência e Prática para o Seu Desempenho
      </h1>
      <p style="font-size: 1.1rem; color: var(--text-secondary);">
        Explore nossos 9 guias aprofundados sobre fisiologia da ereção, controle da ejaculação precoce, respiração diafragmática,
        testosterona natural, minerais e aminoácidos vasodilatadores.
      </p>
    </header>

    <section class="grid-3">
{cards_html}
    </section>
  </main>
{render_footer()}
{META_PIXEL_BODY_END}
</body>
</html>
"""


def build_sitemap_xml() -> str:
    urls = [
        (f"{SITE_DOMAIN}/", "1.0", "weekly"),
        (f"{SITE_DOMAIN}/blog/", "0.9", "weekly"),
    ]
    for p in PRODUCTS:
        urls.append((f"{SITE_DOMAIN}/{p['slug']}/", "0.9", "weekly"))
    for a in BLOG_ARTICLES:
        urls.append((f"{SITE_DOMAIN}/{a['slug']}/", "0.8", "monthly"))

    entries = "\n".join(
        f"""  <url>
    <loc>{loc}</loc>
    <lastmod>2026-10-25</lastmod>
    <changefreq>{freq}</changefreq>
    <priority>{prio}</priority>
  </url>"""
        for loc, prio, freq in urls
    )
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{entries}
</urlset>
"""


def build_robots_txt() -> str:
    return f"""User-agent: *
Allow: /
Sitemap: {SITE_DOMAIN}/sitemap.xml
"""


def generate_all(output_root: str) -> None:
    os.makedirs(output_root, exist_ok=True)

    # Remove any old zip inside site_dir before re-archiving
    old_inner_zip = os.path.join(output_root, "loja-do-cabo-site.zip")
    if os.path.exists(old_inner_zip):
        os.remove(old_inner_zip)

    # 1. Home
    with open(os.path.join(output_root, "index.html"), "w", encoding="utf-8") as f:
        f.write(build_home_page())

    # 2. 6 Products
    for p in PRODUCTS:
        p_dir = os.path.join(output_root, p["slug"])
        os.makedirs(p_dir, exist_ok=True)
        with open(os.path.join(p_dir, "index.html"), "w", encoding="utf-8") as f:
            f.write(build_product_page(p))

    # 3. Blog index
    blog_dir = os.path.join(output_root, "blog")
    os.makedirs(blog_dir, exist_ok=True)
    with open(os.path.join(blog_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(build_blog_index())

    # 4. 2 New Blog Articles (Task 3)
    t_dir = os.path.join(output_root, "testosterona-natural-mitos-e-verdades")
    os.makedirs(t_dir, exist_ok=True)
    with open(os.path.join(t_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(build_testosterona_post())

    r_dir = os.path.join(output_root, "respiracao-para-durar-mais-na-cama")
    os.makedirs(r_dir, exist_ok=True)
    with open(os.path.join(r_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(build_respiracao_post())

    # 5. 7 Existing Blog Articles
    existing = build_existing_posts()
    for slug, html in existing.items():
        a_dir = os.path.join(output_root, slug)
        os.makedirs(a_dir, exist_ok=True)
        with open(os.path.join(a_dir, "index.html"), "w", encoding="utf-8") as f:
            f.write(html)

    # 6. sitemap.xml & robots.txt
    with open(os.path.join(output_root, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write(build_sitemap_xml())

    with open(os.path.join(output_root, "robots.txt"), "w", encoding="utf-8") as f:
        f.write(build_robots_txt())


if __name__ == "__main__":
    site_dir = "/home/z/my-project/download/loja-do-cabo-site"
    generate_all(site_dir)

    # Copy scripts into site_dir/scripts as well
    scripts_dst = os.path.join(site_dir, "scripts")
    os.makedirs(scripts_dst, exist_ok=True)
    for fn in ["post_template.py", "gen_new_posts.py", "gen_existing_posts.py", "gen_site.py"]:
        src_p = os.path.join("/app/applet/scripts", fn)
        if os.path.exists(src_p):
            shutil.copy2(src_p, os.path.join(scripts_dst, fn))

    # Sync entire site_dir to /app/applet/public/
    pub_dir = "/app/applet/public"
    os.makedirs(pub_dir, exist_ok=True)
    for item in os.listdir(site_dir):
        if item in ("scripts", "loja-do-cabo-site.zip"):
            continue
        s = os.path.join(site_dir, item)
        d = os.path.join(pub_dir, item)
        if os.path.isdir(s):
            if os.path.exists(d):
                shutil.rmtree(d)
            shutil.copytree(s, d)
        else:
            shutil.copy2(s, d)

    # Create ZIP archive at /home/z/my-project/download/loja-do-cabo-site.zip and /app/applet/public/loja-do-cabo-site.zip
    zip_path = "/home/z/my-project/download/loja-do-cabo-site.zip"
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for root, dirs, files in os.walk(site_dir):
            if "scripts" in dirs:
                dirs.remove("scripts")
            for file in sorted(files):
                if file.endswith(".zip"):
                    continue
                full_p = os.path.join(root, file)
                rel_p = os.path.relpath(full_p, site_dir)
                zf.write(full_p, rel_p)

    shutil.copy2(zip_path, os.path.join(pub_dir, "loja-do-cabo-site.zip"))
    print(f"Generated site in {site_dir} and packaged {zip_path} ({os.path.getsize(zip_path)} bytes).")
