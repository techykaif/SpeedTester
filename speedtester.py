import tkinter as tk
from tkinter import messagebox
import speedtest
import time

def run_speed_test():
    st = speedtest.Speedtest()
    st.get_best_server()
    download_speed = st.download() / 10**6  # Convert to Mbps

    # Add a delay before measuring upload speed
    upload_speed = "N/A"  # Default value for upload speed
    try:
        time.sleep(5);
        upload_speed = st.upload() / 10**6  # Convert to Mbps
    except:
        pass

    ping = st.results.ping

    result_text = f"Download Speed: {download_speed:.2f} Mbps\n"
    result_text += f"Upload Speed: {upload_speed:.2f} Mbps\n"
    result_text += f"Ping: {ping:.2f} ms"

    messagebox.showinfo("Speed Test Results", result_text)
    print("Speed Test Results",result_text)

def main():
    root = tk.Tk()
    root.title("Speed Test")

    frame = tk.Frame(root)
    frame.pack(padx=20, pady=20)

    button = tk.Button(frame, text="Run Speed Test\n", command=run_speed_test)
    button.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
