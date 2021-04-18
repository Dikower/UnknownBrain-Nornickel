import os
import subprocess

#print(os.listdir('D:/Programming/Hackathones/Nornickel/experiments/great_data'))
l = os.listdir('D:/Programming/Hackathones/Nornickel/backend/data')

d = []
for name in l[1:]:
    infile = name[:-4]
    # outfile = name[:-2] + 'mp4'
    d.append(infile)
    # subprocess.run(['ffmpeg', '-i', infile, outfile])
print(d)
