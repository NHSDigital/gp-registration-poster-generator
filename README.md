# Python script to generate posters and flyers for GP Practices using the GPREG service.

The posters and flyers contain a unique QR code that goes to the practices unique URL on the GPREG service. This allows a patient to scan the QR code on the printed material in the GP Practice, and be navigated to the registration sign up page.

The script interacts with the user and asks them for the required information.

The script supports single practice mode, or bulk csv import mode. A csv template is included in the repo.

## Setup:
pip install Pillow
pip install qrcode

## Download precompiled windows (.exe) binary
You can also download a .exe binary from the /dist folder:
https://github.com/NHSDigital/gp-registration-poster-generator/blob/main/dist/NHSE%20GPREG%20Poster%20QR%20Generator%20v1.1.zip
