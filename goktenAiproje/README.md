
---

## 🧠 Modül Açıklamaları

### 🔍 `detection/` — Nesne Tespiti

- **`detector.py`**  
  Görüntü üzerinde nesne tespiti yapan modelin (örneğin YOLO) sarmalayıcı (wrapper) modülüdür. Çıktı olarak `bounding box`, `class label` ve `confidence score` döner.

- **`preprocessor.py`**  
  Görüntüyü modele uygun hale getirmek için normalize etme, yeniden boyutlandırma gibi işlemleri yapar.

- **`postprocessor.py`**  
  Tespit sonuçlarını filtreler, eşik değerine göre karar verir ve özel kurallara dayalı kararlar (örneğin iniş uygunluğu) üretir.

---

### 📍 `localization/` — Konum Kestirimi ve Hareket Analizi

- **`estimator.py`**  
  Tespit edilen nesnelerin konumunu, görüntü verisi ve sabit noktalar yardımıyla hesaplar. PnP veya sabit UAP/UAİ bölgeleri kullanabilir.

- **`evaluator.py`**  
  Gerçek konumlar ile tahmin konumlar arasındaki farkı hesaplar (örneğin RMSE ile), sistemin doğruluğunu değerlendirir.

- **`trajectory.py`**  
  Nesnelerin hareket geçmişini analiz eder. Hız, yön değişimi, hareket sınıflandırması gibi analizler içerir.

- **`utils.py`**  
  Ortak kullanılan matematiksel dönüşümler ve yardımcı fonksiyonları içerir.

---

### 🔁 `pipeline/` — Ana Görsel İşlem Hattı

- **`vision_pipeline.py`**  
  Tüm sistemi entegre eder:  
  `Preprocessor → Detector → Estimator → Postprocessor` sırasıyla çalışarak bir görsel girdiden konum, sınıf ve karar çıktısı üretir.

- **`config.yaml`**  
  Model yolu, eşik değerleri, çıktı dizini gibi ayarların tanımlandığı YAML dosyasıdır.

---

## ⚙️ Kullanım Amacı

Bu yapı sayesinde:

- Modüller ayrı ayrı test edilebilir ve geliştirilebilir.
- Farklı tespit ve konum algoritmaları kolayca entegre edilebilir.
- Görsel veri işleme tabanlı birçok AI projesine temel oluşturabilir.

---

## 🧪 Önerilen Geliştirme Yönleri

- Optical Flow veya Kalman filtresi gibi gelişmiş konum kestirimi teknikleri entegre edilebilir.
- LSTM tabanlı hareket tahmin algoritmaları eklenebilir.
- Karar modülü daha dinamik hale getirilerek durumsal senaryolar işlenebilir.

---

> 📌 Not: Bu belge sadece modül yapısını ve dosya içeriklerini açıklamaktadır. Projenin genel amacı ve yarışma kapsamı ayrı bir README dosyasında ele alınacaktır.
