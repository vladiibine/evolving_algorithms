from primitive import Solver, DefFunc, DefObj

__author__ = 'shefuto'


def generate_candidate(func_template):
    initial = Solver()
    function = func_template()
    print function
    function(initial)


def deprecated_template_exec():
    """
    """
    apply = None
    try:
        exec """
def apply(solver, *args):
    defnode = DefNode(solver)
    deffunc = DefFunc(solver)


    pass
            """
    except SyntaxError:
        pass
    return apply


def evolve(candidate, problem, solution):
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
        candidate = generate_candidate(deprecated_template_exec)
        solver = evolve(candidate, problem, solution)
        solvers.append(solver)

    return solvers


generate_candidate(deprecated_template_exec)