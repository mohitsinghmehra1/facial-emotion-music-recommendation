# 🎵 Facial Emotion Music Recommendation

An AI-powered music recommendation system that detects a user's facial emotion through a live camera feed and recommends songs that match their mood.

This project uses **Deep Learning, Computer Vision, and the Spotify API** to analyze facial expressions, identify emotions, and provide personalized music recommendations. Users can open their camera, analyze their facial emotion, view the detected mood, discover recommended songs, and play music through the application.

## ✨ Features

- **📷 Live Camera Access:** Open the camera to capture the user's facial expressions in real time.
- **🧠 Facial Emotion Detection:** Analyze facial expressions using a trained Convolutional Neural Network (CNN).
- **⚡ Transfer Learning:** Use the EfficientNet architecture with transfer learning to build the emotion detection model.
- **😊 Emotion Recognition:** Identify the emotion detected from the user's facial expression.
- **🎶 Mood-Based Music Recommendations:** Recommend songs based on the detected emotion using the Spotify API.
- **▶️ Song Playback:** Display recommended songs and provide a play button to start playback.
- **🖥️ Interactive Web Interface:** Use Streamlit to provide a simple and user-friendly application interface.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Interactive web application interface |
| Keras | Deep learning model development |
| OpenCV | Camera access and image processing |
| EfficientNet | CNN architecture for facial emotion recognition |
| Transfer Learning | Leverage pretrained model features for emotion classification |
| Spotify API | Fetch music recommendations based on detected emotions |

## 🚀 How It Works

The application follows a simple workflow:

1. **Open the Camera:** The user clicks the camera button to access the live camera feed.
2. **Capture Facial Expressions:** The application obtains an image of the user's face.
3. **Analyze the Emotion:** The user clicks the emotion analysis button to process the captured image.
4. **Predict the Emotion:** The trained EfficientNet-based CNN model analyzes the facial expression and predicts an emotion.
5. **Recommend Songs:** The application uses the detected emotion to retrieve relevant song recommendations through the Spotify API.
6. **Display and Play Music:** The detected emotion and recommended songs are displayed in the Streamlit interface, allowing the user to click the play button to start playback.

## 🏗️ System Architecture

```text
        User
         |
         v
   Streamlit Interface
         |
         v
     Open Camera
         |
         v
  Capture Facial Image
         |
         v
   OpenCV Processing
         |
         v
  EfficientNet CNN Model
    (Transfer Learning)
         |
         v
  Emotion Classification
         |
         v
   Spotify API Integration
         |
         v
  Mood-Based Song Results
         |
         v
     Play Music
```

## 📦 Project Requirements

The project uses Python and the following technologies:

- Streamlit
- Keras
- OpenCV
- EfficientNet-based CNN model
- Spotify API access and credentials

The trained emotion recognition model and Spotify API configuration must be available for the complete application to work.

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/mohitsinghmehra1/facial-emotion-music-recommendation.git
```

### 2. Install Dependencies


### 3. Configure Spotify API Access


### 4. Prepare the Emotion Recognition Model

Ensure that the trained EfficientNet-based emotion recognition model is available at the location expected by your application.

If the model must be trained separately, complete the training process before running the application.

### 5. Run the Application

If your main Streamlit application file is named `app.py`, run:

```bash
streamlit run app.py
```

**Note:** Replace `app.py` with the actual filename of your Streamlit entry point if it differs.

## 🎮 How to Use

1. Launch the application using Streamlit.
2. Open the camera using the provided camera button.
3. Position your face in front of the camera.
4. Click the **Analyze Emotion** button.
5. Wait for the model to predict your facial emotion.
6. View the detected emotion in the application.
7. Explore the songs recommended for that emotion.
8. Click the play button to start playback, subject to the application's Spotify integration and playback requirements.

## 🧠 Model Overview

The facial emotion recognition component uses a **Convolutional Neural Network (CNN)** based on the EfficientNet architecture and transfer learning.

Transfer learning allows a pretrained neural network to be adapted to a facial emotion classification task, reducing the need to train an entire deep learning architecture from scratch.

The model processes facial image data and predicts an emotion from the classes it was trained to recognize. The predicted emotion is then used as an input for the music recommendation component.

The exact emotion categories, dataset, pretrained EfficientNet variant, training parameters, and model evaluation metrics depend on the implementation used in this project.

## 🎧 Music Recommendation System

The music recommendation component connects the detected emotion to music suggestions through the Spotify API.

The general process is:

- Receive the emotion predicted by the model.
- Map the detected emotion to an appropriate music search or recommendation query.
- Retrieve relevant song information through the Spotify API.
- Display the recommended songs in the application.
- Allow the user to initiate playback through the provided play control.

Actual playback functionality depends on the Spotify API endpoints, authentication permissions, and playback method implemented in the application.

## 📁 Project Structure

The following is an illustrative structure for organizing the project. Adapt the filenames and folders to match your actual repository.

```text
facial-emotion-music-recommendation/
│
├── .git/                                  # Git version control data
├── .spotify_cache                         # Spotify authentication cache
│
├── facialmodeltrainingnotebook.ipynb      # Jupyter notebook for model training
├── facial_model_raf_best.keras            # Trained facial emotion recognition model
├── face_detection_yunet_2023mar.onnx      # YuNet face detection model
├── camera.png                             # Camera-related image asset
├── app.py                                 # Main Streamlit application
└── modelClasses.py                        # Model and emotion class definitions

```

## 🔒 Privacy and Security

- Camera access should be initiated by the user.
- Facial images should be handled according to the application's privacy requirements.
- Spotify credentials and access tokens should not be committed to the repository.
- Use environment variables or Streamlit secrets to manage sensitive configuration.
- Do not assume that facial emotion predictions perfectly represent a person's actual mood.

## 🔮 Future Improvements

Potential improvements for the project include:

- Improving emotion classification accuracy through model evaluation and fine-tuning.
- Adding support for a wider range of emotion categories.
- Enhancing the music recommendation logic with user preferences.
- Improving the interface for displaying recommended songs and playback controls.
- Improving camera feedback and handling cases where no face is detected.
- Adding automated tests for emotion prediction and recommendation workflows.

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

1. Fork the repository.
2. Create a new branch for your changes.
3. Implement and test your improvements.
4. Commit your changes with a descriptive message.
5. Open a pull request describing your changes.

## 📄 License

No license has been specified for this project yet.

Before making the repository publicly available for reuse, choose an appropriate license and add a corresponding `LICENSE` file. Until a license is added, others generally do not have permission to reuse, distribute, or modify your copyrighted code beyond what applicable law permits.

## 👨‍💻 Author

**Your Name**

- GitHub: [mohitsinghmehra1](https://github.com/mohitsinghmehra1)

---

⭐ If you find this project interesting, consider starring the repository!

**Facial Emotion Music Recommendation** — connecting computer vision, artificial intelligence, and music to create a mood-based listening experience.
