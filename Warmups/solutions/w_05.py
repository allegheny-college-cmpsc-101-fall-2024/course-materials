# Why does this crash?
# Try to answer before running it

# This crashes because the function is called in the last line without any arguments
# and there are no default values for the arguments. The python interpreter
# therefore has no idea what to do!

# The second to last is completely fine.
from typing import List, Tuple, Any

def compute_intersection(tuple_one: Tuple[Any,...], tuple_two: Tuple[Any,...]) -> Tuple[Any,...]:
    return ('place_holder',)

return_val_of_type = type(compute_intersection)
return_val_of_compute_intersection = compute_intersection()
