import os
from typing import Dict, Optional
import yaml

from addressformatting.util import clean_address, first, render

PACKAGE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_FILE = os.path.join(PACKAGE_DIR, "data/worldwide.yml")
TEMPLATE_FILE = os.path.abspath(TEMPLATE_FILE)


class AddressFormatter:
    def __init__(self) -> None:
        with open(TEMPLATE_FILE, "r", encoding="utf-8") as fp:
            self.model: Dict[str, Dict[str, str]] = yaml.load(
                fp, Loader=yaml.FullLoader
            )

    def _format(
        self, address: Dict[str, Optional[str]], country: Optional[str] = None
    ) -> str:
        search_key = country.upper() if country is not None else "default"
        fmt = self.model.get(search_key, None)
        if fmt is None:
            fmt = self.model.get("default", None)
            if fmt is None:
                raise RuntimeError("Missing the default address model!")

        # Some country configurations redirect to other countries but
        # change the country name in the process:
        use_country = fmt.get("use_country")
        if use_country is not None:
            country = fmt.get("change_country")
            if country is not None:
                address["country"] = country
            return self._format(address, country=use_country)

        cleaned_address: Dict[str, str] = {}
        for key, value in address.items():
            if value is not None:
                cleaned_address[key] = value

        cleaned_address["first"] = first(cleaned_address)  # type: ignore
        return render(fmt["address_template"], cleaned_address)

    def format(
        self, address: Dict[str, Optional[str]], country: Optional[str] = None
    ) -> str:
        return clean_address(self._format(address, country=country))

    def one_line(
        self, address: Dict[str, Optional[str]], country: Optional[str] = None
    ) -> str:
        line = ", ".join(self.format(address, country=country).split("\n"))
        return clean_address(line)
