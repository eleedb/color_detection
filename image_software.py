from PIL import Image
import numpy as np

def detect_color_range(image_path, lower_bound, upper_bound):
    # Read image and convert to RGB
    img = Image.open(image_path).convert('RGB')  # Convert to RGB
    arr = np.array(img)
    
    # Create mask where pixels are within bounds for all channels
    mask = np.logical_and.reduce([
        arr[:,:,0] >= lower_bound[0],  # Red channel lower bound
        arr[:,:,0] <= upper_bound[0],  # Red channel upper bound
        arr[:,:,1] >= lower_bound[1],  # Green channel lower bound
        arr[:,:,1] <= upper_bound[1],  # Green channel upper bound
        arr[:,:,2] >= lower_bound[2],  # Blue channel lower bound
        arr[:,:,2] <= upper_bound[2]   # Blue channel upper bound
    ])
    
    return mask

# Example usage:
# Let's detect reddish pixels
lower = (199, 0, 57)      # Minimum RGB values
upper = (255, 192, 203)  # Maximum RGB values

mask = detect_color_range('rachuela.jpg', lower, upper)

# Create a new image showing only the detected pixels
img = Image.open('rachuela.jpg').convert('RGB')  # Convert to RGB
arr = np.array(img)

# Set pixels outside the range to black
arr[~mask] = [0, 0, 0]

# Save result
result = Image.fromarray(arr)
result.save('detected_colors.jpg')
