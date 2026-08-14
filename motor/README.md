# Flört AI — organik reel motoru

Sahte Instagram DM sohbeti formatındaki dikey reelleri **koddan** üretir. Canva yok, elle
kurgu yok: bir JSON yazıyorsun, karşılığında 1080×1920 / 24 fps mp4 çıkıyor.

Şablon, ritim ve yerleşim `FLÖRT Aİ REELS` arşivindeki 63 organik reelin (790 tasarım karesi)
ve yayınlanmış 77 videonun ölçülmesiyle çıkarıldı. Sayılar tahmin değil, ölçüm.

---

## Kurulum

```bash
bash kur.sh
python3 render.py            # scripts.json içindeki her şeyi render eder
python3 render.py T01 T03    # sadece belirli id'leri
```

Gereken: `python3`, `ffmpeg`, `curl`. `kur.sh` playwright + chromium + fontları hallediyor.
Çıktılar `out/` klasörüne düşer.

---

## Dosyalar

| Dosya | Ne işe yarar |
|---|---|
| `template.html` | Şablonun kendisi. Sohbet sahnesi, meme sahnesi, uygulama ekranı, animasyon zaman çizelgesi. |
| `render.py` | Playwright ile kare basar, ffmpeg ile mp4'e çevirir. |
| `scripts.json` | İçerik. Her kayıt bir reel. |
| `photos/havuz/` | Hikaye fotoğrafı havuzu (arşivden çıkarıldı), `index.json` içinde seviye etiketleri. |
| `memes/` | Meme kütüphanesi. `hazir_*` = üstünde manşet olanlar, diğerleri temiz fotoğraf. |
| `arsiv-script-kutuphanesi.json` | 63 eski reelin kare kare çözümü — kanca, replik, punchline, final. Yeni şaka yazarken kaynak. |

---

## Bir reel nasıl tanımlanır

```jsonc
{
  "id": "T01",
  "slug": "kahve",
  "spice": 1,                    // 0-3, cesaret seviyesi (öğrenme etiketi)
  "son": "randevu",              // numara | randevu | gülme | fail  (öğrenme etiketi)
  "photo": "photos/T01.jpg",     // hikaye fotoğrafı
  "suggestion": "Çünkü insanı ayakta tutan şey\nkarşısındaki",   // ⚡ hapındaki replik
  "appAfter": 5,                 // uygulama ekranı hangi birimden sonra girsin
  "zoomFrom": 7,                 // punchline zoom'u hangi birimde başlasın
  "endHold": 1.2,
  "messages": [
    { "from": "u", "text": "Sen kahve içmiyorsundur" },
    { "from": "g", "text": "Neden ki" },
    { "from": "u", "text": "karşısındaki", "rx": "❤️" }
  ],
  "memes": [
    { "after": 2, "src": "memes/terim_ciddi.jpg", "chip": "Sebebi var", "hold": 1.25 },
    { "after": 7, "src": "memes/hazir_ibre.jpg", "hold": 1.35 },
    { "after": 12, "src": "memes/terim_stadyum.jpg",
      "label": "Son dakika", "head": "İMZA\nTAMAM", "yellow": true, "headSize": 118 }
  ]
}
```

**Birim (unit) numaralandırması:** 0 = hikaye başlığı + fotoğraf, 1 = ilk mesaj, 2 = ikinci mesaj…
`appAfter` ve `memes[].after` bu numarayı kullanır. `after: -1` videonun en başına koyar
(soğuk açılış — arşiv ölçümüne göre önerilmez).

**Mesaj alanları:** `from` = `u` (kullanıcı, sağda pembe) veya `g` (kız, solda mor).
`rx` = balonun altına düşen emoji reaksiyonu. Metinde `█` karakterleri sansür bandına dönüşür.

**Meme alanları:** `chip` = ortada siyah kutulu beyaz altyazı. `label` + `head` = kırmızı
etiket + Anton fontuyla dev manşet (haber kartı stili). `yellow: true` manşeti sarı yapar.

---

## Ölçülmüş sabitler — bunlara dokunma

Bunlar arşivden çıkarıldı, keyfi değil:

- **Beat: 1,55 sn.** Her mesaj ~1,0 sn sabit durur, ~0,55 sn yukarı kayar. Dört ayrı
  yayınlanmış videoda ölçüldü, sapma yok.
- **Uygulama ekranı videonun ortasında.** 63 reelin 63'ünde var, medyan konum %50.
- **Uygulama ekranı bant halinde**, tam ekran değil: kadrajın ~%60'ı, ortalanmış.
  Orijinallerde %63 / üstte %11 boşluk.
- **İlk meme ~2,5. saniyede**, en başta değil. Önce bir mesaj alışverişi olur.
  Sonra ortalama her 5 saniyede bir meme.
- **Meme duruşu 1,25–1,5 sn.**
- **Süre hedefi 20–26 sn.** Arşiv ortalaması 30 sn'ydi, TikTok için kısaltıldı.
- **Altyazı: ortada, siyah kutu, ~74 px.** Sol alt köşe okunmuyor.

---

## Ton

**Kullanıcı:** kısa, noktalama yok, özgüvenli. Asla açıklama yapmaz, terslemeye üstüne
giderek cevap verir. Punchline'ın %92'si ondan gelir.

**Kız:** bilinçli yazım hataları (`beğendinmi`, `sanıyon`, `Anlamadımmm`), klavye kahkahası
(`ahsjdjshd`, `AHAHAHHSHSHSH`), kapanışta emoji teslimiyeti (🫠 🥹).

**Kalıp:** hikaye yanıtı → bağlamsız cüretkâr kanca → kızın direnci → ⚡ uygulama ekranı →
yapıştır → kızın kırılması → ödül (numara %56, randevu %16).

**Meme kuralı:** her meme ya bir önceki repliğe tepki ya da bir sonrakine hazırlık olmalı.
Dolgu meme koyma.

---

## Öğrenme

`spice`, `son`, `tema` alanları performans ölçümü için var. Her reel etiketli veri olarak
doğduğu için "hangi değişken kazanıyor" sorusu cevaplanabiliyor — Canva'da üretilseydi
cevaplanamazdı. Yaklaşık 30 videodan sonra yön, 60-80'de güvenilir sinyal çıkar.
