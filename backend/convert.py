import subprocess

infile = '../experiments/data/F1_1_1_1.ts'
outfile = 'video.mp4'

subprocess.run(['ffmpeg', '-i', infile, outfile])
