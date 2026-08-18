#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""@dmsihirbazi icin 6 reel — gece temasi + kart meme'ler."""
import json, io
from pathlib import Path
B = Path(__file__).parent

COM = dict(appAfter=5, zoomFrom=8, endHold=1.2, muzik="muzik/bed.mp3",
           muzikBaslangic=14, muzikSes=0.85, hesap="dmsihirbazi",
           tema2="gece", baslik_tipi="punchline")
D1="#dm #mesaj #yazışma #keşfet #flörtai"
D2="#dm #sohbet #manita #keşfetteyizzz #flörtai"
D3="#dm #mesajatma #tinder #keşfet #flörtai"
SEP=" • • • • • "
def u(t,rx=None):
    d={"from":"u","text":t}
    if rx:d["rx"]=rx
    return d
def g(t): return {"from":"g","text":t}
def yorum(after,rows,hold=1.4,bas="Yorumlar"):
    return {"after":after,"kart":"yorum","baslik":bas,"rows":rows,"hold":hold}
def arama(after,sorgu,rows,hold=1.35):
    return {"after":after,"kart":"arama","sorgu":sorgu,"rows":rows,"hold":hold}
def bildirim(after,ikon,bas,gov,renk="#3E6BFF",hold=1.3):
    return {"after":after,"kart":"bildirim","ikon":ikon,"baslik":bas,"govde":gov,"renk":renk,"hold":hold}

R=[]
R.append(dict(COM, id="D25", slug="fal", tema="kelime oyunu", spice=2, son="numara",
  photo="photos/havuz/P04.jpg", suggestion="Fincanda hep aynı şey çıkıyor,\nbiri sana çok bakıyor",
  messages=[u("Falına baktım"),g("Ne falı"),g("Kahve bile içmedik"),
            u("Gerek yok"),g("Nasıl yani"),
            u("Fincanda hep aynı şey çıkıyor"),u("biri sana çok bakıyor"),
            g("ahsjdjshd"),g("falcı mısın sen"),
            u("Sadece dikkatliyim"),g("0533 ███ ██ ██"),g("gerisini de söyle bakalım")],
  memes=[arama(2,"kahve falı gerçek mi",[{"tx":"kahve falı tutar mı"},{"tx":"fincanda biri sana bakıyor ne demek","hit":True},{"tx":"falcıya nasıl cevap verilir"}]),
         bildirim(5,"🔮","Fal hazır","Fincanda tek bir şey görünüyor","#7A4BD1"),
         yorum(7,[{"ad":"@burakk","tx":"abi bu nasıl bir giriş","n":"2.1B"},{"ad":"@elifnurr","tx":"falcıymış 😭","n":"940"}]),
         bildirim(9,"☕","Fincan kapandı","Üç gün içinde haber var","#C2379B"),
         yorum(11,[{"ad":"@mertcan","tx":"üç gün beklemedi bile","n":"5.4B"},{"ad":"@sudenaz","tx":"fal tuttu resmen","n":"2.9B"}],hold=1.7)],
  baslik="Fincan doğru çıktı"+SEP+D1))

R.append(dict(COM, id="D26", slug="kombin", tema="özgüven", spice=2, son="numara",
  photo="photos/havuz/P53.jpg", suggestion="Ne giysen aynı kapıya çıkıyor,\nkimse kıyafete bakmıyor",
  messages=[u("Kombin yanlış"),g("Nesi yanlışmış"),g("Saatlerce uğraştım"),
            u("Uğraşman gereksizdi"),g("Neden"),
            u("Ne giysen aynı kapıya çıkıyor"),u("kimse kıyafete bakmıyor"),
            g("AHAHAHSHSH"),g("laf mı sokuyorsun"),
            u("İltifat ediyorum"),g("0546 ███ ██ ██"),g("düzgün söyle bakalım")],
  memes=[bildirim(2,"👗","Kombin uyarısı","Bu kombin 4 saat sürdü","#D9803A"),
         arama(5,"iltifat mı hakaret mi",[{"tx":"ne giysen aynı ne demek"},{"tx":"bu iltifat mı","hit":True}]),
         yorum(7,[{"ad":"@sena.k","tx":"iltifat mı bu kavga mı","n":"3.8B"},{"ad":"@onurcn","tx":"riskli ama tuttu","n":"1.2B"}]),
         bildirim(9,"⚠️","Risk alındı","Karşı taraf hâlâ yazıyor","#2FA37A"),
         yorum(11,[{"ad":"@dilaraa","tx":"numara verdi bak","n":"6.7B"},{"ad":"@arda.k","tx":"kombin kurtardı","n":"1.9B"}],hold=1.7)],
  baslik="Kombin onaylandı"+SEP+D2))

R.append(dict(COM, id="D27", slug="tatil", tema="kelime oyunu", spice=1, son="randevu",
  photo="photos/havuz/P63.jpg", suggestion="Deniz manzarası zaten profilinde,\nuçağa binmene gerek yok",
  messages=[u("Tatil planın iptal"),g("Kim iptal etmiş"),g("Bileti aldım bile"),
            u("Yanlış yere gidiyorsun"),g("Nereye gidecekmişim"),
            u("Deniz manzarası zaten profilinde"),u("uçağa binmene gerek yok","❤️"),
            g("hshshshs"),g("acente misin"),
            u("Rehberim"),g("cumartesi tur var mı o zaman")],
  memes=[arama(2,"bilet iptal edilir mi",[{"tx":"son dakika bilet iptali"},{"tx":"tatil yerine ne yapılır","hit":True}]),
         bildirim(5,"✈️","Rota güncellendi","Varış noktası değişti","#2E8FD9"),
         yorum(7,[{"ad":"@kaan_","tx":"adam bileti iptal ettirdi","n":"4.2B"},{"ad":"@zeynepp","tx":"rehbermiş 💀","n":"1.8B"}]),
         bildirim(9,"🧭","Tur programı","Cumartesi için yer ayrıldı","#2FA37A"),
         yorum(11,[{"ad":"@efe.t","tx":"rezervasyon tamam","n":"7.1B"},{"ad":"@melis","tx":"bilet iade edilsin","n":"2.2B"}],hold=1.7)],
  baslik="Rota değişti"+SEP+D3))

R.append(dict(COM, id="D28", slug="diyet", tema="özgüven", spice=2, son="numara",
  photo="photos/havuz/P48.jpg", suggestion="Hikayene bakınca\ntatlı krizine girdim",
  messages=[u("Diyetin bozuldu"),g("Nereden biliyorsun"),g("Bir şey yemedim ki"),
            u("Sen değil ben bozdum"),g("Ne alaka"),
            u("Hikayene bakınca"),u("tatlı krizine girdim"),
            g("AHAHAHSHSHSH"),g("bu ne biçim laf"),
            u("Dürüst laf"),g("0532 ███ ██ ██"),g("kaç kalori bakalım")],
  memes=[bildirim(2,"🥗","Diyet takibi","Bugün 0 kalori girildi","#2FA37A"),
         arama(5,"tatlı krizi nasıl geçer",[{"tx":"gece tatlı krizi"},{"tx":"tatlı krizi psikolojik mi","hit":True}]),
         yorum(7,[{"ad":"@barissss","tx":"tatlı krizi diyor 😭","n":"9.3B"},{"ad":"@ecrin","tx":"bunu not aldım","n":"2.4B"}]),
         bildirim(9,"🍰","Kalori uyarısı","Bu hesap tutmuyor","#D9803A"),
         yorum(11,[{"ad":"@umutcn","tx":"diyet bitmiş bile","n":"8.8B"},{"ad":"@nazlim","tx":"tatlı krizi efsane","n":"3.3B"}],hold=1.7)],
  baslik="Diyet bitti"+SEP+D1))

R.append(dict(COM, id="D29", slug="alarm", tema="özgüven", spice=3, son="gülme",
  photo="photos/havuz/P01.jpg", suggestion="Hikayeni gördüm,\nbu gece kimse uyumuyor",
  messages=[u("Alarmını kapat"),g("Sana ne alarmımdan"),g("Erken kalkmam lazım"),
            u("Zaten uyuyamayacaksın"),g("Neden"),
            u("Hikayeni gördüm"),u("bu gece kimse uyumuyor"),
            g("AHAHAHSHSH"),g("sende hiç utanma yok"),
            u("Var ama az"),g("ahahah tamam yeter 🫠")],
  memes=[bildirim(2,"⏰","Alarm kuruldu","06:30 — 5 saat 12 dakika kaldı","#3E6BFF"),
         arama(5,"gece uyuyamama sebepleri",[{"tx":"gece neden uyuyamıyorum"},{"tx":"telefon yüzünden uyku kaçtı","hit":True}]),
         yorum(7,[{"ad":"@caner..","tx":"bu cümleyi kaydettim","n":"11.2B"},{"ad":"@irem","tx":"utanması yok 😭","n":"3.1B"}]),
         bildirim(9,"😴","Alarm ertelendi","Yeniden kurulmadı","#7A4BD1"),
         yorum(11,[{"ad":"@aleynaa","tx":"kız pes etti","n":"9.9B"},{"ad":"@berkay_","tx":"alarm çalmayacak","n":"4.1B"}],hold=1.7)],
  baslik="Alarm iptal"+SEP+D2))

R.append(dict(COM, id="D30", slug="kurs", tema="kelime oyunu", spice=2, son="numara",
  photo="photos/havuz/P06.jpg", suggestion="İnsan böyle bakmayı nerede öğreniyor,\nben de öğreneyim dedim",
  messages=[u("Kursa yazıldım"),g("Ne kursu"),g("Bana ne yani"),
            u("Senin yüzünden"),g("Ne yapmışım"),
            u("İnsan böyle bakmayı nerede öğreniyor"),u("ben de öğreneyim dedim","❤️"),
            g("ahsjdjs"),g("öğrenilmez o"),
            u("Özel ders alırım"),g("0507 ███ ██ ██"),g("hocası benim o zaman")],
  memes=[arama(2,"bakış kursu var mı",[{"tx":"göz teması nasıl kurulur"},{"tx":"böyle bakmak öğrenilir mi","hit":True}]),
         bildirim(5,"🎓","Kayıt alındı","Kontenjan: 1 kişi","#2E8FD9"),
         yorum(7,[{"ad":"@tolgaa","tx":"kursa yazılmış adam","n":"6.5B"},{"ad":"@buse.","tx":"öğrenilmez dedi ama","n":"2.7B"}]),
         bildirim(9,"📚","Özel ders","Hoca henüz atanmadı","#C2379B"),
         yorum(11,[{"ad":"@kerem","tx":"hocasını da buldu","n":"10.4B"},{"ad":"@ilaydaa","tx":"özel ders başlıyor","n":"3.6B"}],hold=1.7)],
  baslik="Kayıt yapıldı"+SEP+D3))

if __name__=="__main__":
    p=B/"scripts.json"; cur=json.load(open(p,encoding="utf-8"))
    cur=[x for x in cur if not x["id"].startswith("D")]
    cur+=R
    json.dump(cur, io.open(p,"w",encoding="utf-8"), ensure_ascii=False, indent=1)
    for r in R:
        assert r["messages"][5]["from"]=="u" and r["messages"][6]["from"]=="u", r["id"]
        assert (B/r["photo"]).exists(), r["photo"]
        assert len(r["baslik"])<=150, r["id"]
        assert all(m.get("kart") for m in r["memes"]), r["id"]
    rx=sum(1 for r in R for m in r["messages"] if m.get("rx"))
    print(f"{len(R)} reel eklendi, toplam {len(cur)}. rx: {rx}/6")
    for r in R: print(f"  {r['id']} {r['slug']:8s} {len(r['messages'])} mesaj {r['son']:7s} {r['photo'].split('/')[-1]}")
