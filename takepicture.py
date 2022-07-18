import cv2

def take_snapshot():
    videoCaptureObject=cv2.VideoCapture(1)
    result=True
    while(result):
        ret,frame=videoCaptureObject.read()
        print("frame",frame)
        cv2.imwrite("D:\Siddhant\Python\Webcam Security\newpicture1.jpg",frame)
        
        result=False
        
    videoCaptureObject.release()
    cv2.destroyAllWindows()
    print(frame)
take_snapshot()
