def atik_turu_aciklama():
    # Atık türlerinin açıklamaları
    atik_turleri = {
        "Plastik": "Plastik atıklar, şişeler, ambalajlar, poşetler ve plastik kaplar gibi eşyaları içerir.",
        "Kağıt": "Kağıt atıklar, gazete, dergi, kutular, kartonlar ve herhangi bir kağıt ambalajı içerir.",
        "Cam": "Cam atıklar, şişeler, kavanozlar ve cam ambalajlar gibi eşyaları içerir.",
        "Organik": "Organik atıklar, yemek artıkları, meyve ve sebze kabukları gibi biyolojik çöpler içerir.",
        "Elektronik": "Elektronik atıklar, telefonlar, bilgisayarlar, TV'ler ve elektrikli cihazlar gibi atıkları içerir.",
        "Metaller": "Metaller, alüminyum kutular, metal şişeler ve diğer metal eşyaları içerir.",
        "Diğer": "Diğer atıklar, geri dönüşümü zor olan ya da spesifik bir kategoriye girmeyen atıklardır."
    }
    
    print("Atık Türleri ve Açıklamaları:")
    for tur, aciklama in atik_turleri.items():
        print(f"{tur}: {aciklama}")
    print("\n")

def atik_turu_sec():
    print("Atık türünü seçin:")
    print("1. Plastik")
    print("2. Kağıt")
    print("3. Cam")
    print("4. Organik")
    print("5. Elektronik")
    print("6. Metaller")
    print("7. Diğer")
    
    secim = input("Seçiminizi yapın (1-7): ")
    return secim

def atik_kutusu(secim):
    # Atık türüne göre hangi kutuya atılacağını belirler
    if secim == "1":
        return "Plastik atık kutusuna atın. (Çok katmanlı ambalajlar ve plastik poşetler hariç.)"
    elif secim == "2":
        return "Kağıt atık kutusuna atın. (Müşterek kağıtlar ve kirli kağıtlar hariç.)"
    elif secim == "3":
        return "Cam atık kutusuna atın. (Çatlamış camlar ve bazı cam türleri hariç.)"
    elif secim == "4":
        return "Organik atık kutusuna atın. (Yemek artıkları ve sebze-meyve kabukları gibi.)"
    elif secim == "5":
        return "Elektronik atık kutusuna atın. (Telefonlar, bilgisayarlar ve diğer elektronik eşyalar.)"
    elif secim == "6":
        return "Metal atık kutusuna atın. (Alüminyum kutular, metal şişeler ve diğer metal atıklar.)"
    elif secim == "7":
        return "Diğer atık kutusuna atın. (Geri dönüşümü zor olan atıklar.)"
    else:
        return "Geçersiz seçim, lütfen 1 ile 7 arasında bir seçenek girin."

def atik_yonetimi():
    print("Atık Yönetimi Sistemi")
    
    while True:
        atik_turu_aciklama()  # Atık türleri ve açıklamaları gösterilir
        secim = atik_turu_sec()  # Kullanıcıdan atık türü seçmesi istenir
        
        sonuc = atik_kutusu(secim)  # Kullanıcıya uygun kutuyu gösterir
        print("\n" + sonuc)
        
        # Kullanıcıya tekrar atık türü seçmek isteyip istemediği sorulur
        devam = input("Başka bir atık türü seçmek ister misiniz? (Evet/Hayır): ").lower()
        if devam != "evet":
            print("\nTeşekkürler! Çevreye katkı sağladığınız için teşekkür ederiz.")
            break

# Ana fonksiyonu çalıştır
atik_yonetimi()
