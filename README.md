# Image Processing Application

This is a Python application designed to process PNG images based on user-defined parameters. The application provides a menu for selecting various image processing options and includes functionality to check the resolution of images before processing.

## Features

- Process PNG images for different social media platforms (e.g., Twitter, Instagram).
- Check the resolution of images and prompt for confirmation if the resolution is low.
- User-friendly menu for selecting processing tasks.

## Project Structure

```
image-processing-app
├── src
│   ├── main.py            # Entry point of the application
│   ├── image_processor.py  # Contains the ImageProcessor class for image processing
│   ├── menu.py            # Displays the menu for user options
│   └── utils
│       └── resolution_checker.py  # Checks image resolution
├── requirements.txt       # Lists project dependencies
└── README.md              # Project documentation
```

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

To run the application, execute the following command in your terminal:
```
python src/main.py
```

If no parameters are provided, the application will prompt you for input.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.