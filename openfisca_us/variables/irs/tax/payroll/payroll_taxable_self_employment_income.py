from openfisca_us.model_api import *


class payroll_taxable_self_employment_income(Variable):
    value_type = float
    entity = Person
    label = "Taxable self-employment income"
    definition_period = YEAR
    unit = USD
    reference = "https://www.law.cornell.edu/uscode/text/26/1402#a"

    def formula(person, period, parameters):
        irs = parameters(period).irs
        payroll = irs.payroll
        combined_rate = (
            payroll.social_security.rate.self_employment
            + payroll.medicare.rate.self_employment
        )
        deduction_rate = irs.ald.misc.employer_share * combined_rate
        net_se = person("sey", period) * (1 - deduction_rate)
        # Exclude net self-employment income below the reporting threshold.
        return where(
            net_se < payroll.self_employment_net_earnings_exemption, 0, net_se
        )
