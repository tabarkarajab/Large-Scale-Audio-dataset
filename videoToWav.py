#!/usr/bin/env python
import os
import logging
import traceback
import shlex, subprocess
if __name__ == '__main__':
    outputdir = os.path.abspath("/home/ncbc/Desktop/WorkSpace_NCBC/Siren/Other testing/zu_road")
    outputdir2 = os.path.abspath("/home/ncbc/Desktop/WorkSpace_NCBC/Siren/Other testing/zu_road")
    for root, dirs, files in os.walk(outputdir):
        for f in files:
            path = os.path.join(root, f)
            base, ext = os.path.splitext(f)
            outputpath = os.path.join(outputdir2, base + ".wav")
            if ext == '.mp4':
                print('converting %s to %s' % (path, outputpath))
                status, output = subprocess.getstatusoutput('ffmpeg -i "%s" "%s"' % (path, outputpath))
                if status:
                    logging.error (output)
'''
import moviepy.editor as mp
my_clip = mp.VideoFileClip(r"videotest.mov")
my_clip.audio.write_audiofile(r"my_result.mp3")'''