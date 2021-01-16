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


