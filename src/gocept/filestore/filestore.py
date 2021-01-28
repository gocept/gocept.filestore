
import gocept.filestore.interfaces
import os
import os.path
import shutil
import zope.interface


@zope.interface.implementer(gocept.filestore.interfaces.IFileStore)
class FileStore(object):

    sub_dirs = ('tmp', 'new', 'cur')

    def __init__(self, path):
        self.path = path

    def prepare(self):
        if not os.path.isdir(self.path):
            os.mkdir(self.path)
        for dir in self.sub_dirs:
            dir = os.path.join(self.path, dir)
            if not os.path.exists(dir):
                os.mkdir(dir)

    def create(self, filename, mode='w'):
        path = os.path.join(self.path, 'tmp', filename)
        f = open(path, mode)
        return f

    def copy(self, filename, source, destination):
        filename = os.path.basename(filename)
        source_path = os.path.join(self.path, source, filename)
        dest_path = os.path.join(self.path, destination, filename)
        shutil.copy(source_path, dest_path)

    def move(self, filename, source, destination):
        filename = os.path.basename(filename)
        source_path = os.path.join(self.path, source, filename)
        dest_path = os.path.join(self.path, destination, filename)
        os.rename(source_path, dest_path)

    def remove(self, filename, source):
        path = os.path.join(self.path, source, filename)
        os.remove(path)

    def list(self, section):
        path = os.path.join(self.path, section)
        return [os.path.join(self.path, section, path)
                for path in os.listdir(path)]
