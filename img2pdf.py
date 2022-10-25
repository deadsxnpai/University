from PIL import Image 
import os
import re

def main():
    a = (i for i in os.listdir('/home/deadsxnpai/Downloads/images/') if i.endswith(".jpg"))
    imgs = list(a)
    imgs.sort(key=lambda f: int(re.sub('\D', '', f)))
    print(imgs)
    images = [Image.open("//home/deadsxnpai/Downloads/images/" + f) for f in imgs]
    pdf_path = "kursovaya.pdf"
    images[0].save(pdf_path, "PDF" ,resolution=100.0, save_all=True, append_images=images[1:])

if __name__ == '__main__':
    main()