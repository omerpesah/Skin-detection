import cv2
import Functions

print("Type 1 for greenish code or 0 to radioactive zombie!")
choice = input()

path = "C:\Users\Omer\Desktop\New video2.mp4"
cap = cv2.VideoCapture(path)

if choice == 1:

    while (True):
        ret, frame = cap.read()
        if ret:

            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) # change from RGB to HSV and put the skin color range.
            mask1 = cv2.inRange(hsv, (0, 48, 80), (20, 255, 255)) # for image change to (0, 50, 0) (120, 150, 255).

            # manipulating the mask.
            mask = Functions.minErosion(mask1)
            mask = Functions.maxDilation(mask)
            mask = Functions.medianBlur(mask, 3)
            mask = Functions.makeItGreen(mask, frame)

            cv2.imshow("video", mask)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break
    cv2.destroyAllWindows()


elif choice == 0:

    while (True):
        ret, frame = cap.read()
        if ret:

            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            mask1 = cv2.inRange(hsv, (0, 48, 80), (20, 255, 255))

            mask = Functions.minErosion(mask1)
            mask = Functions.maxDilation(mask)
            mask = Functions.medianBlur(mask, 5)
            mask3 = Functions.makeItRadioactiveGreen(mask, frame)

            cv2.imshow("video", mask3)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break
    cv2.destroyAllWindows()


