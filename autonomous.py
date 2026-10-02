from coppeliasim_zmqremoteapi_client import RemoteAPIClient
import cv2
import numpy as np
import time

# Connect to CoppeliaSim
client = RemoteAPIClient()
sim = client.getObject('sim')

script = sim.getScript(sim.scripttype_simulation,
                       sim.getObject('/UR5'))

print("Connected to CoppeliaSim")

cap = cv2.VideoCapture(0)

lastColor = ""
lastCommandTime = 0
cooldown = 3  # seconds

while True:

    ret, frame = cap.read()

    if not ret:
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # ---------------- RED ----------------
    lower_red1 = np.array([0, 120, 70])
    upper_red1 = np.array([10, 255, 255])

    lower_red2 = np.array([170, 120, 70])
    upper_red2 = np.array([180, 255, 255])

    redMask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    redMask2 = cv2.inRange(hsv, lower_red2, upper_red2)
    redMask = redMask1 + redMask2

    # ---------------- BLUE ----------------
    lower_blue = np.array([100, 150, 50])
    upper_blue = np.array([140, 255, 255])

    blueMask = cv2.inRange(hsv, lower_blue, upper_blue)

    redPixels = cv2.countNonZero(redMask)
    bluePixels = cv2.countNonZero(blueMask)

    currentTime = time.time()

    # ---------------- RED DETECTED ----------------
    if redPixels > 5000:

        cv2.putText(frame, "RED", (20, 40),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1, (0, 0, 255), 2)

        if (lastColor != "RED") and ((currentTime - lastCommandTime) > cooldown):

            sim.callScriptFunction(
                'setTargetColor',
                script,
                'RED'
            )

            print("RED sent")

            lastColor = "RED"
            lastCommandTime = currentTime

    # ---------------- BLUE DETECTED ----------------
    elif bluePixels > 5000:

        cv2.putText(frame, "BLUE", (20, 40),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1, (255, 0, 0), 2)

        if (lastColor != "BLUE") and ((currentTime - lastCommandTime) > cooldown):

            sim.callScriptFunction(
                'setTargetColor',
                script,
                'BLUE'
            )

            print("BLUE sent")

            lastColor = "BLUE"
            lastCommandTime = currentTime

    # ---------------- NO OBJECT ----------------
    else:
        lastColor = ""

    cv2.imshow("Webcam", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()