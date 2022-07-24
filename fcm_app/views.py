from django.shortcuts import render
from django.http.request import HttpHeaders
from django.http import HttpResponse
import requests
import json


# Create your views here.
def send_notification(registration_ids, message_title, message_text):
    fcm_api = "AAAAPWE-sFA:APA91bF06cw6WiTE5o7J3LJCJIxRz9pq60K4TgGSSqB02yUGEo8AmzmEK35r9DSxvQLzW_UOHGY8LlziKEQyIaEDpFgp9B5ORB97dp_EwPLX_Z2-4_SZN7a_l8jbF_2DOC4u16BsihdP"
    url = "https://fcm.googleapis.com/fcm/send"

    headers = {
        "Content-Type": "application/json",
        "Authorization": 'key=' + fcm_api}

    payload = {
        "registration_ids": registration_ids,
        "priority": "high",
        "notification": {
            "body": message_text,
            "title": message_title,
            # "image": "https://i.ytimg.com/vi/m5WUPHRgdOA/hqdefault.jpg?sqp=-oaymwEXCOADEI4CSFryq4qpAwkIARUAAIhCGAE=&rs=AOn4CLDwz-yjKEdwxvKjwMANGk5BedCOXQ",
            # "icon": "https://yt3.ggpht.com/ytc/AKedOLSMvoy4DeAVkMSAuiuaBdIGKC7a5Ib75bKzKO3jHg=s900-c-k-c0x00ffffff-no-rj",

        }
    }

    result = requests.post(url, data=json.dumps(payload), headers=headers)
    print(result.json())


def index(request):
    return render(request, 'index.html')


def send(request):
    registration = ['c9gMmXGEUGfS8oqyUDRJWn:APA91bGuo8dgNGE9VRKkVmST1F2XqvEyDVZYhx5oxUuktMzEupjSsLGjD4UUizvuBA-GL8zG8_9aw8J209B_hT9z8Af7cdhedrF3ldSePmIkp98Li2IjXI3mc_LColF1EnHf3wWlbl0t']
    send_notification(registration,
                      'Code Keen added a new video',
                      'Code Keen new video alert')
    return HttpResponse("sent")


def showFirebaseJS(request):
    data = 'importScripts("https://www.gstatic.com/firebasejs/8.2.0/firebase-app.js");' \
           'importScripts("https://www.gstatic.com/firebasejs/8.2.0/firebase-messaging.js"); ' \
           'var firebaseConfig = {' \
           '        apiKey: "AIzaSyBUZSfVyCsCbpDAfRToAq4xycnNi_MiLTY",' \
           '        authDomain: "djangofcm-ffc7c.firebaseapp.com",' \
           '        databaseURL: "https://djangofcm-ffc7c-default-rtdb.firebaseio.com/",' \
           '        projectId: "djangofcm-ffc7c",' \
           '        storageBucket: "djangofcm-ffc7c.appspot.com",' \
           '        messagingSenderId: "263624503376",' \
           '        appId: "1:263624503376:web:3461f9a997fea6ed042155",' \
           '        measurementId: "G-LCZ9KETX5T"' \
           ' };' \
           'firebase.initializeApp(firebaseConfig);' \
           'const messaging=firebase.messaging();' \
           'messaging.setBackgroundMessageHandler(function (payload) {' \
           '    console.log(payload);' \
           '    const notification=JSON.parse(payload);' \
           '    const notificationOption={' \
           '        body:notification.body,' \
           '        icon:notification.icon' \
           '    };' \
           '    return self.registration.showNotification(payload.notification.title,notificationOption);' \
           '});'

    return HttpResponse(data, content_type="text/javascript")
