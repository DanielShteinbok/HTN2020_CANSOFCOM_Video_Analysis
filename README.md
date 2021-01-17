# CANSOFCOM Video Summarizer
This is the repository primarily for:
* video analysis and object detection/tracking
via YOLOv3 and Darknet
* Retrieval of data from Dropbase

The main browser tool is located in a 
[different repo](https://github.com/pizzapineapple/HTN2021_videotracker_browserUI)

## Why Exeunt?
Exeunt is a system for tracking the entrance and exit of objects, people, vehicles,
animals and more into and out of the camera's field of view. It uses YOLOv3, one 
of the fastest classifiers out there, trained on the COCO dataset and running via
an optimized C library (Darknet). This provides the opportunity to:
* monitor a wide variety of activity, getting a "big picture" view
* respond in real time to things like a person or vehicle entering an area, without
requiring someone to continuously watch a CCTV.

We believe that, when it comes to analysis of general behaviour, it is infeasible
for any algorithm to provide an accurate description of activities, while
remaining "big picture" (i.e. monitoring things other than people). Even then,
much of our analysis of human behaviour and sentiment could not be accurately
predicted by an algorithm, and even the risk of one omission could mean that
a human has to double-check all the video anyway.

### Use Cases:
* You, as an investigator, are looking for a truck that passed through a busy
intersection some time in the last 24 hours. Will you spool through 24 hours of 
film? No, you will use Exeunt to see every truck that entered, all in an instant!
* You are tasked with ensuring that people don't trespass over a field that
is constantly in motion etc (perhaps tall grass and wind, or animals),
so use of motion detection is impossible. Exeunt can let you know the instant
a person enters the camera's field of vision.
* How many people walked along a particular path on Sunday? What is the
ratio of cars to trucks to motorcycles on a road?
* An animal eats your carrots. Was it a squirrel or a raccoon? Without
a motion detection setup, Exeunt can show you all the animals that passed 
through your garden.

Generally, our philosophy is as follows:
People are good at understanding things we see, but video records provide
an excess of information. Why not use a computer to help set up checkpoints
in the video to help people spool through, *without* pretending to be a human
and trying to make assumptions. Down with the machines! Down with SKYNET!
Be a patriotic human, use Exeunt!

## Technical Challenges:
Unfortunately, Cross-Origin Resource Sharing is a thing,
so we were unable to query Dropbase directly from the browser.
Instead, we ran a node-express server that acted as the interface
between Dropbase and the locally-hosted browser app.

Furthermore, we could not get Darknet's CUDA GPU acceleration to
work, since we did not have a working computer with an NVIDIA Graphics
Card, so it took a long time for us to run the neural network.
However, we overcame this by using a more lightweight version, YOLOv3-tiny.
