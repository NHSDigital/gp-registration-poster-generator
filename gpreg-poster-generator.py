import qrcode
from PIL import Image
import os
import csv

# --- Temp Location ---
# Parameter structure for variable pos: pos = (img_bg.size[0] - img_qr.size[0], img_bg.size[0] - img_qr.size[0])

def gpreg_poster_generator():

    try:
    
        codeMode = input("\nType '1' for ad-hoc mode or type '2' for bulk csv import: ")
        skipAllMode = "n"

        if codeMode == '1':
            gpName = input("Enter the GP Practice Name: ")
            gpOds = input("Enter the GP Practice ODS Code: ")
            gpUrl = ('https://gp-registration.nhs.uk/' + gpOds)
            print("Generating posters and flyers for",gpOds,"please wait..")

            # Create output folder if it doesn't already exist
            if not os.path.exists('gpreg-poster-output/' + gpName + ' (' + gpOds + ')' ):
                os.makedirs('gpreg-poster-output/' + gpName + ' (' + gpOds + ')' )

            # --- Poster Grey Background ---
            img_bg = Image.open('resources/posters/0507-GP-Register-Campaign-concept_POSTER-BW-Template.png')
            qr = qrcode.QRCode(
                box_size=22,
                border=0,
                )
            qr.add_data(gpUrl)
            qr.make()
            img_qr = qr.make_image(back_color=(232, 237, 238))
            pos = (1670,2350)
            img_bg.paste(img_qr, pos)
            if os.path.exists('gpreg-poster-output/' + gpName + ' (' + gpOds + ')/' + gpName + ' (' + gpOds + ')' + ' - Register With GP - Poster BW.png'):
                if skipAllMode == "oa":
                    img_bg.save('gpreg-poster-output/' + gpName + ' (' + gpOds + ')/' + gpName + ' (' + gpOds + ')' + ' - Register With GP - Poster BW.png')
                elif skipAllMode == "sa":
                    print(gpName + ' (' + gpOds + ')' + ' - Register With GP - Poster BW.png already exists. Skipping file..')
                elif skipAllMode == "n":
                    existingFileDecision = input(gpName + ' (' + gpOds + ')' + ' - Register With GP - Poster BW.png already exists. Enter "s" to skip, "sa" to skip all, "o" to overwrite or "oa" to overwrite all: ')
                    if existingFileDecision != "s" and existingFileDecision != "sa" and existingFileDecision != "o" and existingFileDecision != "oa":
                        print (existingFileDecision)
                        existingFileDecision = input('Invalid response. Enter "s" to skip, "sa" to skip all, "o" to overwrite or "oa" to overwrite all: ')
                    elif existingFileDecision == "sa":
                        skipAllMode = existingFileDecision
                        print(gpName + ' (' + gpOds + ')' + ' - Register With GP - Poster BW.png already exists. Skipping file..')
                    elif existingFileDecision == "oa":
                        img_bg.save('gpreg-poster-output/' + gpName + ' (' + gpOds + ')/' + gpName + ' (' + gpOds + ')' + ' - Register With GP - Poster BW.png')
                        print(gpName + ' (' + gpOds + ')' + ' - Register With GP - Poster BW.png already exists. Overwriting file..')
                    elif existingFileDecision == "s":
                        print(gpName + ' (' + gpOds + ')' + ' - Register With GP - Poster BW.png already exists. Skipping file..')
                    elif existingFileDecision == "o":
                        img_bg.save('gpreg-poster-output/' + gpName + ' (' + gpOds + ')/' + gpName + ' (' + gpOds + ')' + ' - Register With GP - Poster BW.png')
            else:
                img_bg.save('gpreg-poster-output/' + gpName + ' (' + gpOds + ')/' + gpName + ' (' + gpOds + ')' + ' - Register With GP - Poster BW.png')

            # --- Poster Yellow Background ---
            img_bg = Image.open('resources/posters/0507-GP-Register-Campaign-concept_POSTER-Template.png')
            qr = qrcode.QRCode(
                box_size=22,
                border=0,
                )
            qr.add_data(gpUrl)
            qr.make()
            img_qr = qr.make_image(back_color=(239, 214, 0))
            pos = (1670,2350)
            img_bg.paste(img_qr, pos)
            img_bg.save('gpreg-poster-output/' + gpName + ' (' + gpOds + ')/' + gpName + ' (' + gpOds + ')' + ' - Register With GP - Poster.png')

            # --- Flyer Grey Background ---
            img_bg = Image.open('resources/flyers/0507-GP-Register-Campaign-concept_FLYER-A5-BW-Template.png')
            qr = qrcode.QRCode(
                box_size=13,
                border=0,
                )
            qr.add_data(gpUrl)
            qr.make()
            img_qr = qr.make_image(back_color=(232, 237, 238))
            pos = (830,1830)
            img_bg.paste(img_qr, pos)
            img_bg.save('gpreg-poster-output/' + gpName + ' (' + gpOds + ')/' + gpName + ' (' + gpOds + ')' + ' - Register With GP - Flyer A5 BW.png')

            # --- Flyer Yellow Background ---
            img_bg = Image.open('resources/flyers/0507-GP-Register-Campaign-concept_FLYER-A5-Template.png')
            qr = qrcode.QRCode(
                box_size=13,
                border=0,
                )
            qr.add_data(gpUrl)
            qr.make()
            img_qr = qr.make_image(back_color=(239, 214, 0))
            pos = (830,1830)
            img_bg.paste(img_qr, pos)
            img_bg.save('gpreg-poster-output/' + gpName + ' (' + gpOds + ')/' + gpName + ' (' + gpOds + ')' + ' - Register With GP - Flyer A5.png')

            print("Posters and Flyers for",gpOds,"successfully generated! See folder 'gpreg-poster-output/" + gpName + " (" + gpOds + ")'")

        if codeMode == '2':
            gpCsv = input("Enter the file path of the CSV file, or drag and drop the CSV file here: ")
            
            # Count the total number of csv rows for progress counter
            with open(gpCsv, mode ='r') as file:
                csvCache = csv.reader(file)
                progress_count = 0
                row_count = sum(1 for row in csvCache)

            # Begin bulk csv processing
            with open(gpCsv, mode ='r') as file:
                csvCache = csv.reader(file)

                for row in csvCache:
                    gpName = (row[0])
                    gpOds = (row[1])
                    gpUrl = ('https://gp-registration.nhs.uk/' + row[1])
                    progress_count = progress_count + 1

                    print("Generating posters and flyers for",gpOds,"please wait..","(",progress_count,"of",row_count,")")

                    #Create folder if not exist
                    if not os.path.exists('gpreg-poster-output/' + gpName + ' (' + gpOds + ')' ):
                        os.makedirs('gpreg-poster-output/' + gpName + ' (' + gpOds + ')' )

                    # --- Poster Grey Background ---
                    img_bg = Image.open('resources/posters/0507-GP-Register-Campaign-concept_POSTER-BW-Template.png')
                    qr = qrcode.QRCode(
                        box_size=22,
                        border=0,
                        )
                    qr.add_data(gpUrl)
                    qr.make()
                    img_qr = qr.make_image(back_color=(232, 237, 238))
                    pos = (1670,2350)
                    img_bg.paste(img_qr, pos)
                    img_bg.save('gpreg-poster-output/' + gpName + ' (' + gpOds + ')/' + gpName + ' (' + gpOds + ')' + ' - Register With GP - Poster BW.png')

                    # --- Poster Yellow Background ---
                    img_bg = Image.open('resources/posters/0507-GP-Register-Campaign-concept_POSTER-Template.png')
                    qr = qrcode.QRCode(
                        box_size=22,
                        border=0,
                        )
                    qr.add_data(gpUrl)
                    qr.make()
                    img_qr = qr.make_image(back_color=(239, 214, 0))
                    pos = (1670,2350)
                    img_bg.paste(img_qr, pos)
                    img_bg.save('gpreg-poster-output/' + gpName + ' (' + gpOds + ')/' + gpName + ' (' + gpOds + ')' + ' - Register With GP - Poster.png')

                    # --- Flyer Grey Background ---
                    img_bg = Image.open('resources/flyers/0507-GP-Register-Campaign-concept_FLYER-A5-BW-Template.png')
                    qr = qrcode.QRCode(
                        box_size=13,
                        border=0,
                        )
                    qr.add_data(gpUrl)
                    qr.make()
                    img_qr = qr.make_image(back_color=(232, 237, 238))
                    pos = (830,1830)
                    img_bg.paste(img_qr, pos)
                    img_bg.save('gpreg-poster-output/' + gpName + ' (' + gpOds + ')/' + gpName + ' (' + gpOds + ')' + ' - Register With GP - Flyer A5 BW.png')

                    # --- Flyer Yellow Background ---
                    img_bg = Image.open('resources/flyers/0507-GP-Register-Campaign-concept_FLYER-A5-Template.png')
                    qr = qrcode.QRCode(
                        box_size=13,
                        border=0,
                        )
                    qr.add_data(gpUrl)
                    qr.make()
                    img_qr = qr.make_image(back_color=(239, 214, 0))
                    pos = (830,1830)
                    img_bg.paste(img_qr, pos)
                    img_bg.save('gpreg-poster-output/' + gpName + ' (' + gpOds + ')/' + gpName + ' (' + gpOds + ')' + ' - Register With GP - Flyer A5.png')
            
            print("Posters and Flyers successfully generated!")
        
        # Restart Application
        gpreg_poster_generator()

    except Exception as e:
    
        print("An error occured: ",e)
        
        # Restart Application
        gpreg_poster_generator()

# Start Application
try:
    
    print(" ~ NHSE Register with a GP Surgery Service - Poster and Flyer QR Code Generation Tool v1.1 ~ ")
    gpreg_poster_generator()

except Exception as e:
    
    print("An error occured: ",e)
