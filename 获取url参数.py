from urllib import parse
url = 'https://docs.python.org/3.5/search.html?q=parse&check_keywords=yes&area=default'
parseResult = parse.urlparse(url)
print(parseResult)
