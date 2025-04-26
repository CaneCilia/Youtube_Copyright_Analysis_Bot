from moviepy.editor import TextClip

def generate_report_video(text="No Match Found"):
    clip = TextClip(text, fontsize=40, color='white', size=(640, 360)).set_duration(5)
    clip.write_videofile("report.mp4", fps=24)
