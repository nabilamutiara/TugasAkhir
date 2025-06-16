import cv2
import os


video_path = 'video.mp4' 
output_folder = 'videotophotocaptures' 

os.makedirs(output_folder, exist_ok=True)

cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Video tidak bisa dibuka.")
    exit()


fps = cap.get(cv2.CAP_PROP_FPS)
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
duration = total_frames / fps
print(f"Durasi video: {duration:.2f} detik")

interval = 5  
frame_interval = int(fps * interval)

frame_number = 0
capture_count = 0

while True:
    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_number)
    ret, frame = cap.read()
    
    if not ret:
        break

    filename = os.path.join(output_folder, f'capture_{capture_count:03}.jpg')
    cv2.imwrite(filename, frame)
    print(f"Disimpan: {filename}")

    capture_count += 1
    frame_number += frame_interval

cap.release()
print("Selesai!")
