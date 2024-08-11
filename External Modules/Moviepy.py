# install pygame for preview

from moviepy.editor import (
    AudioFileClip,
    VideoFileClip,
    ImageClip,
    CompositeVideoClip,
    clips_array,
    TextClip,
)


audio = AudioFileClip('assets/musica_de_fundo.mp3').subclip(50, 55)
video = VideoFileClip('assets/video_0.mp4').subclip(0, 5)
image = ImageClip('assets/david.jpg', duration=5).resize(.5)

# print(video.duration, video.size, video.fps)
# print(video.iter_frames())  # All matrix's
# print(image.img)  # Numpy array

# image.preview()

# compose = CompositeVideoClip([video, image])
# compose.audio = audio
# compose.write_videofile('test.mp4')

"""video_0 = video.resize(0.5)
video_1 = VideoFileClip('assets/video_1.mp4').subclip(0, 5).resize(.5)

compose = clips_array(  # Grid composition
    [
        [video_0, video_1],
        [video_1, video_0]
    ]
)
compose.audio = audio"""

# Need install ImageMagick https://imagemagick.org
text = TextClip('wmark', color='white', fontsize=50).set_duration(3)

compose = CompositeVideoClip([video, text]).set_audio(audio)

compose.preview()
