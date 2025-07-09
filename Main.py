import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

import cv2
import numpy as np
import os
import DetectChars
import DetectPlates
import PossiblePlate

SCALAR_BLACK = (0.0, 0.0, 0.0)
SCALAR_WHITE = (255.0, 255.0, 255.0)
SCALAR_YELLOW = (0.0, 255.0, 255.0)
SCALAR_GREEN = (0.0, 255.0, 0.0)
SCALAR_RED = (0.0, 0.0, 255.0)

showSteps = False

def main():
    image_folder = "LicPlateImages"  # Folder containing images
    image_files = [f for f in os.listdir(image_folder) if f.endswith((".png", ".jpg", ".jpeg"))]

    if not image_files:
        print("\nError: No images found in the folder\n")
        return

    for image_file in image_files:
        img_path = os.path.join(image_folder, image_file)
        imgOriginalScene = cv2.imread(img_path)  # Read each image

        if imgOriginalScene is None:
            print(f"\nError: Could not read {img_path}\n")
            continue

        print(f"\nProcessing: {img_path}")

        listOfPossiblePlates = DetectPlates.detectPlatesInScene(imgOriginalScene)
        listOfPossiblePlates = DetectChars.detectCharsInPlates(listOfPossiblePlates)

        if len(listOfPossiblePlates) == 0:
            print(f"No license plates detected in {image_file}")
        else:
            listOfPossiblePlates.sort(key=lambda plate: len(plate.strChars), reverse=True)

            for licPlate in listOfPossiblePlates:
                if len(licPlate.strChars) == 0:
                    continue  # Skip if no characters detected

                drawRedRectangleAroundPlate(imgOriginalScene, licPlate)
                writeLicensePlateCharsOnImage(imgOriginalScene, licPlate)

                print(f"License plate read: {licPlate.strChars}")

            cv2.imshow(f"Processed: {image_file}", imgOriginalScene)

        cv2.waitKey(0)  # Wait for keypress before processing next image

    #cv2.destroyAllWindows()

def drawRedRectangleAroundPlate(imgOriginalScene, licPlate):
    p2fRectPoints = cv2.boxPoints(licPlate.rrLocationOfPlateInScene)
    p2fRectPoints = np.intp(p2fRectPoints)

    for i in range(4):
        cv2.line(imgOriginalScene, tuple(p2fRectPoints[i]), tuple(p2fRectPoints[(i+1) % 4]), SCALAR_RED, 2)

def writeLicensePlateCharsOnImage(imgOriginalScene, licPlate):
    ( (intPlateCenterX, intPlateCenterY), (intPlateWidth, intPlateHeight), _ ) = licPlate.rrLocationOfPlateInScene

    intPlateCenterX = int(intPlateCenterX)
    intPlateCenterY = int(intPlateCenterY)

    fltFontScale = float(intPlateHeight) / 30.0
    intFontThickness = int(round(fltFontScale * 1.5))

    textSize, baseline = cv2.getTextSize(licPlate.strChars, cv2.FONT_HERSHEY_SIMPLEX, fltFontScale, intFontThickness)

    ptLowerLeftTextOriginX = int(intPlateCenterX - (textSize[0] / 2))
    ptLowerLeftTextOriginY = int(intPlateCenterY + intPlateHeight + 10)

    cv2.putText(imgOriginalScene, licPlate.strChars, (ptLowerLeftTextOriginX, ptLowerLeftTextOriginY),
                cv2.FONT_HERSHEY_SIMPLEX, fltFontScale, SCALAR_YELLOW, intFontThickness)

if __name__ == "__main__":
    main()
