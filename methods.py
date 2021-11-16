def main():
    url = sanitize_url("https://bytebank.com/cambio?source=real&target=dolar")
    url_base, url_parameters = get_base_and_parameters_in_url(url)
    source = get_parameter_by_name(url_parameters, "source") if url_parameters else None
    target = get_parameter_by_name(url_parameters, "target") if url_parameters else None
    print("url ..................................... ", url)
    print("url base ................................ ", url_base)
    print("url parameters .......................... ", url_parameters)
    print("source .................................. ", source)
    print("target .................................. ", target)


def sanitize_url(url):
    url = url.strip().replace(" ", "")
    if not url:
        raise ValueError("Url is empty")
    return url


def get_base_and_parameters_in_url(url, separator_char="?"):
    index = url.find(separator_char)

    if index == -1:
        return url, None

    return url[:index], url[index+1:]


def get_parameter_by_name(parameters, parameter_name, delimiter_char="&"):
    value = ""
    key_index = parameters.find(parameter_name)

    if key_index == -1:
        return None
    
    value_index = key_index + len(parameter_name) + 1
    delimiter = parameters.find(delimiter_char, value_index)

    return parameters[value_index:delimiter] if delimiter != -1 else parameters[value_index:]


if __name__ == "__main__":
    main()
