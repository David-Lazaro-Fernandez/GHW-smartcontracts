# Store Value - Example for illustrative purposes only.

import smartpy as sp


@sp.module
def main():
    class VotingContract(sp.Contract):
        def __init__(self, options):
           
            self.data.options = options

        @sp.entrypoint
        def vote(self, option):
            self.data.options[option] +=1
if "templates" not in __name__:

    @sp.add_test(name="StoreValue")
    def test():
        options = ['A','B','C']
        options_map = sp.map({option:0 for option in options})
        print(options_map)
        c1 = main.VotingContract(options_map)
        scenario = sp.test_scenario(main)
        scenario.h1("Options Test")
        scenario += c1
        c1.vote('A')
