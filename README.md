#computer-vision-study
OpenCV:

# 🎨 Real-Time Video Color Thresholding with OpenCV

This project demonstrates how to perform **real-time color detection and thresholding** from a webcam feed using OpenCV in Python. It uses the HSV color space to isolate specific colors in each video frame.

---

## 📌 Objective

To capture live video and isolate specific colors (like red, blue, green, etc.) using color thresholding in the HSV color space.

---

## 🧰 Techniques Used

- Real-time video capture using `cv2.VideoCapture()`
- Conversion from BGR to HSV color space
- Color masking using `cv2.inRange()`
- Result visualization with `cv2.bitwise_and()`

---

## 🧪 Color Thresholding Logic

HSV values are used because they separate color (hue) from lighting (value), making color detection more accurate.

For example:
```python
lower_color = np.array([100, 150, 50])  # lower HSV bound
upper_color = np.array([140, 255, 255])  # upper HSV bound
📸 Sample Output
🎥 Original Frame: Shows the raw webcam feed

🎭 Mask: Black and white mask for the target color

🎯 Color Thresholded: Final frame with only the selected color shown

🧱 Dependencies
Python 3.x

OpenCV

NumPy

Install them using:

pip install opencv-python numpy
🧠 How It Works
Open webcam using OpenCV

Convert each frame to HSV

Define color bounds in HSV

Apply a binary mask using cv2.inRange()

Display the original frame, mask, and result

🚀 How to Run
Clone the repository:

git clone https://github.com/yourusername/color-thresholding-opencv.git
cd color-thresholding-opencv
Run the script:

python color_threshold.py
Press q to exit the window.

🎯 Example: Detecting Blue
lower_blue = np.array([100, 150, 50])
upper_blue = np.array([140, 255, 255])
You can modify the HSV values to detect different colors. Use online tools or OpenCV trackbars to tune HSV in real-time.

📌 Future Improvements
Add HSV trackbars to change threshold values dynamically

Integrate morphological operations for noise removal

Add object tracking based on the masked output

🧑‍💻 Author
[Your Name]
Feel free to contribute or fork the repo!

📄 License
This project is licensed under the MIT License - see the LICENSE file for details.


---

Let me know if you also want:
- A version with trackbars to change HSV live
- A sample `color_threshold.py` file
- Or a version that supports multiple color detection at once!
