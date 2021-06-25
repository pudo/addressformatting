import pystache
import functools


renderer = pystache.Renderer()


@functools.lru_cache(maxsize=None)
def compile(text):
    return pystache.parse(text)


def render(template, context):
    return renderer.render(compile(template), context)


def first(address):
    def _first(content):
        tokens = [token.strip() for token in content.split("||")]
        for t in tokens:
            result = render(t, address)
            if result.strip() != "":
                return result
        return ""

    return _first


def clean_address(full):
    # TODO: there's probably a higher-performance way of doing this via
    # a regex or something.
    prev = None
    while prev != full:
        prev = full
        full = full.replace(" ,", ",")
        full = full.replace(",,", ",")
        full = full.strip(",")
        full = full.strip()
    return full
