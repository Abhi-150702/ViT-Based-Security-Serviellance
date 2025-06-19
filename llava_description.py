import base64
import requests
import json
import cv2

class LLAVA:
    """
    Uses LLaVA model by Ollama to generate image descriptions from frames.
    """

    def __init__(self):
        self.model_name = 'llava'
        self.prompt = "Describe what is happening in this image."
        self.rules = {
            "loitering": ["person loitering", "standing"],
            "vehicle": ["car", "truck", "ship", "vehicle", "cruise", "bike"],
            "arson": ["arson", "fire", "explorsion", "flames", "smoke", "burining"]
        }
        
        
    def get_llava_description(self, frame):
        """
        Encodes frame and sends to LLaVA for description.
        """

        # encoding frame to send it to llava model via api
        success, encoded_img = cv2.imencode('.jpg', frame)
        if not success:
            raise ValueError("Failed to encode image frame")

        img_bytes = encoded_img.tobytes()
        img_base64 = base64.b64encode(img_bytes).decode("utf-8")

        payload = {
            "model": self.model_name,
            "prompt": self.prompt,
            "images": [img_base64]
        }
        
        # hits locally pulled ollama api
        response = requests.post("http://localhost:11434/api/generate", json=payload, stream=True)
        description = ""
        for chunk in response.iter_lines():
            if chunk:
                try:
                    data = json.loads(chunk.decode("utf-8"))
                    description += data.get("response", "")
                except:
                    continue
        return description.strip()
    
    