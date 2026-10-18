import cv2
import spotipy
import os
import random
import numpy as np
import tensorflow as tf
import time
from datetime import datetime
from spotipy.oauth2 import SpotifyOAuth
from spotipy.exceptions import SpotifyException


class emotionRecogniationSystem:
    def __init__(self, modelPath):
        if not isinstance(modelPath, str):
            raise FileNotFoundError(f"Plese provide the correct location of the model")

        if not os.path.isfile(modelPath):
            raise FileNotFoundError(f"Plese provide the correct location of the model")

        self.__model = tf.keras.models.load_model(modelPath)
        self.__faceClassifier = 'face_detection_yunet_2023mar.onnx'
        self.__history = []

    def run(self):
        cap = cv2.VideoCapture(0)

        if not cap.isOpened():
            print('Cannot Open the Camera Please Check the Connection.....')
            return None

        print('Camera is Opened.....')
        openTime = datetime.now()

        while True:
            frameRead, frame = cap.read()
            if not frameRead: break

            duration = 500 - (datetime.now() - openTime).seconds

            # Getting Ready ot the user
            if duration > 496:
                frame[:] = 0
                cv2.putText (
                    frame, 'Get Ready', (0, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 4
                )

            # Captureing the user Eomition 
            else: 
                # Detecting the face form the frame.
                face = self.__faceDetection(frame)

                # Predecting the facial Expression.
                emotion = self.__emotionRecogniation(face)
                cv2.putText (
                        frame, f'{emotion}', (0, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 4
                )
            
            cv2.imshow('Live Frames', frame)    
            cv2.waitKey(1)

            if not duration:
                print('Emotion Captured.....')
                break

        cap.release()
        cv2.destroyAllWindows()
        return emotion

    def __faceDetection(self, frame):
        h, w, _ = frame.shape
        croppedImg = None
        detector = cv2.FaceDetectorYN.create(
            self.__faceClassifier, "",
            (w, h), score_threshold = 0.9,
            nms_threshold = 0.3, top_k = 1,
        )
        _, faces = detector.detect(frame)

        if faces is not None:
            for face in faces:
                x, y, w, h = face[:4].astype('int')
                cv2.rectangle (
                    frame, (x, y), (x + w, y + h), color = (0, 255, 0), thickness = 2
                )
                croppedImg = frame[y: y + h, x:x + w]

        return croppedImg
        
    def __emotionRecogniation(self, face_bgr):
        try:
            emotion = ['Angry', 'Happy', 'Neutral', 'Sad', 'Surprise']
            scale = np.array([1.2, 1.0, 1.0, 1.0, 2.3])
            face_rgb = cv2.cvtColor(face_bgr, cv2.COLOR_BGR2RGB)
            face_rgb = cv2.resize(face_rgb, (224, 224)).astype('float32')
            output = self.__model.predict(np.expand_dims(face_rgb, axis = 0), verbose = 0)[0] * scale
            output = output / output.sum()

            return emotion[np.argmax(output)]
            
        except (ValueError, cv2.error) as e:
            print(e)
            return None


class musicRecommendationSystem:
    def __init__(self, clientId, clientSecret, redirectUrl):
        self.__clientId = clientId
        self.__clientSecret = clientSecret
        self.__redirectUrl = redirectUrl

        # authenticating the client.
        try:
            spAuth = SpotifyOAuth(
                client_id = self.__clientId,
                client_secret = self.__clientSecret,
                redirect_uri = self.__redirectUrl,
                scope = "user-modify-playback-state user-read-playback-state",
                cache_path = ".spotify_cache"
            )
        
            self.__sp = spotipy.Spotify(auth_manager = spAuth)

            # Fetching the user Information
            user = self.__sp.current_user()
            print( f"Client {user['display_name']} is authenticate Successfull.... \n")

        except SpotifyException as e:
            print(e)


    def recommendeSong(self, preference: str, n: int = 1):
        if preference is None:
            return None; 
    
        try:
            name = self.__sp.search(
                q = preference,
                type = 'track',
                market = ['US', 'IN']
            )['tracks']['items']

            return [
                    {
                        'albumUrl': song['album']['images'][0]['url'], 
                        'name': song['name'],
                        'artistName': song['artists'][0]['name'],
                        'uri': song['uri']
                    } for song in random.sample(name, n)
                ]

        except KeyError:
            print('No Such Song Avaliable Plese Specify the Song Preference correctly .....')
            
        except SpotifyException as e:
            print(e)

    def playSong(self, uri: str, deviceType: str = 'Computer'):
        if uri is None:
            return None; 
    
        try:
            deviceId = [
                 device['id'] for device in self.__sp.devices()['devices'] 
                 if device['is_active'] and device['type'].lower().strip() == deviceType.lower().strip()
            ]

            self.__sp.start_playback (
                device_id = deviceId[0], uris = [uri], offset=None
            )
            print('Song Played Successfully......')

        except IndexError as e:
            print('No Such device is active Plese Open the Spoitfy in your device.....')

        except SpotifyException as e:
            print(e)


emotionRecogniationSystem('facial_model_raf_best.keras').run()