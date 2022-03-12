# TODO: Create a youtube video downloader with a simple GUI interface.

# imports
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
import pytube
import os


# classes block
class Logic:
    """This class implements logic for downloading videos from https://www.youtube.com"""

    def __init__(self, video_url: str, save_path="C://Downloads"):
        """Init the logic"""
        self.video_url = video_url
        self.save_path = save_path

    def download_video(self):
        """
        This method downloads video from https://youtube.com using pytube library.
        :return: None
        """
        # create a pytube.Youtube instance
        youtube_object = pytube.YouTube(self.video_url)

        # get the quality and the format of the video
        youtube_object = youtube_object.streams \
            .filter(progressive=True, file_extension="mp4").order_by('resolution').desc().first()

        # check if the save path exists
        if not os.path.exists(self.save_path):
            os.mkdir(self.save_path)

        # download the video
        youtube_object.download(self.save_path)


class GUI(Logic):
    """This class implements GUI for the application"""

    def __init__(self):
        """Init the gui"""
        # root creation
        self.root = Tk()

        # root config
        self.root.title("Youtube Downloader")
        self.root.iconbitmap("assets/favicon.ico")

        # styles
        self.mainframe_style = ttk.Style()
        self.mainframe_style.configure("MainFrame.TFrame", background="#FFF")

        self.logo_style = ttk.Style()
        self.logo_style.configure("Logo.TLabel", background="#FFF")

        # mainframe
        self.mainframe = ttk.Frame(self.root, style="MainFrame.TFrame")
        self.mainframe.grid(column=0, row=0)

        # logo
        logo_image = ImageTk.PhotoImage(Image.open("assets/images/logo.png"))
        self.logo_label = ttk.Label(self.mainframe, image=logo_image, style="Logo.TLabel")
        self.logo_label.grid(column=1, row=0, padx=20, pady=20)

        # labels

        # inherit from the parent class
        Logic.__init__(self,
                       "https://www.youtube.com/watch?v=BJ-VvGyQxho&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=43",
                       "C://Users//Ilya//Downloads")

        # mainloop
        self.root.mainloop()


if __name__ == "__main__":
    gui = GUI()
