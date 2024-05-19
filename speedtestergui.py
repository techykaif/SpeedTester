import speedtest
import time
import tkinter as tk
from tkinter import Tk, Label, Button

class SpeedTest:
    @staticmethod
    def run_speed_test():
        st = speedtest.Speedtest()
        st.get_best_server()
        download_speed = st.download() / 10**6  # Convert to Mbps

        # Add a delay before measuring upload speed
        upload_speed = "N/A"  # Default value for upload speed
        try:
            time.sleep(5)
            upload_speed = st.upload() / 10**6  # Convert to Mbps
        except:
            pass

        ping = st.results.ping

        # Update labels with speed test results
        lbShowDownload.config(text=f"{download_speed:.2f} Mbps")
        lbShowUpload.config(text=f"{upload_speed:.2f} Mbps")
        lbShowPing.config(text=f"{ping:.2f} ms")

    def __init__(self, root):
        self.root = root
        self.root.title("Speed Tester")
        self.root.geometry("800x600+100+0")

        global lbShowDownload, lbShowUpload, lbShowPing

        lbDownload = Label(self.root, text="Download Speed : ", padx=100, pady=50)
        lbDownload.grid(row=0, column=1)
        lbShowDownload = Label(self.root, text="Here will be the download Speed", padx=100, pady=50)
        lbShowDownload.grid(row=0, column=2)

        lbUpload = Label(self.root, text="Upload Speed : ", padx=100, pady=50)
        lbUpload.grid(row=1, column=1)
        lbShowUpload = Label(self.root, text="Here will be the upload Speed", padx=100, pady=50)
        lbShowUpload.grid(row=1, column=2)

        lbPing = Label(self.root, text="Ping : ", padx=100, pady=50)
        lbPing.grid(row=2, column=1)
        lbShowPing = Label(self.root, text="Here will be the ping", padx=100, pady=50)
        lbShowPing.grid(row=2, column=2)

        button = Button(self.root, text="Run SpeedTest", padx=10, pady=10, fg="green", width=20, bd=20,
                        relief=tk.RIDGE, activebackground="white", background="black", command=self.run_speed_test)
        button.grid(row=3, column=2)

root = Tk()
ob = SpeedTest(root)
root.mainloop()
