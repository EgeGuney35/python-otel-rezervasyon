from tkinter import *
from tkinter import ttk
import pyodbc

server = 'DESKTOP-UFDKMF2\\SQLEXPRESS'
database = 'python_otel_otomasyonu'
connection = pyodbc.connect(f"DRIVER={{SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;")
cursor = connection.cursor()

def ekran_ortala(pencere, genislik, uzunluk):
    ekran_genislik = pencere.winfo_screenwidth()
    ekran_uzunluk = pencere.winfo_screenheight()
    x_koordinati = (ekran_genislik // 2) - (genislik // 2)
    y_koordinati = (ekran_uzunluk // 2) - (uzunluk // 2)
    pencere.geometry(f"{genislik}x{uzunluk}+{x_koordinati}+{y_koordinati}")
    pencere.resizable(False, False)

def pencere_yarat(baslik, genislik, uzunluk):
    yeni_pencere = Toplevel()
    yeni_pencere.title(baslik)
    ekran_ortala(yeni_pencere, genislik, uzunluk)
    return yeni_pencere

def giris_yap():
    kullanici_adi = kullanici_adi_giris.get()
    sifre = sifre_giris.get()
    if not kullanici_adi or not sifre:
        mesaj_label.config(text="Kullanıcı adı ve şifre boş bırakılamaz", fg="red")
        return
    cursor.execute("SELECT * FROM kullanicilar WHERE kullanici_adi = ? AND sifre = ?", (kullanici_adi, sifre))
    sonuc = cursor.fetchone()
    if sonuc:
        pencere.destroy()
        rezervasyon_paneli()
    else:
        mesaj_label.config(text="Hatalı kullanıcı adı veya şifre", fg="red")

def kayit_ekrani():
    kayit_pencere = pencere_yarat("Kayıt Ol", 400, 300)

    Label(kayit_pencere, text="Kullanıcı Adı", font=("Helvetica", 12)).pack(pady=5)
    yeni_kullanici_adi = Entry(kayit_pencere, font=("Helvetica", 12))
    yeni_kullanici_adi.pack(pady=5)
    Label(kayit_pencere, text="Şifre", font=("Helvetica", 12)).pack(pady=5)
    yeni_sifre = Entry(kayit_pencere, font=("Helvetica", 12), show="*")
    yeni_sifre.pack(pady=5)

    mesaj_kayit_label = Label(kayit_pencere, text="", font=("Helvetica", 10))
    mesaj_kayit_label.pack(pady=5)

    def kayit_ol():
        kullanici = yeni_kullanici_adi.get()
        sifre = yeni_sifre.get()
        if not kullanici or not sifre:
            mesaj_kayit_label.config(text="Kullanıcı adı ve şifre boş bırakılamaz", fg="red")
            return
        cursor.execute("SELECT * FROM kullanicilar WHERE kullanici_adi = ?", (kullanici,))
        if cursor.fetchone():
            mesaj_kayit_label.config(text="Bu kullanıcı adı zaten kullanılıyor", fg="red")
        else:
            cursor.execute("INSERT INTO kullanicilar (kullanici_adi, sifre) VALUES (?, ?)", (kullanici, sifre))
            connection.commit()
            mesaj_kayit_label.config(text="Kayıt başarılı", fg="green")

    Button(kayit_pencere, text="Kayıt Ol", command=kayit_ol, font=("Helvetica", 12), bg="green", fg="white", width=15, height=2).pack(pady=10)

def rezervasyon_paneli():
    def geri_don():
        rezervasyon_pencere.destroy()
        giris_ekrani()

    rezervasyon_pencere = Tk()
    rezervasyon_pencere.title("Rezervasyon Paneli")
    ekran_ortala(rezervasyon_pencere, 800, 500)

    baslik_label = Label(rezervasyon_pencere, text="REZERVASYON SİSTEMİ", font=("Helvetica", 16, "bold"), bg="blue", fg="white", height=2)
    baslik_label.pack(fill=X)

    action_frame = Frame(rezervasyon_pencere, bg="lightgrey")
    action_frame.pack(fill=X, padx=10, pady=10)

    Button(action_frame, text="Rezervasyon Oluştur", bg="green", fg="white", font=("Helvetica", 12), width=18, height=2).grid(row=0, column=0, padx=10)
    Button(action_frame, text="Güncelle", bg="yellow", fg="black", font=("Helvetica", 12), width=12, height=2).grid(row=0, column=1, padx=10)
    Button(action_frame, text="Sil", bg="red", fg="white", font=("Helvetica", 12), width=12, height=2).grid(row=0, column=2, padx=10)
    Button(action_frame, text="Çıkış", bg="orange", fg="white", font=("Helvetica", 12), width=12, height=2, command=geri_don).grid(row=0, column=3, padx=10)

    tree_frame = Frame(rezervasyon_pencere)
    tree_frame.pack(fill=BOTH, expand=True, padx=10, pady=10)

    columns = ("ad", "soyad", "tc", "oda_no", "giris_tarihi", "cikis_tarihi", "fiyat", "kisi_sayisi")
    tree = ttk.Treeview(tree_frame, columns=columns, show="headings", height=15)

    tree.heading("ad", text="AD")
    tree.heading("soyad", text="SOYAD")
    tree.heading("tc", text="T.C.")
    tree.heading("oda_no", text="ODA NO")
    tree.heading("giris_tarihi", text="GİRİŞ TARİHİ")
    tree.heading("cikis_tarihi", text="ÇIKIŞ TARİHİ")
    tree.heading("fiyat", text="FİYAT")
    tree.heading("kisi_sayisi", text="KİŞİ SAYISI")

    for col in columns:
        tree.column(col, anchor=CENTER, width=100)

    tree.pack(fill=BOTH, expand=True)

    #  sample_data = [
        #    ("Ege", "Güney", "12345678901", "101", "27.11.2024", "29.11.2024", "1000", "2"),
        #     ("Sabri", "Yılmaz", "12345678902", "102", "27.11.2024", "28.11.2024", "1200", "3")
        # ]
    #for data in sample_data:
        #tree.insert("", "end", values=data)

    rezervasyon_pencere.mainloop()

pencere = Tk()
pencere.title("Otel Otomasyonu")
ekran_ortala(pencere, 450, 350)

Label(pencere, text="Otel Otomasyonu", font=("Helvetica", 18, "bold")).pack(pady=20)
Label(pencere, text="Kullanıcı Adı", font=("Helvetica", 12)).pack(pady=5)
kullanici_adi_giris = Entry(pencere, font=("Helvetica", 12))
kullanici_adi_giris.pack(pady=5)
Label(pencere, text="Şifre", font=("Helvetica", 12)).pack(pady=5)
sifre_giris = Entry(pencere, font=("Helvetica", 12), show="*")
sifre_giris.pack(pady=5)
mesaj_label = Label(pencere, text="", font=("Helvetica", 10))
mesaj_label.pack(pady=5)
Button(pencere, text="Giriş Yap", command=giris_yap, font=("Helvetica", 12), bg="blue", fg="white", width=15, height=2).pack(pady=10)
Button(pencere, text="Kayıt Ol", command=kayit_ekrani, font=("Helvetica", 12), bg="orange", fg="white", width=15, height=2).pack(pady=5)

pencere.mainloop()
