from PIL import Image

#открываем изображение
image = Image.open('test_file.jpeg')

#приводим изображение к цветовой модели RGB
if image.mode != "RGB":
    image = image.convert("RGB")

#выделяем три канала
red, green, blue = image.split()

#смещение картинки
displacement = 200

#создание красного канала
coordinates = (displacement, 0, red.width, red.height)
left_red = red.crop(coordinates)
coordinates = (displacement//2, 0, red.width-displacement//2, red.height)
middle_red = red.crop(coordinates)
blended_red = Image.blend(left_red, middle_red, 0.5)

#создание синего канала
coordinates = (0, 0, blue.width-displacement, blue.height)
right_blue = blue.crop(coordinates)
coordinates = (displacement//2, 0, blue.width-displacement//2, blue.height)
middle_blue = blue.crop(coordinates)
blended_blue = Image.blend(right_blue, middle_blue, 0.5)

#создание зеленого канала
coordinates = (displacement//2, 0, green.width-displacement//2, green.height)
croped_green = green.crop(coordinates)

#объединение каналов в итоговое изображение
blended_image = Image.merge("RGB", (blended_red, blended_blue, croped_green))
blended_image.save("blended_image.jpeg")

#уменьшенная версия картинки
blended_image.thumbnail((80, 80))
blended_image.save("thumbnailed_image.jpeg")

