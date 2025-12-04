# 📘 Hair Type Classification – Homework 8 (ML Zoomcamp)

This project trains a small Convolutional Neural Network (CNN) from scratch using PyTorch to classify two hair types: **straight** and **curly**.  
The dataset is provided in the homework and contains separate folders for training and testing.

---

## 🎯 Homework Goals

- Load and prepare the image dataset  
- Build a simple CNN model  
- Train it for 10 epochs  
- Add data augmentation and train 10 more epochs  
- Compute accuracy and loss values for the homework quiz  

All steps were followed exactly as instructed.

---

## 🔧 Model Summary

The CNN architecture includes:

- 1 convolution layer (32 filters, 3×3)  
- ReLU activation  
- MaxPooling (2×2)  
- Flatten layer  
- Fully connected layer (64 units + ReLU)  
- Output layer (1 unit for binary classification)

**Loss Function:** `BCEWithLogitsLoss`  
**Optimizer:** `SGD(lr=0.002, momentum=0.8)`  

All images were resized to **200×200**, converted to tensors, and normalized.

---

## 🎛 Training Details

### **First 10 epochs (no augmentation)**  
Transformations:
- Resize  
- Tensor conversion  
- Normalization  

Metrics recorded:
- Training loss  
- Training accuracy  
- Validation loss  
- Validation accuracy  

---

### **Next 10 epochs (with augmentation)**  
Augmentations applied only to the training data:

- `RandomRotation(50)`
- `RandomResizedCrop(200)`
- `RandomHorizontalFlip()`

Validation set remained unchanged.

---

## Final Answers (Based on Notebook Output)

**Question 1:** Loss function  
→ **BCEWithLogitsLoss**

**Question 2:** Total parameters  
→ **20,073,473**

**Question 3:** Median training accuracy (first 10 epochs)  
→ **0.84**

**Question 4:** Standard deviation of training loss  
→ **0.171**

**Question 5:** Mean test loss after training with augmentation  
→ **0.88**

**Question 6:** Average test accuracy for the last 5 augmented epochs  
→ **0.68**

---

## 📎 Notebook Link

GitHub Notebook:  
https://github.com/sks01dev/ML-Zoomcamp/blob/main/Week%208/Hairstyle_Classification.ipynb

Homework Instructions (Main ML Zoomcamp Repo):  
https://github.com/DataTalksClub/machine-learning-zoomcamp/blob/master/cohorts/2025/08-deep-learning/homework.md

---

## 📌 Summary

This homework covered the full workflow of training a CNN from scratch:

- Dataset preparation  
- Model building  
- Training loops  
- Data augmentation  
- Recording accuracy and loss metrics  

All results were submitted successfully on the ML Zoomcamp platform.

