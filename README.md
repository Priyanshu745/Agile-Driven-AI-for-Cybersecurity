# **Agile-Driven AI for Cybersecurity: Enhancing Threat Detection and Adaptive Response**  

## **Overview**  
This project focuses on leveraging **Agile-driven AI and machine learning models** to enhance **cybersecurity threat detection and adaptive response**. By integrating **machine learning, deep learning, and reinforcement learning**, the system continuously evolves to counter sophisticated cyber threats in real time.  

## **Implemented AI Models**  
The following AI models are included in this project:  
 
- **Convolutional Neural Network (CNN)** (`CNN.ipynb`) – Pattern recognition in cybersecurity data.  
- **Decision Tree** (`Decision_Tree.ipynb`) – Rule-based classification for attack detection.  
- **K-Means Clustering** (`Kmean.ipynb`) – Unsupervised clustering for anomaly detection.  
- **Long Short-Term Memory (LSTM)** (`LSTM.ipynb`) – Sequence-based detection of cyber threats.  
- **Random Forest** (`Random_forest.ipynb`) – Ensemble learning for robust classification.  
- **Support Vector Machine (SVM)** (`svm.ipynb`) – High-dimensional data classification for security threats.  

## **Cybersecurity Datasets**  
The project utilizes multiple cybersecurity datasets for training and evaluation. Due to size limitations, the full datasets are hosted on **Google Drive**:  

[🔗 Click here to access the full datasets](https://drive.google.com/drive/folders/1GU6Vr6cdjz9_UUT3U6Nm1IL_JfthiT3E?usp=sharing)  

## **Setting Up the Project in Google Colab**  

### **Step 1: Upload Datasets to Google Drive**  
1. Open your [Google Drive](https://drive.google.com/).  
2. Create a folder named **"Cybersecurity_Datasets"**.  
3. Upload all dataset files into this folder.  

### **Step 2: Mount Google Drive in Google Colab**  
1. Open [Google Colab](https://colab.research.google.com/).  
2. Mount Google Drive using the following code snippet:  

   ```python
   from google.colab import drive
   drive.mount('/content/drive')
