import cv2, dropbox, random, time

startT = time.time()

def Security():
    
    VideoCaptureObject = cv2.VideoCapture(0)
    result = True
    while result:
        number = random.randint(0,100)
        name = "wow" + (str(number) + ".png")
        ret,frame = VideoCaptureObject.read()
        cv2.imwrite(name, frame)
        startT = time.time()
        result = False

    return(name)
    print("Done")

    VideoCaptureObject.release()

    cv2.destroyAllWindows()



def uploadFiles(nameObj):
    access_token = "jukkm3kS-C4AAAAAAAAAAbXw5YXUfC1cwVjqW7X6Yf5gTsUJSeQP9NOy5p2U70Uu"
    
    file_from = nameObj
    file_to = "/wow/" + (nameObj)  # The full path to upload the file to, including the file name
    dbx = dropbox.Dropbox(access_token)
    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(), file_to, mode = dropbox.files.WriteMode.overwrite)
        print('file uploaded')


def Caller():
    while (True):
        if ((time.time() - startT) > 5):
            nameThing = Security()
            uploadFiles(nameThing)



Caller()