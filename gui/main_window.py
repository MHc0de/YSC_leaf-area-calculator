import os
import csv
import math
from PySide6.QtWidgets import QMainWindow, QMessageBox, QFileDialog, QTableWidgetItem, QApplication
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtCore import Qt
from gui.ui_connector import connect_main_window_ui
from gui.uis.windows.main_window.functions_main_window import *
from gui.uis.windows.main_window import *
from gui.core.json_settings import Settings
from gui.widgets import *

from resource_utils import resource_path
from core.analysis import analysis_and_save, main_analysis
from core.file_utils import delete_folder_contents, make_folder

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon(resource_path("logo_icon.ico")))
        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)
        self.settings = Settings().items
        self.hide_grips = True
        self.MainFunctions = MainFunctions
        SetupMainWindow.setup_gui(self)
        self.test_image_selected = False
        connect_main_window_ui(self)

    def select_test_image(self):
        path, _ = QFileDialog.getOpenFileName(self, "image file selet", "", "image (*.jpg *.jpeg *.png *.tif *.tiff)")
        if path:
            self.test_image_path = path
            self.ui.load_pages.path_lineEdit_2.setText(path)
            self.test_image_selected = True
            pixmap = QPixmap(path)
            if not pixmap.isNull():
                label_size = self.ui.load_pages.image_output_2.size()
                scaled = pixmap.scaled(label_size, Qt.KeepAspectRatio, Qt.SmoothTransformation)
                self.ui.load_pages.image_output_2.setPixmap(scaled)
            reply = QMessageBox.question(
                self,
                "Setting image Confirmation",
                "Do you want to proceed with the analysis for this image?",
                QMessageBox.Ok | QMessageBox.Cancel
            )
            if reply == QMessageBox.Cancel:
                return
            self.ui.load_pages.progressBar_2.setValue(0)
            self.ui.load_pages.progressBar_2.setVisible(True)
            thresholds = [200, 220, 240]
            step_percent = 100 / len(thresholds)
            current_progress = 0.0
            image_name = os.path.basename(path).split('.')[0]
            site_folder = os.path.basename(os.path.dirname(path))
            site_path = os.path.dirname(path)
            site_name = "test"
            save_path = os.path.join(site_path, "results")
            delete_folder_contents(save_path)
            save_path = make_folder(save_path)
            new_site_foler = 0
            result_images = {}
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
                if os.path.exists(result_path):
                    pixmap = QPixmap(result_path)
                    if not pixmap.isNull():
                        scaled = pixmap.scaled(label_widget.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
                        label_widget.setPixmap(scaled)
                current_progress += step_percent
                self.ui.load_pages.progressBar_2.setValue(int(current_progress))
                QApplication.processEvents()
            if self.ui.load_pages.A_button_3.isChecked():
                self.display_result_by_threshold(200)
            elif self.ui.load_pages.B_button_3.isChecked():
                self.display_result_by_threshold(220)
            elif self.ui.load_pages.C_button_3.isChecked():
                self.display_result_by_threshold(240)
            self.ui.load_pages.progressBar_2.setValue(100)
            QMessageBox.information(self, "Complete", "The analysis is completed.")
            self.ui.load_pages.Next_button_2.setEnabled(bool(path.strip()))
        return path

    def display_result_by_threshold(self, threshold):
        image_name = os.path.basename(self.test_image_path).split('.')[0]
        site_folder = os.path.basename(os.path.dirname(self.test_image_path))
        site_path = os.path.dirname(self.test_image_path)
        save_path = os.path.join(site_path, "results")
        contour_path = os.path.join(save_path, f"{site_folder}_{image_name}_{threshold}_contour_image.jpg")
        segmented_path = os.path.join(save_path, f"{site_folder}_{image_name}_{threshold}_segmented_image.jpg")
        csv_path = os.path.join(save_path, f"test_{threshold}.csv")
        if os.path.exists(contour_path):
            pixmap1 = QPixmap(contour_path)
            if not pixmap1.isNull():
                size1 = self.ui.load_pages.image1_output_4.size()
                self.ui.load_pages.image1_output_4.setPixmap(pixmap1.scaled(size1, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        if os.path.exists(segmented_path):
            pixmap2 = QPixmap(segmented_path)
            if not pixmap2.isNull():
                size2 = self.ui.load_pages.image2_output_4.size()
                self.ui.load_pages.image2_output_4.setPixmap(pixmap2.scaled(size2, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        if os.path.exists(csv_path):
            def read_csv_with_encoding(csv_path):
                for enc in ['utf-8', 'cp949', 'euc-kr', 'ansi']:
                    try:
                        with open(csv_path, newline='', encoding=enc) as csvfile:
                            return list(csv.reader(csvfile))
                    except UnicodeDecodeError:
                        continue
                return []
            rows = read_csv_with_encoding(csv_path)
            if rows:
                self.ui.load_pages.exel_output_4.setRowCount(len(rows))
                self.ui.load_pages.exel_output_4.setColumnCount(max(len(row) for row in rows))
                for i, row in enumerate(rows):
                    for j, cell in enumerate(row):
                        item = QTableWidgetItem(cell)
                        self.ui.load_pages.exel_output_4.setItem(i, j, item)
                self.ui.load_pages.exel_output_4.setShowGrid(True)
                self.ui.load_pages.exel_output_4.resizeColumnsToContents()
        else:
            self.ui.load_pages.exel_output_4.clear()
            self.ui.load_pages.exel_output_4.setRowCount(0)
            self.ui.load_pages.exel_output_4.setColumnCount(0)

    def select_analysis_folder(self):
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
                "Setting Required",
                "Please perform the setting step before running the analysis."
            )
            return

        folder_path = QFileDialog.getExistingDirectory(self, "Select folder", "")
        next_btn = self.ui.load_pages.Next_button_6

        if folder_path:
            self.ui.load_pages.path_lineEdit_6.setText(folder_path)
            if not os.path.isdir(folder_path):
                QMessageBox.warning(self, "Invalid Path", "Please enter a valid folder path.")
                return

            items = os.listdir(folder_path)
            subfolders = [
                f for f in items
                if os.path.isdir(os.path.join(folder_path, f)) and f != "results"
            ]
            has_file = any(os.path.isfile(os.path.join(folder_path, f)) for f in items)

            if not subfolders:
                QMessageBox.critical(
                    self,
                    "Missing Subfolders",
                    "The selected folder must contain at least one Subfolder.\nAllowed structure: Folder > Subfolder > Image file."
                )
                return
            if has_file:
                QMessageBox.critical(
                    self,
                    "Invalid Folder Structure",
                    "Files are not allowed in the Folder.\nOnly Subfolders should be present in selected Folder.\nAllowed structure: Folder > Subfolder > Image file."
                )
                return

            for sub in subfolders:
                site_path = os.path.join(folder_path, sub)
                site_items = os.listdir(site_path)

                allowed_extensions = ('.jpg', '.jpeg', '.png', '.tif', '.tiff')

                for item in site_items:
                    full_path = os.path.join(site_path, item)
                    if os.path.isdir(full_path):
                        QMessageBox.critical(
                            self,
                            "Nested Folder Detected in Subfolder",
                            f"The Subfolder '{sub}' contains another folder.\nOnly .jpg, jpeg, png, tif, tiff image files are allowed.\nAllowed structure: Folder > Subfolder > Image file."

                        )
                        return
                    if not item.lower().endswith(allowed_extensions):
                        QMessageBox.critical(
                            self,
                            "Invalid File Type",
                            f"The site folder '{sub}' contains a file with an unsupported format.\n"
                            f"Allowed formats: {', '.join(allowed_extensions)}"
                        )
                        return
            reply = QMessageBox.question(
                self,
                "Analysis folder Confirmation",
                "Do you want to proceed with the analysis for this folder?",
                QMessageBox.Ok | QMessageBox.Cancel
            )

            if reply == QMessageBox.Ok:
                self.run_analysis_based_on_checkboxes()
                self.ui.load_pages.Next_button_6.setEnabled(True)
                self.MainFunctions.set_page(self, self.ui.load_pages.page_7)

    def run_analysis_based_on_checkboxes(self):
        experiment_path = self.ui.load_pages.path_lineEdit_6.text()
        if not os.path.isdir(experiment_path):
            QMessageBox.warning(self, "Error", "Please enter a valid folder path.")
            return

        image1_key = self.ui.load_pages.image1_button_5.isChecked()
        image2_key = self.ui.load_pages.image2_button_5.isChecked()
        csv_key = self.ui.load_pages.exel_button_5.isChecked()

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

        QMessageBox.information(self, "Complete", "The analysis is completed.")
        self.ui.load_pages.path_lineEdit_7.setText(save_path)
        self.MainFunctions.set_page(self, self.ui.load_pages.page_7)
        os.startfile(save_path)

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
        self.ui.load_pages.Next_button_2.setEnabled(False)
        self.ui.load_pages.Next_button_5.setEnabled(False)
        self.ui.load_pages.Next_button_6.setEnabled(False)

    def reset_analysis_pages(self):
        lp = self.ui.load_pages
        lp.path_lineEdit_6.clear()
        lp.path_lineEdit_6.repaint()
        lp.progressBar.setValue(0)
        lp.progressBar.repaint()
        lp.path_lineEdit_7.clear()
        lp.path_lineEdit_7.repaint()
        self.ui.load_pages.Next_button_6.setEnabled(False)

    def check_analysis_options(self):
        btn1 = self.ui.load_pages.image1_button_5.isChecked()
        btn2 = self.ui.load_pages.image2_button_5.isChecked()
        btn3 = self.ui.load_pages.exel_button_5.isChecked()
        self.ui.load_pages.Next_button_5.setEnabled(btn1 or btn2 or btn3)

    def btn_clicked(self):
        btn = self.sender()
        if btn.objectName() != "btn_settings":
            self.ui.left_menu.deselect_all_tab()
        if btn.objectName() == "btn_home":
            self.ui.left_menu.select_only_one(btn.objectName())
            self.MainFunctions.set_page(self, self.ui.load_pages.page_1)
            self.reset_test_and_analysis_pages()
        if btn.objectName() == "Test":
            self.ui.left_menu.select_only_one(btn.objectName())
            self.MainFunctions.set_page(self, self.ui.load_pages.page_2)
            self.reset_test_and_analysis_pages()
        if btn.objectName() == "Analysis":
            self.ui.left_menu.select_only_one(btn.objectName())
            self.MainFunctions.set_page(self, self.ui.load_pages.page_6)
            self.reset_analysis_pages()

    def btn_released(self):
        btn = SetupMainWindow.setup_btns(self)
        print(f"Button {btn.objectName()}, released!")

    def resizeEvent(self, event):
        SetupMainWindow.resize_grips(self)

    def mousePressEvent(self, event):
        self.dragPos = event.globalPosition().toPoint()
