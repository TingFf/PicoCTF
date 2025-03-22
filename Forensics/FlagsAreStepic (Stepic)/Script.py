import stepic
from PIL import Image

# Open the stego image
img = Image.open("upz.png")

# Decode the message
message = stepic.decode(img)

print("Hidden message:", message)
