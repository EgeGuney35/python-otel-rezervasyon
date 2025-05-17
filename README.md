# 🏨 Python Otel Rezervasyon Sistemi (Tkinter + MSSQL)

Bu proje, Python’un Tkinter kütüphanesi ile geliştirilen masaüstü tabanlı bir otel otomasyon sistemidir. Kullanıcı kayıt ve giriş işlemlerinin yanı sıra rezervasyon oluşturma, silme, güncelleme ve listeleme gibi temel fonksiyonları destekler.

---

## 🚀 Özellikler

- Kullanıcı girişi ve kayıt olma
- Rezervasyon oluşturma, silme, güncelleme
- MSSQL Server ile veritabanı bağlantısı
- Tkinter GUI ile kullanıcı arayüzü
- Rezervasyonlar `Treeview` tablo yapısında listelenir
- Otomatik pencere ortalama ve sabitleme

---

## 🛠️ Kullanılan Teknolojiler

- Python 3.x
- Tkinter
- Microsoft SQL Server (Express veya tam sürüm)
- pyodbc

---

## 💾 Veritabanı Kurulumu (SQL Server)

Aşağıdaki komutları SQL Server Management Studio (SSMS) üzerinde çalıştırarak veritabanını oluşturabilirsiniz:

```sql
-- Veritabanı oluştur
CREATE DATABASE python_otel_otomasyonu;
GO

USE python_otel_otomasyonu;
GO

-- Kullanıcılar tablosu
CREATE TABLE kullanicilar (
    id INT PRIMARY KEY IDENTITY(1,1),
    kullanici_adi VARCHAR(100),
    sifre VARCHAR(100)
);

-- Rezervasyonlar tablosu
CREATE TABLE rezervasyonlar (
    id INT PRIMARY KEY IDENTITY(1,1),
    ad VARCHAR(100),
    soyad VARCHAR(100),
    tc VARCHAR(11),
    oda_no VARCHAR(10),
    giris_tarihi DATE,
    cikis_tarihi DATE,
    fiyat DECIMAL(10,2),
    kisi_sayisi INT
);
