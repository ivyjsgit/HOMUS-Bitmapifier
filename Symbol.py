from Point import *
import gizeh
import os
import cv2


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
                point_1 = (current_pair[0],current_pair[1])
                point_2  = (next_pair[0],next_pair[1])
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
        if len(self.lines)%2!=0:
            self.lines.pop()
        for i in range(0,len(self.lines),2):
            print(self.lines)
            print(f"Trying {i}")
            point_1 = self.lines[i]
            point_2 = self.lines[i+1]
            points=[(int(point_1[0]),int(point_1[1])),(int(point_2[0]),int(point_2[1]))]
            line_to_draw = gizeh.polyline(points,stroke_width=3, stroke=(0,0,0), fill=(1,1,1))
            # line_to_draw = gizeh.polyline(points=[(int(line.point_1.x),int(line.point_1.y)),(int(line.point_2.x),int(line.point_2.y))],stroke_width=3, stroke=(0,0,0), fill=(1,1,1))
            line_to_draw.draw(surface)
        # cv2.imshow('image', surface.get_npimage())
        surface.write_to_png(f"{filename_to_write}.png")