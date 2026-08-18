#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""@mesajustasi icin 6 reel — gunbatimi temasi + kural/once-sonra kartlari."""
import json, io
from pathlib import Path
B=Path(__file__).parent
COM=dict(appAfter=5, zoomFrom=8, endHold=1.2, muzik="muzik/bed.mp3",
         muzikBaslangic=14, muzikSes=0.85, hesap="mesajustasi",
         tema2="gunbatimi", baslik_tipi="punchline")
M1="#mesaj #yazışma #ilişki #keşfet #flörtai"
M2="#mesaj #sohbet #tavsiye #keşfetteyizzz #flörtai"
M3="#mesaj #ilkmesaj #ilişki #tinder #flörtai"
SEP=" • • • • • "
def u(t,rx=None):
    d={"from":"u","text":t}
    if rx: d["rx"]=rx
    return d
def g(t): return {"from":"g","text":t}
def kural(after,no,tx,hold=1.4):
    return {"after":after,"kart":"kural","no":no,"tx":tx,"hold":hold}
def osk(after,yanlis,dogru,hold=1.5):
    return {"after":after,"kart":"oncesonra","yanlis":yanlis,"dogru":dogru,"hold":hold}

R=[]
R.append(dict(COM, id="M31", slug="berber", tema="özgüven", spice=2, son="numara",
  photo="photos/havuz/P13.jpg", suggestion="Ortada düzeltilecek bir şey yoktu,\nadam boşuna para aldı",
  messages=[u("Berberin işini bilmiyor"),g("Ne alakası var"),g("Yeni kestirdim"),
            u("O yüzden diyorum"),g("Ne olmuş ki"),
            u("Ortada düzeltilecek bir şey yoktu"),u("adam boşuna para aldı"),
            g("ahsjdjshd"),g("berberi mi savunuyorsun"),
            u("Seni savunuyorum"),g("0533 ███ ██ ██"),g("devam et bakalım")],
  memes=[kural(2,"KURAL 01","İLTİFATI\nDOSTA\nSAKLAMA"),
         osk(5,"Saçın çok güzel olmuş","Zaten düzeltilecek bir şey yoktu"),
         kural(7,"KURAL 02","ÖVGÜYÜ\nÜÇÜNCÜ\nKİŞİYE SÖYLET"),
         osk(9,"Şaka yapıyordum","Seni savunuyorum"),
         kural(11,"SONUÇ","MAKAS\nBOŞA\nGİTTİ",hold=1.7)],
  baslik="Makas boşa gitti"+SEP+M1))

R.append(dict(COM, id="M32", slug="konser", tema="kelime oyunu", spice=1, son="randevu",
  photo="photos/havuz/P47.jpg", suggestion="Herkes sahneye bakacak,\nben sana bakacağım",
  messages=[u("Bileti yanlış almışsın"),g("Nereden biliyorsun"),g("Ön sıra aldım"),
            u("Sahne yanlış tarafta"),g("Nasıl yani"),
            u("Herkes sahneye bakacak"),u("ben sana bakacağım","❤️"),
            g("hshshshs"),g("bilet mi alacaksın"),
            u("İki tane"),g("cumartesi görüşürüz o zaman")],
  memes=[kural(2,"KURAL 01","İDDİAYI\nÖNCE AT\nSONRA AÇIKLA"),
         osk(5,"Konsere gidelim mi","Sahne yanlış tarafta"),
         kural(7,"KURAL 02","ÖVGÜYÜ\nPLANIN\nİÇİNE SAKLA"),
         osk(9,"Ben de gelebilir miyim","İki tane"),
         kural(11,"SONUÇ","İKİ BİLET\nKESİLDİ",hold=1.7)],
  baslik="İki bilet kesildi"+SEP+M2))

R.append(dict(COM, id="M33", slug="fatura", tema="özgüven", spice=1, son="numara",
  photo="photos/havuz/P31.jpg", suggestion="Bu ay ekran süresi rekor kırdı,\nhep aynı profil",
  messages=[u("Faturam yüksek geldi"),g("Bana mı diyorsun"),g("Ben ne yaptım"),
            u("Sen sebep oldun"),g("Nasıl"),
            u("Bu ay ekran süresi rekor kırdı"),u("hep aynı profil"),
            g("AHAHAHSHSH"),g("stalker mısın"),
            u("Abone"),g("0546 ███ ██ ██"),g("aboneliği yükselt bakalım")],
  memes=[kural(2,"KURAL 01","SUÇU\nKARŞI TARAFA\nAT"),
         osk(5,"Profiline çok bakıyorum","Bu ay ekran süresi rekor kırdı"),
         kural(7,"KURAL 02","RAKAMLA\nKONUŞ\nLAFLA DEĞİL"),
         osk(9,"Kusura bakma","Abone"),
         kural(11,"SONUÇ","FATURA\nKABARIK",hold=1.7)],
  baslik="Fatura kabarık"+SEP+M3))

R.append(dict(COM, id="M34", slug="kitap", tema="kelime oyunu", spice=1, son="numara",
  photo="photos/havuz/P27.jpg", suggestion="Hikayen çıktı araya,\nsayfa unutuldu",
  messages=[u("Kitabı yarım bıraktım"),g("Sevmedin mi"),g("Hangi kitap"),
            u("Senin yüzünden"),g("Ne yaptım ben"),
            u("Hikayen çıktı araya"),u("sayfa unutuldu"),
            g("ahsjdjs"),g("okumayı bırak o zaman"),
            u("Bıraktım zaten"),g("0532 ███ ██ ██"),g("yeni sayfa aç bakalım")],
  memes=[kural(2,"KURAL 01","KISA\nCÜMLE\nDAHA AĞIR BASAR"),
         osk(5,"Hikayeni izledim","Hikayen çıktı araya"),
         kural(7,"KURAL 02","SONUCU\nSÖYLE\nSEBEBİ SORSUN"),
         osk(9,"Yok yok okuyorum","Bıraktım zaten"),
         kural(11,"SONUÇ","SAYFA\nDEĞİŞTİ",hold=1.7)],
  baslik="Sayfa değişti"+SEP+M1))

R.append(dict(COM, id="M35", slug="kedi", tema="özgüven", spice=1, son="gülme",
  photo="photos/havuz/P12.jpg", suggestion="Her videoda bana bakıyor,\nonaylıyor herhalde",
  messages=[u("Kedin beni tanıyor"),g("Nasıl tanıyor"),g("Hiç görüşmediniz"),
            u("Hikayelerde gördü"),g("Saçmalama"),
            u("Her videoda bana bakıyor"),u("onaylıyor herhalde"),
            g("AHAHAHSHSHSH"),g("kediyi karıştırma"),
            u("Tarafsız gözlemci"),g("ahahah tamam yeter 🫠")],
  memes=[kural(2,"KURAL 01","İDDİAYI\nCİDDİ\nBİR YÜZLE SÖYLE"),
         osk(5,"Kedin çok tatlı","Kedin beni tanıyor"),
         kural(7,"KURAL 02","ŞAKAYI\nSAVUNMA\nÜSTÜNE GİT"),
         osk(9,"Şaka şaka","Tarafsız gözlemci"),
         kural(11,"SONUÇ","KEDİ\nONAYLADI",hold=1.7)],
  baslik="Kedi onayladı"+SEP+M2))

R.append(dict(COM, id="M36", slug="tarif", tema="kelime oyunu", spice=2, son="numara",
  photo="photos/havuz/P10.jpg", suggestion="İnsan böyle nasıl duruyor,\ntarifini versene",
  messages=[u("Tarifi yanlış yazmışsın"),g("Ne tarifi"),g("Ben tarif paylaşmadım"),
            u("Paylaştın sayılır"),g("Nerede"),
            u("İnsan böyle nasıl duruyor"),u("tarifini versene","❤️"),
            g("ahsjdjshd"),g("aşçı mısın"),
            u("Öğrenciyim"),g("0507 ███ ██ ██"),g("ders başlasın o zaman")],
  memes=[kural(2,"KURAL 01","İTHAMLA\nBAŞLA\nSORUYLA DEĞİL"),
         osk(5,"Çok güzelsin","İnsan böyle nasıl duruyor"),
         kural(7,"KURAL 02","İSTEĞİ\nMERAK\nGİBİ GÖSTER"),
         osk(9,"Çok iddialıyım","Öğrenciyim"),
         kural(11,"SONUÇ","TARİF\nİSTENDİ",hold=1.7)],
  baslik="Tarif istendi"+SEP+M3))

if __name__=="__main__":
    p=B/"scripts.json"; cur=json.load(open(p,encoding="utf-8"))
    cur=[x for x in cur if not x["id"].startswith("M")]
    cur+=R
    json.dump(cur, io.open(p,"w",encoding="utf-8"), ensure_ascii=False, indent=1)
    for r in R:
        assert r["messages"][5]["from"]=="u" and r["messages"][6]["from"]=="u", r["id"]
        assert (B/r["photo"]).exists(), r["photo"]
        assert len(r["baslik"])<=150, r["id"]
    print(f"{len(R)} reel eklendi, toplam {len(cur)}. rx: {sum(1 for r in R for m in r['messages'] if m.get('rx'))}/6")
    for r in R: print(f"  {r['id']} {r['slug']:8s} {len(r['messages'])} mesaj {r['son']:7s} {r['photo'].split('/')[-1]}")
