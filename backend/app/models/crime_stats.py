from sqlalchemy import Column, Integer, String, Float
from app.db.base import Base

class DistrictCrimeStats(Base):
    __tablename__ = "district_crime_stats"

    id = Column(Integer, primary_key=True, index=True)
    district_ubigeo = Column(String(10), unique=True, index=True)
    district_name = Column(String)
    total_incidents_count = Column(Integer)
    violent_incidents_count = Column(Integer)
    weighted_crime_rate = Column(Float)

class DistrictCrimeStatsBuilder:
    def __init__(self):
        # Inicia constructor de modelo vacio
        self.stats = DistrictCrimeStats()

    def set_ubigeo(self, ubigeo: str):
        # Asigna el valor ubigeo
        self.stats.district_ubigeo = ubigeo
        return self

    def set_name(self, name: str):
        # Asigna el valor nombre
        self.stats.district_name = name
        return self

    def set_total_incidents(self, total: int):
        # Asigna valor total incidentes
        self.stats.total_incidents_count = total
        return self

    def set_violent_incidents(self, violent: int):
        # Asigna el valor incidentes violentos
        self.stats.violent_incidents_count = violent
        return self

    def set_weighted_rate(self, rate: float):
        # Asigna el valor tasa ponderada
        self.stats.weighted_crime_rate = rate
        return self

    def build(self) -> DistrictCrimeStats:
        # Retorna el objeto construido final
        return self.stats