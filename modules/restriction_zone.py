import cv2


ZONE_X1=252
ZONE_Y1=435
ZONE_X2=480
ZONE_Y2=573



def detect_intrusion(frame, tracked_people):

    intrusion_detected = False
    violating_ids = []

    # Draw restriction zone
    cv2.rectangle(
        frame,
        (ZONE_X1, ZONE_Y1),
        (ZONE_X2, ZONE_Y2),
        (0, 0, 255),
        2
    )

    cv2.putText(
        frame,
        "RESTRICTED ZONE",
        (ZONE_X1, ZONE_Y1 - 10),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0, 0, 255),
        2
    )

    for person in tracked_people:

        person_id = person["track_id"]

        x1, y1, x2, y2 = person["bbox"]

        # Bottom-center of person's box
        foot_x = (x1 + x2) // 2
        foot_y = y2

        # Check if inside zone
        if (
            ZONE_X1 <= foot_x <= ZONE_X2
            and
            ZONE_Y1 <= foot_y <= ZONE_Y2
        ):

            intrusion_detected = True

            violating_ids.append(person_id)

            cv2.putText(
                frame,
                f"INTRUDER ID {person_id}",
                (x1, y1 - 20),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 0, 255),
                2
            )

    return (
        frame,
        intrusion_detected,
        violating_ids
    )