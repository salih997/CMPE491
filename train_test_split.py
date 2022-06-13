import os
import shutil
import sys
from sklearn.model_selection import train_test_split

def main():
    
    base_dir = os.getcwd()
    dataset_dir = os.path.join(base_dir, 'yoga_dataset_deleted')
    train_dir = os.path.join(base_dir, 'yoga_train')
    test_dir = os.path.join(base_dir, 'yoga_test')
    
    try:
        os.mkdir(train_dir)
    except OSError as error:
        print(error)

    try:
        os.mkdir(test_dir)
    except OSError as error:
        print(error)

    data_points = []
    labels = []
    for pose in os.listdir(dataset_dir):
        if not(os.path.isdir(os.path.join(dataset_dir, pose))):
            continue
        try:
            os.mkdir(os.path.join(train_dir, pose))
        except OSError as error:
            print(error)
        try:
            os.mkdir(os.path.join(test_dir, pose))
        except OSError as error:
            print(error)
        for img in os.listdir(os.path.join(dataset_dir, pose)):
            if not(img.endswith(".jpg")):
                continue
            data_points.append(img)
            labels.append(pose)

    X_train, X_test, y_train, y_test = train_test_split(data_points, labels, test_size=0.2, random_state=19)

    for ind, img_train in enumerate(X_train):
        src_path = os.path.join(dataset_dir, y_train[ind], img_train)
        dest_path = os.path.join(train_dir, y_train[ind])
        if os.path.exists(src_path):
            shutil.copy(src_path, dest_path)
            print(y_train[ind], img_train, 'is added to training set.')

    for ind, img_test in enumerate(X_test):
        src_path = os.path.join(dataset_dir, y_test[ind], img_test)
        dest_path = os.path.join(test_dir, y_test[ind])
        if os.path.exists(src_path):
            shutil.copy(src_path, dest_path)
            print(y_test[ind], img_test, 'is added to test set.')

if __name__ == '__main__':
    main()