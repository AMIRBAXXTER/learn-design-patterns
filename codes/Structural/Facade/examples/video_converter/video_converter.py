import os

from moviepy import VideoFileClip


# Subsystem A: MP4 Converter
class MP4Converter:
    def convert(self, input_file: str, output_file: str) -> str:
        try:
            clip = VideoFileClip(input_file)
            clip.write_videofile(output_file, codec="libx264", audio_codec="aac")
            clip.close()
            return f"Video successfully converted to MP4: {output_file}"
        except Exception as e:
            return f"Error converting to MP4: {e}"


# Subsystem B: AVI Converter
class AVIConverter:
    def convert(self, input_file: str, output_file: str) -> str:
        try:
            clip = VideoFileClip(input_file)
            clip.write_videofile(output_file, codec="mpeg4")
            clip.close()
            return f"Video successfully converted to AVI: {output_file}"
        except Exception as e:
            return f"Error converting to AVI: {e}"


# Subsystem C: MKV Converter
class MKVConverter:
    def convert(self, input_file: str, output_file: str) -> str:
        try:
            clip = VideoFileClip(input_file)
            clip.write_videofile(output_file, codec="libx264", audio_codec="aac")
            clip.close()
            return f"Video successfully converted to MKV: {output_file}"
        except Exception as e:
            return f"Error converting to MKV: {e}"


# Facade: Video Converter Interface
class VideoConverterFacade:
    def __init__(self):
        self.converters = {
            "mp4": MP4Converter(),
            "avi": AVIConverter(),
            "mkv": MKVConverter()
        }

    def convert_video(self, input_file: str, target_format: str) -> str:
        target_format = target_format.lower()
        if target_format not in self.converters:
            return f"Error: Format '{target_format}' is not supported."
        if target_format == os.path.splitext(input_file)[1][1:]:
            return f"Error: Input and output formats are the same."

        base_name, _ = os.path.splitext(input_file)
        output_file = f"{base_name}.{target_format}"

        converter = self.converters[target_format]
        return converter.convert(input_file, output_file)


# Client Code
def main():
    video_converter = VideoConverterFacade()
    input_file = "video.mp4"

    print(video_converter.convert_video(input_file, "mp4"))
    print(video_converter.convert_video(input_file, "avi"))
    print(video_converter.convert_video(input_file, "mkv"))
    print(video_converter.convert_video(input_file, "wmv"))


if __name__ == "__main__":
    main()
