from PIL import Image, ImageFilter

img = Image.open('./imagefiles/pikachu.jpg')

print(img.format, img.size, img.mode)

# filter the image using different filter supported in ImageFilter
filtered_img = img.filter(ImageFilter.BLUR)
filtered_img.save('./imagefiles/blur.png', 'png')

# convert the image using gray scale 
filtered_img = img.convert('L')
filtered_img.save('./imagefiles/bw.png', 'png')


# rotate the image
rotated_img = filtered_img.rotate(90)
rotated_img.save('./imagefiles/rotated.png', 'png')

# resize the image
resize_img = filtered_img.resize(tuple([int(a*0.5) for a in img.size]))
resize_img.save('./imagefiles/resize.png', 'png')

# crop the image
box = (0, 0, 200, 200)
crop_img = filtered_img.crop(box)
crop_img.save('./imagefiles/crop.png', 'png')

# crop_img.show()

# create a thumbnail
img.thumbnail((100,100)) #max size the thumbnail will become.  The thumbnail function will try the best to preserve image aspect ratio.
img.save('./imagefiles/thumbnail.png', 'png')
print(img.size)

img.close()