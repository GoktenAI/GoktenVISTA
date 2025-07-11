# 🛩️ GökTenAi — GöktenVISTA Teknofest Havacılıkta Yapay Zeka Projesi

**GökTenVISTA**, Teknofest 2025 "Havacılıkta Yapay Zekâ" yarışması kapsamında geliştirilen, görüntü işleme ve yapay zekâ algoritmalarını birleştirerek hava sahasında görev yapan nesneleri (İHA, insan, taşıt vb.) tespit eden ve analiz eden bütünleşik bir karar destek sistemidir.

---

## 🎯 Projenin Amacı

Bu projenin temel amacı, yarışma tarafından sağlanan görüntü verileri üzerinden:
- **Nesne tespiti** yapmak (örneğin taşıt, insan, UAİ, UAP sınıfları),
- **Tespit edilen nesnelerin hareketlerini analiz etmek** ve konum kestiriminde bulunmak,
- **İniş uygunluğu** gibi durumsal kararlar vererek otonom hava aracı sistemlerine yardımcı olabilecek yapay zekâ tabanlı bir çözüm sunmaktır.

---

## 🧠 Problem Tanımı

Yarışma senaryosu gereği:
- Kamera görüntüleri üzerinden **karmaşık ve dinamik sahneler** işlenmektedir.
- Gerçek zamanlı olarak hareketli nesnelerin izlenmesi, sınıflandırılması ve gerektiğinde **acil durum tespiti** yapılması beklenmektedir.
- Bu süreçte **karar destek sistemi**, yalnızca görsel veriye dayanarak çalışmalıdır.

---

## 🛠️ Geliştirilen Sistem Bileşenleri

GökTenAi sistemi şu temel modüllerden oluşmaktadır:

- 🎯 **Detection**: YOLOv8 tabanlı nesne tespit sistemi ile insan, taşıt, UAİ ve UAP gibi sınıfların yüksek doğrulukla belirlenmesi  
- 📍 **Localization**: Sabit referans bölgeleri ve/veya hareket analizleri ile nesnelerin 3B konum tahmini  
- 📊 **Trajectory Analysis**: Tespit edilen nesnelerin geçmiş hareketlerine bakarak davranış analizi (örneğin ani hızlanma, yön değiştirme)  
- 🤖 **Karar Modülü**: Konum ve sınıf bilgilerini değerlendirerek "inişe uygunluk", "riskli bölge" gibi kararlar üreten yapı  
- ⚙️ **Vision Pipeline**: Tüm sistemin tek bir hat üzerinde entegre çalışmasını sağlayan ana yürütücü

---

## 🌍 Projenin Katkısı

GökTenAi, yalnızca yarışma verilerine yönelik bir çözüm değil; aynı zamanda:
- Hava trafiği izleme,
- Acil durum yönetimi,
- Akıllı hava aracı kontrol sistemleri gibi geniş uygulama alanlarına uyarlanabilecek şekilde **modüler ve ölçeklenebilir** olarak tasarlanmıştır.

---

## 🏁 Yarışma Bağlamı

Bu proje, **TÜBİTAK ve Teknofest tarafından düzenlenen "Havacılıkta Yapay Zekâ Yarışması"** çerçevesinde geliştirilmiştir. Proje sürecinde özgünlük, verimlilik ve gerçek dünya koşullarına uygunluk gibi kriterlere önem verilmiş ve sistem sürekli olarak gerçek verilerle test edilmiştir.

---

> 👨‍💻 Takım: **GökTenAi**
>  
> 🔬 Alan: Görüntü İşleme · Yapay Zeka · Karar Destek Sistemleri  
>  
> 📍 Yarışma: Teknofest 2025 – Havacılıkta Yapay Zekâ Kategorisi  
