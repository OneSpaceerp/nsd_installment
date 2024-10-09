
import frappe
import unittest

class TestInstallmentPlan(unittest.TestCase):
    def test_installment_calculation(self):
        plan = frappe.get_doc({
            'doctype': 'Installment Plan',
            'total_amount': 1000,
            'advance_payment': 200,
            'installment_months': 4
        })
        plan.calculate_installments()
        self.assertEqual(plan.monthly_installment, 200)

    def test_generate_payment_schedule(self):
        plan = frappe.get_doc({
            'doctype': 'Installment Plan',
            'total_amount': 1000,
            'advance_payment': 200,
            'installment_months': 5
        })
        plan.generate_payment_schedule()
        self.assertEqual(len(plan.payment_schedule), 5)
            