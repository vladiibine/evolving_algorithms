__author__ = 'shefuto'


def generate_candidate():
    pass


def generate_solvers(problem, solution, max=1):
    """Given a `problem` and a solution to it, generates `max` number of
        solver algorithms that will solve the problem in that particular way.

        The solver is a callable

    :param problem: the problem (any object)
    :param solution: (any object)
    :param max: max number of solving algorithms
    :return a list of solvers
    """
    solvers = []
    for counter in range(max):
        candidate = generate_candidate()
        solver = evolve(candidate, problem, solution)
        solvers.append(solver)

    pass
