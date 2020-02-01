The topic of my project is skin detection in video. Skin detection is the
process of finding skin-colored pixels and regions in an image or a video.
When the standard RGB color space is used, skin detection can be very
difficult under conditions of variable lighting and contrast. Therefore,
the input video (frame) must be converted to another color space that is
invariant or at least insensitive to lighting changes, such as HSV. Then, I'll
manipulate the image/frame mask and try to optimize the detection and
remove noise. And finally, I will paint those specific pixels in green color.

I added to the project the possibility of getting a "radioactive zombie"
look - skin recognition and color it in radioactive green color on a
background with inverted colors while maintaining the human facial
features.

The purpose of this project was to understand the subject of image
processing and to develop my understanding of this subject. Also, the
final product of the project can be used for students who want to study
the subject of image processing regarding object detection and image
filtering as min/max/median filter.

Future work that can improve identification is to create a learning
machine that will recognize body parts and then know if it sees human
skin. With its help, we can reduce color noise and better track objects.

*This project was done as part of a course – algorithms in multimedia
and machine learning using Python.
