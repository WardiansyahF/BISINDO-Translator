import cv2
import time
import joblib
import streamlit as st
import pandas as pd
import mediapipe as mp
import numpy as np

# Setup MediaPipe dan model
mp_drawing = mp.solutions.drawing_utils
mp_holistic = mp.solutions.holistic
word = ""
sentence = ""
last_word_time = time.time()
RFC = joblib.load("hand_gesture_model.sav")

# Streamlit layout
st.title("Yuk Ngobrol")
st.subheader("Penerjemah Bahasa Isyarat")
st.write("Silakan gunakan bahasa isyarat anda perhuruf")
st.text(" ")

# Display word and sentence
st.markdown("**Kata Terakhir:**")
text_word = st.empty()
st.markdown("**Kalimat:**")
text_sentence = st.empty()
st.text(" ")

# Capture video
cap = cv2.VideoCapture(0)
with mp_holistic.Holistic(min_detection_confidence=0.3, min_tracking_confidence=0.3) as holistic:
    while cap.isOpened():
        curr_word_time = time.time()

        # Read camera input
        ret, frame = cap.read()
        if not ret:
            break

        # BGR to RGB
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Flip on horizontal
        image = cv2.flip(image, 1)

        # Set flag
        image.flags.writeable = False

        # Detections
        results = holistic.process(image)

        # Set flag to true
        image.flags.writeable = True

        # Draw landmarks
        if results.left_hand_landmarks:
            mp_drawing.draw_landmarks(
                image, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS)
        if results.right_hand_landmarks:
            mp_drawing.draw_landmarks(
                image, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS)

        # It has been at least 2 seconds
        if curr_word_time - last_word_time >= 2.0 and (results.right_hand_landmarks or results.left_hand_landmarks):
            # Get landmark coordinates
            lh = list(np.array([[res.x, res.y, res.z] for res in results.left_hand_landmarks.landmark]).flatten()
                      if results.left_hand_landmarks else np.zeros(21 * 3))
            rh = list(np.array([[res.x, res.y, res.z] for res in results.right_hand_landmarks.landmark]).flatten()
                      if results.right_hand_landmarks else np.zeros(21 * 3))

            # Combine rows
            row = lh + rh

            # Predict
            try:
                X = pd.DataFrame([row])
                hand_class = RFC.predict(X)[0]
                word = word + hand_class
                text_word.write(word)
                last_word_time = curr_word_time
            except Exception as e:
                st.error(f"Prediction Error: {e}")

        elif curr_word_time - last_word_time >= 2.0 and not (results.right_hand_landmarks or results.left_hand_landmarks):
            if sentence.endswith(" "):
                sentence = ""
                text_sentence.write(sentence)
                word = ""
                text_word.write(word)
                last_word_time = curr_word_time
            else:
                sentence = sentence + " " + word
                text_sentence.write(sentence)
                word = ""
                text_word.write(word)
                last_word_time = curr_word_time

        st.image(image, channels="RGB")

    cap.release()
    cv2.destroyAllWindows()
    st.write("---")
