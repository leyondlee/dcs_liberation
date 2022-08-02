from dcs import task
from dcs.planes import PlaneType
from dcs.weapons_data import Weapons

from game.modsupport import planemod

@planemod
class VSN_F15E_AA(PlaneType):
    id = "VSN_F15E_AA"
    flyable = True
    height = 5.63
    width = 13.05
    length = 19.43
    fuel_max = 5952
    max_speed = 2649.996
    chaff = 120
    flare = 60
    charge_total = 240
    chaff_charge_size = 1
    flare_charge_size = 2
    category = "Interceptor"  #{78EFB7A2-FD52-4b57-A6A6-3BF0E1D6555F}
    radio_frequency = 127.5

    class Pylon1:
        AIM_120B_AMRAAM___Active_Rdr_AAM = (1, Weapons.AIM_120B_AMRAAM___Active_Rdr_AAM)
        AIM_120C_5_AMRAAM___Active_Rdr_AAM = (1, Weapons.AIM_120C_5_AMRAAM___Active_Rdr_AAM)
        AIM_9M_Sidewinder_IR_AAM = (1, Weapons.AIM_9M_Sidewinder_IR_AAM)
        AIM_9P_Sidewinder_IR_AAM = (1, Weapons.AIM_9P_Sidewinder_IR_AAM)
        Smokewinder___red = (1, Weapons.Smokewinder___red)
        Smokewinder___green = (1, Weapons.Smokewinder___green)
        Smokewinder___blue = (1, Weapons.Smokewinder___blue)
        Smokewinder___white = (1, Weapons.Smokewinder___white)
        Smokewinder___yellow = (1, Weapons.Smokewinder___yellow)
        Smokewinder___orange = (1, Weapons.Smokewinder___orange)
        AIM_9X_Sidewinder_IR_AAM = (1, Weapons.AIM_9X_Sidewinder_IR_AAM)
        AN_ASQ_T50_TCTS_Pod___ACMI_Pod = (1, Weapons.AN_ASQ_T50_TCTS_Pod___ACMI_Pod)

    class Pylon2:
        Fuel_tank_610_gal = (2, Weapons.Fuel_tank_610_gal)
        LAU_115_2_LAU_127_AIM_9X = (2, Weapons.LAU_115_2_LAU_127_AIM_9X)
        LAU_115_2_LAU_127_AIM_120C = (2, Weapons.LAU_115_2_LAU_127_AIM_120C)
        LAU_115_2_LAU_127_AIM_120B = (2, Weapons.LAU_115_2_LAU_127_AIM_120B)

    class Pylon3:
        AIM_120B_AMRAAM___Active_Rdr_AAM = (3, Weapons.AIM_120B_AMRAAM___Active_Rdr_AAM)
        AIM_120C_5_AMRAAM___Active_Rdr_AAM = (3, Weapons.AIM_120C_5_AMRAAM___Active_Rdr_AAM)
        AIM_9M_Sidewinder_IR_AAM = (3, Weapons.AIM_9M_Sidewinder_IR_AAM)
        AIM_9P_Sidewinder_IR_AAM = (3, Weapons.AIM_9P_Sidewinder_IR_AAM)
        AIM_9X_Sidewinder_IR_AAM = (3, Weapons.AIM_9X_Sidewinder_IR_AAM)

    class Pylon4:
        AIM_120B_AMRAAM___Active_Rdr_AAM = (4, Weapons.AIM_120B_AMRAAM___Active_Rdr_AAM)
        AIM_120C_5_AMRAAM___Active_Rdr_AAM = (4, Weapons.AIM_120C_5_AMRAAM___Active_Rdr_AAM)
        AIM_7M_Sparrow_Semi_Active_Radar = (4, Weapons.AIM_7M_Sparrow_Semi_Active_Radar)

    class Pylon5:
        AIM_120B_AMRAAM___Active_Rdr_AAM = (5, Weapons.AIM_120B_AMRAAM___Active_Rdr_AAM)
        AIM_120C_5_AMRAAM___Active_Rdr_AAM = (5, Weapons.AIM_120C_5_AMRAAM___Active_Rdr_AAM)
        AIM_7M_Sparrow_Semi_Active_Radar = (5, Weapons.AIM_7M_Sparrow_Semi_Active_Radar)

    class Pylon6:
        Fuel_tank_610_gal = (6, Weapons.Fuel_tank_610_gal)

    class Pylon7:
        AIM_120B_AMRAAM___Active_Rdr_AAM = (7, Weapons.AIM_120B_AMRAAM___Active_Rdr_AAM)
        AIM_120C_5_AMRAAM___Active_Rdr_AAM = (7, Weapons.AIM_120C_5_AMRAAM___Active_Rdr_AAM)
        AIM_7M_Sparrow_Semi_Active_Radar = (7, Weapons.AIM_7M_Sparrow_Semi_Active_Radar)

    class Pylon8:
        AIM_120B_AMRAAM___Active_Rdr_AAM = (8, Weapons.AIM_120B_AMRAAM___Active_Rdr_AAM)
        AIM_120C_5_AMRAAM___Active_Rdr_AAM = (8, Weapons.AIM_120C_5_AMRAAM___Active_Rdr_AAM)
        AIM_7M_Sparrow_Semi_Active_Radar = (8, Weapons.AIM_7M_Sparrow_Semi_Active_Radar)

    class Pylon9:
        AIM_120B_AMRAAM___Active_Rdr_AAM = (9, Weapons.AIM_120B_AMRAAM___Active_Rdr_AAM)
        AIM_120C_5_AMRAAM___Active_Rdr_AAM = (9, Weapons.AIM_120C_5_AMRAAM___Active_Rdr_AAM)
        AIM_9M_Sidewinder_IR_AAM = (9, Weapons.AIM_9M_Sidewinder_IR_AAM)
        AIM_9P_Sidewinder_IR_AAM = (9, Weapons.AIM_9P_Sidewinder_IR_AAM)
        AIM_9X_Sidewinder_IR_AAM = (9, Weapons.AIM_9X_Sidewinder_IR_AAM)

    class Pylon10:
        Fuel_tank_610_gal = (10, Weapons.Fuel_tank_610_gal)
        LAU_115_2_LAU_127_AIM_9X = (10, Weapons.LAU_115_2_LAU_127_AIM_9X)
        LAU_115_2_LAU_127_AIM_120C = (10, Weapons.LAU_115_2_LAU_127_AIM_120C)
        LAU_115_2_LAU_127_AIM_120B = (10, Weapons.LAU_115_2_LAU_127_AIM_120B)

    class Pylon11:
        AIM_120B_AMRAAM___Active_Rdr_AAM = (11, Weapons.AIM_120B_AMRAAM___Active_Rdr_AAM)
        AIM_120C_5_AMRAAM___Active_Rdr_AAM = (11, Weapons.AIM_120C_5_AMRAAM___Active_Rdr_AAM)
        AIM_9M_Sidewinder_IR_AAM = (11, Weapons.AIM_9M_Sidewinder_IR_AAM)
        AIM_9P_Sidewinder_IR_AAM = (11, Weapons.AIM_9P_Sidewinder_IR_AAM)
        Smokewinder___red = (11, Weapons.Smokewinder___red)
        Smokewinder___green = (11, Weapons.Smokewinder___green)
        Smokewinder___blue = (11, Weapons.Smokewinder___blue)
        Smokewinder___white = (11, Weapons.Smokewinder___white)
        Smokewinder___yellow = (11, Weapons.Smokewinder___yellow)
        Smokewinder___orange = (11, Weapons.Smokewinder___orange)
        AIM_9X_Sidewinder_IR_AAM = (11, Weapons.AIM_9X_Sidewinder_IR_AAM)
        AN_ASQ_T50_TCTS_Pod___ACMI_Pod = (11, Weapons.AN_ASQ_T50_TCTS_Pod___ACMI_Pod)

    pylons = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}

    tasks = [
        task.CAP,
        task.Escort,
        task.FighterSweep,
        task.Intercept,
        task.Reconnaissance
    ]
    task_default = task.CAP
