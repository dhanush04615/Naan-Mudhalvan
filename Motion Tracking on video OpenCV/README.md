# Motion Tracking in Drone Videos using FAST and ORB

This project demonstrates motion tracking in drone videos using the FAST feature detector and ORB descriptor. 
The application is built with Streamlit and allows you to upload drone footage, process it, and download the resulting video with tracked motion.

## How to Run

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Run the Streamlit app:

```bash
streamlit run main.py
```

3. Upload a drone video (`.mp4`, `.avi`, `.mov`) and visualize motion tracking in real-time.

## Files

- `main.py` – Streamlit interface for uploading and displaying video.
- `tracking.py` – Contains the FAST + ORB motion tracking logic.
- `requirements.txt` – Python dependencies.
- `README.md` – Project documentation.