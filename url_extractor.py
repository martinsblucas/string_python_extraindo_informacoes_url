import re


class UrlExtractor:
    def __init__(self, url):
        self._url = self._sanitize(url)
        self._validate()

    @property
    def url(self):
        return self._url

    def _sanitize(self, url):
        return url.strip().replace(" ", "") if type(url) == str else ""

    def _validate(self):
        if not self._url:
            raise ValueError("URL is empty")

        pattern = re.compile("(http(s)?://)(www.)?bytebank.com/cambio")
        match = pattern.match(self._url)
        if not match:
            raise ValueError(f"URL {self._url} is invalid")

    def get_base(self, separator_char="?"):
        index = self._url.find(separator_char)
        if index == -1:
            return self._url
        return self._url[:index]

    def get_parameters(self, separator_char="?"):
        index = self._url.find(separator_char)
        if index == -1:
            return None
        return self._url[index+1:]

    def get_base_and_parameters(self, separator_char="?"):
        return self.get_base(separator_char), self.get_parameters(separator_char)

    def get_parameter_by_name(self, parameter_name, delimiter_char="&"):
        parameters = self.get_parameters()
        if not parameters:
            return None
        
        key_index = parameters.find(parameter_name)
        if key_index == -1:
            return None
        
        value_index = key_index + len(parameter_name) + 1
        delimiter = parameters.find(delimiter_char, value_index)

        return parameters[value_index:delimiter] if delimiter != -1 else parameters[value_index:]

    def __str__(self):
        return self._url
               
    def __len__(self):
        return len(self._url)

    def __eq__(self, other):
        if hasattr(other, "url"):
            return self.url == other.url
        return False


def main():
    extractor = UrlExtractor("https://bytebank.com/cambio?source=real&target=dolar")
    extractor2 = UrlExtractor("https://bytebank.com/cambio?source=euro&target=dolar")
    source = extractor.get_parameter_by_name("source")
    target = extractor.get_parameter_by_name("target")
    print("url 1 ................................... ", extractor)
    print("url 2 ................................... ", extractor2)
    print("url 1 == url 2 .......................... ", extractor == extractor2)
    print("url 1 id ................................ ", id(extractor))
    print("url 2 id ................................ ", id(extractor2))
    print("url 1 is url 2 .......................... ", extractor is extractor2)
    print("source .................................. ", source)
    print("target .................................. ", target)
    print("tamanho da url .......................... ", len(extractor))


if __name__ == "__main__":
    main()
