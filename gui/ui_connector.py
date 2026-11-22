from PySide6.QtWidgets import QPushButton

def connect_main_window_ui(main_window):
    lp = main_window.ui.load_pages
    try: lp.path_button_2.clicked.disconnect()
    except Exception: pass
    lp.pushButton.clicked.connect(lambda: (
            main_window.ui.left_menu.select_only_one("Test"),
            main_window.MainFunctions.set_page(main_window, lp.page_2)))
    lp.path_button_2.clicked.connect(main_window.select_test_image)
    lp.A_button_3.toggled.connect(lambda checked: main_window.display_result_by_threshold(200) if checked else None)
    lp.B_button_3.toggled.connect(lambda checked: main_window.display_result_by_threshold(220) if checked else None)
    lp.C_button_3.toggled.connect(lambda checked: main_window.display_result_by_threshold(240) if checked else None)
    try: lp.path_button_6.clicked.disconnect()
    except Exception: pass
    lp.path_button_6.clicked.connect(main_window.select_analysis_folder)
    lp.image1_button_5.toggled.connect(main_window.check_analysis_options)
    lp.image2_button_5.toggled.connect(main_window.check_analysis_options)
    lp.exel_button_5.toggled.connect(main_window.check_analysis_options)
    lp.Next_button_2.clicked.connect(lambda: main_window.MainFunctions.set_page(main_window, lp.page_3))
    lp.Next_button_3.clicked.connect(lambda: main_window.MainFunctions.set_page(main_window, lp.page_4))
    lp.Next_button_4.clicked.connect(lambda: main_window.MainFunctions.set_page(main_window, lp.page_5))
    lp.Next_button_5.clicked.connect(lambda: (main_window.MainFunctions.set_page(main_window, lp.page_6),
                                              main_window.ui.left_menu.select_only_one("Analysis")))
    lp.Next_button_6.clicked.connect(lambda: main_window.MainFunctions.set_page(main_window, lp.page_7))
    lp.Home_button_7.clicked.connect(lambda: (main_window.reset_test_and_analysis_pages(),
                                              main_window.MainFunctions.set_page(main_window, lp.page_1),
                                              main_window.ui.left_menu.select_only_one("btn_home")))
    lp.Back_button_2.clicked.connect(lambda: (main_window.MainFunctions.set_page(main_window, lp.page_1),
                                              main_window.ui.left_menu.select_only_one("btn_home")))
    lp.Back_button_3.clicked.connect(lambda: main_window.MainFunctions.set_page(main_window, lp.page_2))
    lp.Back_button_4.clicked.connect(lambda: main_window.MainFunctions.set_page(main_window, lp.page_3))
    lp.Back_button_5.clicked.connect(lambda: main_window.MainFunctions.set_page(main_window, lp.page_4))
    lp.Back_button_6.clicked.connect(lambda: (main_window.MainFunctions.set_page(main_window, lp.page_5),
                                              main_window.ui.left_menu.select_only_one("Test")))
    lp.Back_button_7.clicked.connect(lambda: main_window.MainFunctions.set_page(main_window, lp.page_6))

    for btn in main_window.findChildren(QPushButton):
        btn.clicked.connect(main_window.btn_clicked)