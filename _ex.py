import requests


if __name__ == '__main__':
    v = dict(name="Nick", status="healthy", last_pos="uni", pos="uni")
    print(v.get("surname", 'no-name'))
    print(v['name'])
