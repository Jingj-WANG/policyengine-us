from policyengine_us.model_api import *


class md_non_refundable_eitc(Variable):
    value_type = float
    entity = TaxUnit
    label = "MD EITC non-refundable State tax credit"
    unit = USD
    documentation = "Non-refundable EITC credit reducing MD State income tax."
    definition_period = YEAR
    reference = "https://casetext.com/statute/code-of-maryland/article-tax-general/title-10-income-tax/subtitle-7-income-tax-credits/section-10-704-effective-until-6302023-for-earned-income"
    defined_for = StateCode.MD

    adds = [
        "md_married_or_has_child_non_refundable_eitc",
        "md_unmarried_childless_non_refundable_eitc",
    ]
