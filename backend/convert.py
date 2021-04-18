import subprocess

infile = '../experiments/data/F1_2_4_1.ts'
outfile = 'F1_2_4_1.mp4'

subprocess.run(['ffmpeg', '-i', infile, outfile])
