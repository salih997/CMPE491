# Boğaziçi University - CMPE 491 
Welcome to our github repository for Bogazici University's CMPE 491 Course.
You can check our [Wiki section](https://github.com/salih997/CMPE491/wiki) for more information!

## Team Members
[Salih Bedirhan Eker](https://github.com/salih997) and [Ece Dilara Aslan](https://github.com/eceasslan)

## Introduction
Our goal is that developing an deep learning aided yoga pose feedback application.
We use [MediaPipe Pose](https://google.github.io/mediapipe/solutions/pose.html) as our base approach and [Yoga-82](https://sites.google.com/view/yoga-82/home) as our dataset.

## Dataset
Yoga-82 dataset has a large size, it has 28450 samples. So we have given only the samples belong to *tree pose* as an example. Image dataset is created with `create_dataset.py` using original Yoga-82 dataset files which have urls of corresponding images and their labels. `yoga_dataset.txt` file consists of labels (poses).
