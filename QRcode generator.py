#!/usr/bin/env python
# coding: utf-8

# In[1]:


import qrcode
from PIL import Image
from IPython.display import display
from datetime import datetime
import os


# In[2]:


def generate_qr(data, filename=None, box_size=10, border=4, fill_color="black", back_color="white"):
    """
    Generates and displays a QR code from given data.
    
    Parameters:
    - data (str): Text or URL to encode.
    - filename (str, optional): Name of the file to save the QR image.
    - box_size (int): Size of QR boxes.
    - border (int): White border size.
    - fill_color (str): Color of the QR modules.
    - back_color (str): Background color of the QR.
    """

    # Initialize QRCode object
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=box_size,
        border=border,
    )
    
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color=fill_color, back_color=back_color)

    # Generate default filename if none is provided
    if filename is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"qrcode_{timestamp}.png"
    
    # Ensure output directory exists
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)
    full_path = os.path.join(output_dir, filename)

    # Save and display
    img.save(full_path)
    print(f"✅ QR code saved as: {full_path}")
    display(img)
    
    # User input
data = input("Enter the text or URL to encode: ")
generate_qr(data)



# In[ ]:




