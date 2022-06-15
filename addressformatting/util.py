import chevron  # type: ignore
from typing import cast, Callable, Dict

RenderFunc = Callable[[str, Dict[str, str]], str]


def render(template: str, context: Dict[str, str]) -> str:
    return cast(str, chevron.render(template, context))


def first(address: Dict[str, str]) -> Callable[[str, RenderFunc], str]:
    def _first(content: str, render: RenderFunc) -> str:
        tokens = [token.strip() for token in content.split("||")]
        for t in tokens:
            result = render(t, address)
            if result.strip() != "":
                return result
        return ""

    return _first


def clean_address(full: str) -> str:
    # TODO: there's probably a higher-performance way of doing this via
    # a regex or something.
    prev = None
    while prev != full:
        prev = full
        full = full.replace(" ,", ",")
        full = full.replace(",,", ",")
        full = full.replace("  ", " ")
        full = full.strip(",")
        full = full.strip()
    return full
