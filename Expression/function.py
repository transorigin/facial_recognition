from PIL import Image

from facial import emotion_classifier
import numpy as np
import cv2
import os

emotion_labels = ['angry', 'disgust:', 'fear', 'happy', 'sad', 'surprise', 'neutral']
num_class = len(emotion_labels)


def recFacial(imgPath):
    p = os.path.dirname(__file__)
    # 加载emotion
    emotion_images = {}
    for emoji in emotion_labels:
        emotion_images[emoji] = cv2.imread(p + "/emoji/" + emoji + ".png", -1)

    def face2emoji(face, emotion_index, position):
        x, y, w, h = position
        print("index:", emotion_index)
        print('emotion_image', emotion_images[emotion_index])
        emotion_image = cv2.resize(emotion_images[emotion_index], (w, h))
        overlay_img = emotion_image[:, :, :3] / 255.0
        overlay_bg = emotion_image[:, :, 3:] / 255.0
        background = (1.0 - overlay_bg)
        face_part = (face[y:y + h, x:x + w] / 255.0) * background
        overlay_part = overlay_img * overlay_bg

        face[y:y + h, x:x + w] = cv2.addWeighted(face_part, 255.0, overlay_part, 255.0, 0.0)

        return face

    faces, img_gray, img = emotion_classifier.face_detect(imgPath)
    try:

        print(emotion_classifier.predict_emotion(faces))
    except:
        path = p + '/static/test.jpg'
        cv2.imwrite(path, img)
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
        # emoji_show = img.copy()
        emoji = face2emoji(img, emo, (x, y, w, h))
        # cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        # www_s = int((w + 20) * 2 / 100) * 2 / 5
        # cv2.putText(img, emo, (x + 2, y + h - 2), cv2.FONT_HERSHEY_SIMPLEX,
        #             www_s, (150, 25, 150), thickness=2, lineType=1)
        print(p)
        path = p + '/static/test.jpg'
        cv2.imwrite(path, emoji)
        emoStore[emo] = result_sum[label]
    print(emoStore)
    image_data = open(path, "rb").read()
    return image_data, emoStore


if __name__ == '__main__':
    recFacial('img/1.jpg')
