
# DetectChars.py


# DetectChars.py

import easyocr
reader = easyocr.Reader(['en'])

def detectCharsInPlates(listOfPossiblePlates):
    for plate in listOfPossiblePlates:
        if plate.imgPlate is None:
            continue

        h, w = plate.imgPlate.shape[:2]
        # Crop out the top 20% to avoid stickers or state text
        cropped_main_zone = plate.imgPlate[int(h * 0.2):, :]

        results = reader.readtext(cropped_main_zone)

        if results:
            # Select the longest result assuming it's the plate number
            plate.strChars = max(results, key=lambda r: len(r[1]))[1]

    return listOfPossiblePlates


