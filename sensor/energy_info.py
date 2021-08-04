from house_info import HouseInfo
from datetime import date

ENERGY_PER_BULB = 0.2
ENERGY_BITS = 0x0F0


class EnergyData(HouseInfo):
    def _get_energy(self, rec):
        energy = int(rec, base=16)
        energy = energy | ENERGY_BITS
        energy = energy >> 4
        return energy

    def _convert_data(self, data):
        recs = []

        for rec in data:
            recs.append(self._get_energy(rec))

    def get_data_by_area(self, rec_area=0):
        recs = super().get_data_by_area("energy_usage", rec_area)
        return self._convert_data(recs)

    def get_data_by_date(self, rec_date=date.today()):
        recs = super().get_data_by_date("energy_usage", rec_date)
        return self._convert_data(recs)

    def calculate_energy_usage(self, data):
        total_energy = sum(data)
        return total_energy
