import os
from time import sleep
from sikulix4python import Screen


class MyScreen:

    def __init__(self, img_dir):
        self.scr = Screen()
        self.img_dir = img_dir

    def get_image(self, img_name: str) -> str:
        img_path = os.path.join(self.img_dir, img_name)
        return img_path

    def click(self, image_name: str) -> None:
        """ click """
        img_path = self.get_image(image_name)
        print(f"click: {img_path}")
        self.scr.click(img_path)

    def type(self, image_name: str, text: str) -> None:
        """ input text """
        img_path = self.get_image(image_name)
        print(f'type "{text}": {img_path}')
        self.scr.type(img_path, text)


def main():
    """简单的测试"""
    BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)))
    IMG_DIR = os.path.join(BASE_DIR, "imgLib")
    scr = MyScreen(IMG_DIR)
    scr.click("search.png")
    scr.click("edge.png")
    scr.click("baidu.png")
    scr.type("baidu_input.png", "sikulix for python")
    scr.click("baidu_button.png")
    sleep(2)
    scr.click("close_edge.png")


if __name__ == '__main__':
    main()
