import cv2
import sys


def artifact2(image):
    # Greyscale input
    imageGreyed = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Find faces from input
    faces = faceCascade.detectMultiScale(imageGreyed)

    # For each face:
    for xPosition, yPosition, width, height in faces:

        # Outline face with green rectangle
        image = cv2.rectangle(image, (xPosition, yPosition), (xPosition + width, yPosition + height), (0, 255, 0), 2)

        # Get face
        face = image[yPosition: yPosition + height, xPosition: xPosition + width]

        # Find eyes in face
        for eyeXPosition, eyeYPosition, eyeWidth, eyeHeight in eyeCascade.detectMultiScale(imageGreyed[yPosition: yPosition + height, xPosition: xPosition + width]):
            # Outline eyes with red rectangle
            cv2.rectangle(face, (eyeXPosition, eyeYPosition), (eyeXPosition + eyeWidth, eyeYPosition + eyeHeight), (255, 0, 0), 2)
    return image


if __name__ == "__main__":
    # Variable Declaration
    choice = -1
    faceCascade = cv2.CascadeClassifier("haarcascades/haarcascade_frontalface_alt.xml")
    eyeCascade = cv2.CascadeClassifier("haarcascades/haarcascade_eye.xml")
    image = []

    # Handle arguments
    if len(sys.argv) < 2:
        choice = input("Enter parameter: ")
        if choice == '':
            print("Parameter error: No Parameters entered.")
            exit(-1)
        if choice[0] == '"' and choice[-1] == '"':
            choice = choice[1:-1]
    else:
        choice = sys.argv[1]
    if choice == '0':
        print("Press the 'q' button to exit the application")
        cam = cv2.VideoCapture(0)
        while True:
            # Get Input
            _, frame = cam.read()

            cv2.imshow("frame", artifact2(frame))
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cam.release()
        cv2.destroyAllWindows()
    else:
        try:
            image = cv2.imread(choice, 1)
            cv2.imshow("Original Image", image)
        except:
            print("Parameter error: Image " + choice + " could not be read.")
            exit(-2)
        cv2.imshow("Detected", artifact2(image))
        cv2.waitKey(0)
        cv2.destroyAllWindows()
