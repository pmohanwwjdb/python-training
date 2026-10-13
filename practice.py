
# username = input("Enter the name:")
# if username == "jinwoo":
#     print("valid")
#     password = input("Enter the password:")
#     if password == "solo leveling":
#         print("login successfully")
# else:
#     print("invalid")





# i = 1
# sum =0
# while i <= 5:
#     sum += i
#     i+=1
#     print(sum)  


# n = int(input("Enter the number:"))
# count = 0
# for i in range (1,n):
#     if i%3==0:
#         count += 1
# print(count)

# n = int(input("Enter the number:"))
# for i in range (1,n+1):
#     print(i**3)


# n = int(input("Enter the value of n:"))
# sum =0
# for i in range (1,n+1):
#     if i%2 != 0:
#         sum = sum+iJI
# print("sum of odd number =",sum)  


# name = input("enter the name:")
# if name.isalpha():
#     print("Alpha")
# else :
#     print("Not Alpha")


# name = input("Enter the name:")
# names = ["car","motor","bike"]
# if name in names:
#     print("found")
# else:
#     print("not found")

# names = ["jinwoo","solo","leveling","nah"]
# for i in names:
#     print(i)



# n = [20,30,40,50]
# sum = 0
# for i in n:
#     sum = sum+i
#     print(sum)


# n = [24,25,78,46,89,23]
# for i in n:
#     if i%2 == 0:
#         print("even number=",i)
#     else:
#         print("odd number=",i)


# n = [24,25,78,46,89,23]
# sum = 0
# for i  in n:
#     sum += i
# print(sum//len(n))

# n = int(input("Enter the number:"))
# num = [2,4,3,5,6]
# for i in num:
#     if n == i:
#         print("found")
#     else :
#         print("not found")

# n = [2,3,-6,7,5,9,-4,-8]
# for i in n:
#     if i >0:
#         print("positive number=",i)
#     else:
#         print("negative number=",i) 




import cv2
import mediapipe as mp
import pyautogui
import math

# Open webcam
cap = cv2.VideoCapture(0)

# Get screen size
screen_width, screen_height = pyautogui.size()

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

mp_draw = mp.solutions.drawing_utils

while True:
    success, frame = cap.read()

    if not success:
        print("Failed to access webcam.")
        break

    # Flip image
    frame = cv2.flip(frame, 1)

    # Convert to RGB
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process hand
    results = hands.process(rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:

            mp_draw.draw_landmarks(
                frame,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS
            )

            # Index finger tip
            index = hand_landmarks.landmark[
                mp_hands.HandLandmark.INDEX_FINGER_TIP
            ]

            # Thumb tip
            thumb = hand_landmarks.landmark[
                mp_hands.HandLandmark.THUMB_TIP
            ]

            # Move mouse
            mouse_x = int(index.x * screen_width)
            mouse_y = int(index.y * screen_height)
            pyautogui.moveTo(mouse_x, mouse_y)

            # Click gesture
            distance = math.hypot(
                index.x - thumb.x,
                index.y - thumb.y
            )

            if distance < 0.04:
                pyautogui.click()
                pyautogui.sleep(0.3)

    cv2.imshow("Virtual Mouse", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()