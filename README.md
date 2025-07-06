# ViT-Based-Security-Serviellance

A real‑time surveillance service that watches any video stream, detects critical security or safety events, and automatically writes human‑readable alerts.

*⚡️ Powered by LLaVA for image understanding and Llama 3 for natural‑language reasoning.*

---

## ✨ Key Features

| Capability                   | Details                                                                                                                        |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| **Multi‑event recognition**  | Detects *loitering, arson, fire, vehicle movement, night‑time activity*, and more by analysing each frame.                     |
| **Vision‑Language pipeline** | Uses **OpenCV** to grab frames → **LLaVA** to describe the scene → **Llama 3** to summarise the event.                         |
| **Natural‑language alerts**  | Generates one‑ or two‑line alerts that can be stored in any database, forwarded as notifications, or displayed on a dashboard. |
| **Pluggable camera source**  | Works with RTSP/HTTP cameras, local files, or any custom source via the `Camera` class.                                        |
| **Easy CLI**                 | Pass the stream with `--url` and you’re live.                                                                                  |

---

## 🖼️  System Workflow

1. **Frame Capture** – `Camera.read_stream()` yields frames in real‑time.
2. **Scene Description** – Each frame is sent to **LLaVA** with a prompt that lists the supported event types.
3. **Event Reasoning** – **Llama 3** decides which event is happening and crafts a concise alert sentence.
4. **Alert Storage** – The alert object (timestamp, type, description, extra metadata) is persisted.

---

## 🚀 Quick Start

### 1. Clone & Install

```bash
git clone https://github.com/Abhi-150702/ViT-Based-Security-Serviellance.git
cd <repo>
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Configure Environment

Create a `.env` file or export variables:

```bash
# Large‑Language Model endpoints
LLAVA_API= OLLAMA's llama3
LLAMA_API=http://<machine_ip_on_which_ollama_is_running>:11434/api/generate

# Database (example: MongoDB)
MONGO_URI=mongodb://localhost:27017
DB_NAME=alerts
```

### 3. Run

```bash
python main.py --url "rtsp://user:pass@192.168.1.25:554/stream1"
```

Use `-h` or `--help` to see all CLI flags.

---

## 📑 Alert Schema

The system stores every detection twice: as a **row in SQLite** for durability and as a **JSON document** for downstream services and dashboards.

### SQLite table

```sql
CREATE TABLE alerts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    frame_id INTEGER,
    timestamp TEXT,
    description TEXT,
    alert TEXT
);
```

### JSON representation

```json
{
  "timestamp": "2025‑07‑06T11:30:45Z",
  "frame_id": 123456,
  "description": "Person loitering near the south gate for over 60 seconds",
  "alert": "loitering"
}
```

You can extend either schema with optional fields such as `confidence`, `bbox`, `camera_id`, etc., if your application requires richer metadata.

---

## 🛠️  Project Structure

```
.
├── app/
│   ├── camera.py          # Camera wrapper around OpenCV
│   ├── vision.py          # LLaVA client
│   ├── language.py        # Llama client
│   └── db.py              # DB helper functions
├── main.py                # Entry point (CLI)
├── requirements.txt       # Python dependencies
└── README.md
```

---

## 🔧 Configuration Options

| Flag            | Env           | Default    | Meaning                              |
| --------------- | ------------- | ---------- | ------------------------------------ |
| `--url` / `-u`  | –             | *required* | Video source (RTSP, HTTP, file path) |
| `--fps`         | `FPS`         | 5          | Max frames per second to process     |
| `--save-frames` | `SAVE_FRAMES` | `false`    | Store raw frames for debugging       |
| `--log-level`   | `LOG_LEVEL`   | `INFO`     | Logging verbosity                    |

---

## 🗺️  Roadmap

-

---

## 🤝 Contributing

1. Fork the repo & create a new branch (`git checkout -b feature/my‑feature`).
2. Commit your changes (`git commit -m 'Add my feature'`).
3. Push to the branch (`git push origin feature/my‑feature`).
4. Open a Pull Request.

Please follow the [Conventional Commits](https://www.conventionalcommits.org) spec.

---

## 🪪 License

This project is released under the **MIT License**. See [`LICENSE`](LICENSE) for details.

---

## 🙏 Acknowledgements

- [LLaVA](https://llava-vl.github.io) – Large Language and Vision Assistant
- [Llama 3](https://ai.meta.com/llama/) – Meta’s open LLM family
- [OpenCV](https://opencv.org/) – Real‑time computer vision library

> Built with ♥ by Abhishek Kumbharde
