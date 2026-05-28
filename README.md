# 🚗 Car Damage Classification using Deep Learning

A deep learning-based image classification system for detecting and classifying car damage using CNNs and transfer learning models such as ResNet and EfficientNet.

The project explores multiple deep learning approaches, compares their performance, and deploys the final trained model using Streamlit. The project also includes an experimental FastAPI backend integration architecture for scalable model inference and deployment testing using Render.

---

## 🌐 Live Demo

🔗 Streamlit App: https://dl-car-damage-detection2.streamlit.app/

---

## 📌 Features

- Image preprocessing and augmentation
- Custom CNN implementation using PyTorch
- Transfer learning with ResNet and EfficientNet
- Hyperparameter tuning using Optuna
- Model evaluation using confusion matrix and classification report
- Streamlit frontend for real-time predictions
- Experimental FastAPI backend integration for scalable inference
- Backend deployment testing using Render

---

## 🛠️ Tech Stack

### Deep Learning & ML
- PyTorch
- Torchvision
- Optuna
- Scikit-learn

### Deployment
- Streamlit (standalone frontend deployment)
- FastAPI (experimental backend API integration)
- Render (backend deployment testing)

### Visualization
- Matplotlib
- Seaborn

---

## 📂 Dataset

The dataset contains images of damaged and non-damaged cars. Since the dataset size was limited, data augmentation techniques were applied to improve model generalization.

### Data Augmentation
- Horizontal flipping
- Rotation
- Zooming
- Brightness adjustments

### Image Preprocessing
- Resize to `224 × 224`
- Tensor conversion
- ImageNet normalization

---

## 🤖 Models Implemented

| Model | Description |
|---|---|
| Baseline CNN | Basic convolutional neural network |
| CNN + Regularization | Added dropout and regularization |
| EfficientNet | Transfer learning using pretrained EfficientNet |
| ResNet | Transfer learning using pretrained ResNet |
| Optuna Tuned ResNet | Hyperparameter tuned ResNet model |

---

## 📊 Results

- Transfer learning significantly outperformed baseline CNN models.
- ResNet with hyperparameter tuning achieved the best validation accuracy.
- Data augmentation improved model generalization and reduced overfitting.

---

## 🚀 Future Improvements

- Train on a larger and more diverse dataset
- Experiment with Vision Transformers (ViTs)
- Apply advanced augmentation techniques
- Extend the project to damage localization/object detection
- Deploy on cloud platforms

---

## ✅ Conclusion

This project demonstrates an end-to-end deep learning workflow including:

- Data preprocessing
- CNN modeling
- Transfer learning
- Hyperparameter tuning
- Model evaluation
- API integration
- Frontend deployment

The final system integrates PyTorch and Streamlit to provide real-time car damage classification. The project also explores a separate FastAPI backend architecture and Render deployment workflow for scalable inference serving.

---

## 👤 Author

Elza