# Image Processing Application

Python application designed to process PNG images based on user-defined parameters. It is tailored for social media illustrators who keep private high-resolution images behind paywalls and still want to offer a lower resolution version for the public. The application includes a CLI menu for selecting processing options and functionality to check the resolution of images before processing.

## Features

- Optimize PNG images for different social media platforms (e.g., Twitter, Instagram).
- Check the resolution of images and prompt for confirmation if the resolution is less than A3/300dpi.
- CLI menu for option selection.
- Drag-and-drop images into file for silent, background processing.

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd image-processing-app
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the application, either execute the following command in your terminal:
```
python src/main.py
```
If no parameters are provided, the application will prompt you for input.

OR

Drag and drop a PNG image file on main.py, this will generate all versions of the image.


## License

This project is licensed under the MIT License. See the LICENSE file for more details.