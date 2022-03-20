# TODO: Create a youtube video downloader with a simple GUI interface.

# imports
from tkinter import *
from tkinter import ttk
from tkinter.font import Font
from tkinter import messagebox
from PIL import ImageTk, Image
import concurrent.futures
import pytube
import os


# classes block
class Logic:
    """This class implements logic for downloading videos from https://www.youtube.com"""

    def __init__(self, video_url: str, save_path="C://Downloads"):
        """
        Init the logic of the application
        :param video_url: url of the video that you want to download
        :param save_path: directory where you want your video to be saved
        """
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


class GUI:
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

        font_for_labels = Font(family="Arial", size=18, weight="bold")
        self.labels_style = ttk.Style()
        self.labels_style.configure("Labels.TLabel", foreground="#000", background="#FFF", font=font_for_labels)

        font_for_entries = Font(family="Arial", size=12)
        self.entries_style = ttk.Style()
        self.entries_style.configure("Entries.TEntry")

        # mainframe
        self.mainframe = ttk.Frame(self.root, style="MainFrame.TFrame")
        self.mainframe.grid(column=0, row=0)

        # logo
        logo_image = ImageTk.PhotoImage(Image.open("assets/images/logo.png"))
        self.logo_label = ttk.Label(self.mainframe, image=logo_image, style="Logo.TLabel")
        self.logo_label.grid(column=0, row=0, padx=20, columnspan=4)

        # labels
        self.url_label = ttk.Label(self.mainframe, text="Video URL", style="Labels.TLabel", )
        self.url_label.grid(column=0, row=1, padx=10, pady=10, columnspan=2, sticky=W)

        self.save_path_label = ttk.Label(self.mainframe, text="Save Path", style="Labels.TLabel")
        self.save_path_label.grid(column=0, row=2, padx=10, pady=10, columnspan=2, sticky=W)

        # entries
        self.url_entry = ttk.Entry(self.mainframe, width=40, style="Entries.TEntry", font=font_for_entries)
        self.url_entry.grid(column=2, row=1, padx=10, pady=10, columnspan=2)

        self.save_path_entry = ttk.Entry(self.mainframe, width=40, style="Entries.TEntry", font=font_for_entries)
        self.save_path_entry.grid(column=2, row=2, padx=10, pady=10, columnspan=2)

        # inherit from the parent class
        logic = Logic(str(self.url_entry.get()), str(self.save_path_entry.get()))

        # buttons
        self.download_button = ttk.Button(self.mainframe, text="Download", style="Buttons.TButton", padding=5,
                                          command=logic.download_video)
        self.download_button.grid(column=1, row=3, padx=10, pady=10, sticky=E)

        self.close_button = ttk.Button(self.mainframe, text="Close", style="Buttons.TButton",
                                       command=self.mainframe.quit, padding=5)
        self.close_button.grid(column=3, row=3, padx=10, pady=10)

        # mainloop
        self.root.mainloop()


if __name__ == "__main__":
    gui = GUI()
