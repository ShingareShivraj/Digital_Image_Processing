import numpy as np
import glob
import tifffile as tiff

def calculate_avg_ndvi(red_img_path, nir_img_path):
    # Read Red and NIR images
    red = tiff.imread(red_img_path).astype(float)
    nir = tiff.imread(nir_img_path).astype(float)

    # Avoid divide by zero
    denom = nir + red
    denom[denom == 0] = 0.01

    # NDVI calculation
    ndvi = (nir - red) / denom

    # Normalize NDVI to 0-1 range
    ndvi_normalized = (ndvi + 1) / 2

    # Average NDVI
    avg_ndvi = np.nanmean(ndvi_normalized)

    return avg_ndvi

# Path to your images
red_images = sorted(glob.glob("DJI_20231005124052_0015_MS_R.tif"))
nir_images = sorted(glob.glob("DJI_20230814123320_0001_MS_NIR.tif"))

all_avg_ndvi = []

for r, n in zip(red_images, nir_images):
    avg = calculate_avg_ndvi(r, n)
    all_avg_ndvi.append(avg)
    print(f"{r} -> Avg NDVI: {avg:.3f}")

# Final city average
final_avg = np.mean(all_avg_ndvi)
print("Final Average NDVI for City:", round(final_avg, 3))
