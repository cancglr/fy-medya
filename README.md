# fy-medya

Flört AI'ın TikTok reel motoru ve yayın kuyruğu. Public depo: otomasyon buradaki
dosyaları anahtarsız, doğrudan ham adresten okuyabilsin diye.

## Klasörler

### `motor/`
Reelleri koddan üreten motor. Sahte Instagram DM sohbeti formatındaki dikey videoları
bir JSON kaydından 1080x1920 / 24 fps mp4 olarak basar. Canva veya elle kurgu yok.

```bash
cd motor
bash kur.sh              # playwright + chromium + fontlar
python3 render.py        # scripts.json içindeki her şeyi render eder
python3 render.py T01    # sadece tek bir id
```

Çıktılar `motor/out/` altına düşer ve git'e girmez.

Şablon, ritim, yerleşim ve süre sabitleri arşivdeki 63 organik reelin ölçülmesiyle
çıkarıldı. Bir reel nasıl tanımlanır, hangi alanlar ne yapar, hangi sabitlere
dokunulmaz: hepsi [`motor/README.md`](motor/README.md) içinde. Motorla çalışmadan önce
oradan başla.

### `videolar/`
Yayına hazır mp4'ler. Kuyruk burası: render edilip onaylanan videolar buraya taşınır,
otomasyon ham adresten çekip yayınlar.

Ham adres formatı:

```
https://raw.githubusercontent.com/cancglr/fy-medya/main/videolar/DOSYAADI.mp4
```

## Kural

Depo public kalır. İçine kimlik bilgisi, anahtar veya token konmaz.
