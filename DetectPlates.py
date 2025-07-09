
# DetectPlates.py

import cv2
import numpy as np
import PossiblePlate
import Preprocess

def detectPlatesInScene(imgOriginalScene):
    listOfPossiblePlates = []

    imgGrayscaleScene, imgThreshScene = Preprocess.preprocess(imgOriginalScene)

    imgThreshCopy = imgThreshScene.copy()

    contours, _ = cv2.findContours(imgThreshCopy, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        possiblePlate = extractPlate(imgOriginalScene, contour)
        if possiblePlate is not None:
            listOfPossiblePlates.append(possiblePlate)

    return listOfPossiblePlates

def extractPlate(imgOriginal, contour):
    rect = cv2.minAreaRect(contour)
    (center, (width, height), angle) = rect

    if width == 0 or height == 0:
        return None

    aspectRatio = float(width) / float(height) if height > 0 else 0

    # Filter contours that have dimensions resembling a license plate
    if aspectRatio < 2 or aspectRatio > 6:
        return None
    if width < 60 or height < 20:
        return None

    rotationMatrix = cv2.getRotationMatrix2D(center, angle, 1.0)
    imgRotated = cv2.warpAffine(imgOriginal, rotationMatrix, (imgOriginal.shape[1], imgOriginal.shape[0]))
    imgCropped = cv2.getRectSubPix(imgRotated, (int(width), int(height)), center)

    possiblePlate = PossiblePlate.PossiblePlate()
    possiblePlate.imgPlate = imgCropped
    possiblePlate.rrLocationOfPlateInScene = rect

    return possiblePlate
