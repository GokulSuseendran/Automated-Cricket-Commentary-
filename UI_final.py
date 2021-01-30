import streamlit as st
import io
import cv2
import os
from PIL import Image
from gtts import gTTS 
import model_final
import similarity





st.title("Play Uploaded File")

uploaded_file = st.file_uploader("Choose a video...", type=["mp4"])
temporary_location = False

if uploaded_file is not None:
    g = io.BytesIO(uploaded_file.read())  ## BytesIO Object
    temporary_location = "testout_simple.mp4"

    with open(temporary_location, 'wb') as out:  ## Open temporary file as bytes
        out.write(g.read())  ## Read bytes into file

    # close file
    out.close()


@st.cache(allow_output_mutation=True)
def get_cap(location):
    print("Loading in function", str(location))
    video_stream = cv2.VideoCapture(str(location))

    # Check if camera opened successfully
    if (video_stream.isOpened() == False):
        print("Error opening video  file")
    return video_stream


scaling_factorx = 0.900
scaling_factory = 0.9
image_placeholder = st.empty()
currentframe = 1
#Enter a directory for the frames to get stored in
target = #'C:/frames'
dr = similarity.DuplicateRemover(target)
list1 = os.listdir(target)
try:
    for i in list1:
        os.remove(target+"/"+i)
except:
    print("Break")
#img1 = str(1) + '.jpg'


def model1(file_name,path):
    # load the tokenizer
    tokenizer = model_final.load(open('tokenizer1.pkl', 'rb'))
    # pre-define the max sequence length (from training)
    max_length = 25
    # load the model
    #model = load_model('/C:/Users/User/Desktop/All_codes/Stremlit/Model/model-ep009-loss0.391-val_loss0.483.h5')
    model = model_final.load_model(os.path.join(os.getcwd(), 'Model', 'model-ep009-loss0.391-val_loss0.483.h5'))
    # load and prepare the photograph
    photo = model_final.extract_features(path)
    #img = plt.imread('C:/Users/User/Desktop/All_codes/Stremlit/Model/1 - Copy.png')
    #plt.imshow(img)
    # generate description
    text = model_final.generate_desc(model, tokenizer, photo, max_length)
    text = text.split()
    #startseq bowler is bowling endseq
    text.remove('startseq')
    text.remove('endseq')
    text = ' '.join(text)
    st.write(text)
    audio(file_name,text)


def audio(b,name2):
    #Enter a directory for audio created for the comments generated to get stored
    target = #"C:Audio/"
    language = 'en'
    myobj = gTTS(text=name2, lang=language, slow=False) 
    myobj.save(target + b + ".mp3")
    os.system(target + b + ".mp3") 




def grey_scale(path,target):
    #list1 = os.listdir(directory)
    #for i in list1:
    length = len(path.split('/'))
    b = path.split('/')[length-1]
    b = b.split('.')[0]
    #name = path
    #print(name)
    img = Image.open(path).convert('LA')
    name2 = target + "/" + b + ".png"
    img.save(name2)
    #st.write(name2)
    model1(b,name2)
    #audio(b,name2)

image_checkpoint = 1

if temporary_location:
    while True:
        # here it is a CV2 object
        video_stream = get_cap(temporary_location)
        # video_stream = video_stream.read()
        ret, image = video_stream.read()
        if ret:
            if len(os.listdir(target)) < 1:
                print("first loop")
                # if video is still left continue creating images 
                name = target +"/"+ str(currentframe) + '.jpg'
                print ('Creating...' + name) 
                img1 = str(currentframe) + '.jpg'
                name1 = currentframe
                # writing the extracted images 
                cv2.imwrite(name, image) 
                #Enter path for the greyscale image of frames to be stored
                grey_scale(name,'C:/Grey_scale')

                # increasing counter so that it will 
                # show how many frames are created 
                currentframe += 1
                #img2 = str(currentframe) + '.jpg'
                cv2.waitKey(100)
                #img1 = name
            else:
                # if video is still left continue creating images 
                #print(img1)
                #img1 = str(name1) + ".jpg"
                #print("second_loop")
                name = target +"/"+ str(currentframe) + '.jpg'
                print ('Creating...' + name) 
                img2 = str(currentframe) + '.jpg'

                # writing the extracted images 
                cv2.imwrite(name, image) 
          

                # increasing counter so that it will 
                # show how many frames are created 
                currentframe += 1
                #img2 = str(currentframe) + '.jpg'
                if dr.similarity_between(target,img1,img2) == 1:
                    os.remove(target + "/" + img2 )
                    #print("similar")
                    count = 1
                else:
                    #print("next image")
                    img1 = str(currentframe-1) + '.jpg'
                    path1 = target + "/" + img1
                    #print(img1)
                    image_checkpoint +=1 
                    if image_checkpoint < 41:
                        if image_checkpoint%5 == 0:
                        # or image_checkpoint == 1:
                            grey_scale(path1,'C:/Grey_scale')
                    #break
        else:
            print("there was a problem or video was finished")
            cv2.destroyAllWindows()
            video_stream.release()
            break
        # check if frame is None
        if image is None:
            print("there was a problem None")
            # if True break the infinite loop
            break

        image_placeholder.image(image, channels="BGR", use_column_width=True)

        cv2.destroyAllWindows()
    video_stream.release()


    cv2.destroyAllWindows()
