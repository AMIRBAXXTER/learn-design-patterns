import re
from abc import ABC, abstractmethod
from PIL import Image, ImageFilter, ImageEnhance
import os


def get_result_filename(directory_name, base_name, extension="jpeg"):
    os.makedirs(directory_name, exist_ok=True)

    files = [file for file in os.listdir(directory_name) if file.startswith(base_name) and
             file.endswith(f".{extension}")]

    numbers = [
        int(re.search(r'\d+', file).group())
        for file in files
        if re.search(r'\d+', file)
    ]
    print(numbers)

    next_number = max(numbers, default=0) + 1

    next_filename = f"{base_name}{next_number}.{extension}"

    return f'{directory_name}/{next_filename}'


# Component
class ImageComponent(ABC):
    @abstractmethod
    def apply_filter(self):
        pass

    @abstractmethod
    def save_image(self, output_path):
        pass


# ConcreteComponent
class BaseImage(ImageComponent):
    def __init__(self, image_path):
        self.image = Image.open(image_path)

    def apply_filter(self):
        return self.image

    def save_image(self, output_path):
        self.image.save(output_path)


# Decorator
class ImageFilterDecorator(ImageComponent):
    def __init__(self, image_component):
        self._image_component = image_component

    @abstractmethod
    def apply_filter(self):
        pass

    def save_image(self, output_path):
        self._image_component.save_image(output_path)


# ConcreteDecoratorA
class BlurFilter(ImageFilterDecorator):
    def apply_filter(self):
        base_image = self._image_component.apply_filter()
        return base_image.filter(ImageFilter.BLUR)


# ConcreteDecoratorB
class BrightnessFilter(ImageFilterDecorator):
    def __init__(self, image_component, factor):
        super().__init__(image_component)
        self.factor = factor

    def apply_filter(self):
        base_image = self._image_component.apply_filter()
        enhancer = ImageEnhance.Brightness(base_image)
        return enhancer.enhance(self.factor)


# ConcreteDecoratorC
class SharpnessFilter(ImageFilterDecorator):
    def __init__(self, image_component, factor):
        super().__init__(image_component)
        self.factor = factor

    def apply_filter(self):
        base_image = self._image_component.apply_filter()
        enhancer = ImageEnhance.Sharpness(base_image)
        return enhancer.enhance(self.factor)


# Client code
def main():
    input_image_path = "images.jpeg"
    output_image_path = get_result_filename('Images', 'image', input_image_path.split('.')[-1])

    base_image = BaseImage(input_image_path)

    blur_filter = BlurFilter(base_image)
    blurred_image = blur_filter.apply_filter()

    brightness_filter = BrightnessFilter(blur_filter, factor=1.5)
    brighter_image = brightness_filter.apply_filter()

    sharpness_filter = SharpnessFilter(brightness_filter, factor=2.0)
    sharp_image = sharpness_filter.apply_filter()

    sharp_image.save(output_image_path)
    print(f"result image saved in {output_image_path}")


if __name__ == "__main__":
    main()
