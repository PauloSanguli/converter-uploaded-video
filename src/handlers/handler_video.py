"""save video on folder resources"""
from src.resources.__path__ import PATH_RESOURCES
from datetime import datetime

import cv2



class Handler:
    @classmethod
    def save_video(cls, video: any, local_capture: str):
        """save video on dir resources"""
        cls.get_info_video(video, local_capture)
        print(PATH_RESOURCES)
        video.save(f"{PATH_RESOURCES}\\{cls.filename}")
        
    @classmethod
    def get_info_video(cls, video: any, local_capture: str):
        """get informations of the file"""
        time_formated = str(datetime.utcnow().time()).\
            replace('.', '_').\
                replace(':', '-')
        datetime_str = f"{local_capture}__{datetime.utcnow().date()}__{time_formated}"
        
        cls.filename = f"{datetime_str}.mp4"

        print(cls.filename)
        