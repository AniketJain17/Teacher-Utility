# Teacher Utility 
## Brief:

This model utilizes MediaPipe's hand tracking functions to get hand landmarks(reference points) that enable the user to actually draw stuff on the screen. 

- Libraries used: OpenCV, MediaPipe, os, numpy, time
- handtrackingmodule.py is actually a class with functions like hand-landmark detector, fingers-up check and much more. We have used an instance(detector) from this class in our main program.
- Index finger tip's landmark is used to draw on the canvas.

**The steps and tacks have been explicitly mentioned in the comments of the code.**


