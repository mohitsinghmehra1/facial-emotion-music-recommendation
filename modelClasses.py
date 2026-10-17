import cv2
import spotipy
import random
import time
from datetime import datetime
from spotipy.oauth2 import SpotifyOAuth
from spotipy.exceptions import SpotifyException


class emotionRecogniationSystem:
    def __init__(self):
        self.__model = None
        self.__faceClassifier = 'face_detection_yunet_2023mar.onnx'

    def run(self):
        cap = cv2.VideoCapture(0)

        if not cap.isOpened():
            print('Cannot Open the Camera Please Check the Connection.....')
            return None

        print('Camera is Opened.....')
        openTime = datetime.now()

        while True:
            frameRead, frame = cap.read()
            if not frameRead: 
                break

            duration = 10 - (datetime.now() - openTime).seconds
            if duration > 6:
                frame[:] = 0
                cv2.putText (
                    frame, 'Get Ready', (0, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 4
                )
            # Detecting the face form the frame.
            face = self.faceDetection(frame)

            # Predecting the facial Expression.
            emotion = self.emotionRecogniation(frame)

            cv2.imshow('Live Frames', frame)
            cv2.waitKey(1)

            if not duration:
                print('Emotion Captured.....')
                break

        cap.release()
        cv2.destroyAllWindows()

    def faceDetection(self, frame):
        h, w, _ = frame.shape
        croppedImg = None;
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
        
    def emotionRecogniation(self, frame):
        return 'Happy'


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
                scope = "user-library-read playlist-modify-public",
                cache_path = ".spotify_cache"
            )
        
            self.__sp = spotipy.Spotify(auth_manager = spAuth)

            # Fetching the user Information
            user = self.__sp.current_user()
            print( f"Client {user['display_name']} is authenticate Successfull.... \n")
            time.sleep(1)

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
