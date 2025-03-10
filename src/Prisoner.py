class Prisoner:
    """
    Prisoner superclass for the iterated Prisoner's Dilemma.
    """

    def __init__(self):
        pass

    def play(self, history):
        """
        Play: return 0 to cooperate, return 1 to defect.
        Default: Always cooperate.
        """
        return 0

    def process_results(self, my_strategy, other_strategy):
        """
        Process the results of a round. Can be overridden by subclasses.
        """
        pass  # Default behavior does nothing
