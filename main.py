from vehicle import Vehicle
from truck import Truck


silverado = Truck('Chevy', 'Silverado', 2020, 'Long Bed')

silverado.drive_vehicle(400)

silverado.engine.change_intake('Supercharger')

silverado.change_tires("Winter", 230, 60, 100)

silverado.load_bed()

silverado.drive_vehicle(1500)

silverado.fill_gas()

silverado.drive_vehicle(200)
