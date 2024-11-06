from flask import Flask, render_template, request, send_file
import qrcode
from qrcode.image.pil import PilImage  # Use the basic PilImage for color customization
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer, SquareModuleDrawer  # For module shapes
from io import BytesIO

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate_qr', methods=['POST'])
def generate_qr():
    # Getting form inputs with defaults if not provided
    data = request.form.get('website_link', 'https://www.example.com')  # Default website link
    fill_color = request.form.get('fill_color', 'black')  # Default fill color
    back_color = request.form.get('back_color', 'white')  # Default background color
    box_size = int(request.form.get('box_size', 10))  # Default box size
    border = int(request.form.get('border', 4))  # Default border size
    style = request.form.get('style', 'square')  # Default style: square

    # Debugging: Print out the inputs received from the form
    print("Website Link:", data)
    print("Fill Color:", fill_color)
    print("Background Color:", back_color)
    print("Box Size:", box_size)
    print("Border Size:", border)
    print("Style:", style)

    # Initialize QRCode object
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=box_size,
        border=border,
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Determine module drawer style based on user input
    if style == 'rounded':
        drawer = RoundedModuleDrawer()  # Use rounded modules
        print("Using RoundedModuleDrawer for rounded style.")
    else:
        drawer = SquareModuleDrawer()  # Default is square modules
        print("Using SquareModuleDrawer for square style.")

    # Generate the image with the correct colors and drawer style
    try:
        img = qr.make_image(
            fill_color=fill_color,
            back_color=back_color,
            image_factory=PilImage,
            module_drawer=drawer,  # Ensure the correct drawer is used
        )
        print("QR Code generated successfully!")
    except Exception as e:
        print("Error in generating QR code:", e)
        return "There was an error generating the QR code."

    # Save image to a BytesIO object for sending as response
    img_io = BytesIO()
    img.save(img_io, 'PNG')
    img_io.seek(0)
    return send_file(img_io, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)

