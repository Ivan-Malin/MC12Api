import cv2
import glob
from convert import append_str_frame, save_str

def process_images_in_folder(folder_path):
    image_paths = glob.glob(folder_path + '/*.png')  # Assuming the images are in JPEG format, you can change the extension if needed

    for path in image_paths:
        img = cv2.imread(path)
        if img is not None:
            rescaled_img = cv2.resize(img, (16, 16), interpolation=cv2.INTER_NEAREST)
            resized_frame, thresholded_frame =  append_str_frame(rescaled_img)
            print(thresholded_frame)
            # Further processing or saving of the resulting image can be done here
process_images_in_folder('C:/Users/Admin/Documents/MCTest/examples/Matrix/modules/convert video/photo_in')
save_str()
