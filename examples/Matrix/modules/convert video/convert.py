import cv2
import numpy as np

def process_video(video_path):
    cap = cv2.VideoCapture(video_path)
    frames = []
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        resized_frame = cv2.resize(gray_frame, (16, 16))
        thresholded_frame = cv2.threshold(resized_frame, 127, 255, cv2.THRESH_BINARY)[1]
        thresholded_frame = np.where(thresholded_frame > 127, 1, 0)  # Convert values to 0 or 1
        
        frames.append(thresholded_frame)
    
    cap.release()
    return frames

if __name__ == '__main__':
    video_path = "NicoNico Douga - Bad Apple.mp4"
    resulting_frames = process_video(video_path)

    for frame in resulting_frames:
        enlarged_frame = cv2.resize(frame, (160, 160), interpolation=cv2.INTER_NEAREST)
        cv2.imshow('Processed Frame', enlarged_frame)
        if cv2.waitKey(30) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()
