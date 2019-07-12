from reporter import header

def test_reporter():
    assert True


def test_create_header():

    author1 = {
        'firstname': 'Miles',
        'lastname': 'Davis',
        'DOB': 1926
    }

    author2 = {
        'firstname': 'John',
        'lastname': 'Coltrane',
        'DOB': 1933
    }

    author3 = {
        'firstname': 'Alfred',
        'lastname': 'McCoy Tyner',
        'DOB': 1938
    }
    authors = [author1,author2,author3]
    
    header_txt = header.create_header(authors)
    assert "Alfred" in header_txt
    assert "McCoy" in header_txt