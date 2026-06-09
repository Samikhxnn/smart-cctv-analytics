

import cv2

def fire_and_smoke_detection(frame,model):

    fire_alert=False
    smoke_alert=False


    results=model(frame)

    if len(results) > 0:
        result=results[0]

        if result.boxes is not None:
            boxes=result.boxes
            for box in boxes:
                x1,y1,x2,y2=box.xyxy[0]
                x1=int(x1)
                y1=int(y1)
                x2=int(x2)
                y2=int(y2)


                  



                conf=float(box.conf[0])
                cls=int(box.cls[0])
                cls_name=model.names[cls]

                if conf > 0.5: 
                    if cls_name=="fire":
                        fire_alert=True

                        cv2.rectangle(frame,
                                    (x1,y1),
                                    (x2,y2),
                                    (0,0,255),
                                    2)
                        cv2.putText(frame,
                                    f"FIRE conf:{conf:.2f}",
                                    (x1,y1-10),
                                    cv2.FONT_HERSHEY_SIMPLEX,
                                    0.5,
                                    (0,0,255),
                                    2)
                    elif cls_name=="smoke":
                        smoke_alert=True
                        cv2.rectangle(frame,
                                    (x1,y1),
                                    (x2,y2),
                                    (155,155,155),
                                    2)
                        cv2.putText(frame,
                                    f"SMOKE conf:{conf:.2f}",
                                    (x1,y1-10),
                                    cv2.FONT_HERSHEY_SIMPLEX,
                                    0.5,
                                    (255,0,0),
                                    2)
                    else:
                        fire_alert=False
                        smoke_alert=False


    # global fire and smoke alert
    if fire_alert:
        cv2.putText(frame,
                    "fire alert",
                    (500,10,),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0,0,255),
                    2)
    if smoke_alert:
        cv2.putText(frame,
        "Smoke_alert",
        (500,30),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (155,155,155),
        2)       

    return frame,fire_alert,smoke_alert    