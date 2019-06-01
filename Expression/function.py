from facial import emotion_classifier
import numpy as np
import cv2
import os
emotion_labels = ['angry', 'disgust:', 'fear', 'happy', 'sad', 'surprise', 'neutral']
num_class = len(emotion_labels)


def recFacial(imgPath):
    faces, img_gray, img = emotion_classifier.face_detect(imgPath)
    print(emotion_classifier.predict_emotion(faces))
    emoStore = {}
    for (x, y, w, h) in faces:
        face_img_gray = img_gray[y:y + h, x:x + w]
        results = emotion_classifier.predict_emotion(face_img_gray)  # face_img_gray
        result_sum = np.array([0] * num_class)
        for result in results:
            result_sum = result_sum + np.array(result)
            print(result)
        angry, disgust, fear, happy, sad, surprise, neutral = result_sum
        print('angry:', angry, 'disgust:', disgust, ' fear:', fear, ' happy:', happy, ' sad:', sad,
              ' surprise:', surprise, ' neutral:', neutral)
        label = np.argmax(result_sum)
        emo = emotion_labels[label]
        print('Emotion : ', emo)
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        www_s = int((w + 20) * 2 / 100) * 2 / 5
        cv2.putText(img, emo, (x + 2, y + h - 2), cv2.FONT_HERSHEY_SIMPLEX,
                    www_s, (150, 25, 150), thickness=2, lineType=1)
        p = os.path.dirname(__file__) + '/'
        print(p)
        path = p + '/img/test.jpg'
        cv2.imwrite(path, img)
        emoStore[emo] = result_sum[label]
    print(emoStore)
    return img, emoStore


if __name__ == '__main__':
    recFacial('img/0.jpg')
