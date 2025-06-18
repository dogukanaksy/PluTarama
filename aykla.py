# veriler.txt dosyasını kontrol eder
urun_parametreler = {}

dosya_adi = "veriler.txt"

try:
    with open(dosya_adi, "r", encoding="utf-8") as file:
        for satir in file:
            satir = satir.strip()
            if not satir:
                continue
            
            alanlar = satir.split(";")
            if not alanlar:
                continue

            tip = alanlar[0]

            if tip == "5":
                urun_kodu = alanlar[2]
                parametre_no = alanlar[3]

                if urun_kodu not in urun_parametreler:
                    urun_parametreler[urun_kodu] = []
                urun_parametreler[urun_kodu].append(parametre_no)
    
    # Sonuçları göster
    bulundu = False
    for urun_kodu, parametreler in urun_parametreler.items():
        tekrar_eden = set()
        gorulen = set()

        for param in parametreler:
            if param in gorulen:
                tekrar_eden.add(param)
            else:
                gorulen.add(param)
        
        if tekrar_eden:
            bulundu = True
            print(f"Ürün {urun_kodu} - Tekrar eden parametre(ler): {', '.join(tekrar_eden)}")

    if not bulundu:
        print("Hiçbir üründe tekrar eden parametre bulunamadı.")

except FileNotFoundError:
    print(f"'{dosya_adi}' dosyası bulunamadı. Lütfen aynı klasöre koyun.")
except Exception as e:
    print(f"Bir hata oluştu: {e}")

input("\nİşlem tamamlandı. Kapatmak için bir tuşa basın...")
