import os
import cv2
from mediapipe import solutions
import numpy as np
import time

def find_landmarks(base_dir, dataset_dir, complexity=1, confidence=0.5):
    
    mp_drawing = solutions.drawing_utils
    mp_drawing_styles = solutions.drawing_styles
    mp_pose = solutions.pose
    
    landmark_dir = os.path.join(base_dir, "complexity"+str(complexity)+"_confidence"+str(confidence))
    try:
        os.mkdir(landmark_dir)
    except OSError as error:
        print(error)
    with mp_pose.Pose(static_image_mode=True, model_complexity=complexity, min_detection_confidence=confidence) as pose:    
        for pose_class in os.listdir(dataset_dir):
            if not(os.path.isdir(os.path.join(dataset_dir, pose_class))):
                continue
            try:
                os.mkdir(os.path.join(landmark_dir, pose_class))
            except OSError as error:
                print(error)
            
            for img in os.listdir(os.path.join(dataset_dir, pose_class)):
                if not(img.endswith('.jpg') or img.endswith('.png')):
                    continue
                
                image = cv2.imread(os.path.join(dataset_dir, pose_class, img))
                results = pose.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

                if not results.pose_landmarks:
                    continue

                annotated_image = image.copy()
                mp_drawing.draw_landmarks(annotated_image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS, landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style())
                cv2.imwrite(os.path.join(landmark_dir, pose_class, img), annotated_image)
                landmarks = []
                for i in range(33):
                    landmarks.append(np.array([results.pose_landmarks.landmark[i].x,
                                      results.pose_landmarks.landmark[i].y,
                                      results.pose_landmarks.landmark[i].z,
                                      results.pose_landmarks.landmark[i].visibility]))
                landmarks = np.array(landmarks)
                np.save(os.path.join(landmark_dir, pose_class, img[:-4]+".npy"), landmarks)
                 
def main():
    
    base_dir = os.getcwd()
    dataset_dir = os.path.join(base_dir, 'yoga_dataset')
    
    start_time = time.time()
    find_landmarks(base_dir, dataset_dir, complexity=2, confidence=0.5)
    end_time = time.time()
    
    print("Landmarks are created in", end_time-start_time, "seconds.")

if __name__ == '__main__':
    main()