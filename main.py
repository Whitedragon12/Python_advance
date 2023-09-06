import requests


def parse(query: str) -> dict:
    response = requests.get(query)
    return response.json()


if __name__ == '__main__':
    assert parse('http://127.0.0.1:5000/?name=ferret&color=purple') == {'color': 'purple', 'name': 'ferret'}
    assert parse('https://127.0.0.1:5000/?name=ferret&color=purple') == {'name': 'Anna', 'color': 'Green'}
    assert parse('http://127.0.0.1:5000/?age=29') == {'age': '29'}
    assert parse('http://127.0.0.1:5000/?gender=man') == {'gender': 'man'}
    assert parse('http://127.0.0.1:5000/?name=Dima') == {'name': 'Dima'}


def parse_cookie(query: str) -> dict:
    response = requests.get(query)
    return dict(response.cookies)


if __name__ == '__main__':
    assert parse_cookie('http://127.0.0.1:5000/?name=ferret&color=purple') == {'color': 'purple', 'name': 'ferret'}
    assert parse('https://127.0.0.1:5000/?name=ferret&color=purple') == {'name': 'Anna', 'color': 'Green'}
    assert parse('http://127.0.0.1:5000/?age=29') == {'age': '29'}
    assert parse('http://127.0.0.1:5000/?gender=man') == {'gender': 'man'}
    assert parse('http://127.0.0.1:5000/?name=Dima') == {'name': 'Dima'}
