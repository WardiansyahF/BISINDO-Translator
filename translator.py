import streamlit as st
import time
import joblib
import pandas as pd
import mediapipe as mp
import numpy as np
import cv2

# Setup MediaPipe and load the model
mp_drawing = mp.solutions.drawing_utils
mp_holistic = mp.solutions.holistic
word = ""
sentence = ""
last_sentence = ""
last_word_time = time.time()

# Load the pre-trained Random Forest model
RFC = joblib.load("hand_gesture_model.sav")


# Sidebar title and page selection
st.sidebar.title("Menu Aplikasi")
st.sidebar.write(
    "Silahkan anda pilih laman yang ingin anda kunjungi melalui dropdown dibawah ini.")
page = st.sidebar.selectbox("Pilih Laman:",
                            ["Beranda", "Apa itu BISINDO?", "Belajar BISINDO", "Penerjemah Bahasa Isyarat", "Kritik dan Saran", "Tentang Pembuat"])

# Sidebar description based on selected page
with st.sidebar.expander("Deskripsi Laman"):
    if page == "Beranda":
        st.write(
            "Halaman utama aplikasi. Di sini Anda akan menemukan informasi umum dan fitur utama aplikasi.")
    elif page == "Apa itu BISINDO?":
        st.write("Penjelasan mengenai BISINDO, yaitu Bahasa Isyarat Indonesia. Halaman ini memberikan informasi tentang sejarah, penggunaan, dan pentingnya BISINDO.")
    elif page == "Belajar BISINDO":
        st.write("Sumber belajar BISINDO termasuk abjad, angka, kata, dan kamus BISINDO. Ada juga video demonstrasi untuk membantu Anda mempelajari BISINDO.")
    elif page == "Penerjemah Bahasa Isyarat":
        st.write("Fitur untuk menerjemahkan bahasa isyarat BISINDO ke teks. Di sini Anda dapat mencoba dan menggunakan aplikasi untuk penerjemahan.")
    elif page == "Kritik dan Saran":
        st.write("Halaman untuk memberikan kritik dan saran mengenai aplikasi. Kami sangat menghargai umpan balik Anda untuk perbaikan aplikasi.")
    elif page == "Tentang Pembuat":
        st.write("Informasi tentang pembuat aplikasi. Anda dapat melihat foto pembuat dan latar belakang mereka di halaman ini.")


if page == "Beranda":
    st.title("Selamat Datang di Aplikasi Penerjemah Bahasa Isyarat")
    st.write("""
    Aplikasi ini dirancang untuk mempermudah Anda dalam mempelajari dan menggunakan Bahasa Isyarat Indonesia (BISINDO). 
    Dengan berbagai fitur yang ada, Anda dapat belajar tentang BISINDO, menggunakan penerjemah bahasa isyarat secara real-time, 
    dan memberikan kritik serta saran untuk pengembangan aplikasi ini.
    """)
    st.write(
        "Pilih halaman dari menu navigasi di sisi kiri untuk mulai menjelajahi aplikasi.")
    st.write("---")

    st.subheader("Fitur Utama")
    st.write("""
    - **Apa itu BISINDO?**: Temukan informasi mendalam tentang Bahasa Isyarat Indonesia, sejarah, dan manfaat mempelajarinya.
    - **Belajar BISINDO**: Akses berbagai materi pembelajaran BISINDO termasuk abjad, angka, kata-kata, kamus, dan demonstrasi.
    - **Penerjemah Bahasa Isyarat**: Gunakan kamera Anda untuk menerjemahkan isyarat tangan dalam BISINDO secara real-time.
    - **Kritik dan Saran**: Berikan masukan dan saran untuk meningkatkan aplikasi.
    - **Tentang Pembuat**: Kenali pembuat aplikasi dan cara menghubungi mereka.
    """)

    st.subheader("Dokumentasi Program")
    st.write("""
    Untuk memahami lebih dalam bagaimana aplikasi ini bekerja, tonton video dokumentasi berikut yang menjelaskan fungsi dan penggunaan aplikasi:
    """)
    st.video(
        "https://youtu.be/mukNGgweHSI")  # Update this link to the actual video URL
    st.write("Tonton video tutorial dan dokumentasi untuk informasi lebih lanjut.")


elif page == "Apa itu BISINDO?":
    st.title("Apa itu BISINDO?")

    # Pengenalan BISINDO
    st.header("Pengenalan BISINDO")
    st.write("""
    Bahasa Isyarat Indonesia (BISINDO) adalah bahasa isyarat yang digunakan oleh komunitas Tuli di Indonesia.
    Seperti bahasa isyarat lainnya di dunia, BISINDO memiliki struktur dan tata bahasa yang berbeda dari bahasa lisan.
    BISINDO berkembang secara alami di dalam komunitas Tuli dan mencerminkan budaya dan identitas mereka.
    """)

    # Sejarah BISINDO
    st.header("Sejarah BISINDO")
    st.write("""
    BISINDO mulai berkembang pada pertengahan abad ke-20 dan kini menjadi bahasa isyarat yang diakui dan digunakan 
    oleh banyak orang Tuli di seluruh Indonesia. Meskipun tidak sepopuler bahasa isyarat internasional seperti ASL 
    (American Sign Language), BISINDO memiliki keunikan dan kekayaan tersendiri yang penting untuk dilestarikan dan dipelajari.
    """)

    # Mengapa Mempelajari BISINDO
    st.header("Mengapa Mempelajari BISINDO?")
    st.write("""
    Mempelajari BISINDO memiliki banyak manfaat, di antaranya:
    - **Meningkatkan Komunikasi:** Memfasilitasi komunikasi dengan teman, keluarga, dan rekan kerja yang Tuli.
    - **Mendukung Inklusi:** Meningkatkan kesadaran dan inklusi sosial bagi komunitas Tuli.
    - **Memperkaya Keterampilan:** Menambah keterampilan baru yang unik dan bermanfaat dalam berbagai situasi.
    """)

    # Abjad BISINDO
    st.header("Abjad BISINDO")
    st.image("abjad.png", caption="Abjad BISINDO", use_column_width=True)
    st.write("""
    Abjad BISINDO merupakan salah satu dasar penting dalam mempelajari bahasa isyarat ini. Dengan mengenal 
    abjad BISINDO, Anda dapat mulai mengeja kata dan memahami struktur dasar bahasa isyarat.
    """)

    # Kamus BISINDO
    st.header("Kamus BISINDO")
    st.write("""
    Untuk memperdalam pengetahuan Anda tentang BISINDO, Anda dapat mengunduh kamus BISINDO berikut:
    - [Unduh Kamus BISINDO (PDF)](https://drive.google.com/file/d/1cIX6gmmtXeG_0O5CEC4tCGh7HEpNYMyr/view?usp=sharing)
    """)

    # Video Tutorial BISINDO
    st.header("Video Tutorial BISINDO")
    st.write("""
    Pelajari lebih lanjut tentang BISINDO melalui video-video tutorial berikut:
    - [Video 1](https://youtube.com/playlist?list=PLfsmXCUc8kvHMpSJI4aYLID1qVIAh1GCZ&si=UdrRoI0BytS5bdNn)
    - [Video 2](https://youtu.be/mukNGgweHSI?si=zEMlc5W_KGtfePA1)
    """)


elif page == "Penerjemah Bahasa Isyarat":
    st.header("Penerjemah Bahasa Isyarat")

    st.write("""
    Laman ini memungkinkan Anda untuk menggunakan kamera Anda untuk menerjemahkan isyarat tangan dalam Bahasa Isyarat Indonesia (BISINDO) secara real-time. Aplikasi ini menggunakan model pembelajaran mesin untuk mengidentifikasi dan menerjemahkan isyarat tangan yang Anda tampilkan di depan kamera ke dalam teks. 
    """)

    st.write("""
    **Tata Cara Penggunaan Penerjemah:**
    
    1. **Pilih Kamera:** Gunakan dropdown untuk memilih kamera yang ingin Anda gunakan. Pastikan kamera sudah terhubung dan aktif.
    
    2. **Aktifkan Kamera:** Klik tombol "Aktifkan Kamera" untuk memulai proses penerjemahan. Kamera akan mulai merekam dan menampilkan video langsung di aplikasi.
    
    3. **Peragakan Isyarat:** Tunjukkan isyarat tangan yang ingin Anda terjemahkan di depan kamera. Aplikasi akan mendeteksi isyarat dan menampilkannya dalam bentuk teks.
    
    4. **Lihat Hasil Terjemahan:** Teks hasil terjemahan akan ditampilkan secara real-time di layar. Kata-kata yang terdeteksi akan muncul di bawah "Kata Saat Ini", dan kalimat yang terbentuk akan muncul di bawah "Kalimat Saat Ini".
    
    5. **Nonaktifkan Kamera:** Setelah selesai, klik tombol "Nonaktifkan Kamera" untuk berhenti merekam. Kamera akan berhenti dan aplikasi akan kembali ke tampilan awal.
    
    6. **Periksa Kalimat Sebelumnya:** Kalimat terakhir yang diterjemahkan akan ditampilkan di bawah "Kalimat Sebelumnya" setelah Anda menyelesaikan isyarat baru.
    """)

    # Dropdown untuk memilih kamera
    camera_options = ["Camera 1", "Camera 2", "Camera 3"]
    camera_selection = st.selectbox("Pilih Kamera", options=camera_options)
    camera_index = camera_options.index(camera_selection)

    frame_placeholder = st.empty()
    text_previous_sentence = st.empty()
    text_current_sentence = st.empty()
    text_word = st.empty()

    # Tombol untuk mengaktifkan dan menonaktifkan kamera
    start_camera = st.button("Aktifkan Kamera")
    stop_camera = st.button("Nonaktifkan Kamera")

    if start_camera:
        cap = cv2.VideoCapture(camera_index)
        if not cap.isOpened():
            st.error(
                "Tidak dapat mengakses kamera. Pastikan kamera terhubung dan pilih yang benar.")
        else:
            with mp_holistic.Holistic(min_detection_confidence=0.3, min_tracking_confidence=0.3) as holistic:
                while cap.isOpened() and not stop_camera:
                    curr_word_time = time.time()

                    # Read camera input
                    ret, frame = cap.read()
                    if not ret:
                        st.error("Tidak dapat membaca input kamera.")
                        break

                    # Convert BGR to RGB
                    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

                    # Flip horizontally for a mirror effect
                    image = cv2.flip(image, 1)

                    # Mark the image as not writeable to pass by reference
                    image.flags.writeable = False

                    # Process the image and find hand landmarks
                    results = holistic.process(image)

                    # Mark the image as writeable for drawing
                    image.flags.writeable = True

                    # Draw hand landmarks
                    if results.left_hand_landmarks:
                        mp_drawing.draw_landmarks(
                            image, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS)
                    if results.right_hand_landmarks:
                        mp_drawing.draw_landmarks(
                            image, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS)

                    # Check if it has been at least 2 seconds
                    if curr_word_time - last_word_time >= 2.0:
                        if results.right_hand_landmarks or results.left_hand_landmarks:
                            # Get landmark coordinates
                            lh = list(np.array([[res.x, res.y, res.z] for res in results.left_hand_landmarks.landmark]).flatten()
                                      if results.left_hand_landmarks else np.zeros(21 * 3))
                            rh = list(np.array([[res.x, res.y, res.z] for res in results.right_hand_landmarks.landmark]).flatten()
                                      if results.right_hand_landmarks else np.zeros(21 * 3))

                            # Combine the landmarks into a single row
                            row = lh + rh

                            # Predict the gesture
                            try:
                                X = pd.DataFrame([row])
                                hand_class = RFC.predict(X)[0]
                                word = word + hand_class
                                text_word.subheader(f"Kata Saat Ini: {word}")
                                last_word_time = curr_word_time
                            except Exception as e:
                                st.error(f"Kesalahan Prediksi: {e}")
                        else:
                            if word:
                                sentence = sentence + " " + word
                                text_current_sentence.subheader(
                                    f"Kalimat Saat Ini: {sentence.strip()}")
                                word = ""
                                text_word.subheader(f"Kata Saat Ini: {word}")
                                last_word_time = curr_word_time
                            else:
                                last_sentence = sentence.strip()
                                text_previous_sentence.subheader(
                                    f"Kalimat Sebelumnya: {last_sentence}")
                                sentence = ""
                                text_current_sentence.subheader(
                                    f"Kalimat Saat Ini: {sentence}")
                                last_word_time = curr_word_time

                    # Display the processed image in the Streamlit app
                    frame_placeholder.image(image, channels="RGB")

                cap.release()
                cv2.destroyAllWindows()
                st.write("---")


elif page == "Belajar BISINDO":
    st.header("Belajar BISINDO")

    st.write("""
    Halaman ini dirancang untuk membantu Anda mempelajari Bahasa Isyarat Indonesia (BISINDO) secara mendalam. 
    Di sini, Anda dapat menemukan berbagai informasi penting tentang BISINDO, termasuk abjad, angka, kata-kata umum, kamus, dan demonstrasi penggunaan. 
    Setiap tab menyediakan materi yang berbeda untuk membantu Anda memahami dan menggunakan BISINDO dengan lebih baik.
    """)

    tab1, tab2, tab3, tab4, tab5 = st.tabs(
        ["Abjad dalam BISINDO", "Angka dalam BISINDO", "Kata dalam BISINDO", "Kamus BISINDO", "Demonstrasi BISINDO"])

    with tab1:
        st.subheader("Abjad dalam BISINDO")
        st.write("""
        **Abjad dalam BISINDO** adalah sistem dasar yang memungkinkan Anda untuk mengeja kata-kata dalam Bahasa Isyarat Indonesia (BISINDO). 
        Setiap huruf abjad diwakili oleh bentuk tangan tertentu yang memudahkan pengguna BISINDO untuk menyusun dan memahami kata-kata.
        """)

        st.write("""
        Abjad BISINDO terdiri dari 26 huruf, mirip dengan abjad Latin, namun dengan gerakan tangan yang spesifik. 
        Ini termasuk huruf vokal (A, E, I, O, U) dan huruf konsonan. Setiap huruf memiliki gerakan yang unik yang dapat dibedakan satu sama lain.
        """)

        st.write("""
        **Contoh Gerakan Abjad:**
        - **A:** Tangan dibentuk seperti kepalan tangan dengan ibu jari menunjuk ke atas.
        - **B:** Tangan dibentuk dengan jari-jari rapat dan telapak tangan menghadap ke depan.
        - **C:** Tangan dibentuk seperti huruf C dengan jari-jari melengkung.
        - **D:** Tangan dibentuk dengan ibu jari dan jari telunjuk membentuk huruf D, jari-jari lainnya ditekuk.
        - **E:** Tangan dibentuk dengan jari-jari sedikit menggulung dan telapak tangan menghadap ke depan.
        """)

        st.image("abjad.png", caption="Abjad BISINDO", use_column_width=True)

        st.write("""
        Menguasai abjad BISINDO adalah langkah awal yang penting dalam mempelajari bahasa isyarat ini. 
        Dengan memahami gerakan setiap huruf, Anda dapat mengeja kata-kata dan menyusun kalimat dalam BISINDO.
        """)

    with tab2:
        st.subheader("Angka dalam BISINDO")
        st.write("""
        **Angka dalam BISINDO** adalah sistem yang memungkinkan Anda untuk menunjukkan angka-angka dari 0 hingga 9 menggunakan isyarat tangan. 
        Angka dalam BISINDO membantu dalam komunikasi numerik sehari-hari seperti menghitung, menyebutkan usia, dan memberikan informasi kuantitatif.
        """)

        st.write("""
        **Contoh Gerakan Angka:**
        - **0:** Tangan dibentuk seperti huruf O dengan jari-jari rapat.
        - **1:** Tangan dibentuk dengan jari telunjuk menunjuk ke atas, jari-jari lainnya ditekuk.
        - **2:** Tangan dibentuk dengan jari telunjuk dan jari tengah menunjuk ke atas, jari-jari lainnya ditekuk.
        - **3:** Tangan dibentuk dengan jari telunjuk, jari tengah, dan jari manis menunjuk ke atas, jari kelingking ditekuk.
        - **4:** Tangan dibentuk dengan jari telunjuk, jari tengah, jari manis, dan jari kelingking menunjuk ke atas, ibu jari ditekuk.
        - **5:** Tangan dibentuk dengan semua jari-jari terbuka ke atas.
        """)

        st.image("angka.png", caption="Angka BISINDO", use_column_width=True)

        st.write("""
        Menguasai angka dalam BISINDO memudahkan Anda dalam berbagai situasi komunikasi yang melibatkan angka. 
        Ini penting untuk interaksi yang melibatkan data numerik, seperti dalam diskusi matematika atau saat memberikan informasi angka.
        """)

    with tab3:
        st.subheader("Kata dalam BISINDO")
        st.write("""
        **Kata dalam BISINDO** merupakan komponen penting dalam berkomunikasi menggunakan Bahasa Isyarat Indonesia (BISINDO). 
        Setiap kata dalam BISINDO terdiri dari kombinasi isyarat tangan yang membentuk makna tertentu. 
        Proses pembentukan kata ini melibatkan penggabungan abjad dan isyarat khusus yang mewakili kata-kata umum dalam bahasa isyarat.
        """)

        st.write("""
        **Contoh Kata-kata Umum:**
        - **Halo:** Tangan diletakkan di sisi kepala dengan jari telunjuk sedikit terangkat, kemudian digerakkan ke depan.
        - **Terima Kasih:** Tangan dibuka dengan jari-jari rapat dan telapak tangan menghadap ke arah diri sendiri, kemudian digerakkan ke arah orang lain.
        - **Tolong:** Tangan dibentuk seperti kepalan tangan dengan ibu jari berada di bawah dagu, kemudian digerakkan ke arah depan.
        - **Ya:** Tangan diletakkan di depan wajah dengan jari-jari terbuka, kemudian digerakkan sedikit ke atas.
        - **Tidak:** Tangan dibentuk seperti kepalan tangan dengan jari-jari rapat, kemudian digerakkan ke samping.
        """)

        st.image("kata.png", caption="Kata BISINDO", use_column_width=True)

        st.write("""
        Memahami dan menggunakan kata-kata umum dalam BISINDO sangat penting untuk berkomunikasi secara efektif. 
        Ini membantu Anda dalam situasi sehari-hari, seperti menyapa seseorang, meminta bantuan, atau menyatakan kebutuhan.
        """)

        st.write("""
        **Latihan:**
        Untuk memperdalam pemahaman Anda tentang kata-kata dalam BISINDO, cobalah latihan berikut:
        - Praktikkan gerakan tangan untuk setiap kata dengan menggunakan panduan gambar atau video.
        - Berlatihlah dengan teman atau keluarga untuk meningkatkan kefasihan.
        - Ikuti kursus online atau tutorial BISINDO untuk mempelajari lebih banyak kosakata dan frasa.
        """)

    with tab4:
        st.subheader("Kamus BISINDO")
        st.write("""
        **Kamus BISINDO** adalah sumber daya penting yang menyediakan daftar istilah dan kata-kata dalam Bahasa Isyarat Indonesia (BISINDO). 
        Kamus ini membantu Anda memahami dan menggunakan berbagai isyarat dalam BISINDO secara efektif. 
        Dengan memiliki kamus ini, Anda dapat memperluas kosakata Anda dan meningkatkan kemampuan berkomunikasi dengan komunitas Tuli di Indonesia.
        """)

        st.write("Unduh kamus BISINDO dan informasi tambahan dari link berikut:")
        st.write(
            "[Unduh Kamus BISINDO (PDF)](https://drive.google.com/file/d/1cIX6gmmtXeG_0O5CEC4tCGh7HEpNYMyr/view?usp=sharing)")

    with tab5:
        st.subheader("Demonstrasi BISINDO")
        st.write("Berikut adalah video tutorial untuk menggunakan BISINDO:")
        st.video("https://youtu.be/mukNGgweHSI")  # Video tutorial

        st.write("""
        Untuk mempelajari lebih lanjut dan melihat lebih banyak contoh penggunaan BISINDO, 
        kunjungi playlist YouTube berikut ini:
        """)
        st.write(
            "[Playlist Belajar BISINDO](https://youtube.com/playlist?list=PLfsmXCUc8kvHMpSJI4aYLID1qVIAh1GCZ)")


elif page == "Kritik dan Saran":
    st.header("Kritik dan Saran")
    st.write("Kami menghargai masukan Anda untuk peningkatan aplikasi ini.")

    # Formulir Umpan Balik
    with st.form(key='feedback_form'):
        st.subheader("Berikan Masukan Anda")

        feedback_type = st.selectbox(
            "Jenis Masukan",
            ["Saran Fitur", "Laporan Bug", "Umpan Balik Umum"]
        )

        feedback_text = st.text_area(
            "Masukkan Kritik dan Saran Anda di sini", height=150)

        submit_button = st.form_submit_button("Kirim")

        if submit_button:
            if feedback_text:
                st.success("Terima kasih atas masukan Anda!")
                # Kirim umpan balik ke backend atau simpan di file/database
            else:
                st.error("Silahkan masukkan kritik dan saran terlebih dahulu.")


elif page == "Tentang Pembuat":
    st.header("Tentang Pembuat")

    # Menampilkan foto pembuat dengan ukuran lebih kecil di tengah halaman
    st.markdown("""
    <div style="text-align: center;">
        <img src="https://media.licdn.com/dms/image/D5603AQHAAnWzc38Pow/profile-displayphoto-shrink_800_800/0/1698143495181?e=1727308800&v=beta&t=V4syJWv1EEaoAOqofZ6VHxQkGUWhqP4CgfJyJ5UNUqM" 
        alt="Wardiansyah Fauzi Abdillah" 
        style="width: 300px;">
        <p><em>Wardiansyah Fauzi Abdillah</em></p>
    </div>
    """, unsafe_allow_html=True)

    st.write("""
    **Nama Pembuat:** 
    
    Wardiansyah Fauzi Abdillah

    **Tentang Pembuat:**
    
    Wardiansyah Fauzi Abdillah adalah seorang pengembang perangkat lunak dan peneliti yang memiliki minat mendalam dalam teknologi bahasa isyarat dan pemrosesan citra. Dengan latar belakang dalam Informatika dan pengalaman dalam machine learning, beliau berkomitmen untuk menciptakan solusi yang meningkatkan komunikasi antara komunitas Tuli dan non-Tuli.
    """)

    st.header("Informasi Kontak")
    st.write("""
    - **Email:** [ardi.dl738@gmail.com](mailto:ardi.dl738@gmail.com)
    - **Telepon:** +62 812 1385 3153
    - **LinkedIn:** [Wardiansyah Fauzi Abdillah](https://www.linkedin.com/in/wardiansyah-fauzi-abdillah)
    - **GitHub:** [WardiansyahF](https://github.com/WardiansyahF)
    """)
