import sys
import os
# === SPLASH 이미지 먼저 표시하기 위한 최소 모듈 임포트 ===
from PySide6.QtWidgets import QApplication, QSplashScreen
from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtCore import Qt, QTimer, QPropertyAnimation, QEasingCurve

import ctypes
myappid = 'yippee_sizecalculator_1.0.0'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

os.environ["QT_FONT_DPI"] = "96"

# QApplication 먼저 생성
app = QApplication(sys.argv)
app.setWindowIcon(QIcon(resource_path("logo_icon.ico")))

# Splash 화면 표시
splash_pixmap = QPixmap(resource_path("gui/images/logo_home_text.png"))

splash = QSplashScreen(splash_pixmap, Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)

splash.setWindowOpacity(0)  # 페이드인 위해 투명하게 시작
splash.show()
splash.showMessage("Launching Yippee Size Calculator...", Qt.AlignBottom | Qt.AlignCenter, Qt.black)
app.processEvents()

# 페이드인 애니메이션
fade_in = QPropertyAnimation(splash, b"windowOpacity")
fade_in.setDuration(500)  # 1초 페이드인
fade_in.setStartValue(0)
fade_in.setEndValue(1)
fade_in.setEasingCurve(QEasingCurve.InOutQuad)
fade_in.start()

from gui.uis.windows.main_window.functions_main_window import *
from qt_core import *
from gui.core.json_settings import Settings
from gui.uis.windows.main_window import *
from gui.widgets import *

# IF IS 4K MONITOR ENABLE 'os.environ["QT_SCALE_FACTOR"] = "2"'

# 필요한 라이브러리와 모듈을 임포트
import cv2  # OpenCV, 컴퓨터 비전 작업을 위한 라이브러리
import numpy as np  # NumPy, 배열 및 수치 계산을 위한 라이브러리
import os  # OS 모듈, 운영 체제와 상호작용을 위한 모듈
import csv  # CSV 파일을 읽고 쓰기 위한 모듈
from PIL import Image # PIL 모듈, 이미지를 열고 저장하기 위한 모듈
import shutil # 파일을 복사하거나 이동하기 위한 모듈
from scipy.ndimage import label as nd_label # SciPy의 ndimage 모듈에서 label 함수를 임포트, 영상 라벨링에 사용
import math
import json 
from PIL import Image

def imread_unicode(path):
    with Image.open(path) as img:
        return cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
    
def imwrite_unicode(path, image):
    # OpenCV 이미지는 BGR 포맷이므로 RGB로 변환 필요
    if image.ndim == 3 and image.shape[2] == 3:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    img_pil = Image.fromarray(image)
    img_pil.save(path)

with open(resource_path("settings.json"), "r", encoding="utf-8") as file:
    settings = json.load(file)
    
def launch_main_window():
    window = MainWindow()
    splash.finish(window)
    window.show()
    
def delete_folder_contents(folder_path):
    try:
        # 폴더가 실제로 존재하는지 확인합니다
        if os.path.isdir(folder_path):
            # 폴더의 모든 항목을 반복하며 삭제합니다
            for item in os.listdir(folder_path):
                item_path = os.path.join(folder_path, item)
                if os.path.isdir(item_path):
                    # 폴더인 경우, 하위 폴더 및 파일을 재귀적으로 삭제합니다
                    shutil.rmtree(item_path)
                else:
                    # 파일인 경우, 직접 삭제합니다
                    os.remove(item_path)
            print(f"All contents of {folder_path} have been deleted successfully.")
        else:
            print(f"{folder_path} is not a directory.")
    except Exception as e:
        print(f"An error occurred while trying to delete the file: {e}")

def make_folder(path):
    # 경로 상에 폴더가 존재하는지 확인 후 없다면 폴더 생성
    if not os.path.exists(path): # 경로가 존재하지 않으면
        os.makedirs(path, exist_ok=True) # 경로 생성 (mkdir은 마지막 경로만 만들음, makedirs는 경로가 없으면 상위까지 전부 만들어줌)
    else:
        print(f"경로 '{path}'이(가) 이미 존재합니다.")

    return path

def csv_file_save(csv_save_path, site_folder, image_name, save_path, leaf_number, leaf_area, new_site_foler):

        if new_site_foler == 0:
            # CSV 파일에 저장할 데이터        
            table_data_list= [

                [site_folder],
                [image_name],
                ['leaf#', 'leaf_area(cm^2)'],
                [leaf_number, leaf_area]]
        elif new_site_foler == 1:
            # CSV 파일에 저장할 데이터        
            table_data_list= [
                [image_name],
                ['leaf#', 'leaf_area(cm^2)'],
                [leaf_number, leaf_area]]
        else:
            table_data_list= [
            
                [leaf_number, leaf_area]]
        
        if not os.path.exists(csv_save_path):
            # 데이터를 CSV 파일에 쓰기 (코드를 한번 돌리고 data를 지우지 않는다면 이어서 쓰기가 될 가능성 있음)
            with open(csv_save_path, 'w', newline='') as csvfile: 
                csv_writer = csv.writer(csvfile)
                csv_writer.writerows(table_data_list)
        else:
            # 데이터를 CSV 파일에 이어서 쓰기
            with open(csv_save_path, 'a', newline='') as csvfile:
                csv_writer = csv.writer(csvfile)
                csv_writer.writerows(table_data_list)

def analysis_and_save(image_path, csv_save_path, site_folder, image_name, save_path, new_site_foler, image1_key, image2_key, csv_key, threshold_value=200):
    image = imread_unicode(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # BGR 컬러 이미지를 그레이스케일로 변환

    # # 이미지의 높이와 너비 가져오기
    # height, width, _ = image.shape

    _, binary_image = cv2.threshold(gray, threshold_value, 255, cv2.THRESH_BINARY_INV)

    min_size = 500 # 객체 필터링을 위한 최소 크기 ✅
    max_size = 10000000 # 객체 필터링을 위한 최대 크기 ✅

    marker, ncc = nd_label(binary_image)

    label_number = 1 # 레이블 번호 초기화
    result_image = np.zeros_like(image)
    # scale_image = np.zeros_like(image)

    # 라벨링된 각 객체에 대해 Watershed 알고리즘을 적용 (각 객체에 대해 반복)
    for number in range(1, ncc+1):
        marker_img = (marker == number) # 현재 라벨에 해당하는 마스크 생성
        marker_area = np.sum(marker_img) # 마스크 영역의 픽셀 수 계산

        if min_size <= marker_area <= max_size:
            result_image[marker == number] = label_number
            label_number += 1
        else:
            pass

    marker, ncc = nd_label(result_image)

    for result_number in range(1, ncc+1):
        result_marker_img = (result_image == result_number) # 현재 라벨에 해당하는 마스크 생성
        result_marker_area = np.sum(result_marker_img) # 마스크 영역의 픽셀 수 계산
        
        if result_number == 1:
            scale_cm2 = result_marker_area / 2

            if new_site_foler == 0:
                pass
            else:
                # csv에 폴더이름, 파일이름을 작성할 key값을 켜기
                new_site_foler = 1   
        else:
            # csv에 폴더이름, 파일이름을 작성할 key값을 끄기    
            new_site_foler = 2

        real_leaf_area = round(result_marker_area / scale_cm2, 2)

        if csv_key == True:
            csv_file_save(csv_save_path, site_folder, image_name, save_path, result_number, real_leaf_area, new_site_foler)

    labeled_image = marker
    num_labels = ncc
    save_image_1 = image.copy()

    # 객체의 특징을 분석하고 필터링
    filtered_objects = [] # 필터링된 객체를 저장할 리스트 초기화
    segmented_image = np.ones_like(labeled_image, dtype=np.uint8) * 255 # 객체를 분할하여 표시할 이미지 초기화
    contour_image = np.zeros_like(binary_image) # 객체의 윤곽선을 표시할 이미지 초기화

    for label in range(1, num_labels + 1):
        mask = (labeled_image == label).astype(np.uint8) # 각 레이블에 해당하는 마스크 생성

        # mask가 단일 채널이 아닐 경우 강제 변환
        if len(mask.shape) == 3:  # 3채널 이미지인 경우
            mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)  # 그레이스케일 변환

        contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) # 마스크로부터 윤곽선 추출
        
        if contours:
            contour = contours[0] # 첫 번째 윤곽선 선택
            area = cv2.contourArea(contour) # 윤곽선의 면적 계산
            perimeter = cv2.arcLength(contour, True) # 윤곽선의 둘레 계산
            
            # 면적과 원형도 기준에 따라 필터링
            if min_size <= area <= max_size:
                filtered_objects.append(label) # 필터링된 객체 저장
                
                for contour in contours:
                    # 윤곽선을 이미지에 그림
                    contour_image[(cv2.drawContours(contour_image, [contour], -1, 255, thickness=1)) == 255] = 255

                    #기존 이미지에 윤곽선만 표시한 이미지 (저장스타일 1)
                    cv2.drawContours(save_image_1, [contour], -1, (0, 0, 255), 2)
                    
                    area = cv2.contourArea(contour)

    # 검출된 객체 수 출력
    count = len(filtered_objects)
    print(f"Total objects detected: {count}")

    # 필터링된 객체를 새로운 이미지에 그리기
    for label in filtered_objects:
        mask = (labeled_image == label).astype(np.uint8) * 255  # 255 (흰색) 마스크 생성

        # mask가 단일 채널이 아닐 경우 강제 변환
        if len(mask.shape) == 3:  # 3채널 이미지인 경우
            mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)  # 그레이스케일 변환

        contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        if contours:
            cv2.drawContours(segmented_image, contours, -1, (0, 0, 0), thickness=cv2.FILLED)

    # segmented_image와 contour_image에서 객체를 찾아 번호를 표시
    segmented_image_colored = segmented_image.copy()
    # segmented_image_colored = cv2.cvtColor(segmented_image, cv2.COLOR_GRAY2BGR)

    for label in filtered_objects:
        mask = (labeled_image == label).astype(np.uint8)  # 각 레이블에 해당하는 마스크 생성

        # mask가 단일 채널이 아닐 경우 강제 변환
        if len(mask.shape) == 3:  # 3채널 이미지인 경우
            mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)  # 그레이스케일 변환

        contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)  # 윤곽선 추출

        if contours:
            contour = contours[0]  # 첫 번째 윤곽선 선택
            M = cv2.moments(contour)  # 객체의 모멘트 계산

            if M["m00"] != 0:  # 무게 중심이 존재하는 경우
                cx = int(M["m10"] / M["m00"])  # 중심 x 좌표
                cy = int(M["m01"] / M["m00"])  # 중심 y 좌표

                # segmented_image에 라벨 번호 표시
                cv2.putText(segmented_image_colored, str(label), (cx, cy), cv2.FONT_HERSHEY_SIMPLEX, 
                            3, (0, 0, 255), 10, cv2.LINE_AA)
                
                # # contour_image에도 라벨 번호 표시
                # cv2.putText(contour_image, str(label), (cx, cy), cv2.FONT_HERSHEY_SIMPLEX, 
                #             3, (255, 255, 255), 10, cv2.LINE_AA)
                
                # save_image_1에도 라벨 번호 표시
                cv2.putText(save_image_1, str(label), (cx, cy), cv2.FONT_HERSHEY_SIMPLEX, 
                            3, (0, 0, 255), 10, cv2.LINE_AA)

    if image1_key == True: 
        save_image_1_save_path = os.path.join(save_path, f"{site_folder}_{image_name}_{threshold_value}_contour_image.jpg")
        imwrite_unicode(save_image_1_save_path, save_image_1)

    if image2_key == True:
        segmented_image_save_path = os.path.join(save_path, f"{site_folder}_{image_name}_{threshold_value}_segmented_image.jpg")
        imwrite_unicode(segmented_image_save_path, segmented_image_colored)

def main_test_multi_threshold(image_path, thresholds=[200, 220, 240]):
    # 테스트이미지의 경로를 지정함 ✅
    image_name = os.path.basename(image_path).split('.')[0]
    site_folder = os.path.basename(os.path.dirname(image_path))
    site_path = os.path.dirname(image_path)
    site_name = "test"

    new_site_foler = 0
    save_path = os.path.join(site_path, "results")
    delete_folder_contents(save_path)
    save_path = make_folder(save_path)
    csv_file_name = site_name + ".csv"
    csv_save_path = os.path.join(save_path, csv_file_name)

    result_paths = {}

    for th in thresholds:
        # threshold에 따라 파일 이름 다르게 설정
        csv_file_name = f"{site_name}_{th}.csv"
        csv_save_path = os.path.join(save_path, csv_file_name)

        analysis_and_save(image_path, csv_save_path, site_folder, image_name, save_path, new_site_foler, True, True, True,threshold_value=th)
        result_image_path = os.path.join(save_path, f"{site_folder}_{image_name}_{th}_contour_image.jpg")
        result_paths[th] = result_image_path
    
    return result_paths

def main_analysis(experiment_path, threshold_value, analysis_image_1_key, analysis_image_2_key, analysis_csv_key, progress_callback=None):
    # 실험 데이터가 저장된 폴더 경로를 지정함 ✅
    experiment_name = os.path.basename(experiment_path)

    # 이미지를 저장할 폴더를 지정, 초기화, 생성
    save_path = os.path.join(experiment_path, "results")
    delete_folder_contents(save_path)
    save_path = make_folder(save_path)

    # CSV 파일 이름을 설정함. 이 파일은 추후에 데이터를 저장하는데 사용됨.
    csv_file_name = experiment_name + ".csv"
    csv_save_path = os.path.join(save_path, csv_file_name)

    # 실험 데이터 폴더 내의 모든 그룹 폴더 목록을 가져옴 (site 폴더)
    site_folderlist = [f for f in os.listdir(experiment_path) if os.path.isdir(os.path.join(experiment_path, f)) and f != "results"]
    total_sites = len(site_folderlist) # 총 그룹 수를 계산함

    # csv에 폴더이름, 파일이름을 작성할 key값을 초기화
    new_site_foler = 0    

    # 각 session 폴더에 대한 반복 처리
    for idx, site_folder in enumerate(site_folderlist): # site 폴더 내의 각 폴더에 대해 반복
        site_path = os.path.join(experiment_path, site_folder) # 서브 폴더의 전체 경로 생성
        file_list = os.listdir(site_path) # 서브 폴더 내의 모든 파일 목록을 가져옴

        new_site_foler = 0

        if site_folder == "results":
            continue    

        # 각 파일(이미지)에 대한 반복 처리
        for image_name_with_ext in file_list: 
            image_name = os.path.splitext(image_name_with_ext)[0] # 파일 이름에서 확장자를 제거하여 기본 파일 이름을 추출
        
            if os.path.splitext(image_name_with_ext)[1].lower() == '.jpg':  # 동영상 파일만 처리

                # 이미지의 경로를 지정
                image_path = os.path.join(site_path, image_name_with_ext)

                # 이미지 분석 및 저장 함수 호출
                analysis_and_save(image_path, csv_save_path, site_folder, image_name, save_path, new_site_foler, 
                                    analysis_image_1_key, analysis_image_2_key, analysis_csv_key, threshold_value)
            
            new_site_foler = 1

            if progress_callback:
                progress_callback(idx, total_sites)

    normalized_path = os.path.normpath(save_path)

    return normalized_path

# MAIN WINDOW
# ///////////////////////////////////////////////////////////////
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Taskbar 아이콘 확실히 설정
        self.setWindowIcon(QIcon(resource_path("logo_icon.ico")))
        
        # SETUP MAIN WINDOw
        # Load widgets from "gui\uis\main_window\ui_main.py"
        # ///////////////////////////////////////////////////////////////
        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)

        # LOAD SETTINGS
        # ///////////////////////////////////////////////////////////////
        settings = Settings()
        self.settings = settings.items

        # SETUP MAIN WINDOW
        # ///////////////////////////////////////////////////////////////
        self.hide_grips = True # Show/Hide resize grips
        SetupMainWindow.setup_gui(self)

        # SHOW MAIN WINDOW
        # ///////////////////////////////////////////////////////////////
        self.show()

        for btn in self.findChildren(QPushButton):
            btn.clicked.connect(self.btn_clicked)

        # Start BTN
        self.ui.load_pages.pushButton.clicked.connect(
            lambda: (self.ui.left_menu.select_only_one("Test"),  # 왼쪽 메뉴 중 "Test" 버튼 선택
                    MainFunctions.set_page(self, self.ui.load_pages.page_2)))  # Start Button Page 1 to Page 2
        
        # 초기 상태에서 NEXT BTN 비활성화
        self.ui.load_pages.Next_button_2.setEnabled(False)
        self.ui.load_pages.Next_button_5.setEnabled(False)
        self.ui.load_pages.Next_button_6.setEnabled(False)

        self.test_image_selected = False

    def resizeEvent_test_path(self, event):
        super().resizeEvent_test_path(event)

        if hasattr(self, "test_image_path") and self.test_image_path:
            pixmap = QPixmap(self.test_image_path)
            if not pixmap.isNull():
                label_size = self.ui.load_pages.image_output_2.size()
                scaled_pixmap = pixmap.scaled(label_size, Qt.KeepAspectRatio, Qt.SmoothTransformation)
                self.ui.load_pages.image_output_2.setPixmap(scaled_pixmap)


    def select_test_image(self):
        path, _ = QFileDialog.getOpenFileName(self, "Image file select", "", "Images (*.jpg)")
        if path:
            self.test_image_path = path
            self.ui.load_pages.path_lineEdit_2.setText(path)

            self.test_image_selected = True

            # 최종 결과 표시
            pixmap = QPixmap(path)
            if not pixmap.isNull():
                label_size = self.ui.load_pages.image_output_2.size()
                scaled = pixmap.scaled(label_size, Qt.KeepAspectRatio, Qt.SmoothTransformation)
                self.ui.load_pages.image_output_2.setPixmap(scaled)

            reply = QMessageBox.question(
                self,
                "Test image Confirmation",
                "Do you want to proceed with the analysis for this image?",
                QMessageBox.Ok | QMessageBox.Cancel
            )
            if reply == QMessageBox.Cancel:
                return

            # 프로그레스 바 초기화
            self.ui.load_pages.progressBar_2.setValue(0)
            self.ui.load_pages.progressBar_2.setVisible(True)

            thresholds = [200, 220, 240]
            step_percent = 100 / len(thresholds)
            current_progress = 0.0

            # 경로 설정
            image_name = os.path.basename(path).split('.')[0]
            site_folder = os.path.basename(os.path.dirname(path))
            site_path = os.path.dirname(path)
            site_name = "test"
            save_path = os.path.join(site_path, "results")
            delete_folder_contents(save_path)
            save_path = make_folder(save_path)

            new_site_foler = 0
            result_images = {}

            # 분석 반복
            for th, label_widget in zip(thresholds,
                                        [self.ui.load_pages.A_image_output_3,
                                        self.ui.load_pages.B_image_output_3,
                                        self.ui.load_pages.C_image_output_3]):

                csv_file_name = f"{site_name}_{th}.csv"
                csv_save_path = os.path.join(save_path, csv_file_name)

                analysis_and_save(
                    path, csv_save_path, site_folder, image_name, save_path,
                    new_site_foler, True, True, True, threshold_value=th
                )

                result_path = os.path.join(save_path, f"{site_folder}_{image_name}_{th}_contour_image.jpg")
                result_images[th] = result_path

                # 이미지 띄우기
                if os.path.exists(result_path):
                    pixmap = QPixmap(result_path)
                    if not pixmap.isNull():
                        scaled = pixmap.scaled(label_widget.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
                        label_widget.setPixmap(scaled)

                # 진행률 반영
                current_progress += step_percent
                self.ui.load_pages.progressBar_2.setValue(int(current_progress))
                QApplication.processEvents()  # UI 즉시 갱신

            if self.ui.load_pages.A_button_3.isChecked():
                self.display_result_by_threshold(200)
            elif self.ui.load_pages.B_button_3.isChecked():
                self.display_result_by_threshold(220)
            elif self.ui.load_pages.C_button_3.isChecked():
                self.display_result_by_threshold(240)

            # 100% 완료
            self.ui.load_pages.progressBar_2.setValue(100)
            # QTimer.singleShot(1000, lambda: self.ui.load_pages.progressBar_2.setVisible(False))

            # 완료 메시지
            QMessageBox.information(self, "Complete", "The analysis is completed.")

            # NEXT BTN 활성화
            self.ui.load_pages.Next_button_2.setEnabled(bool(path.strip()))

        return path
    
    def display_result_by_threshold(self, threshold):
        image_name = os.path.basename(self.test_image_path).split('.')[0]
        site_folder = os.path.basename(os.path.dirname(self.test_image_path))
        site_path = os.path.dirname(self.test_image_path)
        save_path = os.path.join(site_path, "results")

        # 이미지 경로
        contour_path = os.path.join(save_path, f"{site_folder}_{image_name}_{threshold}_contour_image.jpg")
        segmented_path = os.path.join(save_path, f"{site_folder}_{image_name}_{threshold}_segmented_image.jpg")
        csv_path = os.path.join(save_path, f"test_{threshold}.csv")

        # 이미지 1 표시 (contour)
        if os.path.exists(contour_path):
            pixmap1 = QPixmap(contour_path)
            if not pixmap1.isNull():
                size1 = self.ui.load_pages.image1_output_4.size()
                self.ui.load_pages.image1_output_4.setPixmap(pixmap1.scaled(size1, Qt.KeepAspectRatio, Qt.SmoothTransformation))

        # 이미지 2 표시 (segmented)
        if os.path.exists(segmented_path):
            pixmap2 = QPixmap(segmented_path)
            if not pixmap2.isNull():
                size2 = self.ui.load_pages.image2_output_4.size()
                self.ui.load_pages.image2_output_4.setPixmap(pixmap2.scaled(size2, Qt.KeepAspectRatio, Qt.SmoothTransformation))

        # CSV 경로 표시
        # CSV 파일을 QTableWidget에 표시
        if os.path.exists(csv_path):
            with open(csv_path, newline='', encoding='utf-8') as csvfile:
                reader = csv.reader(csvfile)
                rows = list(reader)
                self.ui.load_pages.exel_output_4.setRowCount(len(rows))
                self.ui.load_pages.exel_output_4.setColumnCount(max(len(row) for row in rows))
                for i, row in enumerate(rows):
                    for j, cell in enumerate(row):
                        item = QTableWidgetItem(cell)
                        self.ui.load_pages.exel_output_4.setItem(i, j, item)

                # 그리드 생성 및 열 너비 자동 조정
                self.ui.load_pages.exel_output_4.setShowGrid(True)
                self.ui.load_pages.exel_output_4.resizeColumnsToContents()
        else:
            self.ui.load_pages.exel_output_4.clear()
            self.ui.load_pages.exel_output_4.setRowCount(0)
            self.ui.load_pages.exel_output_4.setColumnCount(0)

    def select_analysis_folder(self):
        # 분석 옵션 및 임계값 설정 여부 확인
        image1_key = self.ui.load_pages.image1_button_5.isChecked()
        image2_key = self.ui.load_pages.image2_button_5.isChecked()
        csv_key = self.ui.load_pages.exel_button_5.isChecked()

        threshold_selected = (
            self.ui.load_pages.A_button_3.isChecked() or
            self.ui.load_pages.B_button_3.isChecked() or
            self.ui.load_pages.C_button_3.isChecked())

        test_image_done = getattr(self, 'test_image_selected', False)

        if not (image1_key or image2_key or csv_key) or not threshold_selected or not test_image_done:
            QMessageBox.critical(
                self,
                "Test Required",
                "Please perform the test step first before running the analysis."
            )
            return # 조건이 충족되지 않으면 파일 탐색기 실행하지 않음

        folder_path = QFileDialog.getExistingDirectory(self, "Select folder", "")
        next_btn = self.ui.load_pages.Next_button_6
        
        if folder_path:
            # 폴더 경로를 입력란에 표시
            self.ui.load_pages.path_lineEdit_6.setText(folder_path)

            # 경로가 폴더인지 확인
            if not os.path.isdir(folder_path):
                QMessageBox.warning(self, "Invalid Path", "Please enter a valid folder path.")
                return

            # 실험 폴더 안의 항목들 불러오기
            items = os.listdir(folder_path)

            # 사이트 폴더만 추출 (analysis 제외)
            subfolders = [
                f for f in items
                if os.path.isdir(os.path.join(folder_path, f)) and f != "results"
            ]

            # 파일이 섞여 있는지 확인
            has_file = any(os.path.isfile(os.path.join(folder_path, f)) for f in items)

            # 1. 하위 폴더가 없는 경우
            if not subfolders:
                QMessageBox.critical(
                    self,
                    "Missing Site Folders",
                    "The selected folder must contain at least one subfolder for site data."
                )
                return

            # 2. 실험 폴더 안에 파일이 섞여 있는 경우
            if has_file:
                QMessageBox.critical(
                    self,
                    "Invalid Folder Structure",
                    "Files are not allowed in the experiment folder.\nOnly site folders should be present in selected experiment folder."
                )
                return

            # 3. 각 사이트 폴더 내부 확인
            for sub in subfolders:
                site_path = os.path.join(folder_path, sub)
                site_items = os.listdir(site_path)

                for item in site_items:
                    full_path = os.path.join(site_path, item)
                    # 3-1. 사이트 폴더 안에 폴더가 있는 경우
                    if os.path.isdir(full_path):
                        QMessageBox.critical(
                            self,
                            "Nested Folder Detected",
                            f"The site folder '{sub}' contains another folder.\nOnly .jpg image files are allowed."
                        )
                        return
                    # 3-2. jpg 외의 확장자가 있는 경우
                    if not item.lower().endswith(".jpg"):
                        QMessageBox.critical(
                            self,
                            "Invalid File Type",
                            f"The site folder '{sub}' contains a non-JPG file.\nOnly .jpg files are allowed."
                        )
                        return
            # 분석 진행 여부 확인
            reply = QMessageBox.question(
                self,
                "Analtysis Confirmation",
                "Do you want to proceed with the analysis for this folder?",
                QMessageBox.Ok | QMessageBox.Cancel
            )

            if reply == QMessageBox.Ok:
                # 분석 실행
                self.run_analysis_based_on_checkboxes()

                # NEXT BTN 활성화
                self.ui.load_pages.Next_button_6.setEnabled(True)

                # 페이지 전환
                MainFunctions.set_page(self, self.ui.load_pages.page_7)

    def run_analysis_based_on_checkboxes(self):
        # 경로 가져오기
        experiment_path = self.ui.load_pages.path_lineEdit_6.text()
        if not os.path.isdir(experiment_path):
            QMessageBox.warning(self, "Error", "Please enter a valid folder path.")
            return

        # 체크박스 상태 가져오기
        image1_key = self.ui.load_pages.image1_button_5.isChecked()
        image2_key = self.ui.load_pages.image2_button_5.isChecked()
        csv_key = self.ui.load_pages.exel_button_5.isChecked()

        # threshold 결정 (라디오 버튼)
        if self.ui.load_pages.A_button_3.isChecked():
            threshold = 200
        elif self.ui.load_pages.B_button_3.isChecked():
            threshold = 220
        elif self.ui.load_pages.C_button_3.isChecked():
            threshold = 240
        else:
            QMessageBox.warning(self, "Error", "Please select the Threshold Value(A or B or C).")
            return

        total = len([f for f in os.listdir(experiment_path) if os.path.isdir(os.path.join(experiment_path, f)) and f != "results"])
        self.ui.load_pages.progressBar.setVisible(True)
        self.ui.load_pages.progressBar.setValue(0)

        def update_progress_bar(current, total):
            percentage = math.floor((current + 1) / total * 100)
            self.ui.load_pages.progressBar.setValue(percentage)

        save_path = main_analysis(
            experiment_path=experiment_path,
            threshold_value=threshold,
            analysis_image_1_key=image1_key,
            analysis_image_2_key=image2_key,
            analysis_csv_key=csv_key,
            progress_callback=update_progress_bar
        )

        # 완료 메시지
        QMessageBox.information(self, "Complete", "The analysis is completed.")

        # page_7로 이동 및 경로 표시
        self.ui.load_pages.path_lineEdit_7.setText(save_path)  # 경로 표시
        MainFunctions.set_page(self, self.ui.load_pages.page_7)  # 페이지 이동
        os.startfile(save_path)  # 파일 탐색기에서 경로 열기

    def reset_test_and_analysis_pages(self):
        lp = self.ui.load_pages

        lp.path_lineEdit_2.clear()
        lp.image_output_2.clear()
        lp.image_output_2.repaint()
        lp.progressBar_2.setValue(0)

        lp.A_button_3.setChecked(True)
        lp.B_button_3.setChecked(False)
        lp.C_button_3.setChecked(False)
        lp.A_image_output_3.clear()
        lp.B_image_output_3.clear()
        lp.C_image_output_3.clear()
        lp.A_image_output_3.repaint()
        lp.B_image_output_3.repaint()
        lp.C_image_output_3.repaint()

        lp.image1_output_4.clear()
        lp.image2_output_4.clear()
        lp.image1_output_4.repaint()
        lp.image2_output_4.repaint()
        lp.exel_output_4.clearContents()
        lp.exel_output_4.setShowGrid(False)

        lp.image1_button_5.setChecked(False)
        lp.image2_button_5.setChecked(False)
        lp.exel_button_5.setChecked(False)

        lp.path_lineEdit_6.clear()
        lp.progressBar.setValue(0)

        lp.path_lineEdit_7.clear()

        # 초기 상태에서 NEXT BTN 비활성화
        self.ui.load_pages.Next_button_2.setEnabled(False)
        self.ui.load_pages.Next_button_5.setEnabled(False)
        self.ui.load_pages.Next_button_6.setEnabled(False)

        # lp.repaint()

    def reset_analysis_pages(self):
        lp = self.ui.load_pages

        lp.path_lineEdit_6.clear()
        lp.path_lineEdit_6.repaint()

        lp.progressBar.setValue(0)
        lp.progressBar.repaint()

        lp.path_lineEdit_7.clear()
        lp.path_lineEdit_7.repaint()

        # 초기 상태에서 NEXT BTN 비활성화
        self.ui.load_pages.Next_button_6.setEnabled(False)

        # lp.repaint()

    def check_analysis_options(self):
        btn1 = self.ui.load_pages.image1_button_5.isChecked()
        btn2 = self.ui.load_pages.image2_button_5.isChecked()
        btn3 = self.ui.load_pages.exel_button_5.isChecked()
        self.ui.load_pages.Next_button_5.setEnabled(btn1 or btn2 or btn3)

    # LEFT MENU BTN IS CLICKED
    # Run function when btn is clicked
    # Check funtion by object name / btn_id
    # ///////////////////////////////////////////////////////////////
    def btn_clicked(self):
        # GET BT CLICKED
        btn = self.sender()
        # btn = SetupMainWindow.setup_btns(self)

        # Remove Selection If Clicked By "btn_close_left_column"
        if btn.objectName() != "btn_settings":
            self.ui.left_menu.deselect_all_tab()

        # # Get Title Bar Btn And Reset Active         
        # top_settings = MainFunctions.get_title_bar_btn(self, "btn_top_settings")
        # top_settings.set_active(False)

        # LEFT MENU
        # ///////////////////////////////////////////////////////////////
        
        # HOME BTN
        if btn.objectName() == "btn_home":
            # Select Menu
            self.ui.left_menu.select_only_one(btn.objectName())

            # Load Page 1
            MainFunctions.set_page(self, self.ui.load_pages.page_1)

        # TEST BTN
        if btn.objectName() == "Test":
            # Select Menu
            self.ui.left_menu.select_only_one(btn.objectName())

            # Load Page 2
            MainFunctions.set_page(self, self.ui.load_pages.page_2)

            # 초기화: page_2 ~ page_7
            self.reset_test_and_analysis_pages()

        # ANALYSIS PAGE
        if btn.objectName() == "Analysis":
            # Select Menu
            self.ui.left_menu.select_only_one(btn.objectName())

            # Load Page 6
            MainFunctions.set_page(self, self.ui.load_pages.page_6)

            # 초기화: page_6, 7
            self.reset_analysis_pages()

        # NEXT BTN
        self.ui.load_pages.Next_button_2.clicked.connect(
            lambda: MainFunctions.set_page(self, self.ui.load_pages.page_3)) # Next Button Page 2 to Page 3
        self.ui.load_pages.Next_button_3.clicked.connect(
            lambda: MainFunctions.set_page(self, self.ui.load_pages.page_4)) # Next Button Page 3 to Page 4
        self.ui.load_pages.Next_button_4.clicked.connect(
            lambda: MainFunctions.set_page(self, self.ui.load_pages.page_5)) # Next Button Page 4 to Page 5
        self.ui.load_pages.Next_button_5.clicked.connect(
            lambda: (MainFunctions.set_page(self, self.ui.load_pages.page_6),
                    self.ui.left_menu.select_only_one("Analysis"))) # Next Button Page 5 to Page 6, select Analysis Menu
        self.ui.load_pages.Next_button_6.clicked.connect(
            lambda: MainFunctions.set_page(self, self.ui.load_pages.page_7)) # Next Button Page 6 to Page 7
        
        # HOME BTN
        self.ui.load_pages.Home_button_7.clicked.connect(
            lambda: (self.reset_test_and_analysis_pages(),  # 초기화 먼저 실행
                    MainFunctions.set_page(self, self.ui.load_pages.page_1),
                    self.ui.left_menu.select_only_one("btn_home"))) # Home Button Page 7 to Page 1, select Analysis Menu
        
        # BACK BTN
        self.ui.load_pages.Back_button_2.clicked.connect(
            lambda: (MainFunctions.set_page(self, self.ui.load_pages.page_1),
                    self.ui.left_menu.select_only_one("btn_home"))) # Next Button Page 2 to Page 1, select Home Menu
        self.ui.load_pages.Back_button_3.clicked.connect(
            lambda: MainFunctions.set_page(self, self.ui.load_pages.page_2)) # Next Button Page 3 to Page 2
        self.ui.load_pages.Back_button_4.clicked.connect(
            lambda: MainFunctions.set_page(self, self.ui.load_pages.page_3)) # Next Button Page 4 to Page 3
        self.ui.load_pages.Back_button_5.clicked.connect(
            lambda: MainFunctions.set_page(self, self.ui.load_pages.page_4)) # Next Button Page 5 to Page 4
        self.ui.load_pages.Back_button_6.clicked.connect(
            lambda: (MainFunctions.set_page(self, self.ui.load_pages.page_5),
                    self.ui.left_menu.select_only_one("Test"))) # Next Button Page 6 to Page 5, select Test Menu
        self.ui.load_pages.Back_button_7.clicked.connect(
            lambda: MainFunctions.set_page(self, self.ui.load_pages.page_6)) # Next Button Page 7 to Page 6
        
        # page2에서 test image 선택 버튼 클릭 시 연결된 함수 해제
        try:
            self.ui.load_pages.path_button_2.clicked.disconnect()
        except TypeError:
            pass  # 연결 안 되어 있으면 무시

        self.ui.load_pages.path_button_2.clicked.connect(self.select_test_image)

        # page3에서 선택되는 버튼에 따라 page4의 이미지를 다르게 보여줌
        self.ui.load_pages.A_button_3.toggled.connect(lambda checked: self.display_result_by_threshold(200) if checked else None)
        self.ui.load_pages.B_button_3.toggled.connect(lambda checked: self.display_result_by_threshold(220) if checked else None)
        self.ui.load_pages.C_button_3.toggled.connect(lambda checked: self.display_result_by_threshold(240) if checked else None)

        #page6에서 분석할 폴더 선택 버튼 클릭 시 연결된 함수 해제
        try:
            self.ui.load_pages.path_button_6.clicked.disconnect()
        except TypeError:
            pass  # 연결 안 되어 있으면 무시
        
        # page6에서 분석할 폴더 선택 버튼 클릭 시 선택된 폴더를 띄움
        self.ui.load_pages.path_button_6.clicked.connect(self.select_analysis_folder)

        # DEBUG
        print(f"Button {btn.objectName()}, clicked!")

        # NEXT BTN 활성화
        self.ui.load_pages.image1_button_5.toggled.connect(self.check_analysis_options)
        self.ui.load_pages.image2_button_5.toggled.connect(self.check_analysis_options)
        self.ui.load_pages.exel_button_5.toggled.connect(self.check_analysis_options)

    # LEFT MENU BTN IS RELEASED
    # Run function when btn is released
    # Check funtion by object name / btn_id
    # ///////////////////////////////////////////////////////////////
    def btn_released(self):
        # GET BT CLICKED
        btn = SetupMainWindow.setup_btns(self)

        # DEBUG
        print(f"Button {btn.objectName()}, released!")

    # RESIZE EVENT
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        SetupMainWindow.resize_grips(self)

    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        # self.dragPos = event.globalPos()
        self.dragPos = event.globalPosition().toPoint() # recommend in pyQt6
    
if __name__ == "__main__":
    # 이미 위에서 QApplication과 splash는 생성되어 있음
    # Dummy 창을 만들어서 Taskbar 아이콘 선점
    dummy = QMainWindow()
    dummy.setWindowIcon(QIcon(resource_path("logo_icon.ico")))
    dummy.show()
    dummy.hide()  # 바로 숨김 (Taskbar 등록만 하고 사용자에게 안 보임)

    # # 메인 윈도우 로드
    # window = MainWindow()

    # # splash 종료 후 메인 윈도우 표시
    # splash.finish(window)
    QTimer.singleShot(2000, launch_main_window)

    # 앱 실행
    sys.exit(app.exec())