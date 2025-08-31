# 🏋️ AI-Powered Fitness Trainer with Chatbot

An **AI-powered fitness trainer** built using **Streamlit**, **OpenCV**, and **MediaPipe** for **pose estimation**.
It tracks your **Bicep Curls, Squats, and Push-Ups** in real time from either your **webcam** or an **uploaded video**.
Additionally, it includes a **Gemini API-powered Chatbot** to answer health & fitness queries.

---

## 🚀 Features

* ✅ Real-time **pose detection** using webcam
* ✅ Option to upload and analyze pre-recorded workout videos
* ✅ Automatic **rep counting** for:

  * 🏋️ Bicep Curls
  * 🏃 Squats
  * 💪 Push-Ups
* ✅ Integrated **Chatbot (Gemini API)** for health & fitness queries
* ✅ Streamlit-powered clean and interactive UI

---

## 🛠️ Technologies Used

* [Python](https://www.python.org/)
* [NumPy](https://numpy.org/)
* [Pandas](https://pandas.pydata.org/)
* [OpenCV](https://opencv.org/)
* [MediaPipe](https://developers.google.com/mediapipe)
* [Streamlit](https://streamlit.io/)
* [Gemini API](https://ai.google.dev/)

---

## 📂 Project Structure

```
📦 AI-Fitness-Trainer
├── AiTrainer/                # Trainer modules
├── ai_trainer.py             # Exercise logic
├── aichatbot.py              # Gemini chatbot
├── app.py                    # Main Streamlit app
├── pose_estimator.py         # Pose detection logic
├── pose_estimator_module.py  # Pose helper functions
├── requirements.txt          # Dependencies
├── skipping.mp4              # Sample workout video
├── test.py                   # Dependency test script
├── README.md                 # Documentation
└── LICENSE                   # License file
```

---

## ⚙️ Installation

1. Clone this repository

```bash
git clone https://github.com/your-username/AI-Fitness-Trainer.git
cd AI-Fitness-Trainer
```

2. Create a virtual environment & activate it

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Add your **Google API Key** in `.env`

```
GOOGLE_API_KEY=your_api_key_here
```

---

## ▶️ Run the App

```bash
streamlit run app.py
```

Open your browser at 👉 `http://localhost:8501`

---

## 📊 How It Works

1. Select your workout type (**Bicep Curl, Squat, Push-Up**)
2. Choose input source (**Webcam / Upload Video**)
3. Click **"Let's goo!!!"**
4. AI will track your body movements and count reps in real-time
5. Ask fitness-related questions in the **Chatbot Panel**
   
---

## 🔮 Future Enhancements

* More workout types (Plank, Lunges, Deadlifts, etc.)
* Posture correction feedback
* Workout summaries & analytics
* Wearable device integration

---

## 👨‍💻 Contributors

* Ved Dahale
* Rohan

---

⚡ If you like this project, don’t forget to **star ⭐ the repo**!

