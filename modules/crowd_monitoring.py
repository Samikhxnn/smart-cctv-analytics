import cv2
def monitor_crowd(tracked_people,frame):

    people_count=len(tracked_people)

    crowd_alert=False
    if people_count > 12:
        crowd_alert=True



    # display total people count on the frame
    cv2.putText(frame,
                 f"people_count:{people_count}",
                 (10,30),
                 cv2.FONT_HERSHEY_SIMPLEX,
                 1,
                 (0,0,255) if crowd_alert else (0,255,0),
                 2
                 )  
    # display crowd alert on the frame
    if crowd_alert:
        cv2.putText(frame,
                    "CROWD ALERT",
                    (10,70),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0,0,255),
                    2)
        

    return frame,people_count,crowd_alert
  