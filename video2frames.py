#!/bin/python
import cv2
import os
import sys

def video_to_frames(video_path, output_folder):
    # Überprüfen, ob das Video existiert
    if not os.path.exists(video_path):
        print(f"Das Video {video_path} wurde nicht gefunden.")
        return

    # Erstellen des Ausgabeordners, falls er nicht existiert
    os.makedirs(output_folder, exist_ok=True)

    # Video öffnen
    cap = cv2.VideoCapture(video_path)
    
    if not cap.isOpened():
        print("Das Video konnte nicht geöffnet werden.")
        return

    frame_count = 0

    while True:
        # Frame lesen
        ret, frame = cap.read()

        if not ret:
            break

        # Frame als Bild speichern
        frame_filename = os.path.join(output_folder, f"frame_{frame_count:05d}.jpg")
        cv2.imwrite(frame_filename, frame)

        frame_count += 1

    cap.release()
    print(f"{frame_count} Frames wurden im Ordner '{output_folder}' gespeichert.")

# Beispielaufruf
if __name__ == "__main__":
    assert len(sys.argv) == 3
    assert sys.argv[1].endswith(".mp4")
    video_path = sys.argv[1]   # Pfad zum Video
    output_folder = sys.argv[2]
    # Ordner, in dem die Frames gespeichert werden
    video_to_frames(video_path, output_folder)
