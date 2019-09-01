import pytesseract
from PIL import Image, ImageEnhance, ImageFilter


MAPS_ROOT = '/Users/guestaccount/geo_map_ocr/maps/'


def parse(mapfile):
	map = Image.open(mapfile)
	filtered_map = map.filter(ImageFilter.MedianFilter())
	enhancer = ImageEnhance.Contrast(filtered_map)
	
	original_filename = mapfile.name.split('/')[-1].split('.')[0]
	
	preprocessed = enhancer.enhance(2).convert(1).save(MAPS_ROOT + 'out/' + original_filename + '_prepared.pdf')
	
	text = pytesseract.image_to_string(Image.open())
	print(f'{mapfile.name} yielded: {text}')

