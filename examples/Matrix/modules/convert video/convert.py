import cv2
import numpy as np

def process_video(video_path):
    global STR
    cap = cv2.VideoCapture(video_path)
    frames = []
    
    fl = False
    i = 0
    while True:
        ret, frame = cap.read()
        i += 1
        if i<30:
            continue
        i = 0
        if not ret:
            break
        
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # resized_frame = gray_frame
        resized_frame = cv2.resize(gray_frame, (16, 16))
        thresholded_frame = cv2.threshold(resized_frame, 80, 255, cv2.THRESH_BINARY)[1]
        thresholded_frame = np.where(thresholded_frame > 100, 1, 0)  # Convert values to 0 or 1
        A0, A1, A2, A3 = split_arrays(thresholded_frame)
        STR[0] += '\n'+arr_to_str_frame(A0)
        STR[1] += '\n'+arr_to_str_frame(A1)
        STR[2] += '\n'+arr_to_str_frame(A2)
        STR[3] += '\n'+arr_to_str_frame(A3)
        if not fl:
            print(resized_frame)
            print(thresholded_frame)
            # print()
            fl |= True
        
        frames.append(thresholded_frame)
    
    cap.release()
    return frames

global STR
STEP = 100 #n
STR = \
[""".define Count8 
 +0ns 00
""" for i in range(4)]

def byte_to_displacement(b, wait=STEP):
    S = hex(b)[2:].upper()
    bl = 0
    bh = 0
    if   len(S)==1:
        bl = S[0]
    elif len(S)==2:
        bl = S[1]
        bh = S[0]
    return f" ++{wait}n {bh}{bl}"

# def add_byte(b):
#     global STR
#     d = byte_to_displacement(b)
#     STR += '\n'+f'{d}'

def get_arr_byte(arr, i):
    # for 2d binary (0/1) array
    I = i
    b = 0
    for i in range(len(arr)):
        if arr[i][I]==1:
            b |= (1<<i)
    return b

def arr_to_str_frame(arr):
    # for 8 x n array
    global STEP
    S = ''
    n = len(arr)
    print(n)
    for i in range(n):
        s = byte_to_displacement(
                get_arr_byte(arr,i),
                STEP*n
            ) + '\n'
        S += s
    return S

def split_arrays(original_array):
    splitted_arrays = [
        original_array[:8, :8],   # Array 1
        original_array[:8, 8:],    # Array 3
        original_array[8:, :8],    # Array 2
        original_array[8:, 8:]     # Array 4
    ]
    return splitted_arrays

if __name__ == '__main__':
    video_path = "C:/Users/Admin/Documents/MCTest/examples/Matrix/modules/convert video/0001-0159.avi"
    file_path  = "C:/Users/Admin/Documents/MCTest/examples/Matrix/modules/convert video/frames/STR{0}.txt"
    save_path  = "C:/Users/Admin/Documents/MCTest/examples/Matrix/modules/convert video/photo"
    resulting_frames = process_video(video_path)

    for i in range(4):
        f = open(file_path.format(i), 'w')
        f.write(STR[i])
        f.close()
    i = 0
    for frame in resulting_frames:
        i += 1
        # print(frame)
        image = (frame*255).astype(np.uint8)
        enlarged_image = cv2.resize(image, (160, 160), interpolation=cv2.INTER_NEAREST)
        cv2.imshow('Processed Frame', enlarged_image)
        cv2.imwrite(save_path+f'/frame_{i}.png', enlarged_image) 
        if cv2.waitKey(30) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()
