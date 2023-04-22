import easyocr
import cv2
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


# this needs to run only once to load the model into memory
reader = easyocr.Reader(['en'])

vid = cv2.VideoCapture(0)

while (True):

    # Capture the video frame
    # by frame
    ret, frame = vid.read()

    result = reader.readtext(frame)
    print(result)
    cv2.imshow('frame', frame)

    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()

# https://www.jaided.ai/easyocr/modelhub/
