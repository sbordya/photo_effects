from PIL import Image
import logging

logging.basicConfig(format = u'%(levelname)-8s [%(asctime)s] %(message)s', level = logging.DEBUG, filename = u'mylog.log')

image = Image.open("monro.jpg")
logging.debug( f'Ширина - {image.width}' )
logging.debug( f'Высота - {image.height}' )
logging.debug( f'Цветовая модель - {image.mode}' )

red, green, blue = image.split()
shift = 25
coordinates_1 = (2 * shift, 0, image.width, image.height)
coordinates_2 = (0, 0, image.width - 2 * shift, image.height)
coordinates_3 = (shift, 0, image.width - shift, image.height)
red_blended = Image.blend(red.crop(coordinates_1),
                          red.crop(coordinates_3),
                          0.5)
blue_blended = Image.blend(blue.crop(coordinates_2),
                          blue.crop(coordinates_3),
                          0.5)
green_cropped = green.crop(coordinates_3)

monro = Image.merge("RGB", (red_blended, green_cropped,                                        blue_blended))
#monro.thumbnail((80, 80))
monro.save("monro_effects.jpg")
