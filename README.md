# Automated-Cricket-Commentary-
The objective of the project is to generate automatic commentary for cricket videos with the help of computer vision and neural networks.\
This project contains two branches

1. Modelling
2. User-Interface

Modelling

In this folder there is Data folder and Modelling Jupyter file. In Data folder there is Images file containing link to images, Ntest.txt which is testing data, Ntrain.txt which is training data and N_token.txt which contains the image name and respective comments. For each image five different comments are written.

The model used is a basic merge model. This model uses VGG16 pre-trained model for the feature extraction from the frames and used RNN-LSTM to process the sequence of the text input. The outputs of these two models are taken as the inputs for the decoder or the merger where the inputs are merged and are processed by the dense layer for the final prediction. A few dropout layers have been implementd to reduce overfitting.




User-Interface 

Three python files namely UI_final.py, model_final.py and similarity.py We are using streamlit for creating User interface. The UI_final.py file consists of the code to create user interface. In the modelling part, we get a model for image captioning, based on this model we can predict captioning for images. While playing the video frames are considered and non similar frames are captioned. That will be the output.

Project Presentation - https://www.slideshare.net/GokulSuseendran/automated-cricket-commentary
