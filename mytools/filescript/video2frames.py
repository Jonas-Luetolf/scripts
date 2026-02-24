from mytools.resources.argparser import parse_args
import cv2
import os

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


def main():
    args, _ = parse_args()

    assert len(args) == 2, "Es müssen genau zwei Argumente übergeben werden: <video_path> <output_folder>"
    assert args[0].endswith(".mp4")
    video_path = args[0]
    output_folder = args[1]

    video_to_frames(video_path, output_folder)


if __name__ == "__main__":
    main()
