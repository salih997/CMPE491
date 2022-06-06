import os
import cv2

def main():
    
    base_dir = os.getcwd()
    dataset_dir = os.path.join(base_dir, 'yoga_dataset')
    
    cnt = 0
    removed_images = []
    for pose_class in os.listdir(dataset_dir):
        if not(os.path.isdir(os.path.join(dataset_dir, pose_class))):
            continue
        for img in os.listdir(os.path.join(dataset_dir, pose_class)):
            if not(img.endswith('.jpg') or img.endswith('.png')):
                continue
            image = cv2.imread(os.path.join(dataset_dir, pose_class, img))
            if image is None:
                cnt = cnt + 1
                removed_images.append(pose_class + "/" + img)
                print("NoneType:", pose_class, img)
                os.remove(os.path.join(dataset_dir, pose_class, img))
                
    with open(os.path.join(base_dir, "yoga_dataset.txt")) as f:
        lines = f.readlines()
        
    with open(os.path.join(base_dir, "yoga_dataset.txt"), "w") as o:
        for line in lines:
            count = 0
            for removed in removed_images:
                if not line.startswith(removed):
                    count = count + 1
            if count == len(removed_images):
                o.write(line)

    print("Number of deleted files is", cnt)
    print("***** FINISHED *****")

if __name__ == '__main__':
    main()