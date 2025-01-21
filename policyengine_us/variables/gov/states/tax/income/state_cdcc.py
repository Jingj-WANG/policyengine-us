from policyengine_us.model_api import *


class state_cdcc(Variable):
    value_type = float
    entity = TaxUnit
    label = "State Child and Dependent Care Tax Credit"
    unit = USD
    definition_period = YEAR
    adds = "gov.states.household.state_cdccs"
