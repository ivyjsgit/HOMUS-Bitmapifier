from Point import *
import gizeh
import os
import cv2
import Resizing

class Symbol:
    name = "Unnamed Symbol"
    lines = []
    filename = "unnamed"
    def __init__(self, filename):
        self.filename = os.path.basename(filename).replace(".txt", "")
        with open(filename) as f:
            self.name = f.readline().replace("\n","")
            lines = f.read().split("\n")
            self.lines = self.turn_text_into_points(lines)            
    def turn_text_into_points(self,text_lines):
        lines = []
        for line_of_text in text_lines:
            splitted_by_semicolon = line_of_text.split(";")
            splitted_by_semicolon.remove('')

            for i in range(0,len(splitted_by_semicolon)-1):
                current_pair = splitted_by_semicolon[i].split(",")
                next_pair = splitted_by_semicolon[i+1].split(",")
                point_1 = (int(current_pair[0]),int(current_pair[1]))
                point_2  = (int(next_pair[0]),int(next_pair[1]))
                lines.append(point_1)
                lines.append(point_2)
                # line = Line(Point(current_pair[0],current_pair[1]), Point(next_pair[0],next_pair[1]))

                # lines.append(line)
        # print(lines)
        return lines

    def draw(self,filename_to_write):
        surface = gizeh.Surface(width=300, height=300)
        square = gizeh.square(l=600, fill=(1,1,1), xy=(0,0))
        square.draw(surface)

        #start resizing them and stuff
        moved_to_corner = Resizing.movePointsToCorner(self.lines)
        resized = Resizing.scalePoints(moved_to_corner, 300, 10.0)
        scooted = Resizing.scootPoints(resized, 0.0)



        if len(scooted)%2!=0:
            scooted.pop()
        for i in range(0,len(scooted),2):
            point_1 = scooted[i]
            point_2 = scooted[i+1]
            points=[(int(point_1[0]),int(point_1[1])),(int(point_2[0]),int(point_2[1]))]
            line_to_draw = gizeh.polyline(points,stroke_width=3, stroke=(0,0,0), fill=(1,1,1))
            line_to_draw.draw(surface)
        surface.write_to_png(f"{filename_to_write}.png")