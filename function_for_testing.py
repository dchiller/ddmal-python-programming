"""
Provides a class "PopulationSearch" that has a method to return
the population of a given country.
"""

from typing import Optional, TypedDict, List
import requests


class CountryPopulation(TypedDict):
    country: str
    population: int


class PopulationSearch:
    def __init__(self) -> None:
        self.url = "https://raw.githubusercontent.com/samayo/country-json/master/src/country-by-population.json"
        self.data: List[CountryPopulation] = requests.get(self.url, timeout=20).json()

    def get_population(self, country: str) -> Optional[int]:
        """
        Given a country name, return the population of that country.
        """
        for entry in self.data:
            if entry["country"] == country:
                return entry["population"]
        return None

    @staticmethod
    def standardize_country_name(country_name: str) -> str:
        """
        Utility function that takes a country name
        and capitalizes the first letter of each word
        and keeps the rest lowercase.
        """
        return country_name.lower().capitalize()
