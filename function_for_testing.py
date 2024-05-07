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
        standardized_country_name = self.standardize_country_name(country)
        for entry in self.data:
            if entry["country"] == standardized_country_name:
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

    def get_population_difference(self, country_a: str, country_b: str) -> int:
        """
        Given two country names, return the difference in population
        between the two countries.
        """
        population_a = self.get_population(country_a)
        population_b = self.get_population(country_b)
        if population_a is None or population_b is None:
            raise ValueError("One or both countries not found.")
        return abs(population_a - population_b)
