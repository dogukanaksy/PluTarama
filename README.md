# PluTarama

Kasalara gönderilen **PLU (ürün) dosyasında**, aynı ürüne aynı parametrenin birden fazla kez tanımlandığı satırları bulan küçük bir Python aracı.

Örneğin bir ürüne `A3` parametresi zaten tanımlıyken aynı dosyada bir kez daha gönderilirse kasadaki ürün yapısı bozulabilir. Bu araç, dosya kasalara gitmeden önce bu hatalı kayıtları tespit eder.

## Nasıl çalışır

- `veriler.txt` dosyasını satır satır okur (alanlar `;` ile ayrılmış).
- Tipi `5` olan satırlarda ürün kodu ve parametre numarasını toplar.
- Bir üründe tekrar eden parametreler varsa ürün koduyla birlikte ekrana yazar.

## Kullanım

```bash
# veriler.txt dosyasını aykla.py ile aynı klasöre koyun
python aykla.py
```

Örnek çıktı:

```
Ürün 123456789 - Tekrar eden parametre(ler): 12
```

## Teknolojiler

Python 3 (ek kütüphane gerekmez)
