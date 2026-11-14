from math import sin,cos,pi
from pathlib import Path
import os, sys
sys.path.insert(0, str(Path(__file__).resolve().parent))
# Çıktılar her zaman dist/ klasörüne yazılır; kökteki index.html (yönlendirme) korunur.
os.chdir(Path(__file__).resolve().parent / 'dist')
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
css="""*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;background:#f7f4eb;color:#203d35;font:16px/1.6 'DM Sans',Arial,sans-serif}main,header,footer{max-width:1230px;margin:auto;padding:0 5%}header,footer,.bar{display:flex;align-items:center;justify-content:space-between;gap:18px}header{height:78px;border-bottom:1px solid #c4c8b8}.brand{font:bold 22px Georgia,serif}nav{display:flex;gap:22px}a{color:inherit;text-decoration:none}a:hover{text-decoration:underline}h1,h2,h3{font-family:'Instrument Serif',Georgia,serif;font-weight:400;line-height:1.06;margin:0}.hero{display:grid;grid-template-columns:1.15fr 1fr;gap:6%;align-items:center;padding:52px 0}.hero svg{display:block;border-radius:50% 50% 3px 3px;aspect-ratio:1.22;width:100%}h1{font-size:clamp(54px,7vw,98px);letter-spacing:-.065em}em{color:#a64b32}.hero p,.intro{max-width:49ch}.cta{display:inline-block;margin-top:10px;background:#203d35;color:#fff;padding:11px 20px;border-radius:4px}.label{color:#8b432f;font-size:12px;font-weight:bold;letter-spacing:.1em;text-transform:uppercase}.feats{display:grid;grid-template-columns:repeat(6,1fr);gap:23px;margin-top:26px}.feat{grid-column:span 2;background:#eeeade;padding:24px 24px 20px;border-top:3px solid #203d35}.feat.stat{grid-column:span 3;border-top-color:#a64b32}.feat .big{display:block;font:400 clamp(56px,6vw,84px)/1 'Instrument Serif',Georgia,serif;letter-spacing:-.04em;color:#a64b32;margin-bottom:6px}.feat h3{font-size:27px;margin:0 0 8px}.feat p{margin:0;max-width:52ch}.steps{list-style:none;padding:0;margin:26px 0 0;display:grid;grid-template-columns:repeat(3,1fr);gap:34px}.steps li{border-top:1px solid #203d35;padding-top:16px}.step-n{display:block;font:400 64px/1 'Instrument Serif',Georgia,serif;color:#a64b32;margin-bottom:10px}.steps h3{font-size:27px;margin:0 0 10px}.steps p{margin:0}.contact{background:#203d35;color:#f7f4eb;padding:48px 6%;margin:20px 0 49px}.contact h2{color:#f7f4eb}.contact p{max-width:58ch}.contact .phone{font-size:20px}.contact .phone a{text-decoration:underline;text-underline-offset:4px}.cta.light{background:#f7f4eb;color:#203d35}.foot-links{display:flex;gap:20px}@media(max-width:900px){.feats{grid-template-columns:1fr 1fr}.feat,.feat.stat{grid-column:auto}.steps{grid-template-columns:1fr;gap:22px}}@media(max-width:560px){.feats{grid-template-columns:1fr}}
.orgs{margin-top:34px;display:grid;grid-template-columns:1fr;gap:12px;border-top:1px solid #203d35;padding-top:18px}.orgs h3{font-size:22px;color:#8b432f}.orgs ul{list-style:none;margin:0;padding:0;display:flex;flex-wrap:wrap;gap:10px 0}.orgs li{font:400 28px/1.2 'Instrument Serif',Georgia,serif;padding:0 26px;border-left:1px solid #bdc2b2}.orgs li:first-child{border-left:0;padding-left:0}@media(max-width:700px){.orgs{grid-template-columns:1fr;gap:10px}.orgs li{font-size:23px;padding:0 16px}}.exam-tabs{display:grid;grid-template-columns:repeat(3,1fr);gap:23px;margin:26px 0 0}.exam-tabs button{font:inherit;text-align:left;color:#203d35;background:transparent;border:0;border-top:3px solid #c4c8b8;padding:18px 24px 20px;cursor:pointer;display:flex;flex-direction:column;gap:4px;transition:background .2s,border-color .2s}.exam-tabs button strong{font:400 32px/1.1 'Instrument Serif',Georgia,serif;letter-spacing:-.02em}.exam-tabs button:hover{background:#eeeade}.exam-tabs button[aria-selected=true]{background:#eeeade;border-top-color:#a64b32}.exam-tabs button:focus-visible{outline:3px solid #a64b32;outline-offset:3px}@media(max-width:760px){.exam-tabs{grid-template-columns:1fr;gap:10px}.exam-tabs button{padding:14px 18px}.exam-tabs button strong{font-size:26px}}.exam-panel{display:grid;grid-template-columns:1fr 1fr;gap:44px;padding:34px 0 6px}.exam-panel[hidden]{display:none}.exam-panel h3{font-size:34px;margin:0 0 12px}.exam-panel p{margin:0 0 14px;max-width:52ch}.exam-panel .proof{display:inline-block;background:#eeeade;border-left:3px solid #a64b32;padding:8px 14px;font-size:15px}.exam-panel ul{margin:0;padding:0;list-style:none}.exam-panel li{padding:12px 0 12px 26px;border-bottom:1px solid #c4c8b8;position:relative}.exam-panel li::before{content:'';position:absolute;left:4px;top:calc(50% - 6px);width:9px;height:9px;border:2px solid #a64b32;border-radius:50%}@media(max-width:760px){.exam-panel{grid-template-columns:1fr;gap:16px}}.weekly-grid{display:grid;grid-template-columns:minmax(0,3fr) minmax(0,2fr);gap:44px;align-items:start;margin-top:18px}.weekly-grid figure{margin:0;text-align:center}.weekly-grid svg{display:block;width:100%;max-width:300px;margin:0 auto}.weekly h3{font-size:30px}.weekly p{max-width:60ch}.weekly details{margin-top:12px}@media(max-width:760px){.weekly-grid{grid-template-columns:1fr;gap:20px}}
.collection,.about{border-top:1px solid #bdc2b2;padding:35px 0 49px}h2{font-size:clamp(32px,4vw,48px);letter-spacing:-.045em}.grid{display:grid;grid-template-columns:repeat(3,1fr);gap:23px;margin-top:26px}.card svg{width:100%;height:auto;display:block;margin-bottom:14px}.card h3{font-size:27px;margin:8px 0}.card small{font-size:14px}.about p,article p{max-width:65ch}.back{display:inline-block;margin:28px 0}.story{max-width:820px;margin:0 auto 50px}.story h1{font-size:clamp(43px,6vw,74px);margin:12px 0 24px}.story svg{width:100%;height:220px;display:block}.story p{font-family:Georgia,serif;font-size:20px}footer{border-top:1px solid #bdc2b2;padding-top:22px;padding-bottom:24px}a:focus-visible{outline:3px solid #a64b32;outline-offset:4px}@media(max-width:700px){header{height:62px}nav{gap:12px;font-size:14px}.hero{grid-template-columns:1fr;gap:26px;padding:36px 0}.hero svg{aspect-ratio:2;border-radius:100px 100px 3px 3px}.grid{grid-template-columns:1fr}.card svg{height:180px}.brand{font-size:19px}}"""
Path('style.css').write_text(css)
SITE_URL='https://umutkose-stack.github.io/matematik-atolyesi/'
# Yayına hazır olunca True yap: arama motorları siteyi indeksleyebilir.
INDEXABLE=False
ROBOTS='' if INDEXABLE else '<meta name="robots" content="noindex, nofollow">'
SITE_DESC='ODTÜ Matematik mezunu ve ICF akreditasyonlu eğitim koçu Umut Köse ile ezberlemeden, mantığıyla matematik: birebir dersler, sınav hazırlığı ve süreç takibi.'
def meta(title,desc=SITE_DESC,path=''):
    t=f'{title} · Umut Köse'
    return (ROBOTS+f'<meta name="description" content="{desc}"><link rel="canonical" href="{SITE_URL}{path}">'
      f'<meta property="og:type" content="website"><meta property="og:site_name" content="Matematik Atölyesi">'
      f'<meta property="og:title" content="{t}"><meta property="og:description" content="{desc}">'
      f'<meta property="og:url" content="{SITE_URL}{path}"><meta property="og:image" content="{SITE_URL}og.png">'
      f'<meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta property="og:locale" content="tr_TR">'
      f'<meta name="twitter:card" content="summary_large_image">')
def page(title,body,desc=SITE_DESC,path=''):
    return f'<!doctype html><html lang="tr"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{title} · Umut Köse</title>{meta(title,desc,path)}<link rel="stylesheet" href="style.css"><header><a class="brand" href="index.html">Umut Köse<span style="color:#a64b32">.</span></a><nav><a href="index.html#hakkimda">Hakkımda</a><a href="index.html#sinavlar">Sınavlar</a><a href="index.html#yaklasim">Yaklaşım</a><a href="index.html#icerikler">Yazılar</a><a href="index.html#iletisim">İletişim</a></nav></header><main>{body}</main><footer><b>Umut Köse</b><span class="foot-links"><a href="https://umutkose-stack.github.io/bist-tablolar/">BIST Tablolar ↗</a><a href="https://github.com/umutkose-stack">GitHub ↗</a></span></footer></html>'
cards=''
for i,(slug,category,title,sub,p,q) in enumerate(items):
    cards+=f'<a class="card" href="{slug}.html">{art(i)}<span class="label">{category}</span><h3>{title}</h3><small>{sub} ↗</small></a>'
    article = (Path(__file__).parent / "articles" / (slug + ".html")).read_text()
    Path(slug+'.html').write_text(page(title,desc=f'{sub}. Matematik Atölyesi’nden kısa bir yazı.',path=slug+'.html',body=f'<article class="story"><a class="back" href="index.html#icerikler">← Tüm yazılar</a><div class="label">{category}</div><h1>{title}</h1>{article}</article>'))
# İletişim: numara eklenince aşağıdaki üç değeri doldur, bölüm kendiliğinden güncellenir.
PHONE_DISPLAY=''; PHONE_TEL=''; WHATSAPP=''
contact_html=(f'<p class="phone">Telefon / WhatsApp: <a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></p><a class="cta light" href="{WHATSAPP}">WhatsApp’tan yaz</a>' if PHONE_DISPLAY else '<p class="phone">İletişim bilgileri çok yakında burada olacak.</p>')
feats=[('stat','10+','Yıl eğitim deneyimi','Online ve yüz yüze birebir derslerde, farklı seviye ve hedeflere yönelik kişiselleştirilmiş matematik eğitimi.'),
 ('stat','100.000+','Dakika online ders','Yalnızca inekle.com platformunda gerçekleştirilen aktif birebir ders tecrübesi.'),
 ('','','Derece ve üniversite başarıları','LGS Türkiye birincisini çıkaran eğitim kadrosunda yer aldım. Lise gruplarında ODTÜ, Boğaziçi ve Koç gibi üniversitelere yerleşen öğrenciler yetiştirdim.'),
 ('','','Müfredat ve yayın hâkimiyeti','Sınav Koleji, Palme Yayınevi soru çözümleri ve Sebit bünyesindeki müfredat çalışmalarıyla öğrencilerin en sık zorlandığı noktalara doğrudan çözüm.'),
 ('','','Uluslararası deneyim','İngiltere ve Almanya’dan öğrencilere, IB ve SAT’e hazırlanan öğrencilere ders verdim. Münster Üniversitesi ve Friedrich-Alexander Üniversitesi’nden (FAU) aldığım Data Science ve Matematik yüksek lisans kabulleri, yurt dışında eğitim hedefleyen öğrencilere de yol göstermemi sağlıyor.')]
ORGS=['Sebit','Sınav Koleji','Özel Artı Analiz','Palme Yayınevi','inekle.com']
orgs_html=''.join(f'<li>{o}</li>' for o in ORGS)
EXAMS=[('lgs','LGS','Yeni nesil soruları okumayı öğrenmek',
  'LGS’de soruların çoğu uzun bir metnin, tablonun ya da grafiğin içine yerleştirilmiş durumda. Önce soruyu doğru okumayı, sonra hangi bilginin işe yarayacağını seçmeyi birlikte çalışıyoruz.',
  ['Yeni nesil soruları okuma ve metinden matematiksel modeli çıkarma','Deneme sonuçlarına göre konu eksiklerini belirleme ve hedefli tekrar','Düzenli ödev takibi, odaklanma ve süre yönetimi','Gelişim hakkında veliyle düzenli bilgilendirme'],
  'LGS’de Türkiye birincisi çıkaran eğitim kadrosu deneyimi'),
 ('yks','YKS (TYT – AYT)','TYT’de hız, AYT’de derinlik',
  'TYT’de temeli sağlam ve hızlı kurmayı, AYT’de ise konuların arkasındaki mantığı kavrayıp zor sorulara yorum gücüyle yaklaşmayı hedefliyoruz.',
  ['TYT için temel konuların ve problem tiplerinin sistemli tekrarı','AYT’de fonksiyonlar, limit, türev ve integralde kavramsal derinleşme','Deneme analizine göre şekillenen haftalık çalışma programı','Hedef üniversite ve bölüme göre net planlaması'],
  'ODTÜ, Boğaziçi ve Koç gibi üniversitelere yerleşen öğrenciler'),
 ('ib-sat','IB & SAT','İngilizce matematik, uluslararası bakış',
  'Uluslararası programlarda başarı, konuyu bilmek kadar soruyu İngilizce terminolojiyle doğru okumaya da bağlı. Dersleri öğrencinin programına ve sınav takvimine göre planlıyoruz.',
  ['IB matematik müfredatına uygun konu anlatımı ve sınav pratiği','SAT Math için soru tipleri, hız ve strateji çalışması','İngilizce matematik terminolojisine hâkimiyet','Yurt dışında eğitim hedefleyen öğrencilere akademik yol gösterme'],
  'İngiltere ve Almanya’dan öğrencilerle online ders deneyimi')]
AUD={'lgs':'Ortaokul','yks':'Lise','ib-sat':'Uluslararası'}
tab_btns=''.join(f'<button type="button" role="tab" id="tab-{k}" aria-controls="panel-{k}" aria-selected="{"true" if i==0 else "false"}" tabindex="{0 if i==0 else -1}"><span class="label">{AUD[k]}</span><strong>{n}</strong></button>' for i,(k,n,*_) in enumerate(EXAMS))
tab_panels=''.join(f'<div class="exam-panel" role="tabpanel" id="panel-{k}" aria-labelledby="tab-{k}"><div><h3>{t}</h3><p>{d}</p><p class="proof">{proof}</p></div><ul>'+''.join(f'<li>{x}</li>' for x in pts)+'</ul></div>' for k,n,t,d,pts,proof in EXAMS)
exams_html=(f'<section class="collection" id="sinavlar"><h2>Hangi sınava hazırlanıyorsunuz?</h2><div class="exam-tabs" role="tablist" aria-label="Sınav grupları">{tab_btns}</div>{tab_panels}'
 '<script>(function(){var t=[].slice.call(document.querySelectorAll(\'.exam-tabs [role=tab]\'));function sel(b,f){t.forEach(function(x){var on=x===b;x.setAttribute(\'aria-selected\',on);x.tabIndex=on?0:-1;document.getElementById(x.getAttribute(\'aria-controls\')).hidden=!on;});if(f)b.focus();}'
 't.forEach(function(b,i){b.addEventListener(\'click\',function(){sel(b)});b.addEventListener(\'keydown\',function(e){var j=e.key===\'ArrowRight\'?i+1:e.key===\'ArrowLeft\'?i-1:-1;if(j<0&&e.key!==\'ArrowLeft\')return;e.preventDefault();sel(t[(j+t.length)%t.length],true);});});sel(t[0]);})();</script></section>')
feat_html=''.join(f'<div class="feat {k}">'+(f'<strong class="big">{n}</strong>' if n else '')+f'<h3>{t}</h3><p>{d}</p></div>' for k,n,t,d in feats)
steps=[('İlk değerlendirme ve yol haritası','İlk görüşmede öğrencimizin mevcut durumunu, zorlandığı konuları ve hedeflerini birlikte değerlendiriyor; ardından tamamen kendisine özel bir çalışma planı oluşturuyoruz.'),
 ('Etkileşimli ve sadeleştirilmiş ders işleyişi','Kurumsal müfredat ve yayın deneyiminin getirdiği birikimle karmaşık konuları öğrencinin ihtiyacına göre sadeleştiriyor, online dersleri aktif ve verimli bir çalışma ortamına dönüştürüyorum.'),
 ('ICF akreditasyonlu süreç takibi','Eğitim koçluğu yetkinliğim doğrultusunda yalnızca ders saatlerini değil, öğrencinin genel çalışma disiplinini de takip ediyorum. Haftalık programını birlikte hazırlıyor, seviyesine uygun kaynakları belirliyor ve gelişimi hakkında aileyle düzenli iletişim kuruyorum.')]
step_html=''.join(f'<li><span class="step-n">{i}</span><h3>{t}</h3><p>{d}</p></li>' for i,(t,d) in enumerate(steps,1))
body=(f'<section class="hero"><div><div class="label">Birebir matematik dersi ve eğitim koçluğu</div><h1>Matematiği ezberlemeden,<br><em>mantığıyla kavrayın.</em></h1>'
 f'<p>ODTÜ Matematik Bölümü mezunu ve ICF akreditasyonlu eğitim koçu Umut Köse ile kişiye özel matematik dersleri, sınav hazırlığı ve akademik süreç takibi.</p>'
 f'<a class="cta" href="#iletisim">Ön görüşme planla</a></div>{art(0)}</section>'
 f'<section class="about" id="hakkimda"><h2>Hakkımda</h2>'
 f'<p>Ben Umut Köse. ODTÜ Matematik Bölümü mezunuyum ve on yılı aşkın süredir online ve yüz yüze derslerle öğrencileri sınavlara hazırlıyorum.</p>'
 f'<p>Her öğrencinin öğrenme biçiminin, motivasyonunun ve ihtiyaçlarının farklı olduğuna inanıyor; derslerimi öğrencinin seviyesine ve hedeflerine göre şekillendiriyorum. Yeni nesil soruların yapısına ve sınav sistemine hâkim olmanın yanında, öğrencilerin yalnızca soru çözmesini değil, sorunun arkasındaki mantığı anlamasını önemsiyorum.</p>'
 f'<p>Münster Üniversitesi ve Friedrich-Alexander Üniversitesi’nden Data Science ve Matematik alanlarında yüksek lisans kabulleri almış olmam sayesinde, öğrencilerime yalnızca sınav odaklı değil; akademik gelişim ve yurt dışı eğitim seçeneklerini de kapsayan daha geniş bir bakış açısı sunuyorum.</p></section>'
 f'<section class="collection" id="deneyim"><h2>Deneyim ve yetkinlikler</h2><div class="feats">{feat_html}</div><div class="orgs"><h3>Çalıştığım kurumlar</h3><ul>{orgs_html}</ul></div></section>'
 +exams_html+f'<section class="collection" id="yaklasim"><h2>Eğitim ve koçluk yaklaşımı</h2><ol class="steps">{step_html}</ol></section>'
 f'<section class="collection" id="icerikler"><h2>Okumalık yazılar</h2><p class="intro">Formüllerin arkasındaki hikâyeler ve şaşırtıcı örüntüler üzerine kısa yazılar.</p><div class="grid">{cards}</div></section>'
 f'<section class="contact" id="iletisim"><h2>Süreci birlikte planlayalım</h2><p>Öğrencimizin mevcut durumunu ve hedeflerini değerlendireceğimiz kısa bir ön görüşme için iletişime geçebilirsiniz.</p>'
 f'{contact_html}</section>')
Path('index.html').write_text(page('Birebir matematik dersi ve eğitim koçluğu',body))

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
from weekly import weekly
def board_svg():
    cells=[]
    for r in range(8):
        for c in range(8):
            if (r,c) in ((0,0),(7,7)): continue
            fill='#203d35' if (r+c)%2==0 else '#e6e2d0'
            cells.append(f'<rect x="{c*30}" y="{r*30}" width="30" height="30" fill="{fill}"/>')
    cells.append('<g fill="none" stroke="#a64b32" stroke-width="2" stroke-dasharray="4 3"><rect x="1" y="1" width="28" height="28"/><rect x="211" y="211" width="28" height="28"/></g>')
    return '<svg viewBox="0 0 240 240" role="img" aria-label="Karşılıklı iki köşesi kesilmiş 8×8 satranç tahtası. Kesilen iki köşe de koyu renkli.">'+''.join(cells)+'</svg>'
fig={'tahta':board_svg}.get(weekly.get('figure'),lambda:'')()
weekly_html=(f'<section class="collection weekly" id="haftanin-sorusu"><h2>Haftanın sorusu</h2><div class="weekly-grid"><div>'
  f'<div class="label">{weekly["date"]}</div><h3>{weekly["title"]}</h3><p>{weekly["question"]}</p>'
  f'<details><summary>İpucu</summary><p>{weekly["hint"]}</p></details>'
  f'<details><summary>Çözümü göster</summary><p>{weekly["answer"]}</p></details></div>'
  +(f'<figure>{fig}<figcaption>Kesilen köşeler kesik çizgiyle gösterildi.</figcaption></figure>' if fig else '')+'</div></section>')
body=body.replace('<section class="contact"',weekly_html+'<section class="contact"',1)
Path('index.html').write_text(page('Birebir matematik dersi ve eğitim koçluğu',body))
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

# Eski /dist/ adreslerini yeni köke yönlendir (GitHub Actions yayınında dist/ içeriği kökte durur)
Path('dist').mkdir(exist_ok=True)
Path('dist/index.html').write_text('<!doctype html><meta charset="utf-8"><title>Taşındı</title>'+ROBOTS+'<meta http-equiv="refresh" content="0; url=../"><link rel="canonical" href="'+SITE_URL+'"><a href="../">Siteye git</a>')
Path('404.html').write_text('<!doctype html><html lang="tr"><meta charset="utf-8"><title>Sayfa bulunamadı · Umut Köse</title>'+ROBOTS+'<script>var p=location.pathname;if(p.indexOf("/dist/")>-1){location.replace(p.replace("/dist/","/")+location.hash);}</script><body style="font:16px/1.6 Arial,sans-serif;background:#f7f4eb;color:#203d35;padding:10vh 8%"><h1 style="font:400 48px Georgia,serif">Bu sayfa bulunamadı</h1><p><a href="'+SITE_URL+'">Ana sayfaya dön</a></p></body></html>')
