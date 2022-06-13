import os

def main():
    
    base_dir = os.getcwd()
    dataset_dir = os.path.join(base_dir, 'yoga_dataset_deleted2')
        
    pose_classes = os.listdir(dataset_dir)
    for pose_class in pose_classes:
        if not(os.path.isdir(os.path.join(dataset_dir, pose_class))):
            continue
        for ind, img in enumerate(os.listdir(os.path.join(dataset_dir, pose_class))):
            if not(img.endswith(".jpg")):
                continue
            num = f"{(ind+1):03d}"
            os.rename(os.path.join(dataset_dir, pose_class, img), os.path.join(dataset_dir, pose_class, "image_" + num + ".jpg"))
   
if __name__ == '__main__':
    main()