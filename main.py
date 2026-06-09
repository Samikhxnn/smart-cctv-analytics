# import functions and modules

from modules.tracking import track_people
from modules.crowd_monitoring import monitor_crowd
from modules.fire_and_smoke import fire_and_smoke_detection
from modules.ppe import ppe_compliance

from modules.telegram import (fire_alert_func,
                              smoke_alert_func,
                              crowd_alert_func,
                              ppe_violation_alert)



from ultralytics import YOLO
import cv2

# setup models
model = YOLO("models/yolo11n.pt")
fire_model=YOLO("models/fire.pt")
ppe_model=YOLO("models/besthv.onnx")
print(ppe_model.names)






#-------------------------------------------------------------
# create main LOOP
#-------------------------------------------------------------


cap = cv2.VideoCapture("C:\\Users\\Asus\\Downloads\\13751290_3840_2160_50fps.mp4")
while True:
    ret, frame = cap.read()

    tracked_people,frame=track_people(frame,model)


    # crowd monitoring
    frame,people_count,crowd_alert=monitor_crowd(tracked_people,frame)

    if crowd_alert:
        crowd_alert_func()


    # fire and smoke detection
    frame,fire_alert,smoke_alert=fire_and_smoke_detection(frame,fire_model)
    
    if fire_alert:
        fire_alert_func()


    if smoke_alert:
        smoke_alert_func()  



    # ppe compliance detection
    frame,ppe_alert,violating_ids=ppe_compliance(frame,tracked_people,ppe_model)

    if ppe_alert:
        ppe_violation_alert(violating_ids)



    
    frame = cv2.resize(frame, (2040, 800))
    cv2.imshow("Person Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()