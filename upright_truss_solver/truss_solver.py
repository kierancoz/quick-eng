import operator
import json
import sys
sys.path.append("")
from eng_core import CoordinateSystem, Vector, Force, Moment, space_truss_solver


def import_situations(path):
    return_dict = {}
    info_dict = json.load(open(path, "r+"))
    main_coords = CoordinateSystem(info_dict.get("cog_location"))
    # all input locations are in 'inches', need to be converted to 'feet'
    main_coords.convert_units(1/12)

    # setup output forces
    output_moments = []
    for force in info_dict.get("forces"):
        location = main_coords.convert_location(force.get("location"))
        output_moments.append(Moment(location, force.get("direction")))
    return_dict.update({"output_moments" : output_moments})

    # setup load cases
    weight = info_dict.get("weight")
    for name, case in info_dict.get("contact_patch_cases").items():

        # weight definition
        weight_vec = Vector([accel*weight for accel in case.get("acceleration")])
        weight_force = Force(weight_vec.unit_vector, weight_vec.magnitude)
        print(list(weight_force))

        # contact patch definition
        contact_vec = Vector(case.get("force"))
        contact_force = Force(contact_vec.unit_vector, contact_vec.magnitude)
        contact_location = main_coords.convert_location(Vector(case.get("location")))
        print(list(contact_force))

        # get force and moment
        active_force = weight_force - contact_force
        active_moment = Moment.to_moment(weight_force, Vector([0,0,0])) - Moment.to_moment(contact_force, contact_location)

        # get location and direction of force
        return_dict.update({name : {"force" : active_force, "moment" : active_moment}})

    return return_dict

def run_situation(input_dict, output_moments):
    space_truss_solver(input_dict.get("force"), input_dict.get("moment"), output_moments)

    for force in output_moments:
        print(force.value)

def main():
    right_rear_upright = import_situations("upright_truss_solver/rear_truss.json")
    output_moments = right_rear_upright.get("output_moments")

    # braking case
    #run_situation(right_rear_upright.get("braking"), output_moments)

    # cornering case
    #run_situation(right_rear_upright.get("cornering"), output_moments)

if __name__ == "__main__":
    main()