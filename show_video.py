import cv2

video = cv2.VideoCapture("mountain.mp4", cv2.CAP_DSHOW)

if not video.isOpened():
    print("❌ Could not open video.")
    exit()

while True:
    ret, frame = video.read()
    if not ret:
        print("✅ End of video or can't read frame.")
        break

    cv2.imshow("Video Frame", frame)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
