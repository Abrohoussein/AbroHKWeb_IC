FROM python:latest

COPY main.py ./main.py
COPY shape_predictor_68_face_landmarks.dat ./shape_predictor_68_face_landmarks.dat
COPY requirements.txt ./requirements.txt
COPY vieux.jpg /vieux.jpg
RUN apt-get update && apt-get install -y libgl1-mesa-glx
RUN pip install -r requirements.txt

CMD ["python", "/main.py"]
