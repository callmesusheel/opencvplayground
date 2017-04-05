#!/usr/bin/env python

'''
Watershed segmentation
=========

This program demonstrates the watershed segmentation algorithm
in OpenCV: watershed().

Usage
-----
watershed.py [image filename]

Keys
----
  1-7   - switch marker color
  SPACE - update segmentation
  r     - reset
  s     - save
  ESC   - exit

'''


# Python 2/3 compatibility

import numpy as np
import cv2

class Sketcher:
    def __init__(self, windowname, dests, colors_func):
        self.prev_pt = None
        self.windowname = windowname
        self.dests = dests
        self.colors_func = colors_func
        self.dirty = False
        self.show()
        cv2.setMouseCallback(self.windowname, self.on_mouse)

    def show(self):
        cv2.imshow(self.windowname, self.dests[0])

    def on_mouse(self, event, x, y, flags, param):
        pt = (x, y)
        if event == cv2.EVENT_LBUTTONDOWN:
            self.prev_pt = pt
        elif event == cv2.EVENT_LBUTTONUP:
            self.prev_pt = None

        if self.prev_pt and flags & cv2.EVENT_FLAG_LBUTTON:
            for dst, color in zip(self.dests, self.colors_func()):
                cv2.line(dst, self.prev_pt, pt, color, 5)
            self.dirty = True
            self.pt = pt
            print("X & Y : " + `x` + " , " + `y`)
            self.prev_pt = pt
            self.show()

class App:
    def __init__(self, fn):
        self.img = cv2.imread(fn)
        if self.img is None:
            raise Exception('Failed to load image file: %s' % fn)

        h, w = self.img.shape[:2]
        self.markers = np.zeros((h, w), np.int32)
        self.markers_vis = self.img.copy()
        self.dummyImg = self.img.copy()
        self.dummyImg = cv2.cvtColor(self.dummyImg, cv2.COLOR_RGB2BGRA)
        self.cur_marker = 1
        self.colors = np.int32( list(np.ndindex(2, 2, 2)) ) * 255

        self.auto_update = False
        self.sketch = Sketcher('img', [self.markers_vis, self.markers], self.get_colors)

    def get_colors(self):
        return list(map(int, self.colors[self.cur_marker])), self.cur_marker

    def watershed(self):
        m = self.markers.copy()
        cv2.watershed(self.img, m)
        print("Self.Colors : " + `self.colors`)
        print("np.maximum(m, 0): " + `np.maximum(m, 0)`)
        overlay = self.colors[m]
        vis = cv2.addWeighted(self.img, 0.5, overlay, 0.5, 0.0, dtype=cv2.CV_8UC3)
        print("Touched area : " + `vis[self.sketch.pt[1], self.sketch.pt[0]]`)
        # print("Overlay area : " + `overlay[self.sketch.pt[1], self.sketch.pt[0]]`)
        
        print("Dummy Pixel : " + `self.dummyImg[25,25]`)
        for x in xrange(self.img.shape[0]):
            for y in xrange(self.img.shape[1]):
                if overlay[x,y][2] == 255:
                    self.dummyImg[x,y] = [0,0,0,0]
                else :
                    (b,g,r) = self.img[x,y]
                    self.dummyImg[x,y] = [b,g,r,255]

        cv2.imshow('watershed', self.dummyImg)

    def run(self):
        while cv2.getWindowProperty('img', 0) != -1 or cv2.getWindowProperty('watershed', 0) != -1:
            ch = cv2.waitKey(50)
            if ch == 27:
                break
            if ch >= ord('1') and ch <= ord('2'):
                self.cur_marker = ch - ord('0')
                print('marker: ', self.cur_marker)
            if ch == ord(' ') or (self.sketch.dirty and self.auto_update):
                self.watershed()
                self.sketch.dirty = False
            if ch in [ord('a'), ord('A')]:
                self.auto_update = not self.auto_update
                print('auto_update if', ['off', 'on'][self.auto_update])
            if ch in [ord('r'), ord('R')]:
                self.markers[:] = 0
                self.markers_vis[:] = self.img
                self.sketch.show()
            if ch in [ord('s'), ord('S')]:
                cv2.imwrite('result.png', self.dummyImg)
        cv2.destroyAllWindows()


if __name__ == '__main__':
    import sys
    try:
        fn = sys.argv[1]
    except:
        fn = '../data/fruits.jpg'
    print(__doc__)
    App(fn).run()
