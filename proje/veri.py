
import cv2
import os

# Dosya yolları (raw string olarak DÜZGÜN yaz!)
video_yolu = r"C:\Users\Dell Precision\Desktop\GöktenAI havacılıkta yapay zeka Teknofest\2025_HYZ_Ornek_Veriler\2023 Örnek Video.mp4"
frame_klasoru = r"C:\Users\Dell Precision\frames"  # Basit, kısa klasör olsun

# Test: video var mı
print("🔍 Video dosyası var mı:", os.path.exists(video_yolu))

# Klasör oluştur
os.makedirs(frame_klasoru, exist_ok=True)

# Video aç
video = cv2.VideoCapture(video_yolu)
print("🎞 Toplam kare sayısı:", int(video.get(cv2.CAP_PROP_FRAME_COUNT)))
print("🎥 FPS:", video.get(cv2.CAP_PROP_FPS))

if not video.isOpened():
    print("❌ Video açılamıyor.")
    exit()

frame_sayisi = 0
while True:
    basarili, frame = video.read()
    if not basarili:
        print("✅ Video bitti.")
        break
    if frame is None:
        print(f"⚠️ Frame {frame_sayisi} boş, atlanıyor.")
        continue

    frame_yolu = os.path.join(frame_klasoru, f"frame_{frame_sayisi:05d}.jpg")
    kayit_basarili = cv2.imwrite(frame_yolu, frame)

    if kayit_basarili:
        print(f"✅ Kaydedildi: {frame_yolu}")
    else:
        print(f"❌ Kaydedilemedi: {frame_yolu}")

    frame_sayisi += 1

video.release()
