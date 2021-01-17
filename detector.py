import sys, os
sys.path.append(os.path.join(os.getcwd(),'/home/daniel/htn2020/video_summarizer/darknet/python/'))

import darknet as dn

#net = dn.load_net(b"/home/daniel/htn2020/video_summarizer/darknet/cfg/yolov3.cfg", b"/home/daniel/htn2020/video_summarizer/darknet/yolov3.weights", 0)
net = dn.load_net(b"/home/daniel/htn2020/video_summarizer/darknet/cfg/yolov3.cfg", b"/home/daniel/htn2020/video_summarizer/darknet/yolov3.weights", 0)
meta = dn.load_meta(b"/home/daniel/htn2020/video_summarizer/darknet/cfg/coco.data")


def array_to_image(arr):
    arr = arr.transpose(2,0,1)
    c = arr.shape[0]
    h = arr.shape[1]
    w = arr.shape[2]
    arr = (arr/255.0).flatten()
    data = dn.c_array(dn.c_float, arr)
    im = dn.IMAGE(w,h,c,data)
    return im

def detect2(net, meta, image, thresh=.5, hier_thresh=.5, nms=.45):
    num = dn.c_int(0)
    pnum = dn.pointer(num)
    dn.predict_image(net, image)
    dets = dn.get_network_boxes(net, image.w, image.h, thresh, hier_thresh, None, 0, pnum)
    num = pnum[0]
    if (nms): dn.do_nms_obj(dets, num, meta.classes, nms);

    res = []
    for j in range(num):
        for i in range(meta.classes):
            if dets[j].prob[i] > 0:
                b = dets[j].bbox
                res.append({"name":meta.names[i], "conf":dets[j].prob[i], "box":(b.x, b.y, b.w, b.h)})
    res = sorted(res, key=lambda x: x["name"])
    #dn.free_image(im)
    dn.free_detections(dets, num)
    return res

def yolo_int(cv_img_array):
    im = array_to_image(cv_img_array)
    dn.rgbgr_image(im)
    toReturn = detect2(net, meta, im)
    return toReturn
