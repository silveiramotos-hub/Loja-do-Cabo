#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Shared template and components for Loja do Cabo static site (lojadocabo.com).
Includes dark-luxury styling (#0B0B10, gold gradient #F5B942 -> #FF8A00, Outfit/Inter),
Meta Pixel (PageView, Contact on wa.me, InitiateCheckout on Braip/buy buttons),
google-site-verification placeholder, JSON-LD generators, <picture> WebP+PNG helper,
official Braip checkout links (30/60/90/120 capsules — no 10-capsule Express kits),
official external product websites, and shared navigation/footer with all 6 products and 9 blog articles.
"""

import json
from typing import List, Dict, Any

SITE_DOMAIN = "https://lojadocabo.com"
WHATSAPP_NUMBER = "5571983821218"
WHATSAPP_DISPLAY = "(71) 98382-1218"
INSTAGRAM_URL = "https://www.instagram.com/loja.do.cabo.ltda/"
INSTAGRAM_HANDLE = "@loja.do.cabo.ltda"

PRODUCTS: List[Dict[str, Any]] = [
    {
        "slug": "tada-power",
        "name": "Tada Power",
        "external_url": "https://tadapower.com.br/",
        "tagline": "Energia, Confiança e Desempenho Seguro",
        "subtitle": "Fórmula equilibrada com 3 mg de Tadalafila + Blend de Minerais Essenciais para homens jovens e adultos que buscam elevar a performance com segurança.",
        "formula": "3 mg de Tadalafila + Zinco Quelato + Magnésio + Selênio + Vitamina B6",
        "indication": "Homens a partir de 25 anos · Baixa disfunção ou melhora recreativa do vigor e rigidez",
        "badge": "Mais Procurado 25–39 anos",
        "img": "tada-power",
        "width": 600,
        "height": 600,
        "default_checkout_url": "https://ev.braip.com/checkout/plapredn/che14zvv",
        "kits": [
            {
                "caps": "30 cápsulas",
                "price": "R$ 169,90",
                "label": "30 cápsulas — R$ 169,90",
                "url": "https://ev.braip.com/checkout/plapredn/che14zvv"
            },
            {
                "caps": "60 cápsulas",
                "price": "R$ 249,90",
                "label": "60 cápsulas — R$ 249,90",
                "url": "https://ev.braip.com/checkout/plazz1dz/che14zvv"
            },
            {
                "caps": "90 cápsulas",
                "price": "R$ 349,90",
                "label": "90 cápsulas — R$ 349,90",
                "url": "https://ev.braip.com/checkout/plagzeoj/che14zvv"
            },
            {
                "caps": "120 cápsulas",
                "price": "R$ 419,90",
                "label": "120 cápsulas — R$ 419,90",
                "url": "https://ev.braip.com/checkout/pla2r1we/che14zvv"
            }
        ],
        "highlights": [
            "Auxilia na vasodilatação periférica com dosagem suave de 3 mg",
            "Reposição de minerais cofatores da síntese natural de testosterona",
            "Reduz a insegurança e o receio de falhar na hora H",
            "Ideal para uso planejado ou rotina de vitalidade masculina"
        ],
        "description_long": (
            "O Tada Power foi desenvolvido pela Loja do Cabo especialmente para homens que desejam "
            "eliminar de vez a insegurança na hora H sem recorrer a dosagens agressivas. Sua composição "
            "une 3 mg de Tadalafila a um complexo de minerais biodisponíveis (Zinco, Magnésio e Selênio), "
            "favorecendo o fluxo sanguíneo peniano, a resposta ao estímulo e a manutenção de ereções firmes "
            "do início ao fim da relação."
        ),
        "how_to_use": "Ingerir 1 cápsula ao dia com água, preferencialmente 45 a 60 minutos antes da relação ou conforme orientação profissional.",
        "faq": [
            {
                "q": "Para quem o Tada Power é mais indicado?",
                "a": "É ideal para homens jovens e adultos (25 a 45 anos) que enfrentam oscilações pontuais de ereção por estresse, cansaço ou ansiedade de desempenho e buscam uma fórmula leve e segura."
            },
            {
                "q": "Em quanto tempo o Tada Power começa a agir?",
                "a": "A absorção média ocorre entre 40 e 60 minutos após a ingestão com água, mantendo janela de resposta favorável ao estímulo sexual por até 24 horas."
            },
            {
                "q": "O envio é discreto?",
                "a": "Sim. Todos os pedidos da Loja do Cabo são enviados em embalagem parda lacrada, sem menção ao nome do produto ou conteúdo no exterior da caixa, com frete grátis para todo o Brasil."
            },
            {
                "q": "Quais tratamentos estão disponíveis no checkout oficial da Braip?",
                "a": "Trabalhamos com potes de 30, 60, 90 e 120 cápsulas no checkout seguro da Braip para ciclos completos de tratamento e economia progressiva."
            }
        ]
    },
    {
        "slug": "tadamaxx",
        "name": "TadaMaxx",
        "external_url": "https://tadamaxx.com/",
        "tagline": "Até 36 Horas de Potência, Vasodilatação e Firmeza",
        "subtitle": "A combinação sinérgica de 8 mg de Tadalafila + L-Arginina + Taurina para máxima resposta vascular e resistência física.",
        "formula": "8 mg de Tadalafila + L-Arginina (precursora de óxido nítrico) + Taurina",
        "indication": "Homens 40+ · Casos moderados a intensos de queda na rigidez e disposição",
        "badge": "Ação Prolongada 36h",
        "img": "tadamaxx",
        "width": 600,
        "height": 600,
        "default_checkout_url": "https://ev.braip.com/checkout/plalvlxe/chepmkvz",
        "kits": [
            {
                "caps": "30 cápsulas",
                "price": "R$ 169,90",
                "label": "30 cápsulas — R$ 169,90",
                "url": "https://ev.braip.com/checkout/plalvlxe/chepmkvz"
            },
            {
                "caps": "60 cápsulas",
                "price": "R$ 249,90",
                "label": "60 cápsulas — R$ 249,90",
                "url": "https://ev.braip.com/checkout/plalvlxk/chepmkvz"
            },
            {
                "caps": "90 cápsulas",
                "price": "R$ 349,90",
                "label": "90 cápsulas — R$ 349,90",
                "url": "https://ev.braip.com/checkout/plaxpxgq/chepmkvz"
            }
        ],
        "highlights": [
            "Tríade vasodilatadora: Tadalafila 8 mg + L-Arginina + Taurina",
            "Janela de resposta ativa de até 36 horas mediante estímulo sexual",
            "Apoia a produção endotelial de óxido nítrico (NO) e o vigor muscular",
            "Fórmula balanceada para minimizar desconfortos e maximizar a firmeza"
        ],
        "description_long": (
            "O TadaMaxx é um dos campeões de vendas da Loja do Cabo para homens a partir dos 40 anos. "
            "Sua fórmula combina 8 mg de Tadalafila com L-Arginina — aminoácido essencial para a síntese "
            "de óxido nítrico nas paredes dos vasos sanguíneos — e Taurina, que combate a fadiga física "
            "e melhora a contratilidade vascular. O resultado é uma resposta erétil consistente, potente "
            "e duradoura por até um final de semana inteiro."
        ),
        "how_to_use": "Ingerir 1 cápsula com água cerca de 45 minutos antes da atividade íntima, respeitando o intervalo mínimo de 24 a 36 horas entre as doses.",
        "faq": [
            {
                "q": "Por que o TadaMaxx combina Tadalafila com L-Arginina e Taurina?",
                "a": "Porque a L-Arginina fornece o substrato para produzir óxido nítrico (que inicia a vasodilatação), enquanto a Tadalafila preserva o GMP cíclico que mantém os corpos cavernosos preenchidos de sangue, e a Taurina reduz a fadiga."
            },
            {
                "q": "O efeito de 36 horas significa ereção ininterrupta?",
                "a": "Não. A ereção ocorre apenas quando há desejo e estímulo sexual. A janela de 36 horas significa que seu organismo estará pronto para responder com firmeza sempre que houver estímulo nesse período."
            },
            {
                "q": "Quais são os kits disponíveis do TadaMaxx?",
                "a": "Trabalhamos com os tratamentos oficiais de 30 cápsulas (1 mês), 60 cápsulas (2 meses) e 90 cápsulas (3 meses) diretamente pela Braip com frete grátis."
            },
            {
                "q": "Como faço meu pedido com segurança?",
                "a": "Basta selecionar o seu kit de 30, 60 ou 90 cápsulas para finalizar no checkout seguro da Braip, ou falar com nossa equipe pelo WhatsApp (71 98382-1218)."
            }
        ]
    },
    {
        "slug": "erectus-plus",
        "name": "Erectus Plus",
        "external_url": "https://erectusplus.com.br/",
        "tagline": "Vitalidade, Libido e Firmeza para Homens 50+",
        "subtitle": "Desenvolvido com 10 mg de Tadalafila + Minerais + Aminoácidos + Fitohormônios para restaurar o vigor masculino após os 50 anos.",
        "formula": "10 mg de Tadalafila + Zinco + Magnésio + L-Arginina + Compostos Fitoativos",
        "indication": "Homens 50+ · Recuperação da potência, libido e confiança na maturidade",
        "badge": "Especialista 50+",
        "img": "erectus-plus",
        "width": 600,
        "height": 600,
        "default_checkout_url": "https://ev.braip.com/checkout/pla48l1v/chedd8lj",
        "kits": [
            {
                "caps": "30 cápsulas",
                "price": "R$ 169,90",
                "label": "30 cápsulas — R$ 169,90",
                "url": "https://ev.braip.com/checkout/pla48l1v/chedd8lj"
            },
            {
                "caps": "60 cápsulas",
                "price": "R$ 249,90",
                "label": "60 cápsulas — R$ 249,90",
                "url": "https://ev.braip.com/checkout/pla0n42m/chedd8lj"
            },
            {
                "caps": "90 cápsulas",
                "price": "R$ 349,90",
                "label": "90 cápsulas — R$ 349,90",
                "url": "https://ev.braip.com/checkout/plaoqyz6/chedd8lj"
            }
        ],
        "highlights": [
            "10 mg de Tadalafila combinados com cofatores hormonais e vasculares",
            "Suporte nutricional completo para homens acima dos 50 anos",
            "Melhora simultânea da qualidade da ereção e da disposição geral",
            "Recupere a segurança e o prazer com acompanhamento e envio discreto"
        ],
        "description_long": (
            "A partir dos 50 anos, é natural que o endotélio vascular perca parte da elasticidade e que a "
            "biodisponibilidade de micronutrientes diminua. O Erectus Plus foi formulado exatamente para "
            "atender essa fase da vida masculina: une 10 mg de Tadalafila a minerais quelatos, aminoácidos "
            "vasodilatadores e fitohormônios naturais que apoiam a energia metabólica, a libido e a rigidez peniana."
        ),
        "how_to_use": "Tomar 1 cápsula com água de 45 a 60 minutos antes da relação, ou conforme recomendação individualizada.",
        "faq": [
            {
                "q": "Qual a diferença entre o Erectus Plus e o Tada Power?",
                "a": "O Erectus Plus possui concentração mais robusta (10 mg de Tadalafila contra 3 mg do Tada Power) e adiciona aminoácidos e fitonutrientes pensados para o metabolismo do homem maduro (50+)."
            },
            {
                "q": "O Erectus Plus ajuda na disposição física além da ereção?",
                "a": "Sim. Graças à combinação de minerais (zinco e magnésio) e fitoativos, ele combate a sensação de esgotamento e apoia a vitalidade masculina integral."
            },
            {
                "q": "Qual o prazo e forma de entrega?",
                "a": "Enviamos para todo o Brasil com frete grátis em embalagem 100% discreta, com pagamento seguro processado pela Braip."
            },
            {
                "q": "Quais kits estão disponíveis?",
                "a": "Você pode escolher entre os kits de 30, 60 ou 90 cápsulas diretamente no checkout oficial da Braip."
            }
        ]
    },
    {
        "slug": "erectus-retard",
        "name": "Erectus Retard",
        "external_url": "https://lojadocabo.com/erectus-retard/",
        "tagline": "Controle da Ejaculação Precoce e Tempo Prolongado na Cama",
        "subtitle": "Fórmula dupla ação: 10 mg de Tadalafila + Vasodilatadores + Ativos Modulares Naturais para equilíbrio do reflexo ejaculatório.",
        "formula": "10 mg de Tadalafila + L-Triptofano / Fitocalmantes Naturais + Vasodilatadores",
        "indication": "Controle do tempo de relação · Redução da ansiedade de desempenho e ereção firme",
        "badge": "Foco em Controle e Duração",
        "img": "erectus-retard",
        "width": 600,
        "height": 600,
        "default_checkout_url": "https://ev.braip.com/checkout/plagyn2m/che16g1v",
        "kits": [
            {
                "caps": "30 cápsulas",
                "price": "R$ 249,90",
                "label": "30 cápsulas — R$ 249,90",
                "url": "https://ev.braip.com/checkout/plagyn2m/che16g1v"
            },
            {
                "caps": "60 cápsulas",
                "price": "R$ 379,90",
                "label": "60 cápsulas — R$ 379,90",
                "url": "https://ev.braip.com/checkout/pla2qdyz/che16g1v"
            },
            {
                "caps": "90 cápsulas",
                "price": "R$ 529,90",
                "label": "90 cápsulas — R$ 529,90",
                "url": "https://ev.braip.com/checkout/plaxq8gg/che16g1v"
            }
        ],
        "highlights": [
            "Atua nas duas frentes: mantém a ereção firme e desacelera o reflexo ejaculatório",
            "Reduz a hiperatividade simpática causada pela ansiedade na hora H",
            "Não causa dormência local (ação sistêmica equilibrada, diferente de anestésicos tópicos)",
            "Permite recuperar o ritmo da relação com tranquilidade e domínio"
        ],
        "description_long": (
            "Muitos homens sofrem com a combinação de ansiedade de desempenho e perda precoce do controle "
            "ejaculatório. O Erectus Retard foi projetado para agir exatamente nesse ciclo: enquanto 10 mg "
            "de Tadalafila e vasodilatadores garantem rigidez total (mesmo que você faça pausas estratégicas "
            "durante o ato), seus compostos moduladores naturais ajudam a acalmar a resposta nervosa simpática, "
            "prolongando o tempo até o clímax sem retirar a sensibilidade natural."
        ),
        "how_to_use": "Ingerir 1 cápsula ao dia ou 60 minutos antes da relação sexual com um copo de água. Para melhores resultados no controle ejaculatório, recomenda-se o uso regular aliado às técnicas de respiração e controle pélvico.",
        "faq": [
            {
                "q": "O Erectus Retard tira a sensibilidade como as pomadas anestésicas?",
                "a": "Não! Diferente das pomadas de lidocaína/benzocaína que adormecem a pele, o Erectus Retard age de dentro para fora modulando a ansiedade e garantindo a firmeza erétil, preservando todo o prazer."
            },
            {
                "q": "Em quanto tempo percebo melhora no controle?",
                "a": "O suporte na firmeza da ereção já ocorre na primeira tomada (45–60 min), enquanto o ganho progressivo de controle do tempo se consolida ao longo das primeiras 2 a 4 semanas de uso."
            },
            {
                "q": "Posso combinar o Erectus Retard com exercícios de Kegel e respiração?",
                "a": "Sim, essa é a combinação padrão-ouro! O suplemento reduz a tensão fisiológica e garante a ereção, facilitando a aplicação da respiração diafragmática e do controle do assoalho pélvico."
            },
            {
                "q": "Como adquirir o Erectus Retard original?",
                "a": "Escolha seu kit de 30, 60 ou 90 cápsulas para finalizar no checkout oficial da Braip com garantia e frete grátis."
            }
        ]
    },
    {
        "slug": "erectus-caps-turbo",
        "name": "Erectus Caps Turbo",
        "external_url": "https://erectusturbo.com/",
        "tagline": "Estímulo Natural de Libido, Vigor e Controle Masculino",
        "subtitle": "Sinergia de 4 mg de Tadalafila + Fitohormônios e Micronutrientes para homens que buscam energia diária, desejo ativo e potência.",
        "formula": "4 mg de Tadalafila + Complexo Fitohormonal + Boro + Zinco + Maca e Tribulus",
        "indication": "Aumento da libido, disposição física, resposta rápida e controle",
        "badge": "Energia + Libido Diária",
        "img": "erectus-caps-turbo",
        "width": 600,
        "height": 600,
        "default_checkout_url": "https://ev.braip.com/checkout/plalv6lk/cheejgxk",
        "kits": [
            {
                "caps": "30 cápsulas",
                "price": "R$ 169,90",
                "label": "30 cápsulas — R$ 169,90",
                "url": "https://ev.braip.com/checkout/plalv6lk/cheejgxk"
            },
            {
                "caps": "60 cápsulas",
                "price": "R$ 249,90",
                "label": "60 cápsulas — R$ 249,90",
                "url": "https://ev.braip.com/checkout/plavv2qn/cheejgxk"
            },
            {
                "caps": "90 cápsulas",
                "price": "R$ 349,90",
                "label": "90 cápsulas — R$ 349,90",
                "url": "https://ev.braip.com/checkout/pla14v92/cheejgxk"
            },
            {
                "caps": "120 cápsulas",
                "price": "R$ 419,90",
                "label": "120 cápsulas — R$ 419,90",
                "url": "https://ev.braip.com/checkout/pladge44/cheejgxk"
            }
        ],
        "highlights": [
            "Dosagem versátil de 4 mg de Tadalafila ideal para rotina de alta disposição",
            "Rico em fitonutrientes que apoiam o desejo sexual e o vigor masculino",
            "Melhora a qualidade das ereções matinais e a prontidão para o ato",
            "Combate o cansaço mental e físico acumulado da rotina intensa"
        ],
        "description_long": (
            "Quando o estresse do trabalho, o cansaço acumulado e a queda de libido começam a esfriar a "
            "vida íntima, apenas um vasodilatador isolado pode não bastar. O Erectus Caps Turbo reúne "
            "4 mg de Tadalafila a um blend concentrado de fitohormônios naturais e minerais pró-testosterona, "
            "devolvendo o apetite sexual, a energia física e a firmeza necessária para noites memoráveis."
        ),
        "how_to_use": "Tomar 1 cápsula ao dia com água, preferencialmente no mesmo horário ou 45 minutos antes da relação.",
        "faq": [
            {
                "q": "Qual o diferencial do Erectus Caps Turbo?",
                "a": "Sua fórmula equilibra 4 mg de Tadalafila (ótima tolerabilidade para uso frequente) com fitoativos focados no aumento da libido e disposição energética."
            },
            {
                "q": "Ajuda quem sente falta de desejo ou cansaço constante?",
                "a": "Sim. Os compostos fitohormonais e minerais da fórmula atuam justamente corrigindo carências associadas à fadiga e ao baixo desejo masculino."
            },
            {
                "q": "Quantas cápsulas vêm em cada pote?",
                "a": "Disponível em tratamentos de 30, 60, 90 e 120 cápsulas no checkout da Braip com descontos progressivos e frete grátis."
            },
            {
                "q": "Posso pagar via Pix, Boleto ou Cartão?",
                "a": "Sim, o checkout oficial da Braip aceita Pix com aprovação imediata, cartão de crédito em até 12x e boleto bancário."
            }
        ]
    },
    {
        "slug": "madeirada",
        "name": "Madeirada",
        "external_url": "https://madeirada.com.br/",
        "tagline": "Desempenho Máximo e Firmeza Inabalável para Homens 60+",
        "subtitle": "A fórmula mais concentrada da linha: 20 mg de Tadalafila + Aminoácidos + Vasodilatadores Naturais para potência máxima.",
        "formula": "20 mg de Tadalafila + L-Arginina + Citrulina + Vasodilatadores Naturais",
        "indication": "Homens 60+ ou casos que exigem potência vascular máxima e rigidez superior",
        "badge": "Potência Máxima 20 mg",
        "img": "madeirada",
        "width": 600,
        "height": 600,
        "default_checkout_url": "https://ev.braip.com/checkout/pla04zqy/ched6vg7",
        "kits": [
            {
                "caps": "30 cápsulas",
                "price": "R$ 249,90",
                "label": "30 cápsulas — R$ 249,90",
                "url": "https://ev.braip.com/checkout/pla04zqy/ched6vg7"
            },
            {
                "caps": "60 cápsulas",
                "price": "R$ 379,90",
                "label": "60 cápsulas — R$ 379,90",
                "url": "https://ev.braip.com/checkout/pla1jv0n/ched6vg7"
            },
            {
                "caps": "90 cápsulas",
                "price": "R$ 529,90",
                "label": "90 cápsulas — R$ 529,90",
                "url": "https://ev.braip.com/checkout/plarx1j8/ched6vg7"
            }
        ],
        "highlights": [
            "Concentração máxima de 20 mg de Tadalafila por cápsula",
            "Reforçada com aminoácidos precursores de óxido nítrico para fluxo intenso",
            "Desenvolvida especialmente para homens experientes (60+) que exigem resultado firme",
            "Devolve a confiança plena e a rigidez com ação prolongada"
        ],
        "description_long": (
            "A maturidade traz experiência, mas também exige um suporte vascular à altura. O Madeirada é "
            "o suplemento de maior concentração da Loja do Cabo, formulado com 20 mg de Tadalafila associados "
            "a aminoácidos e vasodilatadores naturais de alta absorção. É a escolha definitiva para homens "
            "com mais de 60 anos — ou que não obtiveram resultado satisfatório com dosagens baixas — conquistarem "
            "ereções potentes, firmes e seguras."
        ),
        "how_to_use": "Ingerir 1 cápsula com água 45 a 60 minutos antes da relação. Não exceder 1 cápsula no período de 36 a 48 horas.",
        "faq": [
            {
                "q": "Por que o Madeirada é indicado especialmente para homens 60+?",
                "a": "Porque reúne a dosagem plena de 20 mg de Tadalafila com cofatores vasodilatadores que compensam a menor produção natural de óxido nítrico na maturidade."
            },
            {
                "q": "Quais apresentações do Madeirada estão disponíveis?",
                "a": "Contamos com os tratamentos completos de 30, 60 e 90 cápsulas no checkout oficial da Braip com frete grátis para todo o Brasil."
            },
            {
                "q": "Quem tem pressão alta ou toma medicamentos deve ter cuidado?",
                "a": "Sim. Homens que utilizam medicamentos à base de nitratos (para dor no peito/angina) ou têm cardiopatias instáveis devem sempre consultar seu médico antes de usar compostos com tadalafila."
            },
            {
                "q": "Como pedir o Madeirada com entrega discreta?",
                "a": "Selecione o kit desejado (30, 60 ou 90 cápsulas) para comprar na Braip ou chame nossa equipe no WhatsApp (71 98382-1218). Garantimos sigilo absoluto na embalagem."
            }
        ]
    }
]

BLOG_ARTICLES: List[Dict[str, Any]] = [
    {
        "slug": "testosterona-natural-mitos-e-verdades",
        "title": "Testosterona Natural: 8 Mitos e Verdades Que Todo Homem Precisa Conhecer",
        "category": "Hormônios & Saúde Masculina",
        "read_time": "8 min de leitura",
        "date": "25 Out 2026",
        "excerpt": "Dormir 5 horas por noite derruba sua testosterona em até 15% em uma única semana. Descubra o que realmente funciona e o que é mito na produção hormonal masculina.",
        "cta_product_slug": "erectus-plus",
        "is_new": True
    },
    {
        "slug": "respiracao-para-durar-mais-na-cama",
        "title": "Respiração para Durar Mais na Cama: 4 Técnicas Que Realmente Funcionam",
        "category": "Controle & Desempenho",
        "read_time": "9 min de leitura",
        "date": "25 Out 2026",
        "excerpt": "Entenda como o sistema nervoso simpático dispara o reflexo ejaculatório e aprenda 4 técnicas respiratórias práticas para ativar o freio parassimpático na hora H.",
        "cta_product_slug": "erectus-retard",
        "is_new": True
    },
    {
        "slug": "exercicios-de-kegel-masculino",
        "title": "Exercícios de Kegel Masculino: Como Fazer Passo a Passo para Controle e Ereção Firme",
        "category": "Treino Pélvico",
        "read_time": "7 min de leitura",
        "date": "18 Out 2026",
        "excerpt": "O músculo bulbocavernoso sustenta a pressão sanguínea da ereção e ajuda a frear o reflexo ejaculatório. Veja como localizar e treinar 5 minutos por dia.",
        "cta_product_slug": "erectus-retard",
        "is_new": False
    },
    {
        "slug": "minerais-para-potencia-masculina",
        "title": "Minerais para Potência Masculina: O Papel do Zinco, Magnésio, Selênio e Boro",
        "category": "Nutrição & Vigor",
        "read_time": "7 min de leitura",
        "date": "15 Out 2026",
        "excerpt": "Sem zinco e magnésio suficientes, as células de Leydig reduzem a produção de testosterona livre. Conheça as doses ideais e fontes alimentares.",
        "cta_product_slug": "tada-power",
        "is_new": False
    },
    {
        "slug": "aminoacidos-para-erecao",
        "title": "Aminoácidos para Ereção: Como L-Arginina, Citrulina e Taurina Atuam na Vasodilatação",
        "category": "Fisiologia Vascular",
        "read_time": "8 min de leitura",
        "date": "12 Out 2026",
        "excerpt": "A ereção depende diretamente da produção endotelial de óxido nítrico. Entenda a sinergia bioquímica entre L-Arginina, L-Citrulina e Taurina.",
        "cta_product_slug": "tadamaxx",
        "is_new": False
    },
    {
        "slug": "alimentos-vasodilatadores-para-erecao",
        "title": "Alimentos Vasodilatadores para Ereção: 10 Opções Naturais Que Melhoram a Circulação",
        "category": "Alimentação & Fluxo Sanguíneo",
        "read_time": "7 min de leitura",
        "date": "09 Out 2026",
        "excerpt": "Beterraba, melancia, cacau amargo, alho e romã fornecem nitratos e flavonoides que protegem as artérias e potencializam a resposta erétil.",
        "cta_product_slug": "tadamaxx",
        "is_new": False
    },
    {
        "slug": "combinacao-de-valeriana-e-damiana-controle-da-ejaculacao-precoce",
        "title": "Combinação de Valeriana e Damiana: Controle Natural da Ejaculação Precoce",
        "category": "Fitoterapia Masculina",
        "read_time": "6 min de leitura",
        "date": "05 Out 2026",
        "excerpt": "A ansiedade de desempenho acelera o clímax. Veja como a ação ansiolítica da Valeriana somada ao estímulo tônico da Damiana equilibra o tempo na cama.",
        "cta_product_slug": "erectus-retard",
        "is_new": False
    },
    {
        "slug": "como-usar-pomada-anestesica-para-ejaculacao-precoce",
        "title": "Como Usar Pomada Anestésica Para Ejaculação Precoce: Guia Seguro e Alternativas",
        "category": "Guia Prático",
        "read_time": "6 min de leitura",
        "date": "02 Out 2026",
        "excerpt": "Pomadas dessensibilizantes podem ajudar, mas o uso incorreto causa dormência excessiva e perda da ereção. Aprenda os cuidados e alternativas sistêmicas.",
        "cta_product_slug": "erectus-retard",
        "is_new": False
    },
    {
        "slug": "quanto-tempo-dura-uma-relacao-normal",
        "title": "Quanto Tempo Dura uma Relação Normal? O Que a Ciência Diz Sobre o Tempo na Cama",
        "category": "Ciência & Sexualidade",
        "read_time": "6 min de leitura",
        "date": "28 Set 2026",
        "excerpt": "Estudos clínicos internacionais mostram que o tempo médio real de penetração é muito diferente dos mitos da internet. Veja os parâmetros médicos reais.",
        "cta_product_slug": "erectus-caps-turbo",
        "is_new": False
    }
]


def picture_tag(
    img_name: str,
    alt: str,
    width: int = 600,
    height: int = 600,
    lazy: bool = True,
    img_class: str = "",
    picture_class: str = ""
) -> str:
    loading_attr = 'loading="lazy" decoding="async"' if lazy else 'fetchpriority="high" decoding="async"'
    cls_attr = f' class="{img_class}"' if img_class else ""
    pic_cls = f' class="{picture_class}"' if picture_class else ""
    return (
        f'<picture{pic_cls}>'
        f'<source srcset="/img/{img_name}.webp" type="image/webp">'
        f'<img src="/img/{img_name}.png" alt="{alt}" width="{width}" height="{height}" {loading_attr}{cls_attr}>'
        f'</picture>'
    )


META_PIXEL_HEAD = """  <!-- Google Site Verification -->
  <meta name="google-site-verification" content="SEU_CODIGO_GOOGLE_SEARCH_CONSOLE" />
  <!-- Meta Pixel Code -->
  <script>
  !function(f,b,e,v,n,t,s)
  {if(f.fbq)return;n=f.fbq=function(){n.callMethod?
  n.callMethod.apply(n,arguments):n.queue.push(arguments)};
  if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';
  n.queue=[];t=b.createElement(e);t.async=!0;
  t.src=v;s=b.getElementsByTagName(e)[0];
  s.parentNode.insertBefore(t,s)}(window, document,'script',
  'https://connect.facebook.net/en_US/fbevents.js');
  fbq('init', 'SEU_PIXEL_ID');
  fbq('track', 'PageView');
  </script>
  <noscript><img height="1" width="1" style="display:none"
  src="https://www.facebook.com/tr?id=SEU_PIXEL_ID&ev=PageView&noscript=1"
  /></noscript>
  <!-- End Meta Pixel Code -->"""

META_PIXEL_BODY_END = """  <!-- Eventos Meta Pixel: Contact (WhatsApp) e InitiateCheckout (Compra / Braip) -->
  <script>
  document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('a[href*="wa.me"]').forEach(function(el) {
      el.addEventListener('click', function() {
        if (typeof fbq === 'function') {
          fbq('track', 'Contact');
        }
      });
    });
    document.querySelectorAll('.btn-buy, [data-checkout="true"], a[href*="braip.com"]').forEach(function(el) {
      el.addEventListener('click', function() {
        if (typeof fbq === 'function') {
          fbq('track', 'InitiateCheckout');
        }
      });
    });
  });
  </script>"""


SHARED_CSS = """
    :root {
      --bg-primary: #0B0B10;
      --bg-surface: #12131C;
      --bg-elevated: #181A26;
      --text-primary: #F4F5F8;
      --text-secondary: #B8BCCF;
      --text-muted: #858A9E;
      --gold-start: #F5B942;
      --gold-end: #FF8A00;
      --whatsapp: #25D366;
      --whatsapp-dark: #1DA851;
      --border-subtle: rgba(255, 255, 255, 0.08);
      --border-gold: rgba(245, 185, 66, 0.24);
    }
    * { box-sizing: border-box; margin: 0; padding: 0; }
    html { scroll-behavior: smooth; background-color: var(--bg-primary); color: var(--text-primary); }
    body {
      font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
      background-color: var(--bg-primary);
      color: var(--text-primary);
      line-height: 1.68;
      font-size: 16px;
      -webkit-font-smoothing: antialiased;
    }
    h1, h2, h3, h4, .font-display {
      font-family: 'Outfit', sans-serif;
      line-height: 1.2;
      letter-spacing: -0.02em;
      text-wrap: balance;
    }
    a { color: inherit; text-decoration: none; transition: color 0.18s ease, opacity 0.18s ease, transform 0.18s ease; }
    img { max-width: 100%; height: auto; display: block; }
    .container { width: 100%; max-width: 1200px; margin: 0 auto; padding: 0 24px; }
    .container-narrow { width: 100%; max-width: 820px; margin: 0 auto; padding: 0 24px; }

    /* Top Bar Contract: 3 Zones */
    .site-header {
      position: sticky;
      top: 0;
      z-index: 50;
      background: rgba(11, 11, 16, 0.92);
      backdrop-filter: blur(12px);
      border-bottom: 1px solid var(--border-subtle);
    }
    .header-inner {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 32px;
      height: 72px;
    }
    .brand-wordmark {
      font-family: 'Outfit', sans-serif;
      font-weight: 800;
      font-size: 1.25rem;
      letter-spacing: 0.02em;
      background: linear-gradient(135deg, var(--gold-start), var(--gold-end));
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      white-space: nowrap;
      flex-shrink: 0;
    }
    .main-nav {
      display: flex;
      align-items: center;
      gap: 28px;
    }
    .main-nav a {
      font-size: 0.9375rem;
      font-weight: 500;
      color: var(--text-secondary);
      white-space: nowrap;
      flex-shrink: 0;
    }
    .main-nav a:hover { color: var(--gold-start); }
    .btn-header-cta {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 10px 20px;
      border-radius: 10px;
      font-family: 'Outfit', sans-serif;
      font-weight: 700;
      font-size: 0.875rem;
      background: linear-gradient(135deg, var(--gold-start), var(--gold-end));
      color: #0B0B10;
      white-space: nowrap;
      flex-shrink: 0;
    }
    .btn-header-cta:hover { transform: translateY(-1px); opacity: 0.95; }

    /* Buttons */
    .btn-gold {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 10px;
      padding: 14px 24px;
      border-radius: 12px;
      font-family: 'Outfit', sans-serif;
      font-weight: 700;
      font-size: 0.96rem;
      background: linear-gradient(135deg, var(--gold-start), var(--gold-end));
      color: #0B0B10;
      white-space: nowrap;
      border: none;
      cursor: pointer;
    }
    .btn-gold:hover { transform: translateY(-2px); opacity: 0.96; }
    .btn-whatsapp {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 10px;
      padding: 14px 24px;
      border-radius: 12px;
      font-family: 'Outfit', sans-serif;
      font-weight: 700;
      font-size: 0.96rem;
      background: linear-gradient(135deg, var(--whatsapp), var(--whatsapp-dark));
      color: #FFFFFF;
      white-space: nowrap;
    }
    .btn-whatsapp:hover { transform: translateY(-2px); opacity: 0.96; }
    .btn-outline {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      padding: 11px 20px;
      border-radius: 10px;
      font-family: 'Outfit', sans-serif;
      font-weight: 600;
      font-size: 0.9rem;
      border: 1px solid var(--border-gold);
      color: var(--gold-start);
      background: rgba(245, 185, 66, 0.05);
      white-space: nowrap;
    }
    .btn-outline:hover { background: rgba(245, 185, 66, 0.14); }

    /* Braip Kit Buttons inside cards */
    .kit-list {
      display: grid;
      gap: 8px;
      margin: 14px 0;
    }
    .btn-kit-braip {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 10px 14px;
      border-radius: 10px;
      background: #171925;
      border: 1px solid rgba(245, 185, 66, 0.28);
      font-family: 'Outfit', sans-serif;
      font-size: 0.88rem;
      font-weight: 600;
      color: var(--text-primary);
      font-variant-numeric: tabular-nums;
    }
    .btn-kit-braip:hover {
      background: linear-gradient(135deg, var(--gold-start), var(--gold-end));
      color: #0B0B10;
      border-color: transparent;
      transform: translateY(-1px);
    }
    .btn-kit-braip span.kit-cta {
      color: var(--gold-start);
      font-weight: 700;
      font-size: 0.82rem;
    }
    .btn-kit-braip:hover span.kit-cta {
      color: #0B0B10;
    }

    /* Metadata line (Zero-Pill discipline) */
    .meta-line {
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      gap: 8px;
      font-size: 0.8125rem;
      color: var(--text-muted);
      font-variant-numeric: tabular-nums;
    }
    .meta-sep { color: var(--gold-start); opacity: 0.7; }
    .kicker {
      font-family: 'Outfit', sans-serif;
      font-size: 0.8125rem;
      font-weight: 600;
      letter-spacing: 0.06em;
      color: var(--gold-start);
      margin-bottom: 10px;
      display: block;
    }

    /* Cards & Grids */
    .grid-3 {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 28px;
    }
    .grid-2 {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 28px;
    }
    .surface-card {
      background: var(--bg-surface);
      border: 1px solid var(--border-subtle);
      border-radius: 16px;
      padding: 26px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      transition: transform 0.18s ease, border-color 0.18s ease;
    }
    .surface-card:hover {
      transform: translateY(-2px);
      border-color: var(--border-gold);
    }
    .product-img-wrap {
      background: #161823;
      border-radius: 12px;
      padding: 16px;
      margin-bottom: 18px;
      display: flex;
      align-items: center;
      justify-content: center;
      aspect-ratio: 1 / 1;
      overflow: hidden;
    }
    .product-img-wrap img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      border-radius: 8px;
    }

    /* Article Content */
    .article-header {
      padding: 56px 0 36px;
      border-bottom: 1px solid var(--border-subtle);
      margin-bottom: 40px;
    }
    .article-title {
      font-size: clamp(2rem, 3.8vw, 3rem);
      font-weight: 800;
      margin: 12px 0 18px;
      color: var(--text-primary);
    }
    .article-lead {
      font-size: 1.15rem;
      color: var(--text-secondary);
      max-width: 70ch;
    }
    .toc-box {
      background: var(--bg-surface);
      border: 1px solid var(--border-gold);
      border-radius: 14px;
      padding: 24px 28px;
      margin: 0 0 36px;
    }
    .toc-title {
      font-family: 'Outfit', sans-serif;
      font-weight: 700;
      font-size: 1.05rem;
      color: var(--gold-start);
      margin-bottom: 12px;
    }
    .toc-list {
      list-style: decimal;
      padding-left: 20px;
      display: grid;
      gap: 8px;
      color: var(--text-secondary);
      font-size: 0.95rem;
    }
    .toc-list a:hover { color: var(--gold-start); text-decoration: underline; }

    .prose h2 {
      font-size: clamp(1.5rem, 2.5vw, 2rem);
      font-weight: 700;
      color: var(--text-primary);
      margin: 44px 0 16px;
      padding-top: 8px;
    }
    .prose h3 {
      font-size: 1.25rem;
      font-weight: 700;
      color: var(--gold-start);
      margin: 28px 0 12px;
    }
    .prose p {
      color: var(--text-secondary);
      margin-bottom: 20px;
      max-width: 72ch;
    }
    .prose ul, .prose ol {
      color: var(--text-secondary);
      padding-left: 22px;
      margin-bottom: 24px;
      display: grid;
      gap: 10px;
    }
    .prose strong { color: var(--text-primary); font-weight: 600; }
    .prose a {
      color: var(--gold-start);
      text-decoration: underline;
      text-underline-offset: 3px;
    }

    /* Callouts: All-around hairline border */
    .tip-box {
      background: #131622;
      border: 1px solid rgba(245, 185, 66, 0.32);
      border-radius: 14px;
      padding: 22px 26px;
      margin: 28px 0;
    }
    .tip-box-title {
      font-family: 'Outfit', sans-serif;
      font-weight: 700;
      font-size: 0.95rem;
      color: var(--gold-start);
      margin-bottom: 8px;
      display: block;
    }
    .warn-box {
      background: #1A1318;
      border: 1px solid rgba(248, 113, 113, 0.32);
      border-radius: 14px;
      padding: 22px 26px;
      margin: 28px 0;
    }
    .warn-box-title {
      font-family: 'Outfit', sans-serif;
      font-weight: 700;
      font-size: 0.95rem;
      color: #FCA5A5;
      margin-bottom: 8px;
      display: block;
    }

    /* CTA Banner inside Articles */
    .cta-banner {
      background: linear-gradient(145deg, #161826 0%, #10111A 100%);
      border: 1px solid var(--border-gold);
      border-radius: 18px;
      padding: 32px;
      margin: 44px 0;
      display: grid;
      grid-template-columns: 180px 1fr;
      gap: 28px;
      align-items: center;
    }
    .faq-section { margin: 48px 0; }
    .faq-item {
      background: var(--bg-surface);
      border: 1px solid var(--border-subtle);
      border-radius: 12px;
      padding: 20px 24px;
      margin-bottom: 14px;
    }
    .faq-q {
      font-family: 'Outfit', sans-serif;
      font-weight: 700;
      font-size: 1.05rem;
      color: var(--text-primary);
      margin-bottom: 8px;
    }
    .faq-a { color: var(--text-secondary); font-size: 0.95rem; }

    /* Footer with all 6 products & all 9 articles */
    .site-footer {
      background: #08080C;
      border-top: 1px solid var(--border-subtle);
      padding: 64px 0 40px;
      margin-top: 80px;
    }
    .footer-grid {
      display: grid;
      grid-template-columns: 1.2fr 1fr 1.6fr;
      gap: 40px;
      margin-bottom: 48px;
    }
    .footer-title {
      font-family: 'Outfit', sans-serif;
      font-weight: 700;
      font-size: 1rem;
      color: var(--gold-start);
      margin-bottom: 16px;
    }
    .footer-links {
      list-style: none;
      display: grid;
      gap: 10px;
      font-size: 0.875rem;
      color: var(--text-secondary);
    }
    .footer-links a:hover { color: var(--gold-start); }
    .footer-bottom {
      padding-top: 28px;
      border-top: 1px solid var(--border-subtle);
      display: flex;
      flex-wrap: wrap;
      justify-content: space-between;
      gap: 16px;
      font-size: 0.8125rem;
      color: var(--text-muted);
    }

    @media (max-width: 960px) {
      .grid-3 { grid-template-columns: repeat(2, 1fr); }
      .footer-grid { grid-template-columns: 1fr; }
      .cta-banner { grid-template-columns: 1fr; text-align: left; }
      .cta-banner picture { max-width: 180px; }
    }
    @media (max-width: 680px) {
      .main-nav { display: none; }
      .grid-3, .grid-2 { grid-template-columns: 1fr; }
      .header-inner { height: 64px; }
    }
"""


def render_header() -> str:
    wa_link = f"https://wa.me/{WHATSAPP_NUMBER}?text=Ol%C3%A1%21%20Vim%20pelo%20site%20da%20Loja%20do%20Cabo%20e%20quero%20atendimento."
    return f"""  <header class="site-header">
    <div class="container header-inner">
      <a href="/" class="brand-wordmark">LOJA DO CABO</a>
      <nav class="main-nav" aria-label="Navegação Principal">
        <a href="/">Início</a>
        <a href="/tada-power/">Tada Power</a>
        <a href="/tadamaxx/">TadaMaxx</a>
        <a href="/erectus-plus/">Erectus Plus</a>
        <a href="/erectus-retard/">Erectus Retard</a>
        <a href="/blog/">Blog</a>
      </nav>
      <a href="{wa_link}" target="_blank" rel="noopener" class="btn-header-cta">
        Falar no WhatsApp
      </a>
    </div>
  </header>"""


def render_footer() -> str:
    wa_link = f"https://wa.me/{WHATSAPP_NUMBER}?text=Ol%C3%A1%21%20Gostaria%20de%20conhecer%20os%20produtos%20da%20Loja%20do%20Cabo."
    prod_items = "\n".join(
        f'            <li><a href="/{p["slug"]}/">{p["name"]}</a> · <a href="{p["external_url"]}" target="_blank" rel="noopener" style="color: var(--gold-start);">Site Oficial</a> · <a href="{p["default_checkout_url"]}" target="_blank" rel="noopener" class="btn-buy" data-checkout="true">Checkout Braip</a></li>'
        for p in PRODUCTS
    )
    blog_items = "\n".join(
        f'            <li><a href="/{a["slug"]}/">{a["title"]}</a></li>'
        for a in BLOG_ARTICLES
    )
    return f"""  <footer class="site-footer">
    <div class="container">
      <div class="footer-grid">
        <div>
          <p class="footer-title">LOJA DO CABO LTDA</p>
          <p style="color: var(--text-secondary); font-size: 0.9rem; margin-bottom: 16px;">
            Suplementos naturais e fórmulas avançadas para desempenho, vigor e vitalidade masculina em todas as fases da vida. Envio 100% discreto com frete grátis para todo o Brasil.
          </p>
          <p style="font-size: 0.875rem; color: var(--text-secondary); margin-bottom: 6px;">
            WhatsApp Vendas: <a href="{wa_link}" target="_blank" rel="noopener" style="color: var(--gold-start); font-weight: 600;">{WHATSAPP_DISPLAY}</a>
          </p>
          <p style="font-size: 0.875rem; color: var(--text-secondary);">
            Instagram: <a href="{INSTAGRAM_URL}" target="_blank" rel="noopener" style="color: var(--gold-start);">{INSTAGRAM_HANDLE}</a>
          </p>
        </div>
        <div>
          <p class="footer-title">Linha de Produtos e Checkouts (6)</p>
          <ul class="footer-links">
{prod_items}
          </ul>
        </div>
        <div>
          <p class="footer-title">Guias e Artigos do Blog (9)</p>
          <ul class="footer-links">
            <li><a href="/blog/" style="color: var(--gold-start); font-weight: 600;">Ver Todos os Artigos do Blog →</a></li>
{blog_items}
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <span>© 2026 Loja do Cabo Ltda · Salvador - BA · Todos os direitos reservados.</span>
        <span>As informações deste site têm caráter informativo e não substituem avaliação médica.</span>
      </div>
    </div>
  </footer>"""


def build_faq_jsonld(faqs: List[Dict[str, str]]) -> str:
    schema = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": item["q"],
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": item["a"]
                }
            }
            for item in faqs
        ]
    }
    return json.dumps(schema, ensure_ascii=False, indent=2)


def render_article_page(
    slug: str,
    title: str,
    meta_description: str,
    category: str,
    read_time: str,
    date_str: str,
    lead: str,
    toc: List[Dict[str, str]],
    body_html: str,
    faqs: List[Dict[str, str]],
    cta_product_slug: str,
    related_slugs: List[str]
) -> str:
    canonical = f"{SITE_DOMAIN}/{slug}/"
    faq_jsonld = build_faq_jsonld(faqs)
    product = next((p for p in PRODUCTS if p["slug"] == cta_product_slug), PRODUCTS[0])
    wa_msg = f"Ol%C3%A1%21%20Li%20o%20artigo%20sobre%20{slug}%20e%20quero%20saber%20mais%20sobre%20o%20{product['name']}."
    wa_url = f"https://wa.me/{WHATSAPP_NUMBER}?text={wa_msg}"

    toc_items = "\n".join(
        f'          <li><a href="#{item["id"]}">{item["label"]}</a></li>'
        for item in toc
    )

    faq_html = "\n".join(
        f"""        <div class="faq-item">
          <h3 class="faq-q">{item["q"]}</h3>
          <p class="faq-a">{item["a"]}</p>
        </div>"""
        for item in faqs
    )

    related_articles = [a for a in BLOG_ARTICLES if a["slug"] in related_slugs]
    related_cards = "\n".join(
        f"""        <article class="surface-card">
          <div>
            <div class="meta-line" style="margin-bottom: 10px;">
              <span>{a["category"]}</span>
              <span class="meta-sep">·</span>
              <span>{a["read_time"]}</span>
            </div>
            <h3 style="font-size: 1.15rem; font-weight: 700; margin-bottom: 10px;">
              <a href="/{a["slug"]}/">{a["title"]}</a>
            </h3>
            <p style="color: var(--text-secondary); font-size: 0.9rem; margin-bottom: 18px;">{a["excerpt"]}</p>
          </div>
          <a href="/{a["slug"]}/" style="color: var(--gold-start); font-weight: 600; font-size: 0.9rem;">Ler artigo completo →</a>
        </article>"""
        for a in related_articles
    )

    prod_pic = picture_tag(
        product["img"],
        f"{product['name']} - Loja do Cabo",
        width=product["width"],
        height=product["height"],
        lazy=True
    )

    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title} | Loja do Cabo</title>
  <meta name="description" content="{meta_description}" />
  <link rel="canonical" href="{canonical}" />
  <meta property="og:type" content="article" />
  <meta property="og:title" content="{title} | Loja do Cabo" />
  <meta property="og:description" content="{meta_description}" />
  <meta property="og:url" content="{canonical}" />
  <meta property="og:site_name" content="Loja do Cabo" />
  <meta property="og:image" content="{SITE_DOMAIN}/img/{product['img']}.png" />
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="{title}" />
  <meta name="twitter:description" content="{meta_description}" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Outfit:wght@600;700;800&display=swap" rel="stylesheet" />
  <script type="application/ld+json">
{faq_jsonld}
  </script>
{META_PIXEL_HEAD}
  <style>{SHARED_CSS}</style>
</head>
<body>
{render_header()}
  <main class="container-narrow">
    <header class="article-header">
      <div class="meta-line">
        <a href="/blog/" style="color: var(--gold-start);">Blog Loja do Cabo</a>
        <span class="meta-sep">·</span>
        <span>{category}</span>
        <span class="meta-sep">·</span>
        <span>{read_time}</span>
        <span class="meta-sep">·</span>
        <span>Atualizado em {date_str}</span>
      </div>
      <h1 class="article-title">{title}</h1>
      <p class="article-lead">{lead}</p>
    </header>

    <nav class="toc-box" aria-label="Índice do Artigo">
      <p class="toc-title">Neste Guia Completo</p>
      <ol class="toc-list">
{toc_items}
      </ol>
    </nav>

    <article class="prose">
{body_html}
    </article>

    <section class="cta-banner" aria-label="Recomendação Loja do Cabo">
      <div>
        {prod_pic}
      </div>
      <div>
        <span class="kicker">SOLUÇÃO RECOMENDADA LOJA DO CABO</span>
        <h2 style="font-size: 1.5rem; font-weight: 800; margin-bottom: 8px;">{product["name"]}: {product["tagline"]}</h2>
        <p style="color: var(--text-secondary); font-size: 0.95rem; margin-bottom: 16px;">
          {product["subtitle"]} Frete grátis e embalagem 100% discreta para todo o Brasil.
        </p>
        <div style="display: flex; flex-wrap: wrap; gap: 12px;">
          <a href="{product['default_checkout_url']}" target="_blank" rel="noopener" class="btn-gold btn-buy" data-checkout="true">
            Comprar {product["name"]} na Braip
          </a>
          <a href="{wa_url}" target="_blank" rel="noopener" class="btn-whatsapp">
            Dúvidas no WhatsApp ({WHATSAPP_DISPLAY})
          </a>
          <a href="/{product['slug']}/" class="btn-outline">
            Ver Kits (30/60/90 cáps)
          </a>
        </div>
      </div>
    </section>

    <section class="faq-section" id="faq">
      <h2 style="font-size: 1.75rem; font-weight: 800; margin-bottom: 20px;">Perguntas Frequentes (FAQ)</h2>
{faq_html}
    </section>

    <section style="margin: 56px 0;">
      <h2 style="font-size: 1.5rem; font-weight: 800; margin-bottom: 20px;">Artigos Relacionados</h2>
      <div class="grid-2">
{related_cards}
      </div>
    </section>
  </main>
{render_footer()}
{META_PIXEL_BODY_END}
</body>
</html>
"""
