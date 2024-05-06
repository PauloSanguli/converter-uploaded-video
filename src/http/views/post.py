from src.http.app import app
from flask import make_response, jsonify
from flask import request




@app.post("/record-video")
def record_video():
    VIDEO_TO_SAVE = request.files.get("")
    return 