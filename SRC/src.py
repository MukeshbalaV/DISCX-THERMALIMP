import sys
import cv2
import numpy as np
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QFileDialog, QProgressBar, QDialog, QSlider, QAction
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QImage

class SettingsDialog(QDialog):
    def __init__(self, parent=None):
        super(SettingsDialog, self).__init__(parent)
        self.setWindowTitle('Processing Settings')

        self.slider1 = QSlider(Qt.Horizontal)
        self.slider2 = QSlider(Qt.Horizontal)

        layout = QVBoxLayout()
        layout.addWidget(QLabel('Customize Non-uniformity Correction:'))
        layout.addWidget(self.slider1)
        layout.addWidget(QLabel('Customize Contrast Enhancement:'))
        layout.addWidget(self.slider2)

        self.setLayout(layout)

class ImageEditorDialog(QDialog):
    def __init__(self, parent=None):
        super(ImageEditorDialog, self).__init__(parent)
        self.setWindowTitle('Image Editor')

        self.brightness_slider = QSlider(Qt.Horizontal)
        self.contrast_slider = QSlider(Qt.Horizontal)
        self.save_button = QPushButton('Save Changes', self)
        self.save_button.clicked.connect(self.save_changes)

        layout = QVBoxLayout()
        layout.addWidget(QLabel('Adjust Brightness:'))
        layout.addWidget(self.brightness_slider)
        layout.addWidget(QLabel('Adjust Contrast:'))
        layout.addWidget(self.contrast_slider)
        layout.addWidget(self.save_button)

        self.setLayout(layout)

    def save_changes(self):
        
        self.parent().apply_manual_adjustments()

class ThermalImageProcessor(QWidget):
    def __init__(self):
        super().__init__()

        self.image_path = None
        self.raw_data = None
        self.processed_data = None
        self.conversion_factor = 0.1
        self.brightness = 0
        self.contrast = 1.0

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.label = QLabel('Select a thermal image:')
        layout.addWidget(self.label)

        load_button = QPushButton('Load Image', self)
        load_button.clicked.connect(self.load_image)
        layout.addWidget(load_button)

        process_button = QPushButton('Process Image', self)
        process_button.clicked.connect(self.process_image)
        layout.addWidget(process_button)

        settings_button = QPushButton('Settings', self)
        settings_button.clicked.connect(self.show_settings)
        layout.addWidget(settings_button)

        manual_edit_button = QPushButton('Manual Edit', self)
        manual_edit_button.clicked.connect(self.show_manual_edit)
        layout.addWidget(manual_edit_button)

        self.reticle_label = QLabel('Temperature:')
        layout.addWidget(self.reticle_label)

        self.progress_bar = QProgressBar(self)
        layout.addWidget(self.progress_bar)

        save_action = QAction('Save Processed Image', self)
        save_action.triggered.connect(self.save_processed_image)
        self.addAction(save_action)

        self.setLayout(layout)
        self.setGeometry(100, 100, 400, 200)
        self.setWindowTitle('Thermal Image Processor')
        self.show()

    def load_image(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_dialog = QFileDialog()
        file_dialog.setOptions(options)
        file_dialog.setNameFilter("Images (*.png *.jpg *.bmp)")
        file_dialog.setWindowTitle("Select Thermal Image")
        if file_dialog.exec_():
            self.image_path = file_dialog.selectedFiles()[0]
            self.label.setText(f'Selected image: {self.image_path}')

    def non_uniformity_correction(self, image):
        corrected_image = image * 1.2
        corrected_image[corrected_image > 255] = 255
        corrected_image = corrected_image.astype(np.uint8)
        return corrected_image

    def contrast_enhancement(self, image):
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
        enhanced_image = clahe.apply(image)
        return enhanced_image

    def process_image(self):
        if self.image_path is not None:
            
            self.reticle_label.setText('Processing image...')

            self.raw_data = cv2.imread(self.image_path, cv2.IMREAD_GRAYSCALE)

            corrected_data = self.non_uniformity_correction(self.raw_data)
            self.processed_data = self.contrast_enhancement(corrected_data)

           
            self.display_processed_image()

           
            self.progress_bar.setValue(100)
            self.reticle_label.setText('Image processed successfully')

    def display_processed_image(self):
        cv2.imshow("Original Thermal Image", cv2.applyColorMap(self.raw_data, cv2.COLORMAP_JET))
        cv2.imshow("Processed Thermal Image", cv2.applyColorMap(self.processed_data, cv2.COLORMAP_JET))

        cv2.setMouseCallback("Processed Thermal Image", self.mouse_callback)

        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def mouse_callback(self, event, x, y, flags, param):
        if event == cv2.EVENT_MOUSEMOVE:
            temperature = self.processed_data[y, x] * self.conversion_factor
            temperature_fahrenheit = (temperature * 9/5) + 32
            color_info = f'Color: {self.processed_data[y, x]}'
            height, width = self.processed_data.shape
            self.reticle_label.setText(f'Temperature: {temperature:.2f} °C | {temperature_fahrenheit:.2f} °F | {color_info} | Coordinates: ({x}, {y}) | Dimensions: {width}x{height} | Unit: Celsius')

    def show_settings(self):
        settings_dialog = SettingsDialog(self)
        settings_dialog.exec_()

    def save_processed_image(self):
        if self.processed_data is not None:
            save_path, _ = QFileDialog.getSaveFileName(self, 'Save Processed Image', '', 'Images (*.png *.jpg *.bmp)')
            if save_path:
                cv2.imwrite(save_path, self.processed_data)
                self.reticle_label.setText(f'Image saved to {save_path}')
            else:
                self.reticle_label.setText('Image not saved')

    def show_manual_edit(self):
        editor_dialog = ImageEditorDialog(self)
        editor_dialog.brightness_slider.valueChanged.connect(self.adjust_brightness)
        editor_dialog.contrast_slider.valueChanged.connect(self.adjust_contrast)
        editor_dialog.exec_()

    def adjust_brightness(self, value):
        self.brightness = value
        self.apply_manual_adjustments()

    def adjust_contrast(self, value):
        self.contrast = value / 100.0
        self.apply_manual_adjustments()

    def apply_manual_adjustments(self):
        if self.raw_data is not None:
    
            adjusted_data = self.raw_data + self.brightness
            adjusted_data = np.clip(adjusted_data, 0, 255)
            adjusted_data = (adjusted_data * self.contrast).astype(np.uint8)

            
            corrected_data = self.non_uniformity_correction(adjusted_data)
            self.processed_data = self.contrast_enhancement(corrected_data)
            self.display_processed_image()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ThermalImageProcessor()
    sys.exit(app.exec_())
