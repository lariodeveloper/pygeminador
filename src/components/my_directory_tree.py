import os
from pathlib import Path
from tkinter import PhotoImage, END, ttk, Event
from pathlib import Path


class MyDirectoryTree(ttk.Treeview):

    def __init__(self, *args, app, directory: str, ignore:list,  **kwargs):
        self.directory = directory
        self.app = app
        self.ignore = ignore
        self.objects_path = {}
        super().__init__(*args, **kwargs)

        self.tag_bind("fstag", "<<TreeviewOpen>>", self.item_opened)

        self.file_image = PhotoImage(file=os.path.join(self.app.paths.imgs, 'file.png'))
        self.folder_image = PhotoImage(file=os.path.join(self.app.paths.imgs, 'folder.png'))
        self.file_python = PhotoImage(file=os.path.join(self.app.paths.imgs, 'python.png'))
        
        self.load_tree(Path(self.directory))

    def safe_iterdir(self, path: Path) -> tuple[Path, ...] | tuple[()]:
        """
        Like `Path.iterdir()`, but do not raise on permission errors.
        """
        try:
            return tuple(path.iterdir())
        except PermissionError:
            print("You don't have permission to read", path)
            return ()
        
    def get_icon(self, path: Path, extension:str) -> PhotoImage:
        
        if path.is_dir():
            return self.folder_image
        else:
            if extension == '.py':
                return self.file_python
            else:
                return self.file_image

    def insert_item(self, name: str, path: Path, parent: str = "") -> str:
        """
        Insert a file or folder into the treeview and return the item ID.
        """
        _, extension = os.path.splitext(path)
        iid = self.insert(
            parent, END, text=name, tags=("fstag",),
            image=self.get_icon(path, extension))
        self.objects_path[iid] = path
        return iid

    def load_tree(self, path: Path, parent: str = "") -> None:
        """
        Load the contents of `path` into the treeview.
        """
        for fsobj in self.safe_iterdir(path):
            if fsobj.name not in self.ignore:
                fullpath = path / fsobj
                child = self.insert_item(fsobj.name, fullpath, parent)
                # Preload the content of each directory within `path`.
                # This is necessary to make the folder item expandable.
                if fullpath.is_dir():
                    for sub_fsobj in self.safe_iterdir(fullpath):
                        self.insert_item(sub_fsobj.name, fullpath / sub_fsobj, child)

    def load_subitems(self, iid: str) -> None:
        """
        Load the content of each folder inside the specified item
        into the treeview.
        """
        for child_iid in self.get_children(iid):
            if self.objects_path[child_iid].is_dir():
                self.load_tree(self.objects_path[child_iid],
                            parent=child_iid)

    def item_opened(self, _event: Event) -> None:
        """
        Handler invoked when a folder item is expanded.
        """
        # Get the expanded item.
        iid = self.selection()[0]
        # If it is a folder, loads its content.
        self.load_subitems(iid)

