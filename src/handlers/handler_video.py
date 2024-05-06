"""save video on folder resources"""
from src.resources.__path__ import PATH_RESOURCES
from datetime import datetime

import cv2



class Handler:
    @classmethod
    def save_video(cls, video: any):
        """save video on dir resources"""
        cls.get_info_video(video)
        print(PATH_RESOURCES)
        video.save(f"{PATH_RESOURCES}\\{cls.filename}")
        
    @classmethod
    def get_info_video(cls, video: any):
        """get informations of the file"""
        time_formated = str(datetime.utcnow().time()).\
            replace('.', '_').\
                replace(':', '-')
        datetime_str = f"{datetime.utcnow().date()}_{time_formated}"
        
        cls.filename = f"{datetime_str}.mp4"

        print(cls.filename)
        