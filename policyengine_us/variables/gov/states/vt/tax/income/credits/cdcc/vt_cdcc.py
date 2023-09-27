from policyengine_us.model_api import *


class vt_cdcc(Variable):
    value_type = float
    entity = TaxUnit
    label = "Vermont child care and dependent care credit"
    unit = USD
    definition_period = YEAR
    reference = (
        "https://tax.vermont.gov/sites/tax/files/documents/IN-112-2022.pdf#page=2"
        "https://tax.vermont.gov/individuals/personal-income-tax/tax-credits"
    )
    defined_for = StateCode.VT

    def formula(tax_unit, period, parameters):
        p = parameters(period).gov.states.vt.tax.income.credits.cdcc
        federal_cdcc = tax_unit("cdcc", period)
        return federal_cdcc * p.rate