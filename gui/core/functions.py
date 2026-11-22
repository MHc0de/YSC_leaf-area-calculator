# ///////////////////////////////////////////////////////////////
#
# BY: WANDERSON M.PIMENTA
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////

# IMPORT PACKAGES AND MODULES
# ///////////////////////////////////////////////////////////////
import os
import sys

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)


# APP FUNCTIONS
# ///////////////////////////////////////////////////////////////
class Functions:

    # SET SVG ICON
    @staticmethod
    # ///////////////////////////////////////////////////////////////
    def set_svg_icon(icon_name):
        folder = resource_path("gui/images/svg_icons")
        return os.path.join(folder, icon_name)

    # SET SVG IMAGE
    @staticmethod
    # ///////////////////////////////////////////////////////////////
    def set_svg_image(icon_name):
        folder = resource_path("gui/images/svg_images")
        return os.path.join(folder, icon_name)

    # SET IMAGE
    @staticmethod
    # ///////////////////////////////////////////////////////////////
    def set_image(image_name):
        folder = resource_path("gui/images/images")
        return os.path.join(folder, image_name)