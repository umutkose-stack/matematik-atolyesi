lessons = [
    ("ebob-ekok", "LGS · Sayılar", "İki zil neden hiç buluşmasın?", "Bir başlangıç farkı, EKOK hesabının cevabını değiştirir.",
     "Bir düzenekte mavi zil 0. saniyeden başlayarak her 24 saniyede bir çalıyor. Turuncu zil ilk kez 6. saniyede çalıyor ve her 36 saniyede bir tekrarlanıyor. Bir öğrenci “EKOK 72, o hâlde 72. saniyede birlikte çalarlar” diyor. İddiayı önce 72. saniye için, sonra bütün zamanlar için sına.",
     "72. saniyede mavi çalar. Turuncunun ilk üç zamanı 6, 42, 78’dir. Daha güçlü bir sonuç da var: Mavinin her zamanı 12’nin katıdır. Turuncunun her zamanı 12’ye bölündüğünde 6 kalanını verir. Bu iki liste hiçbir zaman kesişmez.",
     "Turuncu zilin ilk çalma anını 6’dan 12’ye al. İlk ortak zaman nedir? Bundan sonra iki zil kaç saniyede bir yeniden buluşur?",
     "Mavi 0, 24, 48…; turuncu 12, 48… İlk buluşma 48. saniyede olur. Bu andan sonra her iki zilin de tam tur atacağı en kısa süre EKOK(24, 36) = 72 saniyedir. İkinci buluşma 120. saniyededir. İlk buluşma anı ile buluşmalar arasındaki süre farklı niceliklerdir."),
    ("dogrusal-model", "Lise · Fonksiyonlar", "Faturadan tarifeyi geri kurmak", "İki fiş bir doğru belirler. Üçüncü fiş varsayımı sınar.",
     "Bir bisikletçi 2 saat için 100 TL, 5 saat için 160 TL ödüyor. Ücretin sabit bir açılış bedeli ve sabit saat ücretinden oluştuğu varsayılırsa 8 saatlik fişte ne yazmalı?",
     "İki fiş arasında 3 saat ve 60 TL fark var. Açılış bedeli fark alınırken silinir; saat ücreti 20 TL’dir. İki saatlik fişten açılış bedeli 100 − 40 = 60 TL çıkar. Model 8 saat için 60 + 8 × 20 = 220 TL öngörür.",
     "Üçüncü fişte 8 saat için 200 TL yazıyor. Kasiyer günlük tavan uygulandığını söylüyor. Diğer koşullar aynıysa bu açıklama üç fişle uyumlu mu? Tavan ilk kaçıncı tam saatte devreye girer?",
     "200 TL’lik tavan üç fişle uyumludur. Ücret min(60 + 20x, 200) olur. 7 saatte doğrusal tutar 200’e ulaşır; tavanın ödenecek tutarı düşürdüğü ilk tam süre 8 saattir. Üç fiş bu açıklamayla uyuşur, ama tek başına indirim gibi başka açıklamaları elemez."),
    ("istatistik", "Lise · İstatistik", "Her iki grubun ortalaması artarken okulunki düşebilir mi?", "Bir deneme raporunu öğrenci sayılarıyla yeniden okumak",
     "Birinci denemeye A grubundan 8 öğrenci katılıyor ve ortalama 80. B grubundan 2 öğrenci katılıyor ve ortalama 40. İkinci denemede A grubundan 2 öğrenci ortalama 85, B grubundan 8 öğrenci ortalama 45 yapıyor. Önce okul ortalamasının yönünü tahmin et. Sonra puan toplamlarından hesapla.",
     "İlk denemede toplam 8 × 80 + 2 × 40 = 720 puan, ortalama 72. İkincide toplam 2 × 85 + 8 × 45 = 530 puan, ortalama 53. Her grup 5 puan yükselmiş. Ancak ikinci denemede katılımcıların çoğu ortalaması daha düşük olan gruptan geliyor.",
     "İkinci denemenin grup ortalamalarını koruyup katılım ağırlıklarını ilk denemedeki gibi %80 A ve %20 B alırsan ne bulursun? Buradan her öğrencinin geliştiği çıkar mı?",
     "0,8 × 85 + 0,2 × 45 = 77. Aynı ağırlıklarla karşılaştırınca 72’den 77’ye çıkış görülür. Bu, grup ortalamalarındaki artışı özetler. Tek tek öğrencilerin gelişimi için iki denemeye de giren öğrencilerin eşleştirilmiş sonuçlarına ihtiyaç vardır.")
]
