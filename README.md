# QR Code Generator

This project is a **web-based QR code generator** that allows users to input a link and receive a corresponding QR code. The backend is powered by **Python Flask**, while the frontend is created using **HTML** and **CSS**.

## Features

- **Link-to-QR Conversion**: Enter any valid URL and generate a QR code instantly.
- **User-Friendly Interface**: Clean and simple HTML/CSS design for ease of use.
- **Customization**: Choose QR code colors, adjust border size, and set the box size.
- **Fast and Lightweight**: Minimal dependencies for quick setup and fast processing.

## Tech Stack

- **Flask** - Web framework for building the application.
- **qrcode** - Python library for generating QR codes.
- **HTML/CSS** - Frontend design for user interaction.

## Getting Started

Follow these instructions to set up and run the QR code generator locally:

### Prerequisites

- Python 3.x
- Flask (install via `pip install flask`)
- Any web browser to view the frontend

### Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/ianjiteshan/QRCode_gen.git
    cd QRCode_gen
    ```

2. **Install dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Flask app**:

    ```bash
    python app.py
    ```

4. **Access the app**:

    Open your web browser and go to `http://127.0.0.1:5000`.

## Usage

- Open the app in your browser.
- Enter the URL you want to convert into a QR code.
- Customize the QR code's color, size, and border as per your preference.
- Click the "Generate QR" button to create and display the QR code.

## Deployed Application

You can access the deployed version of the QR Code Generator application here:

[Live QR Code Generator](https://qrcodegen-production.up.railway.app/)

Feel free to visit the link and test the functionality of the app. It allows you to generate QR codes with customizable colors, shapes, and other settings.

## Project Structure

QRCode_gen/ │ ├── app.py # Flask backend logic for QR code generation ├── requirements.txt # Python dependencies for the project ├── static/
│ └── style.css # Custom styles for the frontend │ ├── templates/
│ └── index.html # Frontend HTML template for user input │ ├── .DS_Store # macOS system file (can be ignored) └── README.md # Project documentation (this file)


## Future Enhancements

- **Downloadable QR Codes**: Allow users to download the generated QR code.
- **Customization**: Enable QR code color, shape, and size customization.
- **Error Handling**: Improve validation for URLs and edge cases.

## Contributing

Feel free to open issues or submit pull requests with improvements. All contributions are welcome!

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Make your changes and commit them (`git commit -am 'Add new feature'`).
4. Push to your branch (`git push origin feature-name`).
5. Create a new pull request.

## License

This project is open-source and available under the [MIT License](LICENSE).
