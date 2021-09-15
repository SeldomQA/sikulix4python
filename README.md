# sikulix4python

Use SikuliX from real [Python via py4j](https://www.py4j.org) (but no need to know, how it works ;-)

![](./sikulix.mp4)

## 安装
* 下载 [sikulixapi.jar(2.0.5)](https://raiman.github.io/SikuliX1/downloads.html)
* 运行 `sikulixapi.jar`
```shell
> java -jar .\sikulixide-2.0.5.jar -p
[info] SikulixAPI: Running py4j server on port 25333
...
```
* 安装 py4j
```shell
> pip install py4j
```

## sample

show [demo](./demo.py)

* 封装方法

```python
import os
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
```


* 编写脚本

```python
import os
from time import sleep

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

```

