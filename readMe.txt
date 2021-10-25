In the haarcascades folder one can find the casscades used by Artifact2.py.

In the Test Images folder one can find a number of Test Images that Artifact2.py can be tested on.

To run Artifact2.py make sure the following are installed:
python >= 3.9
opencv-python >= 4.4.0.46

Artifact2.py takes the following parameters:
argv[0] = input
	where: if input is equal to 0 --> A webcam will be used as input
		else input should be a path to an image
NB: Regarding the webcam, no validation is done to ensure a webcam is connected.
    Please ensure that a working webcam is plugged in before making use of the webcam feature.
               