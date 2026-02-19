# 🖐️ Finger Counting Program using MediaPipe Tasks API

A real-time computer vision project that detects and counts the number of fingers shown to the webcam using **MediaPipe Hand Landmarker (Tasks API)** and **OpenCV**.

This project demonstrates landmark-based finger state detection using modern MediaPipe architecture.

---

## 🚀 Features

- Real-time hand detection
- Accurate finger counting logic
- Left & Right hand thumb handling
- Mirrored (selfie-style) camera feed
- Press **'q'** to quit the application
- Built using MediaPipe Tasks API (not deprecated solutions API)

---

## 🛠️ Tech Stack

- Python 3.10.11
- OpenCV
- MediaPipe (Tasks API)
- Computer Vision (Landmark Geometry Logic)

---

## 📂 Project Structure

```
FINGERCOUNTINGPROJECT/
│
├── finger_counting.py
├── hand_landmarker.task
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🧠 How It Works

MediaPipe detects 21 hand landmarks.  
Finger states are determined using landmark coordinate comparisons:

- Thumb → Horizontal (X-axis) comparison (based on handedness)
- Other fingers → Vertical (Y-axis) comparison

Finger tip landmark IDs used:
- Thumb → 4
- Index → 8
- Middle → 12
- Ring → 16
- Pinky → 20

If a finger tip is above its lower joint → Finger is considered "UP".

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/GouravK1107/finger-counting-program.git
cd finger-counting-program
```

---

### 2️⃣ Create Virtual Environment (Recommended)

```bash
python -m venv venv
venv\Scripts\activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Run the Program

```bash
python finger_counting.py
```

Press **'q'** to exit.

---

## 📌 Requirements

If `requirements.txt` is missing, install manually:

```bash
pip install opencv-python mediapipe
```

---

## 🎯 Learning Outcomes

- Understanding MediaPipe Tasks API
- Working with 21 hand landmarks
- Real-time coordinate geometry logic
- Handling left vs right hand detection
- Improving CV pipeline stability

---

## 📷 Demo (Optional)

You can add a demo GIF here later to showcase the working system.

---

## 🔥 Future Improvements

- Add FPS counter
- Add bounding box around hand
- Multi-hand support
- Gesture-based control system
- Django live streaming integration

---

## 👨‍💻 Author

Gourav K  
BCA Student | Backend & AI Enthusiast  
Focused on mastering Computer Vision & AI systems.

---

⭐ If you found this project useful, consider starring the repository!
