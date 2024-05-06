"""save video on folder resources"""
from src.resources.__path__ import PATH_RESOURCES



class Handler:
    @classmethod
    def save_video(cls, video: any):
        """save video on dir resources"""
        cls.get_info_video(video)
        
        
    @classmethod
    def get_info_video(cls, video: any):
        """get informations of the file"""
        print(video.filename)
        