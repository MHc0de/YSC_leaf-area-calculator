import os
import csv
import numpy as np
import cv2
from scipy.ndimage import label as nd_label
from core.image_utils import imread_unicode, imwrite_unicode
from core.file_utils import make_folder, delete_folder_contents

import os
import csv

def detect_encoding(file_path, encodings=['utf-8', 'cp949', 'euc-kr', 'ansi']):
    for enc in encodings:
        try:
            with open(file_path, encoding=enc) as f:
                f.read()
            return enc
        except Exception:
            continue
    # 기본값
    return 'utf-8'

def csv_file_save_append(csv_save_path, rows):
    if os.path.exists(csv_save_path):
        encoding = detect_encoding(csv_save_path, ['utf-8', 'utf-8-sig', 'cp949', 'euc-kr', 'ansi'])
        with open(csv_save_path, 'a', newline='', encoding=encoding) as csvfile:
            csv.writer(csvfile).writerows(rows)
    else:
        # 새 파일 생성 시 원하는 인코딩으로
        with open(csv_save_path, 'w', newline='', encoding='utf-8-sig') as csvfile:
            csv.writer(csvfile).writerows(rows)

def analysis_and_save(image_path, csv_save_path, site_folder, image_name, save_path, new_site_foler, image1_key, image2_key, csv_key, threshold_value=200):
    image = imread_unicode(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, binary_image = cv2.threshold(gray, threshold_value, 255, cv2.THRESH_BINARY_INV)

    min_size = 500
    max_size = 10000000
    marker, ncc = nd_label(binary_image)

    # leaf area 데이터 일괄 저장을 위한 리스트
    csv_rows = []
    label_number = 1
    scale_cm2 = None

    # vectorized 연산으로 각 라벨별 area 계산
    areas = np.bincount(marker.ravel())
    labels = np.arange(len(areas))
    valid_labels = labels[(areas >= min_size) & (areas <= max_size) & (labels != 0)]

    result_image = np.zeros_like(marker, dtype=np.uint8)
    for idx, lbl in enumerate(valid_labels, 1):
        result_image[marker == lbl] = idx
        if scale_cm2 is None:
            scale_cm2 = areas[lbl] / 2
            this_new_site_folder = new_site_foler
        else:
            this_new_site_folder = 2

        if csv_key:
            real_leaf_area = round(areas[lbl] / scale_cm2, 2)
            if this_new_site_folder == 0:
                csv_rows.append([site_folder])
                csv_rows.append([image_name])
                csv_rows.append(['leaf#', 'leaf_area(cm^2)'])
                csv_rows.append([idx, real_leaf_area])
            elif this_new_site_folder == 1:
                csv_rows.append([image_name])
                csv_rows.append(['leaf#', 'leaf_area(cm^2)'])
                csv_rows.append([idx, real_leaf_area])
            else:
                csv_rows.append([idx, real_leaf_area])

    if csv_key and csv_rows:
        if not os.path.exists(csv_save_path):
            csv_file_save_append(csv_save_path, csv_rows)
        else:
            # append 모드로 추가 저장
            with open(csv_save_path, 'a', newline='', encoding='utf-8') as csvfile:
                csv.writer(csvfile).writerows(csv_rows)

    # contour 및 segmentation 이미지 처리
    if image1_key or image2_key:
        save_image_1 = image.copy()
        segmented_image_colored = np.ones((*gray.shape, 3), dtype=np.uint8) * 255

        for idx, lbl in enumerate(valid_labels, 1):
            mask = (result_image == idx).astype(np.uint8)
            contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            if contours:
                cv2.drawContours(save_image_1, contours, -1, (0, 0, 255), 2)
                M = cv2.moments(contours[0])
                if M["m00"] != 0:
                    cx = int(M["m10"] / M["m00"])
                    cy = int(M["m01"] / M["m00"])
                    cv2.drawContours(segmented_image_colored, contours, -1, 0, thickness=cv2.FILLED)
                    cv2.putText(segmented_image_colored, str(idx), (cx, cy), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 0, 255), 10, cv2.LINE_AA)
                    cv2.putText(save_image_1, str(idx), (cx, cy), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 0, 255), 10, cv2.LINE_AA)

        if image1_key:
            save_image_1_save_path = os.path.join(save_path, f"{site_folder}_{image_name}_{threshold_value}_contour_image.jpg")
            imwrite_unicode(save_image_1_save_path, save_image_1)
        if image2_key:
            segmented_image_save_path = os.path.join(save_path, f"{site_folder}_{image_name}_{threshold_value}_segmented_image.jpg")
            imwrite_unicode(segmented_image_save_path, segmented_image_colored)

def main_analysis(experiment_path, threshold_value, analysis_image_1_key, analysis_image_2_key, analysis_csv_key, progress_callback=None):
    experiment_name = os.path.basename(experiment_path)
    save_path = os.path.join(experiment_path, "results")
    delete_folder_contents(save_path)
    save_path = make_folder(save_path)
    csv_file_name = experiment_name + ".csv"
    csv_save_path = os.path.join(save_path, csv_file_name)
    site_folderlist = [f for f in os.listdir(experiment_path) if os.path.isdir(os.path.join(experiment_path, f)) and f != "results"]
    total_sites = len(site_folderlist)
    new_site_foler = 0

    for idx, site_folder in enumerate(site_folderlist):
        site_path = os.path.join(experiment_path, site_folder)
        file_list = os.listdir(site_path)
        new_site_foler = 0

        allowed_extensions = ('.jpg', '.jpeg', '.png', '.tif', '.tiff')

        for image_name_with_ext in file_list:
            image_name = os.path.splitext(image_name_with_ext)[0]
            extension = os.path.splitext(image_name_with_ext)[1].lower()

            if extension in allowed_extensions:
                image_path = os.path.join(site_path, image_name_with_ext)
                analysis_and_save(image_path, csv_save_path, site_folder, image_name, save_path, new_site_foler,
                                    analysis_image_1_key, analysis_image_2_key, analysis_csv_key, threshold_value)
            new_site_foler = 1
        if progress_callback:
            progress_callback(idx, total_sites)
    return os.path.normpath(save_path)
