# Dashboard Stroke Prediction
Nama: Dinar Wahyu Rahman


| | Deskripsi |
| ----------- | ----------- |
| Dataset | [Stroke Prediction Dataset](https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset) |
| Masalah | Menurut Organisasi Kesehatan Dunia (WHO), stroke merupakan penyebab kematian terbanyak ke-2 di dunia, yang menyebabkan sekitar 11% dari total kematian. |
| Solusi machine learning | Solusi yang diusulkan adalah membangun model klasifikasi berbasis machine learning untuk memprediksi apakah seorang pasien memiliki risiko tinggi terkena stroke (1) atau tidak (0). Hal ini dilakukan dengan menganalisis atribut risiko seperti usia, riwayat hipertensi, kadar glukosa rata-rata, status merokok, dan jenis pekerjaan. Model ini dapat membantu para profesional medis untuk mengambil tindakan pencegahan lebih dini. |
| Metode pengolahan | * **Pra-pemrosesan data**: Melakukan imputasi nilai-nilai hilang (khususnya pada kolom `bmi`). <br> * Apply a resampling technique to thr training data tp fix the imbalance. <br> * SMOTE (Synthetic Minority Over-sampling Technique). This is a data processing technique used to overcome the problem of imbalanced data in classification, especially when the minority class (which rarely appears) is too small compared to the majority class. <br> * Menggunakan LabelEncoder() untuk mengubah data kategorikal menjadi angka urut (integer). Contoh: 'Male' jadi 0 dan 'Female' jadi 1. <br> * Pembagian dataset menjadi data latih (80%) dan data uji (20%) untuk mengevaluasi performa model. |
| Arsitektur model | Kami menggunakan beberapa model machine learning, diantaranya: <br> *  **Logistic Regression**  Model ini merupakan baseline untuk klasifikasi biner. Biasanya, Logistic Regression cukup baik untuk data yang linear dan mudah diinterpretasi. Namun, pada kasus data yang kompleks atau tidak linear, performanya bisa terbatas.  <br> * **Random Forest**  Model ini adalah ensemble dari banyak decision tree, sehingga lebih kuat dalam menangkap hubungan kompleks dan interaksi antar fitur. Random Forest juga cukup tahan terhadap overfitting dibanding single decision tree. <br> * **XGBoost (tanpa tuning)**  XGBoost adalah algoritma boosting yang sangat populer untuk kompetisi machine learning. Ia membangun model secara bertahap dan mengoreksi kesalahan model sebelumnya. <br> * **XGBoost (setelah tuning/hasil GridSearchCV)**  Setelah dilakukan hyperparameter tuning dengan GridSearchCV, performa XGBoost biasanya meningkat, terutama pada metrik recall untuk kelas minoritas (stroke). 
| Metrik evaluasi | * Accuracy: Untuk mengukur seberapa baik model memprediksi secara keseluruhan. <br> * Precision: Untuk memastikan model tidak terlalu sering salah memprediksi pasien berisiko stroke. <br> * Recall (Sensitivity): Untuk memastikan semua pasien yang berisiko tinggi terkena stroke dapat terdeteksi dengan benar. <br> * F1-Score: Kombinasi antara precision dan recall sebagai metrik akhir evaluasi. |
| Performa model | * Model XGBoost dengan tuning memberikan hasil terbaik, terutama dalam mendeteksi kasus stroke (kelas minoritas). * Random Forest juga memberikan performa yang baik dan stabil. <br> * Logistic Regression cocok sebagai baseline, namun kurang optimal untuk data kompleks. <br> * Pemilihan model akhir sebaiknya mempertimbangkan trade-off antara akurasi, recall, dan interpretasi, tergantung kebutuhan bisnis/medis. <br> Jika ingin fokus pada deteksi kasus stroke (mengurangi false negative), maka recall pada kelas 1 (stroke) menjadi metrik utama yang perlu diperhatikan.  |


Prototype Website: <a href="https://stroke-risk-prediction-web.up.railway.app/ " target="_blank">Link Demo</a>

Notebook: https://colab.research.google.com/drive/11zbHEcZnVXXD-Fqe_FPWvMxwJFWk4QIO?usp=sharing

![image](https://github.com/user-attachments/assets/cc42a7a5-0a7b-4f0d-9b81-9b20f4bf7a1b)
