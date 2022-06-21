# Ascii-Art-Generator
Ascii Characters Image to Image Generator , Image to Pencil Sketch Generator and Video to Video Generator

With my code:
For a given input image, we could generate ASCII art stored under image formats in different languages (.png, .jpg, ...). In each format, there are 2 options: Black background and white characters, or vice versa
It can generate Pencil Sketch ASCII version of the Image too with both Black and White Backgrounds.
Given input video, we could generate ASCII art stored under video formats in different languages (.mp4, ...)
Video/image outputs could be in grayscale or color format.

TimeLine-
Well, till Week 3, I learned how to convert Images to ASCII colored image, then for 4 days i worked on the ASCII Pencil Sketch Generation and have added the python file for the same, then for the remaining 5 days i worked on the video to video Generation of Ascii characters and added the python file and demo video too in the repository.

In this project I have written a python script which converts a given image into one made out of ASCII characters. I have also written scripts for pencil sketch ASCII image generation and command line ASCII video generation
I had installed OpenCV and Pillow library which enable us to seamlessly work with images on python.

For Video demo Generation-
You can run the command line video by storing the video file in Input folder and editing the path in line 29 of "video2video.py" file, and the corresponding command line video would be generated. It is preffered to have a video with white background for the command line video generator for a more clear output.

The project help me learn more about OpenCV and Pillow library while also strengthening my Python on knowledge. It also increased my confidence as a programmer and most importantly it improved my patience for I spent hours debugging the code to fine minute silly mistakes.

I watched the ACM workshop videos on ASCII Art Generator. Apart from the I intensively used GeekForGeeks platform for to learn about the different library functions of Pillow and OpenCV. I also watch a few Youtube tutorials to better understand the concept behind pencil sketching of the image.

For Pencil Sketch Generator i converted the image to gray image then the gray image is inverted and then i blurred it using Gaussian Blur and then inverted the blurred image again and used the knowledge until week 2 to convert it to ascii characters and returned it as the output.

Requirements->>
python 3.6
cv2
PIL
numpy

Resources and References Used->
1)https://drive.google.com/drive/folders/1HAtoMM4L06yqbZWDG3nEtepRLPOO-i83
2)https://en.wikipedia.org/wiki/ASCII_art#Types_and_styles
3)https://alekya3.medium.com/how-images-are-stored-in-a-computer-f364d11b4e93
4)https://stackoverflow.com/questions/33544897/imagefont-io-error-cannot-open-resource
5)https://www.analyticsvidhya.com/blog/2021/03/grayscale-and-rgb-format-for-storing-images/
6)https://www.geeksforgeeks.org/opencv-overview/
