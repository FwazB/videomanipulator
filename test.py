import subprocess

def apply_glitch_effect(input_video, output_video):
    # Define the ffmpeg command
    command = [
        'ffmpeg',
        '-i', input_video,
        '-vf', 'noise=alls=20:allf=t+u,eq=brightness=0.10:saturation=1.5,unsharp=5:5:1.0',
        #'-vf', 'colorbalance=rs=.3:gs=.3:bs=.3,eq=saturation=1.5,hue=h=90'
        #'-vf', 'split[a][b];[a]lutrgb=r=0:g=1:b=0[a];[b]lutrgb=r=1:g=0:b=0,crop=iw:ih:-2:0[b];[a][b]overlay',
        #'-vf', 'tblend=all_mode=difference,eq=saturation=2:contrast=1.5,hue=h=90',
        #'-vf', 'noise=alls=20:allf=t+u,eq=brightness=0.10:saturation=1.5,unsharp=5:5:1.0',
        '-c:a', 'copy',
        output_video
    ]

    # Run the command
    try:
        subprocess.run(command, check=True)
        print(f"Glitch effect applied successfully. Output saved to {output_video}")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")

# Usage
input_video_path = 'input_video.mp4'
output_video_path = 'output_video.mp4'
apply_glitch_effect(input_video_path, output_video_path)
