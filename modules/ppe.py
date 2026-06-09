
import cv2
def ppe_compliance(frame,tracked_people,model):
    violating_ids=[]
    helmets=[]
    vests=[]
    results=model(frame)
    ppe_alert=False

    if len(results) > 0:
        result=results[0]

        if result.boxes is not None:
            boxes=result.boxes
            for box in boxes:
                cls=int(box.cls[0])
                cls_name=model.names[cls]

                x1,y1,x2,y2=box.xyxy[0]
                x1=int(x1)
                y1=int(y1)
                x2=int(x2)
                y2=int(y2)

                conf=float(box.conf[0])

                if conf  > 0.5:

                    if cls_name.lower() =="hardhat":
                        helmets.append(
                            (x1,y1,x2,y2)
                        )
                    if cls_name.lower() =="vest":
                        vests.append(
                            (x1,y1,x2,y2)
                        )    
                        


    # check for every single person if they are wearing helmet and vest
    for person in tracked_people:
        px1,py1,px2,py2=person["bbox"]
        person_id=person["track_id"]

        person_helmet=False
        person_vest=False

        # check for helmet

        for x1,y1,x2,y2 in helmets:
            
            h_center_x=(x1+x2)//2
            h_center_y=(y1+y2)//2

            if px1 <h_center_x < px2  and py1 < h_center_y  < py2:
                person_helmet=True
                break

        # check for vest

        for x1,y1,x2,y2 in vests:

            v_center_x=(x1+x2)//2
            v_center_y=(y1+y2)//2
            if px1 <v_center_x < px2  and py1 < v_center_y  < py2:

                person_vest=True
                break     


        # ppe compliance status

        if person_helmet and person_vest:
            status="PPE OK"

        elif person_helmet and not person_vest:
            status="NO VEST"
            violating_ids.append(person_id)

        elif not person_helmet and person_vest:
            status="NO HELMET"
            violating_ids.append(person_id)
        else:
            status="NO HELMET AND NO VEST"        
            violating_ids.append(person_id)

        cv2.putText(frame,
                    status,
                    (px1,py1+10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.5,
                    (255,0,255),
                    2)    


    if len(violating_ids)> 0:
        ppe_alert=True       

    return frame,ppe_alert,violating_ids     

    
        
