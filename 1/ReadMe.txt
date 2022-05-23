1. A function that given 2 vectors of integers finds the first repeated number

For this exercise it is not explicit which of the two vectors must be interpreted as the prioritary one,
or if one must be compared over the second just taking the first list position as the global first repeated.

For this function implementation, the first repeated elemented is interpreted as the lowest sum of both list index.
For example:
firstList = [(1), (2), 3, 4, 5]
SeconList = [6, (2), 7, 8, (1)]
(2) Sum of index = 1 + 1 = 2
(1) Sum of index = 0 + 4 = 4
(2) sum is lower than (1), then the first repeated is (2).

firstList = [(1), (2), 3, 4, 5]
SeconList = [(2), (1)]
(2) Sum of index = 1 + 0 = 1
(1) Sum of index = 0 + 1 = 1
If (1) and (2) has the same value, then, firstList first repeated is the valid one, because the exercise sentence
just says that an integer must be returned, never mentions a list of integers.



The testing strategy is based on Boundary Value Analysis (2 variable), BoundaryValueAnalysis_2Var.docx is an abstract scheme of the current
strat.

The test includes 6 different TC:
-- test_TC_BadCase_NoIntegerRepeated: Test that an exception is thrown is there is not any repetead value
-- test_TC_BadCase_NonIntegerValue: Test that throws an exception if any of these list includes a non integer value
-- test_TC_GoodCase_Minimum_Index_Bound
-- test_TC_GoodCase_Nominal_Index_Bound
-- test_TC_GoodCase_Maximum_Index_Bound
-- test_TC_GoodCase_Priority: Test the priorization of the fistList