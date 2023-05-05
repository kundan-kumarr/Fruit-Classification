import os
import shutil
import random

folder_path = r'C:/Users/kkumar/Downloads/HCI575/hci575_data'


train_dir = os.path.join(folder_path, 'train')
test_dir = os.path.join(folder_path, 'test')
os.makedirs(train_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)


for fruit_quality in ['unripe_fruits', 'ripe_fruits', 'overripe_fruits', 'moldy_fruits']:
    # Create subdirectories for train and test
    train_fruit_dir = os.path.join(train_dir, fruit_quality)
    test_fruit_dir = os.path.join(test_dir, fruit_quality)
    os.makedirs(train_fruit_dir, exist_ok=True)
    os.makedirs(test_fruit_dir, exist_ok=True)

    for subfolder in os.listdir(os.path.join(folder_path, fruit_quality)):
        subfolder_path = os.path.join(folder_path, fruit_quality, subfolder)
        if os.path.isdir(subfolder_path):
            # Split images into train and test sets
            images = os.listdir(subfolder_path)
            random.shuffle(images)
            split_idx = int(len(images) * 0.8)
            train_images = images[:split_idx]
            test_images = images[split_idx:]

            for sub_label in ['unripe_apple', 'unripe_banana', 'unripe_lime', 'unripe_orange',
                              'ripe_apple', 'ripe_banana', 'ripe_lime', 'ripe_orange',
                              'overripe_apple', 'overripe_banana', 'overripe_lime', 'overripe_orange',
                              'moldy_apple', 'moldy_banana', 'moldy_lime', 'moldy_orange']:
                os.makedirs(os.path.join(train_fruit_dir, sub_label), exist_ok=True)

            for image in train_images:
                sub_label = image.split('_')[0]  # extract the sub-label from image name
                print(sub_label)
                # if '-' not in sub_label:
                #     continue  # skip this image
                fruit_label = sub_label.split('-')[0]
                # quality_label = sub_label.split('-')[1]
                src = os.path.join(subfolder_path, image)
                dst_folder = os.path.join(train_fruit_dir,subfolder)
                #dst_folder = os.path.join(train_fruit_dir, quality_label, fruit_label)
                dst = os.path.join(dst_folder, image)
                shutil.copy(src, dst)

            # Create subdirectories
            for sub_label in ['unripe_apple', 'unripe_banana', 'unripe_lime', 'unripe_orange',
                              'ripe_apple', 'ripe_banana', 'ripe_lime', 'ripe_orange',
                              'overripe_apple', 'overripe_banana', 'overripe_lime', 'overripe_orange',
                              'moldy_apple', 'moldy_banana', 'moldy_lime', 'moldy_orange']:
                os.makedirs(os.path.join(test_fruit_dir, sub_label), exist_ok=True)

            # # Copy images to test directory
            for image in test_images:
                sub_label = image.split('_')[0]  # extract the sub-label from image name
                # if '-' not in sub_label:
                #     continue  # skip this image
                fruit_label = sub_label.split('-')[0]  # extract the fruit label from sub-label
                # quality_label = sub_label.split('-')[1]  # extract the quality label from sub-label
                src = os.path.join(subfolder_path, image)
                dst_folder = os.path.join(test_fruit_dir, subfolder)
                dst = os.path.join(dst_folder, image)
                shutil.copy(src, dst)
