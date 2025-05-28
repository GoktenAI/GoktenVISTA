import os
import shutil

# Giriş klasörü (kaynak)
input_folder = r"C:\Users\Dell Precision\frames"

# Çıkış klasörü (hedef)
output_folder = r"C:\Users\Dell Precision\Desktop\GöktenAI havacılıkta yapay zeka Teknofest\secilmis_frame\videoframes2023"
os.makedirs(output_folder, exist_ok=True)

# Tüm .jpg dosyalarını sırala
images = sorted([f for f in os.listdir(input_folder) if f.endswith(".jpg")])

# Her 5 fotoğraftan 1 tanesini kopyala
for i, img_name in enumerate(images):
    if i % 35 == 0:
        src_path = os.path.join(input_folder, img_name)
        dst_path = os.path.join(output_folder, img_name)
        shutil.copy2(src_path, dst_path)

print(f"✅ Toplam {len(images) // 5} fotoğraf kopyalandı → {output_folder}")
