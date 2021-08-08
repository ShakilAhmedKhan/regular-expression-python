import re
import os
import requests
import sys
import io

def create_directory(name):
    print("Creating directory", name)
    try:
        os.mkdir(name)
    except FileExistsError:
        print(name, "already Exists")

def get_directory_name(regexp,url):
    folderNameTauple = re.findall(regexp, url)
    dir_name = "_".join(folderNameTauple[0])
    return dir_name

def downloadImage(Image_url, file_name):
    print("Downloading Image", Image_url)
    r = requests.get(Image_url)

    with open( file_name, "wb") as f:
        f.write(r.content)


def process():
    #Creating home dirrectory
    main_dir = "dimik_pub"
    create_directory(main_dir)

    url = "http://dimik.pub/"
    response = requests.get(url)

    if response.ok is False:
        sys.exit("Could not get response from server")

    page_content = response.text

    regexp = re.compile(r'<div class="book-cover">\s*<a href="(.*?)">\s*<img src="(.*?)">.*?<h2 class="sd-title">\s*<.*?>(.*?)<', re.S)

    result = regexp.findall(page_content)

    dir_regexp = re.compile(r'book/(\d+)/(\w+)-(\w+)-')

    for item in result:
        name = item[2]
        url = item[0]
        image_url = item[1]

        dir_name = main_dir + "/" + get_directory_name(dir_regexp,url)
        create_directory(dir_name)

        file_name = dir_name + "/" + "info.txt"
        
        with open(file_name, "w", encoding="utf-8") as fp:
            fp.write(name + "\n")
            fp.write(url)

        img_file_name = dir_name + "/" + "image.png"
        downloadImage(image_url, img_file_name)

 
if __name__ == "__main__":
    process()