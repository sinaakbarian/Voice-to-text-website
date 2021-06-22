# Voice-to-text-website
Using google API to convert voice to text using google cloud backend as a webservice(I used python 3.6)
              
    git clone https://github.com/sinaakbarian/Voice-to-text-website.git
    
Install requirement packages:

     pip install -r requirements.txt 
  
 To test the app on a local server:

     gunicorn -b :8889 app:app -t 120 --graceful-timeout 60
     
Then open a browser go to http://localhost:8889/ and use the app. To deploy it on the GCP you need to install GCP SDK: https://cloud.google.com/sdk/install. Once initialization is done:

            gcloud init
The app will be deployed with the following command:

            gcloud app deploy
The web will be open with:

             gcloud app browse
