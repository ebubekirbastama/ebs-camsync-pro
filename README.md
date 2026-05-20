# ⚡ EBS CamSync Pro (Ultra Sync)

> Real-time Wireless Media Automation & Instant PC Synchronization Ecosystem

EBS CamSync Pro; profesyonel saha muhabirleri, haber ajansları, etkinlik fotoğrafçıları, stüdyo ekipleri ve adli bilişim uzmanları için geliştirilmiş ultra hızlı kablosuz medya aktarım platformudur.

Telefonunuzla çektiğiniz fotoğraf ve videolar; hiçbir kablo, SD kart, bulut servisi veya manuel dosya aktarımı gerektirmeden gerçek zamanlı olarak bilgisayarınıza akar.

Sistem tamamen lokal ağ / hotspot / modem / mobil ağ mimarisi üzerinde çalışır.

---

# 🚀 Yeni Nesil Özellikler

## ⚡ Gerçek Zamanlı TCP Soket Motoru

FTP, MTP veya SMB gibi ağır protokoller yerine ultra hafif özel TCP soket motoru kullanılır.

Avantajları:

* Çok düşük gecikme
* Stabil aktarım
* Büyük medya desteği
* Aynı anda çoklu medya gönderimi
* Mobil veri üzerinden çalışma desteği

---

## 📷 Fotoğraf + 🎥 Video Senkronizasyonu

Sistem artık sadece fotoğraf değil:

* JPG
* PNG
* MP4
* MOV
* Kamera videoları
* Seri çekim medyaları

aktarabilir.

Telefon tarafında medya havuzunda biriken tüm içerikler tek tuşla PC’ye gönderilir.

---

## 📡 QR Kod ile Otomatik Eşleşme

PC paneli artık otomatik QR üretir.

Telefon:

* QR okut
* IP otomatik dolsun
* Port otomatik dolsun
* Tek dokunuşla bağlan

Mantığıyla çalışır.

Manuel IP yazma derdi tamamen kaldırılmıştır.

---

## 💾 Kalıcı Sunucu Hafızası

Telefon uygulaması:

* Son bağlandığı bilgisayarı hafızaya kaydeder
* APK kapansa bile unutmaz
* Tekrar açıldığında otomatik bağlanabilir

SharedPreferences tabanlı ultra hafif yapı kullanılmıştır.

---

## 🧠 Akıllı Arka Plan Medya Motoru

Android tarafında:

* Foreground Service
* Coroutine tabanlı async queue
* Arka planda kesintisiz aktarım
* Bildirim üzerinden canlı senkronizasyon

bulunur.

Telefon ekranı kapansa bile aktarım devam eder.

---

## 🧹 Otomatik Telefon Hafızası Temizleme

PC tarafı medya dosyasını eksiksiz aldığında telefona güvenli OK cevabı yollar.

Telefon:

* başarılı gönderilen medyayı otomatik siler
* hafıza dolmasını engeller
* saha çekimlerinde sınırsız kullanım sağlar

---

## 🧵 Multi-thread Premium Sunucu Mimarisi

Bilgisayar tarafındaki Python sunucu:

* Thread bazlı bağlantı yönetimi
* Aynı anda çoklu medya alımı
* Donmayan UI
* Premium canlı log sistemi
* Progress bar desteği
* Windows toast notification desteği

ile çalışır.

50+ medya aynı anda gelse bile panel kilitlenmez.

---

## 🔥 Windows Güvenlik Duvarı Otomasyonu

Program ilk açılışta:

* Admin yetkisi alır
* Güvenlik duvarı kuralı oluşturur
* TCP portunu otomatik açar

Kullanıcı manuel firewall ayarı yapmak zorunda kalmaz.

---

# 🖥️ PC Sunucu Özellikleri

## Premium Modern UI

CustomTkinter tabanlı siber-metal tasarım:

* Neon mavi detaylar
* Canlı aktivite logları
* Medya aktarım geçmişi
* Tray mode
* Gerçek zamanlı ilerleme çubuğu
* QR bağlantı paneli

---

# 📱 Android APK Özellikleri

## Seri Medya Çekimi

* Peş peşe fotoğraf çek
* Video çek
* Havuzda biriktir
* Toplu gönder

---

## Ultra Hafif Ağ Mimarisi

* TCP Socket
* Direkt byte stream
* Chunk bazlı aktarım
* Timeout koruması
* Ağ kopma toleransı

---

# 📦 Proje Dosya Yapısı

## PC Tarafı

* `ebs_camsync_server.py`
* `ebs_camsync_server_qr.py`

## Android Tarafı

* `MainActivity_QR_Persist_Video.kt`
* `SyncService_Media.kt`

## Build Araçları

* `eski_EBS_Builder.py`

---

# 🛠️ Kurulum

# Bilgisayar Tarafı

```bash
pip install customtkinter
pip install win10toast
pip install pystray
pip install pillow
pip install qrcode
```

Sunucuyu başlat:

```bash
python ebs_camsync_server_qr.py
```

Program:

* QR kod üretir
* IP adresini gösterir
* TCP sunucusunu başlatır

---

# 📱 Android Derleme

`build.gradle` içine ekle:

```gradle
implementation 'com.journeyapps:zxing-android-embedded:4.3.0'
```

APK derle:

```bash
gradlew assembleDebug
```

---

# 📲 Kullanım

1. PC panelini aç
2. QR kod ekranda oluşsun
3. Telefonda “QR ile Bağlan” de
4. Kamera ile okut
5. Fotoğraf/video çek
6. “PC’ye Gönder” de
7. Medyalar anında bilgisayara aksın

---

# 🎯 Kullanım Alanları

## 📰 Haber Ajansları

Sahadan çekilen görüntüler merkeze anında düşer.

## 📸 Düğün & Organizasyon

Fotoğraf baskı masasına anında aktarım yapılır.

## 🛍️ E-Ticaret Stüdyoları

Ürün çekildiği anda bilgisayara düşer.

## 🔬 Adli Bilişim

Olay yeri medyaları direkt analiz istasyonuna aktarılır.

## 🎥 Mobil Yayın Ekipleri

Sahadaki medya reji sistemine canlı akar.

---

# 🔒 Güvenlik

* Lokal ağ tabanlı çalışma
* Bulut bağımlılığı yok
* Harici sunucu yok
* Direkt cihazdan cihaza aktarım
* TCP timeout koruması
* Güvenli aktarım doğrulaması

---

# ⚙️ Teknik Mimari

## PC

* Python
* CustomTkinter
* Threading
* TCP Socket
* PyStray
* Win10Toast

## Android

* Kotlin
* Foreground Service
* Coroutine
* SharedPreferences
* ZXing QR Scanner
* MediaStore API

---

# 🧠 Gelecek Sürümler

Planlanan sistemler:

* Aynı ağdaki serverları otomatik bulma
* Şifreli medya aktarımı
* AES256 desteği
* Çoklu PC eşzamanlama
* Canlı kamera stream modu
* OBS entegrasyonu
* RTMP medya yönlendirme
* Web panel
* Uzaktan medya yönetimi
* AI medya sınıflandırma sistemi

---

# 🔒 Lisans

Bu proje Ebubekir Bastama tarafından geliştirilmiştir.

Telif Hakkı © 2026 EBS Software
Tüm Hakları Saklıdır.
