import os
import cv2
from datetime import datetime
from llama_generation import LLAMA
from llava_description import LLAVA
from db_operations import database

SAVE_FRAMES_PATH = 'frames'
DB_PATH = "alerts.db"

## creating objects of llava and llama for description and generation purpose
llava = LLAVA()
llama = LLAMA()
db = database(DB_PATH)

class Camera:
    """
    Handles video stream reading and frame extraction.
    """

    def __init__(self, url, skip = 30):
        self.url = url
        self.skip = skip
        self.frame_save_path = SAVE_FRAMES_PATH

    def read_stream(self):
        """
        Reada video frame-by-frame and senda to the LlaVa and Llama for description and alert generation purpose.
        """
        print('Video Processing Started !')

        os.makedirs(self.frame_save_path, exist_ok=True)
        cap = cv2.VideoCapture(self.url)
        self.frame_count = -1
        while True:
            self.frame_count += 1
            print('\n\n>>>> ---------------------------------------------------------------- <<<<\t', self.frame_count)
            ret, frame = cap.read()
            if not ret:
                break

            if self.frame_count % self.skip == 0:
                description = llava.get_llava_description(frame)
                print('\n\ndescription: ', description)

                alert_msg = llama.generate_alert(description)
                print('\nalert: ', alert_msg)

                try:
                    
                    # this code return if the frames has no alert worthy events else it saves the event in the database
                    if "no alert triggered" in alert_msg.lower() :
                        continue

                    frame_path = os.path.join(self.frame_save_path, f"frame_{self.frame_count}.jpg")

                    cv2.imwrite(frame_path, frame)

                    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    print('frame_path: ', frame_path)
                    frame_id = int(frame_path.split("/")[-1].split('_')[1].split(".")[0])
                    print('frame_id: ', frame_id)

                    db.save_alert(frame_id, timestamp, description, alert_msg)
                except Exception as e:
                    pass