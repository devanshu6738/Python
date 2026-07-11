with open("IMG_20260711_003409_690.jpg",'rb') as f:
    with open("copy_image.jpg",'wb') as wf:
        wf.write(f.read())