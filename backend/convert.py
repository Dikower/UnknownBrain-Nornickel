import subprocess

infile = '../experiments/data/F5_1_2_1.ts'
outfile = 'F5_1_2_1.mp4'

subprocess.run(['ffmpeg', '-i', infile, outfile])
