from PIL import Image

image = Image.open('test_file.jpeg')

if image.mode != "RGB":
    image = image.convert("RGB")

red, green, blue = image.split()

displacement = 200

coordinates = (displacement, 0, red.width, red.height)
left_red = red.crop(coordinates)
coordinates = (displacement//2, 0, red.width-displacement//2, red.height)
middle_red = red.crop(coordinates)
blended_red = Image.blend(left_red, middle_red, 0.5)

coordinates = (0, 0, blue.width-displacement, blue.height)
right_blue = blue.crop(coordinates)
coordinates = (displacement//2, 0, blue.width-displacement//2, blue.height)
middle_blue = blue.crop(coordinates)
blended_blue = Image.blend(right_blue, middle_blue, 0.5)

coordinates = (displacement//2, 0, green.width-displacement//2, green.height)
croped_green = green.crop(coordinates)

blended_image = Image.merge("RGB", (blended_red, croped_green, blended_blue))
blended_image.save("blended_image.jpeg")

blended_image.thumbnail((80, 80))
blended_image.save("thumbnailed_image.jpeg")

