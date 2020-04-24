"""COVID-19 simulator initialization."""

from whynot.simulators.covid19.simulator import (
    Config,
    dynamics,
    Intervention,
    simulate,
    State,
)
from whynot.simulators.covid19.experiments import COVID19RCT
from whynot.simulators.covid19.environments import *

SUPPORTS_CAUSAL_GRAPHS = True
