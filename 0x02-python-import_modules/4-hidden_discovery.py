#!/usr/bin/python3

if __name__ == "__main__":

    import importlib
    m_import = importlib.import_module('hidden_4')

    for i, enu in enumerate(dir(m_import)):
        if enu[0] == '_':
            continue
        print("{}".format(enu))
