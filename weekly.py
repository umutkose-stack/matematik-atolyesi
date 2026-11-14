# Haftanın sorusu. Her hafta yalnızca bu dosyayı değiştir, sonra generate.py'yi çalıştır.
weekly = {
    'date': '14 Kasım 2026',
    'title': 'Köşeleri kesilmiş satranç tahtası',
    'question': '8 × 8’lik bir satranç tahtasının karşılıklı iki köşesindeki kareleri kesip atıyoruz. Geriye 62 kare kalıyor. Her biri yan yana iki kareyi kaplayan 31 domino taşıyla bu tahtayı boşluk bırakmadan ve taşırmadan kaplayabilir misin?',
    'hint': 'Tahtanın neden iki renkli olduğunu düşün. Bir domino taşı hangi renkten kaç kare örter?',
    'answer': 'Kaplayamazsın. Yan yana iki kare her zaman farklı renktedir, yani her domino taşı bir açık ve bir koyu kare örter. 31 taş, 31 açık ve 31 koyu kare örtmek zorundadır. Ama karşılıklı köşeler aynı renktedir: İkisi de kesilince tahtada bir renkten 32, diğerinden 30 kare kalır. Renk sayıları eşit olmadığı için hiçbir yerleştirme işe yaramaz. Denemeye gerek bırakmayan bir kanıt.',
    'figure': 'tahta',
}
