import os
import requests
import shutil
import sys

def split_data(base_dir, dataset_dir):
    
    print('Splitting training and test set...')
    
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
    
    with open(os.path.join(base_dir,'yoga_train.txt')) as f:
        for line in f:
            pose = line.split(',')[0].split('/')[0]
            sample = line.split(',')[0].split('/')[1]
            src_path = os.path.join(dataset_dir, pose, sample)
            dest_path = os.path.join(train_dir, pose)
            if os.path.exists(src_path):
                shutil.copy(src_path, dest_path)
                print(line.split(',')[0] + ' is added to training set.')
    
    with open(os.path.join(base_dir,'yoga_test.txt')) as f:
        for line in f:
            pose = line.split(',')[0].split('/')[0]
            sample = line.split(',')[0].split('/')[1]
            src_path = os.path.join(dataset_dir, pose, sample)
            dest_path = os.path.join(test_dir, pose)
            if os.path.exists(src_path):
                shutil.copy(src_path, dest_path)
                print(line.split(',')[0] + ' is added to test set.')

def main():
    
    base_dir = os.getcwd()
    dataset_dir = os.path.join(base_dir, 'yoga_dataset')
    
    try:
        os.mkdir(dataset_dir)
    except OSError as error:
        print(error)
        
    url_files = os.listdir(os.path.join(base_dir, 'yoga_dataset_links'))
    for url_file in url_files:
        if not(url_file.endswith('.txt')):
            continue
        try:
            os.mkdir(os.path.join(dataset_dir, url_file[:-4]))
        except OSError as error:
            print(error)
        with open(os.path.join(base_dir, 'yoga_dataset_links', url_file)) as f:
            for line in f:
                img_addr_name = line.split('http')[0].strip()
                img_name = img_addr_name.split('/')[1]
                img_url = 'http' + line.split('http')[1].strip()
                print(img_addr_name, 'is downloading from the link \'', img_url, '\'.')
                try:
                    response = requests.get(img_url, timeout=10)
                except requests.exceptions.RequestException:
                    print(img_addr_name, 'cannot be downloaded.')
                else:
                    if response.status_code >= 200 and response.status_code < 300:
                        with open(os.path.join(dataset_dir, url_file[:-4], img_name), 'wb') as i:
                            i.write(response.content)
                    else:
                        print(img_addr_name, 'cannot be downloaded.')
                        
    samples = []
    with open(os.path.join(os.getcwd(),'yoga_train.txt')) as f:
        samples = f.readlines()
        print(samples[:10])
    with open(os.path.join(os.getcwd(),'yoga_test.txt')) as f:
        samples = samples + f.readlines()
        print(samples[-10:])
    samples.sort()
    with open(os.path.join(os.getcwd(),'yoga_dataset.txt'), 'w') as f:
        f.write(''.join(samples))
        
    if '-split' in sys.argv:
        split_data(base_dir, dataset_dir)

if __name__ == '__main__':
    main()