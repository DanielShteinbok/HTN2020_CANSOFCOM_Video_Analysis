# Darknet does not compile with OpenCV
* set `OPENCV=1` in the `Makefile`
* get error as if cannot find `opencv.pc` in `pkgconfig`
* `opencv4.pc` does exist in `usr/lib/pkgconfig/`, but
it seems as if the `Makefile` is looking for specifically `opencv.pc`
* for now I have abandoned the idea and am using Darknet without opencv
* applied patch I found on the internet (in this folder), and it fixed the
above issues
* opencv was missing a dependency: libhdf5

TODO:
* submit a bug for opencv pacman package, as it has a dependency
of libhdf5 that is not written in as a dependency

Since LMAO efficiency where art thou, we'll just read a VideoCapture
from OpenCV frame-by-frame, and shove each one through the YOLOv3
pretrained network. So far, I have some code (I think) in
[my fork of darknet](https://github.com/DanielShteinbok/darknet),
see in particular the modified version of `examples/detector-scipy-opencv.py`.

TODO as of now:
* write a python script to read my video file frame-by-frame from OpenCV's VideoCapture
* add some stuff to shove each thing through YOLO
	* `generate_sec_conf()` based on gaussian distribution/bounding boxes etc?
* figure out if there are new objects
* add something to make the stuff into, like, a csv format
* dump the csv-formatted stuff to console
* dump the csv-formatted stuff to *not* console (e.g. a `.csv` file??)
* parse the csv??
