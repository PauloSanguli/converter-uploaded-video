"""save video on folder resources"""
from src.resources.__path__ import PATH_RESOURCES
from datetime import datetime

import cv2

import os



class Handler:
    @classmethod
    def save_video(cls, video: any, local_capture: str):
        """save video on dir resources"""
        cls.get_info_video(local_capture)
        
        if ".mp4" in video.filename:
            video.save(f"{PATH_RESOURCES}\\{cls.filename}")
        else:
            FULL_PATH_TEMP = f"{PATH_RESOURCES}\\temp_{video.filename}"
    
            video.save(FULL_PATH_TEMP)
            
            cls.converter_video(FULL_PATH_TEMP)
            
    
    @classmethod
    def converter_video(cls, path_temp: str):
        """convert video webm to mp4"""
        VIDEO_TO_CONVERT_WEBM = cv2.VideoCapture(path_temp)
        
        CONTANTS = [
            cv2.VideoWriter_fourcc(*'mp4v'),
            VIDEO_TO_CONVERT_WEBM.get(cv2.CAP_PROP_FPS),
            (
                int(VIDEO_TO_CONVERT_WEBM.get(cv2.CAP_PROP_FRAME_WIDTH)),
                int(VIDEO_TO_CONVERT_WEBM.get(cv2.CAP_PROP_FRAME_HEIGHT))
            )
        ]
        OUTPUT_VIDEO = f"{PATH_RESOURCES}\\{cls.filename}"
        
        VIDEO_CONVERTED_MP4 = cv2.VideoWriter(OUTPUT_VIDEO, CONTANTS[0], CONTANTS[1], CONTANTS[2])

        while VIDEO_TO_CONVERT_WEBM.isOpened():
            IS_VALID_FRAME, FRAME = VIDEO_TO_CONVERT_WEBM.read()
            if IS_VALID_FRAME:
                VIDEO_CONVERTED_MP4.write(FRAME)
            else: break
            
        VIDEO_TO_CONVERT_WEBM.release()
        VIDEO_CONVERTED_MP4.release()

        cv2.destroyAllWindows()
        
        cls.remove_temp_video(path_temp)
            
    @classmethod
    def remove_temp_video(cls, path_temp: str):
        """remove temporays videos"""
        print(path_temp)
        if os.path.exists(path_temp):
            os.remove(path_temp)

    @classmethod
    def get_info_video(cls, local_capture: str):
        """get informations of the file"""
        time_formated = str(datetime.utcnow().time()).\
            replace('.', '_').\
                replace(':', '-')
        datetime_str = f"{local_capture}__{datetime.utcnow().date()}__{time_formated}"
        
        cls.filename = f"{datetime_str}.mp4"
