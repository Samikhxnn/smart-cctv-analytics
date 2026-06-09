import cv2
def track_people(frame,model):
    
    
    
    results=model.track(
        frame,
        persist=True,
        classes=[0],
        verbose=False

    )
    tracked_people=[]
    annotated_frame=frame.copy()
    if len(results) > 0 :

        result=results[0]

        if result.boxes is not None:

            for box in result.boxes:

                x1,y1,x2,y2=box.xyxy[0]
                x1=int(x1)
                y1=int(y1)
                x2=int(x2)
                y2=int(y2)

                conf=float(box.conf[0])

                if box.id is not None:

                    track_id=int(box.id[0])
                else:
                    track_id=-1

                tracked_people.append({
                    "track_id":track_id,
                    "bbox":[x1,y1,x2,y2],
                    "conf":conf

                })        

                cv2.rectangle(annotated_frame,
                              (x1,y1),
                              (x2,y2),
                              (0,255,0),
                              1
                               )
                cv2.putText(annotated_frame,
                            f"ID:{track_id} conf:{conf:.2f}",
                            (x1,y1-10),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.5,
                            (0,255,0),
                            1
                            )
                
    return tracked_people,annotated_frame            

       
                    