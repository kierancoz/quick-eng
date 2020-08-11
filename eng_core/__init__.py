import numpy
from eng_core.vector import Vector
from eng_core.force import Force
from eng_core.coordinate_system import CoordinateSystem
from eng_core.moment import Moment

### Example ###
# Sum Fx: f0 * f0.unit_vector.X + ... + f5 * f5.unit_vector.X + = acting_force.X
# Sum Fy: f0 * f0.unit_vector.Y + ... + f5 * f5.unit_vector.Y + = acting_force.Y
# Sum Fz: f0 * f0.unit_vector.Z + ... + f5 * f5.unit_vector.Z + = acting_force.Z
# acting_moment = Moment.to_moment(acting_force)
# output_moments = [Moment.to_moment(output_force) for output_force in output_forces]
# Sum Mx: f0 * m0.Mx_coeff + ... + f5 * m5.Mx_coeff = acting_moment.Mx
# Sum My: f0 * m0.My_coeff + ... + f5 * m5.My_coeff = acting_moment.My
# Sum Mz: f0 * m0.Mz_coeff + ... + f5 * m5.Mz_coeff = acting_moment.Mz
# Output = [f0, f1, f2, f3, f4, f5]
### Example ###

# Input types {Force}, {Vector} {[Force]}
def space_truss_solver(acting_force, acting_moment, output_forces):
    force_count = len(output_forces)
    a_matrix = [[] for i in range(6)]
    for force in output_forces:
        a_matrix[0].append(force.unit_vector.X)
        a_matrix[1].append(force.unit_vector.Y)
        a_matrix[2].append(force.unit_vector.Z)

        moment = Moment.to_moment(force)
        coefficients = moment.moment_coefficients
        a_matrix[3].append(coefficients.X)
        a_matrix[4].append(coefficients.Y)
        a_matrix[5].append(coefficients.Z)
    
    b_matrix = list(acting_force) + list(acting_moment)

    # make sure matrix lengths match; remove unnecessary rows
    a_matrix = [row[:force_count - 1] for row in a_matrix]
    results = matrix_solver(a_matrix[:force_count-1], b_matrix[:force_count-1])
    
    for indx, force_magnitude in enumerate(results):
        output_forces[indx].value = force_magnitude

def matrix_solver(a_matrix, b_matrix):
    return list(numpy.linalg.solve(a_matrix, b_matrix))