#!/usr/local/bin/fish
mkdir png
for a in out/*.jpg;  convert $a png/(basename $a .jpg).png; end;
ffmpeg -pattern_type glob -framerate 60 -i ./png/\*.png -c h264 -pix_fmt yuv420p fucked.mp4
