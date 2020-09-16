from Line import *
from Point import *
import gizeh
import os

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
                line = Line(Point(current_pair[0],current_pair[1]), Point(next_pair[0],next_pair[1]))

                lines.append(line)

        return lines

    def draw(self,filename_to_write):
        surface = gizeh.Surface(width=300, height=300)
        for line in self.lines:
            line_to_draw = gizeh.polyline(points=[(int(line.point_1.x),int(line.point_1.y)),(int(line.point_2.x),int(line.point_2.y))],stroke_width=3, stroke=(0,0,0), fill=(1,1,1))
            line_to_draw.draw(surface)
        
        surface.write_to_png(f"{filename_to_write}.png")