import cv2 as cv
import mysql.connector


def draw_boundray(img, classifier, scaleFactor, minNeighbors, color, text, clf):
    grayImage = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    features = classifier.detectMultiScale(
                grayImage, scaleFactor, minNeighbors)

    coord = []

    for(x, y, w, h) in features:
                cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)
                id, predict = clf.predict(grayImage[y:y+h, x:x+w])
                confidence = int((100*(1-predict/300)))

                conn = mysql.connector.connect(
                    user='root', password='password', host='localhost', database='testdb')
                MyCursor = conn.cursor()
                MyCursor.execute(
                    'select StudentName from facerecognition where StudentID='+str(id))
                n = MyCursor.fetchone()
                n = "+".join(n)

                MyCursor.execute(
                    'select RollNo from facerecognition where StudentID='+str(id))
                r = MyCursor.fetchone()
                r = "+".join(r)

                MyCursor.execute(
                    'select Department from facerecognition where StudentID='+str(id))
                d = MyCursor.fetchone()
                d = "+".join(d)

                if confidence > 77:
                    cv.putText(
                        img, f"Roll:{r}", (x, y-55), cv.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv.putText(
                        img, f"Name:{n}", (x, y-30), cv.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv.putText(
                        img, f"Department:{d}", (x, y-5), cv.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                else:
                    cv.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 3)
                    cv.putText(img, "Unknown Face", (x, y-5),
                               cv.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                coord = [x, y, w, h]

    return coord

def recognize(img, clf, faceCascade):
    coord = draw_boundray(img,faceCascade,1.1,10,(255,25,255),'Face',clf) 
    return img

    faceCascade = cv.CascadeClassifier(r'D:\MyPythonProgramming\Face detection attendance system\haarcascade_frontalface_alt.xml')
    clf = cv.face.LBPHFaceRecognizer_create()
    clf.read(r'D:\MyPythonProgramming\Face detection attendance system\classifier.xml')

    VideoCap = cv.VideoCapture(0)

    while True:
            ret,img = VideoCap.read()
            img = recognize(img, clf, faceCascade)
            cv.imshow('Welcome to the Face recognition', img)

            if cv.waitKey(1) == 13:
                break
            VideoCap.release()
            cv.destroyAllWindows()
recognize()