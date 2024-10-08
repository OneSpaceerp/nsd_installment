import frappe
from frappe.model.document import Document

class InstallmentPlan(Document):
    def calculate_total(self):
        # Sum up the total amount of selected sales order items
        self.total_amount = sum([item.amount for item in self.sales_order_items])
        self.calculate_installments()
    
    def calculate_installments(self):
        # Calculate remaining amount and divide by installment months
        remaining_amount = self.total_amount - self.advance_payment
        self.monthly_installment = remaining_amount / self.installment_months
    
    def generate_payment_schedule(self):
        # Create payment schedule based on the number of months
        current_date = frappe.utils.today()
        for month in range(self.installment_months):
            payment_due_date = frappe.utils.add_months(current_date, month)
            self.append('payment_schedule', {
                'due_date': payment_due_date,
                'installment_amount': self.monthly_installment
            })
