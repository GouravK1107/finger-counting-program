# 🖐️ Finger Counting Program using MediaPipe Tasks API

A real-time computer vision project that detects and counts how many fingers you're holding up to the webcam, using **MediaPipe Hand Landmarker (Tasks API)** and **OpenCV**. Demonstrates landmark-based finger-state detection built on MediaPipe's modern architecture — not the deprecated Solutions API.

![Python](https://img.shields.io/badge/Python-3.10.11-3776AB?style=for-the-badge&logo=python&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)
![MediaPipe](https://img.shields.io/badge/MediaPipe-Tasks%20API-0097A7?style=for-the-badge&logo=google&logoColor=white)

---

## 🚀 Features

- ✋ Real-time hand detection
- 🔢 Accurate finger-counting logic
- 👈👉 Correct left & right hand thumb handling
- 🪞 Mirrored (selfie-style) camera feed
- ⌨️ Press **'q'** to quit the application
- 🧩 Built on the modern MediaPipe Tasks API (not the deprecated Solutions API)

---

## 🧠 How It Works

MediaPipe detects 21 hand landmarks per hand. Finger states are determined by comparing landmark coordinates:

- **Thumb** → horizontal (X-axis) comparison, adjusted for handedness
- **Other fingers** → vertical (Y-axis) comparison

**Fingertip landmark IDs used:**

| Finger | Landmark ID |
|---|---|
| Thumb | 4 |
| Index | 8 |
| Middle | 12 |
| Ring | 16 |
| Pinky | 20 |

If a fingertip sits above its lower joint (in the Y-axis), that finger is counted as **"UP"**.

---

## 🛠️ Tech Stack

- Python 3.10.11
- OpenCV
- MediaPipe (Tasks API)
- Computer Vision — landmark coordinate geometry logic

---

## 📂 Project Structure

```
finger-counting-program/
│
├── finger_counting.py     # Main application logic
├── hand_landmarker.task    # MediaPipe hand landmark model
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Installation & Setup

**1️⃣ Clone the repository**
```
git clone https://github.com/GouravK1107/finger-counting-program.git
cd finger-counting-program
```

**2️⃣ Create a virtual environment (recommended)**
```
python -m venv venv
venv\Scripts\activate
```

**3️⃣ Install dependencies**
```
pip install -r requirements.txt
```

**4️⃣ Run the program**
```
python finger_counting.py
```
Press **'q'** to exit.

---

## 📌 Requirements

If `requirements.txt` is missing, install manually:
```
pip install opencv-python mediapipe
```

---

## 🎯 Learning Outcomes

- Understanding the MediaPipe Tasks API
- Working with 21 hand landmarks
- Real-time coordinate geometry logic
- Handling left vs. right hand detection correctly
- Improving overall CV pipeline stability

---

## 🔥 Future Improvements

- 📈 FPS counter
- 🔲 Bounding box around the detected hand
- 👐 Multi-hand support
- 🎮 Gesture-based control system built on top of finger counts
- 🌐 Django live-streaming integration

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome.
Fork → create a branch → commit → push → open a pull request.

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.

---

## 👨‍💻 Author

**Gourav R**
Backend Developer | Applied AI Developer — exploring Computer Vision & AI systems

GitHub: https://github.com/GouravK1107
Portfolio: https://gouravk1107.github.io/my-portfolio/

---

Made with ❤️ and five (or fewer) fingers.
