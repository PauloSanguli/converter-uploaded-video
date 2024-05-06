"""routes post"""
from src.http.app import app

from flask import make_response, jsonify
from flask import request

from src.handlers import Handler




@app.post("/record-video")
def record_video():
    try:
        VIDEO_TO_SAVE = request.files.get("video-captured")
        Handler.save_video(VIDEO_TO_SAVE)
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
