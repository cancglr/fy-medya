#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""tavlamauzman icin 10 yeni reel — scripts.json'a ekler."""
import json, io
from pathlib import Path

B = Path(__file__).parent
COM = dict(appAfter=5, zoomFrom=8, endHold=1.2,
           muzik="muzik/bed.mp3", muzikBaslangic=14, muzikSes=0.85,
           hesap="tavlamauzman", baslik_tipi="punchline")

H1 = "#flört #sevgili #tinder #flörttaktikleri #flörtai"
H2 = "#flört #manita #sohbet #keşfet #flörtai"
H3 = "#flört #sohbet #sevgili #tinder #flörtai"
SEP = " • • • • • "

def u(t, rx=None):
    d = {"from": "u", "text": t}
    if rx: d["rx"] = rx
    return d
def g(t):
    return {"from": "g", "text": t}
def chip(after, src, text):
    return {"after": after, "src": f"memes/{src}.jpg", "chip": text, "style": "alt", "hold": 1.25}
def ibre(after=7):
    return {"after": after, "src": "memes/hazir_ibre.jpg", "hold": 1.35}
def plain(after, src, hold=1.3):
    return {"after": after, "src": f"memes/{src}.jpg", "hold": hold}
def manset(after, head, hold=1.6):
    return {"after": after, "src": "memes/terim_stadyum.jpg", "label": "Son dakika",
            "head": head, "yellow": True, "headSize": 118, "headBottom": 48, "hold": hold}

R = []

# ---------------------------------------------------------------- T15 ofsayt
R.append(dict(COM, id="T15", slug="ofsayt", tema="futbol göndermesi", spice=2, son="numara",
    photo="photos/havuz/P54.jpg",
    suggestion="Sana bakarken hattı geçmişim,\nbayrak kalktı",
    messages=[u("Ofsayta düştüm"), g("Ne"), g("Kimsin sen"),
              u("Hikayeni açtım"), g("Ee"),
              u("Sana bakarken hattı geçmişim"), u("bayrak kalktı"),
              g("ahsjdjshd"), g("futbolcu musun sen"),
              u("Forvet"), g("0533 ███ ██ ██"), g("gol at bakalım")],
    memes=[chip(2, "terim_ciddi", "Pozisyon şüpheli"),
           chip(5, "hoca_saha", "Bayrak hazır"),
           ibre(),
           chip(9, "gunes_isaret", "Forvetmiş"),
           plain(11, "kapak_kral", 1.6)],
    baslik="Bayrak kalktı" + SEP + H1))

# ----------------------------------------------------------------- T16 taksi
R.append(dict(COM, id="T16", slug="taksi", tema="kelime oyunu", spice=2, son="numara",
    photo="photos/havuz/P29.jpg",
    suggestion="Hikayene bakalı on dakika oldu,\nborç birikti",
    messages=[u("Taksimetre açık"), g("Ne taksimetresi"), g("Taksici misin sen"),
              u("Sayaç dönüyor ama"), g("Neyin sayacı"),
              u("Hikayene bakalı on dakika oldu"), u("borç birikti"),
              g("AHAHAHSHSH"), g("ödemem ben"),
              u("Taksit yaparız"), g("0546 ███ ██ ██"), g("hesabı gönder bakalım")],
    memes=[chip(2, "gunes_selam", "Buyurun abi"),
           chip(5, "terim_ciddi", "Sayaç işliyor"),
           ibre(),
           plain(9, "hazir_aceleci"),
           plain(11, "kapak_arda", 1.6)],
    baslik="Sayaç döndü" + SEP + H2))

# ------------------------------------------------------------------ T17 hava
R.append(dict(COM, id="T17", slug="hava", tema="kelime oyunu", spice=1, son="randevu",
    photo="photos/havuz/P28.jpg",
    suggestion="Güneş öğlen çıkar demişlerdi,\nsen üçte çıktın",
    messages=[u("Bugün tahmin tutmadı"), g("Ne tahmini"), g("Yağmur mu yağdı"),
              u("Meteoroloji yanıldı"), g("Nerede yanıldı"),
              u("Güneş öğlen çıkar demişlerdi"), u("sen üçte çıktın"),
              g("hshshshs"), g("meteorolojici misin"),
              u("Yarını da biliyorum"), g("cumartesi görüşürüz o zaman")],
    memes=[chip(2, "terim_ciddi", "Hava kapalı"),
           chip(5, "hoca_saha", "Güneş geliyor"),
           ibre(),
           chip(9, "gunes_isaret", "Güneş burada"),
           manset(11, "RANDEVU\nTAMAM")],
    baslik="Tahmin tuttu" + SEP + H3))

# ---------------------------------------------------------------- T18 market
R.append(dict(COM, id="T18", slug="market", tema="özgüven", spice=2, son="numara",
    photo="photos/havuz/P11.jpg",
    suggestion="Senin gibisinin fiyatı yokmuş,\nsistemde kayıtlı değil",
    messages=[u("Kasada sıkıntı çıktı"), g("Ne kasası"), g("Beni mi diyorsun"),
              u("Barkod okumadı"), g("Neyin barkodu"),
              u("Senin gibisinin fiyatı yokmuş"), u("sistemde kayıtlı değil"),
              g("AHAHAHSHSH"), g("eşya mıyım ben"),
              u("Sınırlı üretim"), g("0507 ███ ██ ██"), g("stoğu kontrol et bakalım")],
    memes=[chip(2, "arda_panik", "Kasada kaldık"),
           chip(5, "terim_ciddi", "Fiyat soruluyor"),
           ibre(),
           plain(9, "hazir_havaya"),
           plain(11, "kapak_kral", 1.6)],
    baslik="Stokta yok" + SEP + H1))

# ----------------------------------------------------------------- T19 kredi
R.append(dict(COM, id="T19", slug="kredi", tema="kelime oyunu", spice=1, son="randevu",
    photo="photos/havuz/P45.jpg",
    suggestion="Değerlendirdim, teminat istemedim,\nyüzün yeterli",
    messages=[u("Başvurun onaylandı"), g("Ne başvurusu"), g("Ben bir şey yapmadım"),
              u("Hikaye attın ya"), g("Ee"),
              u("Değerlendirdim, teminat istemedim"), u("yüzün yeterli"),
              g("ahsjdjs"), g("bankacı mısın sen"),
              u("Müdürüm"), g("cuma imzalarız o zaman")],
    memes=[chip(2, "terim_ciddi", "Dosya inceleniyor"),
           chip(5, "terim_bashi", "Onay verildi"),
           ibre(),
           chip(9, "gunes_selam", "Müdür bey"),
           manset(11, "İMZA\nCUMA")],
    baslik="Onay çıktı" + SEP + H2))

# ---------------------------------------------------------------- T20 recete
R.append(dict(COM, id="T20", slug="recete", tema="kelime oyunu", spice=2, son="numara",
    photo="photos/havuz/P41.jpg",
    suggestion="Hikayende canım sıkkın yazmışsın,\ngünde iki mesaj, bana",
    messages=[u("Reçete yazdım"), g("Ne reçetesi"), g("Doktor musun"),
              u("Şikayetini gördüm"), g("Ne şikayeti"),
              u("Hikayende canım sıkkın yazmışsın"), u("günde iki mesaj, bana", "❤️"),
              g("AHAHAHSHSHSH"), g("yan etkisi var mı"),
              u("Bağımlılık yapar"), g("0532 ███ ██ ██"), g("yaz bakalım şu reçeteyi")],
    memes=[chip(2, "terim_ciddi", "Muayene başladı"),
           chip(5, "hoca_saha", "Teşhis kondu"),
           ibre(),
           plain(9, "hazir_buyukayip"),
           plain(11, "kapak_kral", 1.6)],
    baslik="Reçete yazıldı" + SEP + H3))

# ------------------------------------------------------------------ T21 sira
R.append(dict(COM, id="T21", slug="sira", tema="özgüven", spice=3, son="numara",
    photo="photos/havuz/P08.jpg",
    suggestion="Hikayene dört yüz kişi bakmış,\nben dört yüz birim, beklerim",
    messages=[u("Sıra numarası aldım"), g("Nereden"), g("Ne sırası ya"),
              u("Sende sıra var galiba"), g("Anlamadımmm"),
              u("Hikayene dört yüz kişi bakmış"), u("ben dört yüz birim, beklerim", "❤️"),
              g("ahsjdjshd"), g("sabırlıymışsın"),
              u("Sıram gelecek"), g("0538 ███ ██ ██"), g("sıranı atladım hadi")],
    memes=[chip(2, "gunes_selam", "Sıra bende"),
           chip(5, "terim_ciddi", "Sayı fazla"),
           ibre(),
           plain(9, "hazir_aceleci"),
           plain(11, "kapak_arda", 1.6)],
    baslik="Sıra bize geldi" + SEP + H1))

# --------------------------------------------------------------- T22 penalti
R.append(dict(COM, id="T22", slug="penalti", tema="futbol göndermesi", spice=2, son="gülme",
    photo="photos/havuz/P57.jpg",
    suggestion="Boş kaleye atmadın,\nhakem hâlâ bekliyor",
    messages=[u("Penaltıyı kaçırdın"), g("Ne penaltısı"), g("Maç mı var"),
              u("İki gün önce mesaj attım"), g("Görmedim"),
              u("Boş kaleye atmadın"), u("hakem hâlâ bekliyor"),
              g("AHAHAHSHSHSH"), g("kim bu hakem"),
              u("Ben"), g("ahahahah tamam yeter 🫠")],
    memes=[chip(2, "hoca_saha", "Maç var"),
           chip(5, "arda_panik", "Kaçırdı"),
           ibre(),
           chip(9, "gunes_isaret", "Hakem o"),
           plain(11, "kapak_kral", 1.6)],
    baslik="Tekrar çekilecek" + SEP + H2))

# -------------------------------------------------------------- T23 playlist
R.append(dict(COM, id="T23", slug="playlist", tema="kelime oyunu", spice=2, son="randevu",
    photo="photos/havuz/P61.jpg",
    suggestion="Benim adımın geçtiği,\ndaha yazılmadı",
    messages=[u("Playlistini gördüm"), g("Ee ne olmuş"), g("Beğenmedin mi"),
              u("Bir şarkı eksik"), g("Hangisi"),
              u("Benim adımın geçtiği"), u("daha yazılmadı", "❤️"),
              g("ahsjdjs"), g("sanatçı mısın"),
              u("Söz yazarı"), g("cumartesi dinlerim o zaman")],
    memes=[chip(2, "terim_ciddi", "Liste inceleniyor"),
           chip(5, "hoca_saha", "Söz hazır"),
           ibre(),
           plain(9, "hazir_havaya"),
           manset(11, "ŞARKI\nÇIKIYOR")],
    baslik="Şarkı yazılıyor" + SEP + H3))

# ----------------------------------------------------------------- T24 emlak
R.append(dict(COM, id="T24", slug="emlak", tema="özgüven", spice=2, son="numara",
    photo="photos/havuz/P60.jpg",
    suggestion="Manzara birinci sınıf,\nama kiracı seçiyor",
    messages=[u("İlanını gördüm"), g("Ne ilanı"), g("Ev mi arıyorsun"),
              u("Hikayen ilan gibi"), g("Nasıl yani"),
              u("Manzara birinci sınıf"), u("ama kiracı seçiyor"),
              g("AHAHAHSHSH"), g("emlakçı mısın"),
              u("Talibim"), g("0546 ███ ██ ██"), g("gel bir bak bakalım")],
    memes=[chip(2, "gunes_isaret", "İlan burada"),
           chip(5, "terim_bashi", "Manzara güzel"),
           ibre(),
           chip(9, "arda_panik", "Talip çıktı"),
           plain(11, "kapak_arda", 1.6)],
    baslik="Yer gösterildi" + SEP + H1))

# ---------------------------------------------------------------------------
if __name__ == "__main__":
    p = B / "scripts.json"
    cur = json.load(open(p, encoding="utf-8"))
    cur = [x for x in cur if not x["id"].startswith("T1") and not x["id"].startswith("T2")
           or x["id"] in ("T01", "T02", "T03")]
    cur += R
    with io.open(p, "w", encoding="utf-8") as f:
        json.dump(cur, f, ensure_ascii=False, indent=1)
    # dogrulama
    for r in R:
        assert r["messages"][5]["from"] == "u" and r["messages"][6]["from"] == "u", r["id"]
        assert (B / r["photo"]).exists(), r["photo"]
        for m in r["memes"]:
            assert (B / m["src"]).exists(), m["src"]
        assert len(r["baslik"]) <= 150, r["id"]
    rx = sum(1 for r in R for m in r["messages"] if m.get("rx"))
    print(f"{len(R)} yeni reel eklendi, toplam {len(cur)}. rx sayisi: {rx}/10")
    for r in R:
        print(f"  {r['id']} {r['slug']:9s} {len(r['messages'])} mesaj  {r['son']:7s} {r['photo'].split('/')[-1]}")
