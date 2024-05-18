
import numpy as np
import pandas as pd
from pathlib import Path


def read_menu(menu_path: Path, na_values: str = "Nan") -> pd.DataFrame:
    my_menu = pd.DataFrame(pd.read_excel(menu_path, na_values=na_values))

    # Drop all columns that have only Nan values
    my_menu = my_menu.dropna(axis=1, how="all")

    # Drop all row that have only Nan values
    my_menu = my_menu.dropna(axis=0, how="all")

    return my_menu
