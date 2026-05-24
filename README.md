# Car Damage Classification using Deep Learning

A deep learning-based image classification system for detecting and classifying car damage using Convolutional Neural Networks (CNNs) and transfer learning techniques such as ResNet and EfficientNet.

The project explores multiple deep learning approaches, compares their performance, and deploys the final trained model using Streamlit and FastAPI.

---

## Project Overview

This project focuses on classifying different types of car damage from images. Multiple deep learning architectures were implemented and evaluated, including:

- Custom CNN architectures
- CNN with regularization
- Transfer learning using pretrained ImageNet models
- Hyperparameter tuning using Optuna

The final model was deployed using:

- Streamlit (Frontend)
- FastAPI (Backend API)

---

## Features

- Image preprocessing and augmentation
- Custom CNN implementation using PyTorch
- Transfer learning with pretrained models
- Hyperparameter tuning using Optuna
- Model evaluation using confusion matrix and classification metrics
- Streamlit web application for real-time predictions
- FastAPI backend for serving predictions

---

## Tech Stack

### Deep Learning & ML
- PyTorch
- Torchvision
- Optuna
- Scikit-learn

### Deployment
- Streamlit
- FastAPI

### Visualization
- Matplotlib
- Seaborn

---

## Dataset

The dataset contains images of damaged and non-damaged cars. Since the dataset size was limited, data augmentation techniques were applied to improve model generalization.

### Data Augmentation Techniques
- Horizontal flipping
- Rotation
- Zooming
- Brightness adjustments

### Image Preprocessing
- Resize to `224 × 224`
- Tensor conversion
- ImageNet normalization

---

## Models Implemented

| Model | Description |
|---|---|
| Baseline CNN | Basic convolutional neural network |
| CNN + Regularization | Added dropout and regularization techniques |
| EfficientNet | Transfer learning using pretrained EfficientNet |
| ResNet | Transfer learning using pretrained ResNet |
| Optuna Tuned ResNet | Hyperparameter tuned ResNet model |

---

## Training & Evaluation

The models were evaluated using:

- Training Loss
- Validation Loss
- Validation Accuracy
- Confusion Matrix
- Classification Report

Transfer learning models significantly outperformed custom CNN architectures due to the limited dataset size.

---

## Project Structure

```text
Car-Damage-Classification/
│
├── notebooks/
│   └── Car_Damage_Prediction.ipynb
│
├── Streamlit App/
│   ├── app.py
│   ├── model_helper.py
│   └── Model/
│       └── saved_model.pth
│
├── FastAPI Server/
│   └── server.py
│
├── requirements.txt
└── README.md
```

---

## Streamlit Application

The Streamlit application allows users to:

- Upload car images
- Run real-time damage classification
- View prediction results instantly

Run the Streamlit app:

```bash
python -m streamlit run app.py
```

---

## FastAPI Backend

The FastAPI server exposes a prediction endpoint for model inference.

Run the FastAPI server:

```bash
fastapi dev server.py
```

### API Endpoint

```http
POST /predict
```

---

## Results

- Transfer learning achieved significantly better performance compared to baseline CNN models.
- ResNet with hyperparameter tuning produced the best validation accuracy.
- Data augmentation improved generalization and reduced overfitting.

---

## Future Improvements

- Train on a larger and more diverse dataset
- Experiment with Vision Transformers (ViTs)
- Apply advanced augmentation strategies
- Deploy the application on cloud platforms
- Extend the project to damage localization/object detection

---

## Conclusion

This project demonstrates the complete deep learning workflow for image classification:

- Data preprocessing
- CNN modeling
- Transfer learning
- Hyperparameter tuning
- Model evaluation
- API development
- Frontend deployment

The final system integrates PyTorch, FastAPI, and Streamlit to provide an end-to-end car damage classification solution.

---

## Author

Elza