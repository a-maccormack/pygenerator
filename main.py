import os
from PIL import Image

asset_dir = './assets/'

def generate_images():
    filename = 0
    #Face doesn't change therefore it is outside for loop
    face = Image.open(asset_dir+'main/main.png')

    #Initialize asset dirs
    mouth_dir = os.listdir(asset_dir+"/mouth")
    hat_dir = os.listdir(asset_dir+"/hats")
    background_dir = os.listdir(asset_dir+"/background")


    for mouth_num in mouth_dir:
        for hat_num in hat_dir:
            for background_num in background_dir:
                #Initialize
                background = Image.open(asset_dir+f'background/{background_num}')
                hat = Image.open(asset_dir+f'hats/{hat_num}')
                mouth = Image.open(asset_dir+f'mouth/{mouth_num}')
                
                background_copy = background.copy()
    
                background_copy.paste(face, (0,0), face)
                background_copy.paste(hat, (0,0), hat)
                background_copy.paste(mouth, (0,0), mouth) 

                filename+=1

                background_copy.save(f'output/{str(filename)}.png', quality=100)
    

def main():
    generate_images()
    print('----\nAll images have been successfully generated')

if __name__ == '__main__':
    main() 
