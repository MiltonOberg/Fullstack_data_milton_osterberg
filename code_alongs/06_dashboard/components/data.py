import pandas as pd
from components.constants import SUMMER_GAMES_PATH

class SummerGames:
    def __init__(self) -> None:
        self.df= pd.read_csv(SUMMER_GAMES_PATH, index_col= 0)


class Medals_summer(SummerGames):
    def __init__(self) -> None:
        super().__init__()
        self.df= self.df[self.df["Medal"].notna()]
        
    @property
    def data(self):
        return self.df


class Medals_per_county:
    def __init__(self) -> None:
        self.df_summer_medals= Medals_summer().data
    
    @property
    def summer_noc(self):
        medals_per_country= (self.df_summer_medals.groupby("NOC")["Medal"]
        .count()
        .sort_values(ascending= False)
        )
        return medals_per_country
    
    @property
    def summer_medals_type(self):
        return self.df_summer_medals.groupby(["NOC", "Medal"]).size().unstack(fill_value= 0)


class Swedish_summer_medals:
    def __init__(self) -> None:
        self.df_swe= Medals_summer().data.query("NOC=='SWE'") 
    
    @property
    def per_athlete(self):
        return self.df_swe.groupby("Name")["Medal"].count().sort_values(ascending= False)
    
    @property
    def per_sport(self):
        return self.df_swe.groupby("Sport")["Medal"].count().sort_values(ascending= False)
        
        
        
        
    
class Countries():
    def __init__(self) -> None:
        self.df= SummerGames().df
    
    @property
    def noc(self):
        return self.df["NOC"].unique()
    
    