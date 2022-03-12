# TODO: Create a youtube video downloader with a simple GUI interface.

# imports
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pytube
import os


# classes block
class Logic:
    """This class implements logic for downloading videos from https://www.youtube.com"""

    def __init__(self, video_url: str, file_format: str, save_path="C://Downloads"):
        """Init the logic"""
        self.video_url = video_url
        self.file_format = file_format
        self.save_path = save_path

    def download_video(self):
        """
        This method downloads video from https://youtube.com using pytube library.
        :return: None
        """
        # create a pytube.Youtube instance
        youtube_object = pytube.YouTube(self.video_url)

        # get the quality and the format of the video
        youtube_object = youtube_object.streams\
            .filter(progressive=True, file_extension=self.file_format).order_by('resolution').desc().first()

        # check if the save path exists
        if not os.path.exists(self.save_path):
            os.mkdir(self.save_path)

        # download the video
        youtube_object.download(self.save_path)


if __name__ == "__main__":
    app = Logic("https://www.youtube.com/watch?v=BJ-VvGyQxho&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=43", "mp4",
                "C://Users//Ilya//Downloads")
    app.download_video()

