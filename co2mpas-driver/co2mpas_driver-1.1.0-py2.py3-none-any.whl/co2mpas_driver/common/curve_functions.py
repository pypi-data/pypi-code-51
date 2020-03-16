from co2mpas_driver.common import vehicle_functions as vf
import numpy as np
from co2mpas_driver.common import gear_functions as fg


def gear_curves(my_car):
    """
    Calulate Full load curves of speed and torque

    :param my_car:
    :return:
    """

    full_load_speeds, full_load_torque = vf.get_load_speed_n_torque(my_car)

    '''Speed and acceleration ranges and poitns for each gear'''
    speed_per_gear, acc_per_gear = vf.get_speeds_n_accelerations_per_gear(my_car, full_load_speeds, full_load_torque)

    '''Extract speed acceleration Cubic Slpines'''
    cs_acc_per_gear = vf.get_cubic_splines_of_speed_acceleration_relationship(my_car, speed_per_gear, acc_per_gear)

    '''Start/stop speed for each gear'''
    Start, Stop = vf.get_start_stop(my_car, speed_per_gear, acc_per_gear, cs_acc_per_gear)

    sp_bins = np.arange(0, Stop[-1] + 1, 0.1)

    '''Get resistances'''
    car_res_curve, car_res_curve_force, Alimit = vf.get_resistances(my_car, sp_bins)

    '''Calculate Curves'''
    Curves = vf.calculate_curves_to_use(cs_acc_per_gear, Start, Stop, Alimit, car_res_curve, sp_bins)

    return Curves, cs_acc_per_gear, (Start, Stop)


def gear_curves_n_gs(my_car, gs_style, degree):
    """
    Calculate Full load curves of speed and torque
    Not used in the last version of MFC (for reference).

    :param my_car:
        Vehicle data base.

    :param gs_style:
        Gear shifting style.
    :type gs_style: float

    :param degree:
        Degree.
    :type degree: float

    :return:
    """
    full_load_speeds, full_load_torque = vf.get_load_speed_n_torque(my_car)

    '''Speed and acceleration ranges and poitns for each gear'''
    speed_per_gear, acc_per_gear = vf.get_speeds_n_accelerations_per_gear(my_car, full_load_speeds, full_load_torque)

    '''Extract speed acceleration Cubic Slpines'''
    cs_acc_per_gear = vf.get_cubic_splines_of_speed_acceleration_relationship(my_car, speed_per_gear, acc_per_gear)

    '''Start/stop speed for each gear'''
    Start, Stop = vf.get_start_stop(my_car, speed_per_gear, acc_per_gear, cs_acc_per_gear)

    sp_bins = np.arange(0, Stop[-1] + 1, 0.1)
    '''Get resistances'''
    car_res_curve, car_res_curve_force, Alimit = vf.get_resistances(my_car, sp_bins)

    '''Calculate Curves'''
    Curves = vf.calculate_curves_to_use(cs_acc_per_gear, Start, Stop, Alimit, car_res_curve, sp_bins)

    '''Get gs'''
    coefs_per_gear = vf.get_tan_coefs(speed_per_gear, acc_per_gear, degree)
    Tans = fg.find_list_of_tans_from_coefs(coefs_per_gear, Start, Stop)
    gs = fg.gear_points_from_tan(Tans, gs_style, Start, Stop)

    return Curves, cs_acc_per_gear, (Start, Stop), gs


def gear_curves_n_gs_from_poly(my_car, gs_style, degree):
    """
    Full load curves of speed and torque.

    :param my_car:
    :param gs_style:
    :param degree:
    :return:
    """

    full_load_speeds, full_load_torque = vf.get_load_speed_n_torque(my_car)

    '''Speed and acceleration ranges and poitns for each gear'''
    speed_per_gear, acc_per_gear = vf.get_speeds_n_accelerations_per_gear(my_car, full_load_speeds, full_load_torque)

    '''Extract speed acceleration Splines'''
    coefs_per_gear = vf.get_tan_coefs(speed_per_gear, acc_per_gear, degree)
    poly_spline = vf.get_spline_out_of_coefs(coefs_per_gear, speed_per_gear[0][0])

    '''Start/stop speed for each gear'''
    Start, Stop = vf.get_start_stop(my_car, speed_per_gear, acc_per_gear, poly_spline)

    sp_bins = np.arange(0, Stop[-1] + 1, 0.1)
    '''Get resistances'''
    car_res_curve, car_res_curve_force, Alimit = vf.get_resistances(my_car, sp_bins)

    '''Calculate Curves'''
    Curves = vf.calculate_curves_to_use(poly_spline, Start, Stop, Alimit, car_res_curve, sp_bins)

    Tans = fg.find_list_of_tans_from_coefs(coefs_per_gear, Start, Stop)
    gs = fg.gear_points_from_tan(Tans, gs_style, Start, Stop)

    return Curves, poly_spline, (Start, Stop), gs


def gear_4degree_curves_with_linear_gs(my_car, gs_style):
    """
    Full load curves of speed and torque.

    :param my_car:
    :param gs_style:
    :return:
    """
    full_load_speeds, full_load_torque = vf.get_load_speed_n_torque(my_car)

    '''Speed and acceleration ranges and poitns for each gear'''
    speed_per_gear, acc_per_gear = vf.get_speeds_n_accelerations_per_gear(my_car, full_load_speeds, full_load_torque)

    '''Extract speed acceleration Splines'''
    coefs_per_gear = vf.get_tan_coefs(speed_per_gear, acc_per_gear, 4)
    poly_spline = vf.get_spline_out_of_coefs(coefs_per_gear, speed_per_gear[0][0])

    '''Start/stop speed for each gear'''
    Start, Stop = vf.get_start_stop(my_car, speed_per_gear, acc_per_gear, poly_spline)

    sp_bins = np.arange(0, Stop[-1] + 0.1, 0.1)
    '''Get resistances'''
    car_res_curve, car_res_curve_force, Alimit = vf.get_resistances(my_car, sp_bins)

    '''Calculate Curves'''
    Curves = vf.calculate_curves_to_use(poly_spline, Start, Stop, Alimit, car_res_curve, sp_bins)

    '''Get gs'''
    gs = fg.gear_linear(speed_per_gear, gs_style)

    return Curves, poly_spline, (Start, Stop), gs


def get_ev_curve_main(my_car):
    """
    Full load curves of speed and torque.

    :param my_car:
    :return:
    """
    cs_acc_per_gear, Start, Stop = vf.ev_curve(my_car)

    # sp_bins = np.arange(0, Stop[-1] + 1, 0.01)
    sp_bins = np.arange(0, Stop[-1] + 0.1, 0.1)
    '''Get resistances'''
    car_res_curve, car_res_curve_force, Alimit = vf.get_resistances(my_car, sp_bins)

    '''Calculate Curves'''
    Curves = vf.calculate_curves_to_use(cs_acc_per_gear, Start, Stop, Alimit, car_res_curve, sp_bins)

    ppar = [0.0045, -0.1710, -1.8835]
    dec_curves = np.poly1d(ppar)
    final_dec = []
    Curves_dec = []
    for k in range(len(sp_bins)):
        final_dec.append(dec_curves(sp_bins[k]))
    from scipy.interpolate import CubicSpline, interp1d
    Curves_dec.append(interp1d(sp_bins, final_dec))

    # return Curves, (Start, Stop)
    gs = []
    return Curves, Curves_dec, (Start, Stop), gs