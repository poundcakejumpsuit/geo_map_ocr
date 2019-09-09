import pytesseract
from PIL import Image, ImageEnhance, ImageFilter


MAPS_ROOT = '/home/will/prs/py/geo_map_ocr/maps/'


def parse(mapfile):
	map = Image.open(mapfile).convert('L')
	filtered_map = map.filter(ImageFilter.MedianFilter())
	enhancer = ImageEnhance.Contrast(filtered_map)

	original_filename = mapfile.split('/')[-1].split('.')[0]

	preprocessed = MAPS_ROOT + 'out/' + original_filename + '_prepared.png'
	image = enhancer.enhance(2)
	image = image.convert('1')
	image.save(preprocessed)

	text = pytesseract.image_to_string(image, config='--psm 10')
	print(f'{mapfile} yielded: {text}')
