from PIL import Image
import torch
from torch import nn
from torchvision import models, transforms
import os

trained_model=None
class_names=["Front Breakage","Front Crushed","Front Normal","Rear Breakage","Rear Crushed","Rear Normal"]
MODEL_PATH = os.path.join(
    os.path.dirname(__file__),
    "..",
    "Model",
    "saved_model.pth"
)

#load the pretrained resnet model
class CarClassifierResNet(nn.Module):
    def __init__(self,num_classes=6):
        super().__init__()
        self.model=models.resnet50(weights="DEFAULT")

        #Freeze all layers except final fully connected layer
        for param in self.model.parameters():
            param.requires_grad=False

        #Unfreeze layer 4 and fc layer
        for param in self.model.layer4.parameters():
            param.requires_grad=True

        #Replace the final fully connected layer
        self.model.fc=nn.Sequential(
            nn.Dropout(0.5),
            nn.Linear(self.model.fc.in_features,num_classes)
        )

    def forward(self,x):
        x=self.model(x)
        return x


def predict(image_path):
    image=Image.open(image_path).convert("RGB")
    transform=transforms.Compose([
        transforms.Resize((224,224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485,0.456,0.406],std=[0.229,0.224,0.225])
    ])
    image_tensor=transform(image).unsqueeze(0) #(1,3,224,224) because our nn takes 32 images per batch

    global trained_model

    if not trained_model: #to avoid loading the model multiple times
        trained_model=CarClassifierResNet()
        trained_model.load_state_dict(torch.load(MODEL_PATH,map_location=torch.device('cpu')))  #Loading the saved model parameters to trained model variable
        trained_model.eval()

    with torch.no_grad():
        output=trained_model(image_tensor)
        _,predicted_class=torch.max(output,1)

    return class_names[predicted_class.item()]