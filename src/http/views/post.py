"""routes post"""
from src.http.app import app

from flask import make_response, jsonify
from flask import request

from src.handlers import Handler

import json



@app.post("/record-video/")
def record_video():
    try:
        VIDEO_TO_SAVE = request.files.get("video-captured")
        local_capture = json.loads(request.form.get("jsonData"))
        
        Handler.save_video(VIDEO_TO_SAVE, local_capture["local"].lower())
    except Exception as error:
        print(error)
        return make_response(
            jsonify({
                "msg": "video dont saved"
            }),
            400
        )
    else:
        return make_response(
            jsonify({
                "msg": "video saved with sucess"
            }),
            201
        )
