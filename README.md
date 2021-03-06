# Image Recognition and Classification
## Idea : Using Segmentation Technology for Digital image classification and recognition by Machine Learning.

### In Agriculture,

1. Automatic Pest Counting System Using Image Processing Technique
2. Color image segmentation method based on statistical pattern recognition for plant disease diagnose
3. Fruit or any agriproduct automatic sorting. 
4. Detection of Stress in the products using X ray quarantine inspection on selective fruits or yield
5. Maize Leaf Disease Identifying System Based Image Recognition.

The image processing can be used in agricultural
applications for following purposes:
1. To detect diseased leaf, stem, fruit
2. To quantify affected area by disease.
3. To find shape of affected area.
4. To determine color of affected area
5. To determine size & shape of fruits.
Etc

### In Tourism ,
If a stranger visits jaipur and certain places of jaipur he/she might not know by Using image recognition by Google Cloud Vision API It can be used for landmark detection.
We can make an android based mobile application that can be used as a guide by the tourists. The main function of this application is to recognize a monument or a famous spot from the picture clicked/uploaded by the user and to provide detailed information regarding it. This is achieved by using open-cv for image recognition. It then displays the information that is associated with that monument. The information is available in the JSON database. It will also be able to point the location of that monument on the map.

## Technical Aspects

This project uses a multithreaded approach to create a low latency real-time objection detection app. Built using Tensorflow's Object Detection API and OpenCV.

1. TensorFlow 1.6.0
2. OpenCV
3. Python 3.5.x
4. Pre-Trained Data Set

## Outputs

##### For Real Time Object Detection
```
python Application.py
```
![](images/1.png)
##### For Image Recognition from picture
```
python img_recg.py --image images\pal.jpg --prototxt bvlc_googlenet.prototxt --model bvlc_googlenet.caffemodel --labels synset_words.txt
```
![](images/2.png)
> Extended version of this can be used in Agriculture ie to prevent plant diseases by using segmentation technology analysing the visual symtomps of a plant.This is just a prototype of Real Time Object Detection using pre trained datasets (90 Classes) to demonstrate the technology.

### Links

> Research Papers on Image processing in Agriculture
https://www.ijsr.net/archive/v5i1/NOV152634.pdf

> Implementation of Deep Learning and Image processing by Japan Farmer's son for Cucumber Sorting
https://cloud.google.com/blog/big-data/2016/08/how-a-japanese-cucumber-farmer-is-using-deep-learning-and-tensorflow

### Demo Video Link

> YouTube Link https://www.youtube.com/watch?v=Bjfo80fbUCY
###### USE SUBTITLES FOR EXPLAINATION


