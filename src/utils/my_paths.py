import os


class MyPaths:
    def __init__(self, base_dir: str) -> None:
        src = os.path.join(base_dir, 'src')
        self.imgs = os.path.join(src, 'imgs')
        self.views = os.path.join(src, 'views')
        self.project_folder = ''
