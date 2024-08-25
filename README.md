# 🔥 Thermal Image Processor

**Thermal Image Processor** is an intuitive application designed for the analysis and enhancement of thermal images. The tool provides various image processing functionalities, including non-uniformity correction, contrast enhancement, brightness, and contrast adjustment, all within an easy-to-use graphical interface.

## ✨ Features

- 📸 **Load and Display Thermal Images:** Easily load and visualize thermal images in grayscale and color-mapped formats.
- 🔧 **Non-uniformity Correction:** Automatically corrects non-uniformities in the image for more accurate temperature readings.
- 🎨 **Contrast Enhancement:** Enhance the contrast of thermal images using CLAHE (Contrast Limited Adaptive Histogram Equalization) for better visibility of details.
- 🎛️ **Manual Adjustments:** Fine-tune brightness and contrast manually using sliders, with real-time feedback.
- 🎯 **Temperature Reticle:** Hover over any point in the image to see the exact temperature (in °C and °F) and color value at that point.
- ⚙️ **Settings Customization:** Customize the non-uniformity correction and contrast enhancement algorithms to fit specific requirements.
- 💾 **Save Processed Images:** Save the enhanced thermal images for further analysis or reporting.

## 🚀 Installation

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/yourusername/thermal-image-processor.git
    cd thermal-image-processor
    ```

2. **Install Dependencies:**

    Ensure you have Python 3.x installed. Then install the required packages using pip:

    ```bash
    pip install -r requirements.txt
    ```

    If `requirements.txt` is not provided, you can manually install the necessary packages:

    ```bash
    pip install numpy opencv-python PyQt5
    ```

3. **Run the Application:**

    Execute the script to launch the Thermal Image Processor:

    ```bash
    python thermal_image_processor.py
    ```

## 🎯 Usage

- 🖼️ **Loading Images:** Click on "Load Image" to browse and select a thermal image.
- 🛠️ **Processing Images:** Once an image is loaded, click "Process Image" to apply non-uniformity correction and contrast enhancement.
- ✍️ **Manual Editing:** Adjust the brightness and contrast of the image using the "Manual Edit" option for more control over the final output.
- 💾 **Saving Images:** After processing, save the enhanced image by selecting "Save Processed Image."

## 🌟 Future Enhancements

Here are some innovative ideas to further enhance the application:

- 🚨 **Real-time Temperature Alerts:** Implement a feature that triggers alerts for specific temperature ranges, useful in critical scenarios like fire detection.
- 📂 **Batch Processing:** Add functionality to process multiple images simultaneously, saving time for users with large datasets.
- 📷 **Integration with Thermal Cameras:** Create an interface to directly import live thermal data from compatible thermal cameras.
- 🤖 **AI-based Defect Detection:** Integrate machine learning models to automatically detect and highlight anomalies or defects in thermal images.
- 💻 **Cross-platform Support:** Package the application for easy installation and usage on Windows, macOS, and Linux.

## 📚 Educational Use Only

⚠️ This code is provided strictly for educational purposes. It is intended to serve as a learning tool and should not be used for commercial purposes or in critical applications without appropriate validation and testing.

## 📜 License

[MIT License](LICENSE)

