# coding: utf-8

import os
import glob


def path_file(path_find=None, **kwargs):
    path = os.path.abspath(os.getcwd())
    path_file_ini = kwargs.get("path_file_ini")
    path_find = path_find

    if path_file_ini:
        if glob.glob(path + path_file_ini):
            return path + path_file_ini
        raise Exception("Arquivo não encontrado no caminho especificado.\n"
                        "Caminho especificado: {}".format(path + path_file_ini))

    if path_find:
        if glob.glob(path + path_find):
            return path + path_find
    else:
        return path
