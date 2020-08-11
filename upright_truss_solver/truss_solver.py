import operator
import json
import sys
sys.path.append("")
from eng_core import CoordinateSystem, Vector, Force, Moment, space_truss_solver


def import_situation(path):
    return_dict = {}
    import os
    info_dict = json.load(open(path, "r+"))
    main_coords = CoordinateSystem(info_dict.get("cog_location"))

    # setup output forces
    output_forces = []
    for force in info_dict.get("forces"):
        location = main_coords.convert_location(Vector(force.get("location")))
        output_forces.append(Force(location, Vector(force.get("direction"))))
    return_dict.update({"output_forces" : output_forces})

    # setup load cases
    weight = info_dict.get("weight")
    for name, case in info_dict.get("contact_patch_cases").items():

        # weight definition
        weight_vec = Vector([accel*weight for accel in case.get("acceleration")])
        weight_force = Force(weight_vec, Vector([0,0,0]), weight_vec.magnitude)

        # contact patch definition
        contact_vec = Vector(case.get("force"))
        contact_location = main_coords.convert_location(Vector(case.get("location")))
        contact_force = Force(contact_vec, contact_location, contact_vec.magnitude)

        # get force and moment
        active_force = weight_force - contact_force
        active_moment = Moment.to_moment(weight_force) - Moment.to_moment(contact_force)

        # get location and direction of force
        return_dict.update({name : {"force" : active_force, "moment" : active_moment}})

    return return_dict

def main():
    right_rear_upright = import_situation("upright_truss_solver/rear_truss.json")
    output_forces = right_rear_upright.get("output_forces")

    # braking case
    braking = right_rear_upright.get("braking")
    space_truss_solver(braking.get("force"), braking.get("moment"), output_forces)

    for force in output_forces:
        print(force.value)

    # cornering case
    cornering = right_rear_upright.get("cornering")
    space_truss_solver(cornering.get("force"), braking.get("moment"), output_forces)

    for force in output_forces:
        print(force.value)

if __name__ == "__main__":
    main()