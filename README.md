⚡ EBS CamSync Pro (Ultra Sync)
> Real-time Wireless Camera Automation & Instant PC Synchronization System

EBS CamSync Pro, profesyonel saha çalışanları, muhabirler, fotoğraf stüdyoları ve adli bilişim ekipleri için geliştirilmiş ışık hızında, kablosuz bir fotoğraf otomasyon ekosistemidir. Telefonunuzla seri çekim yaptığınız anda fotoğraflar hiçbir kabloya, hafıza kartına veya bulut servisine ihtiyaç duymadan, yerel/hücresel ağ üzerinden anında bilgisayarınıza aktarılır ve telefon hafızası otomatik olarak temizlenir.

---

## 🚀 Öne Çıkan Özellikleri (+ Avantajları)

* Işık Hızında TCP Soket Motoru: Geleneksel yavaş MTP kablo bağlantılarını veya hantal FTP protokollerini unutun. Özel asenkron TCP motoru sayesinde fotoğraflar saliseler içinde PC panelinize düşer.
* Akıllı Arka Plan İş Parçacığı (Multi-threading): Bilgisayar tarafındaki premium arayüz (CustomTkinter), telefondan peş peşe 50 tane resim gelse bile asla donmaz, kasmaz veya "Yanıt Vermiyor" moduna geçmez. Her aktarım ayrı bir kolda işlenir.
* Otomatik Telefon Hafızası Temizliği: PC tarafı resmi hatasız aldığında telefona güvenli bir OK sinyali gönderir. Telefon sinyali aldığı an yüklenen resmi galeriden kalıcı olarak siler. Sınırsız çekim, sıfır hafıza sorunu!
* Windows Güvenlik Duvarı Otomasyonu: Program ilk açılışta yönetici yetkisi (Admin) alarak ağ kısıtlamalarını ve Windows Defender duvarını otomatik olarak esnetir. Port açma dertleriyle uğraşmazsınız.
* Premium & Modern Arayüz (UI/UX): Siber metalik arka plan ve neon mavi detaylarla donatılmış Canlı Aktivite Günlüğü, anlık Progress Bar ve Windows yerel bildirim (Toast Notification) desteği.

---

## 📦 Proje İçeriği & Dosya Yapısı

* ebs_camsync_server.py: Bilgisayarınızda çalıştıracağınız, asenkron ve çoklu iş parçacıklı premium masaüstü sunucu yazılımı.
* ebs_ultra_sync.apk: Android cihazınıza kurup doğrudan sahada çekim yapacağınız mobil otomasyon uygulaması.
* .gitignore & LICENSE: Projenin kurumsal standartlara uygun tescil ve koruma dosyaları.

---

## 🛠️ Kurulum ve Kullanım Kılavuzu

### 1. Bilgisayar Tarafı (Server)
Yazılımı bilgisayarınızda başlatmak için şu adımları takip edin:

# Gerekli premium kütüphaneleri yükleyin
pip install customtkinter win10toast

# Sunucuyu başlatın (Otomatik olarak admin yetkisi isteyecektir)
python ebs_camsync_server.py

*Sunucu açıldığında ekranın üst kısmında bilgisayarınızın yerel IP adresi (Örn: 192.168.2.150) ve dinlenen port (9999) parıl parıl belirecektir.*

### 2. Mobil Taraf (Telefon)
1. Repodaki ebs_ultra_sync.apk dosyasını telefonunuza indirin ve kurun.
2. Uygulamayı açıp gerekli kamera ve ağ izinlerini onaylayın.
3. PC panelinde gördüğünüz IP Adresini ve Portu telefondaki ilgili alanlara yazın.
4. "Seri Fotoğraf Çek (Biriktir)" butonuna basarak peş peşe fotoğraflarınızı çekin.
5. Çekim bittiğinde "Birikenleri PC'ye Yolla" butonuna basın. Fotoğraflar PC'ye aktıkça telefonunuzdan otomatik olarak silinecektir.

---

## 🎯 Kullanım Alanları

* 📰 Haber Ajansları & Muhabirler: Sahadan anlık çekilen vizyon fotoğrafları saniyesinde yazı işlerinin bilgisayarına düşer.
* 🛍️ E-Ticaret & Ürün Fotoğrafçılığı: Stüdyoda manken veya ürün çekildiği an bilgisayara kaydolur, kart sök-tak derdi biter.
* 💍 Düğün & Etkinlik Fotoğrafçıları: Salonda çekilen anlık fotoğraflar baskı masasındaki bilgisayara kablosuz akar, anında baskıya hazır hale gelir.
* 🔬 Adli Bilişim & Forensik Olay Yeri: Saha inceleme ekiplerinin delil fotoğrafları güvenli lokal ağ üzerinden doğrudan analiz istasyonuna şifresiz/kesintisiz iletilir.

---

## 🔒 Lisans ve Ticari Haklar

Bu proje Ebubekir Bastama tarafından geliştirilmiştir. Tüm ticari kullanım, lisanslama ve kurumsal entegrasyon talepleriniz için GitHub profili üzerinden veya doğrudan iletişim kanallarından bağlantıya geçebilirsiniz. 

Telif Hakkı © 2026 EBS Software. Tüm Hakları Saklıdır.
