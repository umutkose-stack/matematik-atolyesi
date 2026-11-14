from math import sin,cos,pi
from pathlib import Path
def art(i):
    bg,fg=[('#203d35','#e1bf77'),('#ae503b','#f4dcc2'),('#d8d5bd','#315443')][i%3]
    shapes=[]
    if i==0:
        for n in range(58):
            a=n*pi/58
            shapes.append(f'<ellipse cx="200" cy="130" rx="104" ry="48" transform="rotate({a*180/pi} 200 130) translate({33*cos(3*a)} 0)"/>')
    elif i==1:
        for k in range(44):
            pts=' '.join(f'{45+x*3.1:.2f},{130+61*sin(x/21+k/17)+k*1.25-27:.2f}' for x in range(101))
            shapes.append(f'<polyline points="{pts}"/>')
    elif i==3:
        ga=pi*(3-5**.5)
        for n in range(1,260):
            r=7.4*n**.5
            shapes.append(f'<circle cx="{200+r*cos(n*ga):.2f}" cy="{130+r*sin(n*ga):.2f}" r="{1.2+n**.5*.22:.2f}"/>')
    elif i==4:
        pts=[(200+104*cos(2*pi*k/23-pi/2),130+104*sin(2*pi*k/23-pi/2)) for k in range(23)]
        for a in range(23):
            for b in range(a+1,23):
                shapes.append(f'<line x1="{pts[a][0]:.2f}" y1="{pts[a][1]:.2f}" x2="{pts[b][0]:.2f}" y2="{pts[b][1]:.2f}"/>')
    elif i==5:
        for k in range(26):
            t=.86**k
            w,h=330*t,214*t
            shapes.append(f'<rect x="{200-w/2:.2f}" y="{130-h/2+(1-t)*18:.2f}" width="{w:.2f}" height="{h:.2f}"/>')
    else:
        for i1 in range(24):
            for rev in [False,True]:
                pts=[]
                for j in range(61):
                    x,y=i1/23,j/60
                    if rev:x,y=y,x
                    pts.append(f'{195+(x-y)*146:.2f},{178+(x+y)*28-144*(x*y)**.45:.2f}')
                shapes.append('<polyline points="'+' '.join(pts)+'"/>')
    return f'<svg aria-hidden="true" viewBox="0 0 400 260" style="background:{bg}"><g fill="none" stroke="{fg}" stroke-width=".88">{"".join(shapes)}</g></svg>'
items=[('padovan','Araştırma','Bir dizinin geçmişi nasıl bulunur?','Silinen terimden ters matrise','P₀ = 0, P₁ = 0 ve P₂ = 1 başlangıç değerlerini seçelim. Her yeni terimi Pₙ₊₃ = Pₙ₊₁ + Pₙ kuralıyla buluyoruz. Böylece ilk sekiz terim 0, 0, 1, 0, 1, 1, 1, 2 oluyor.','Aynı eşitliği Pₙ = Pₙ₊₃ − Pₙ₊₁ biçiminde yazınca sıfırın gerisine geçebiliriz. Örneğin P₋₁ = P₂ − P₀ = 1. Bir adım daha gidersek P₋₂ = P₁ − P₋₁ = −1 elde edilir. Çalışmalarımda bu geriye gidişin matris kuvvetleriyle ilişkisini inceliyorum.'),('benzerlik','Ders notu','İki üçgen ne zaman benzerdir?','Bir ortak açıdan sonra neye bakılır?','Birbirinden farklı iki dik üçgen çiz. Birinin dik kenarları 3 ve 4, diğerininkiler 3 ve 5 birim olsun. İkisinin de bir açısı 90° olduğu hâlde kısa dik kenarın uzun dik kenara oranları farklıdır. Tek bir açı benzerliği garanti etmez.','Şimdi uzunlukları 3 ve 4 olan dik kenarları iki katına çıkar. Yeni üçgende oran 6/8 = 3/4 olarak korunur. Dik kenarlar aynı oranda büyüdüğü ve aralarındaki açı aynı kaldığı için üçgenler kenar-açı-kenar yoluyla benzerdir.'),('uretim','Modelleme','Üretim %10 arttı. Ne kadarı sermayeden?','Cobb–Douglas ile bir atölye hesabı','Bir üretim modelinde K sermayeyi, L emeği göstersin. Y = A·Kᵅ·Lᵝ denkleminde, A sabitken iki girdiyi de iki katına çıkarırsak yeni üretim eski üretimin 2⁽ᵅ⁺ᵝ⁾ katı olur.','Örneğin α = 0,4 ve β = 0,6 için toplam 1 olur ve üretim iki katına çıkar. Bu kez her iki üssü de 0,4 seçersek çarpan 2⁰·⁸ ≈ 1,74 olur. Girdilerdeki aynı değişim, farklı ölçek getirileri doğurur.'),('altin-oran','Merak','Altın oran gerçekten her yerde mi?','Ayçiçeğinde evet, Mona Lisa’da pek değil','',''),('dogum-gunu','Olasılık','23 kişilik bir sınıfta iki doğum günü çakışır mı?','Sezginin yanıldığı bir olasılık','',''),('sonsuz-otel','Sonsuzluk','Dolu bir otele yeni misafir sığar mı?','Sonsuzlukla ilk tanışma','','')]
css="""*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;background:#f7f4eb;color:#203d35;font:16px/1.6 'DM Sans',Arial,sans-serif}main,header,footer{max-width:1230px;margin:auto;padding:0 5%}header,footer,.bar{display:flex;align-items:center;justify-content:space-between;gap:18px}header{height:78px;border-bottom:1px solid #c4c8b8}.brand{font:bold 22px Georgia,serif}nav{display:flex;gap:22px}a{color:inherit;text-decoration:none}a:hover{text-decoration:underline}h1,h2,h3{font-family:'Instrument Serif',Georgia,serif;font-weight:400;line-height:1.06;margin:0}.hero{display:grid;grid-template-columns:1.15fr 1fr;gap:6%;align-items:center;padding:52px 0}.hero svg{display:block;border-radius:50% 50% 3px 3px;aspect-ratio:1.22;width:100%}h1{font-size:clamp(54px,7vw,98px);letter-spacing:-.065em}em{color:#a64b32}.hero p,.intro{max-width:49ch}.cta{display:inline-block;margin-top:10px;background:#203d35;color:#fff;padding:11px 20px;border-radius:4px}.label{color:#8b432f;font-size:12px;font-weight:bold;letter-spacing:.1em;text-transform:uppercase}.collection,.about{border-top:1px solid #bdc2b2;padding:35px 0 49px}h2{font-size:clamp(32px,4vw,48px);letter-spacing:-.045em}.grid{display:grid;grid-template-columns:repeat(3,1fr);gap:23px;margin-top:26px}.card svg{width:100%;height:auto;display:block;margin-bottom:14px}.card h3{font-size:27px;margin:8px 0}.card small{font-size:14px}.about p,article p{max-width:65ch}.back{display:inline-block;margin:28px 0}.story{max-width:820px;margin:0 auto 50px}.story h1{font-size:clamp(43px,6vw,74px);margin:12px 0 24px}.story svg{width:100%;height:220px;display:block}.story p{font-family:Georgia,serif;font-size:20px}footer{border-top:1px solid #bdc2b2;padding-top:22px;padding-bottom:24px}a:focus-visible{outline:3px solid #a64b32;outline-offset:4px}@media(max-width:700px){header{height:62px}nav{gap:12px;font-size:14px}.hero{grid-template-columns:1fr;gap:26px;padding:36px 0}.hero svg{aspect-ratio:2;border-radius:100px 100px 3px 3px}.grid{grid-template-columns:1fr}.card svg{height:180px}.brand{font-size:19px}}"""
Path('style.css').write_text(css)
def page(title,body):
    return f'<!doctype html><html lang="tr"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{title} · Umut Köse</title><link rel="stylesheet" href="style.css"><header><a class="brand" href="index.html">Umut Köse<span style="color:#a64b32">.</span></a><nav><a href="index.html#icerikler">İçerikler</a><a href="index.html#hakkimda">Hakkımda</a></nav></header><main>{body}</main><footer><b>Umut Köse</b><a href="https://github.com/umutkose-stack">GitHub ↗</a></footer></html>'
cards=''
for i,(slug,category,title,sub,p,q) in enumerate(items):
    cards+=f'<a class="card" href="{slug}.html">{art(i)}<span class="label">{category}</span><h3>{title}</h3><small>{sub} ↗</small></a>'
    article = (Path(__file__).parent / "articles" / (slug + ".html")).read_text()
    Path(slug+'.html').write_text(page(title,f'<article class="story"><a class="back" href="index.html#icerikler">← Tüm içerikler</a><div class="label">{category}</div><h1>{title}</h1>{article}</article>'))
body=f'<section class="hero"><div><div class="label">Umut Köse / Kişisel portfolyo</div><h1>Matematik<br><em>atölyem.</em></h1><p>Ben Umut, matematik yüksek lisans öğrencisiyim. Matematikle uğraşmayı da, onu anlatmayı da çok seviyorum. Burada kısa yazılar, ders dosyaları ve araştırma notlarımı bulabilirsin.</p><a class="cta" href="#icerikler">İçerikleri keşfet ↓</a></div>{art(0)}</section><section class="collection" id="icerikler"><h2>Seçili içerikler</h2><div class="grid">{cards}</div></section><section class="about" id="hakkimda"><h2>Hakkımda</h2><p>Merhaba, ben bir matematik yüksek lisans öğrencisiyim. Hayatımın iki büyük tutkusu var: matematiği derinlemesine çalışmak ve öğrendiklerimi başkalarına anlatmak.</p><p>Burayı formüllerin arkasındaki hikâyeleri, şaşırtıcı örüntüleri ve günlük hayatın içindeki matematiği boğmadan, keyifle okuyabileceğin kısa yazılarla dolduruyorum.</p><p>Matematiğin yanında veriyle çalışan araçlar geliştiriyorum. Bunlardan biri BIST şirketlerinin finansal tablolarını incelemek için hazırladığım proje.</p><a href="https://umutkose-stack.github.io/bist-tablolar/"><u>BIST Tablolar’ı aç ↗</u></a></section>'
Path('index.html').write_text(page('Matematik atölyem',body))

from lessons import lessons

def question(prompt, answer):
    return f'<p>{prompt}</p><details><summary>Çözümü göster</summary><p>{answer}</p></details>'

def slider(label, low, high, step, initial):
    return f'<label>{label}<input type="range" min="{low}" max="{high}" step="{step}" value="{initial}"><b>{initial}</b></label>'

def lab(key, title, controls):
    return f'<section class="lab" data-lab="{key}"><h2>{title}</h2>{controls}<output aria-live="polite"></output></section><script src="studio.js" defer></script>'

extras = {
    'padovan': lab('padovan','Dizide gezin',slider('Terim indisi',-16,20,1,0)) + question('İndisi −3 yapmadan önce tahmin et. Hangi iki terimin farkını alırsın?', 'P₋₃ = P₀ − P₋₂ = 0 − (−1) = 1. Geri giderken çıkarma sırasını korumak önemlidir.'),
    'dogum-gunu': lab('dogum','Sınıfı büyüt',slider('Kişi sayısı',2,80,1,23)) + question('Sınıfta 23 kişi var. Senin doğum gününü paylaşan en az bir kişinin olması için sınıf kaç kişi olmalı ki olasılık %50’yi geçsin?', 'Senden başka n kişi için olasılık 1 − (364/365)ⁿ. Bunun 0,5’i geçmesi için n ≥ 253 gerekir. İlginç bir rastlantı: 23 kişilik sınıftaki ikili sayısı da 253’tür.'),
    'uretim': lab('uretim','Ölçeği dene',slider('Sermayenin üssü α',0,1,.05,.4)+slider('Emeğin üssü β',0,1,.05,.6)) + question('α ile β yer değiştirirse iki girdiyi birlikte ikiye katlamanın sonucu değişir mi?', 'Çarpan yine 2 üzeri (α + β) olur. Yalnızca sermayeyi ikiye katladığında ise çarpan 2 üzeri α olduğundan hangi üssün sermayeye ait olduğu önem kazanır.'),

}
for slug,extra in extras.items():
    path=Path(slug+'.html')
    path.write_text(path.read_text().replace('</article>',extra+'</article>'))

rows=''
SHOW_LESSONS = False  # Ders dosyaları şimdilik gizli; tekrar açmak için True yap
for slug,level,title,subtitle,p,a,q,b in (lessons if SHOW_LESSONS else []):
    rows+=f'<a class="lesson" href="{slug}.html"><span class="label">{level}</span><strong>{title}</strong><span aria-hidden="true">↗</span></a>'
    content=f'<article class="story"><a class="back" href="index.html#dersler">← Ders dosyaları</a><div class="label">{level}</div><h1>{title}</h1><p>{subtitle}</p><h2>Birlikte çözelim</h2>{question(p,a)}<h2>Sıra sende</h2>{question(q,b)}</article>'
    Path(slug+'.html').write_text(page(title,content))
if SHOW_LESSONS: body=body.replace('<section class="about"',f'<section class="collection" id="dersler"><h2>Ders dosyaları</h2>{rows}</section><section class="about"')
Path('index.html').write_text(page('Matematik atölyem',body))
with Path('style.css').open('a') as styles:
    styles.write("""
.lesson{display:grid;grid-template-columns:minmax(145px,1fr) 3fr auto;align-items:center;gap:18px;padding:20px 0;border-bottom:1px solid #c4c8b8}
.lesson strong{font:normal 25px Georgia,serif}.lesson:first-of-type{margin-top:18px}
.story h2{font-size:32px;margin-top:32px}.story details,.lab{padding:18px 22px;background:#eeeade;border-left:3px solid #a64b32}.story details p{margin-bottom:0}
summary{cursor:pointer;font-weight:bold}.lab{margin:30px 0}.lab h2{margin:0 0 15px}.lab label{display:flex;align-items:center;flex-wrap:wrap;gap:14px;padding:6px 0}.lab input{accent-color:#203d35}.lab output{display:block;font-weight:bold;margin-top:10px}
@media(max-width:620px){.lesson{grid-template-columns:1fr auto;gap:3px}.lesson .label{grid-column:1/-1}.lesson strong{font-size:22px}}
""")

with Path("style.css").open("a") as styles:
    styles.write(".matrices{display:flex;gap:2rem;flex-wrap:wrap}.matrices pre{font-size:18px;margin:5px 0}.story figure{margin:1rem 0;background:#eeeade;padding:12px}.story figcaption,.story caption{font-size:14px;text-align:left}.story table{width:100%;border-collapse:collapse}.story th,.story td{text-align:left;padding:6px;border-bottom:1px solid #bdc2b2}.story details+details{margin-top:12px}")
