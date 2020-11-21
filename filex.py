import configparser

config = configparser.ConfigParser()
config.read('extensions.ini')

def filex(filename):
    dconfig = config['default']
    file_ext_type = {}
    finddot = filename.split(".")
    file_ext = finddot[len(finddot) - 1]
    file_ext_type['filename'] = filename
    file_ext_type['ext'] = file_ext
    file_ext_type['description'] = dconfig[file_ext]
    return file_ext_type


if __name__ == '__main__':
    print(filex('sample.txt.cs.java.py'))