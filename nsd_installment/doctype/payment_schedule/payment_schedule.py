import frappe
from frappe.model.document import Document
from frappe import _

class PaymentSchedule(Document):
    def before_save(self):
        # Validate installment amount and due date
        if self.installment_amount <= 0:
            frappe.throw(_("Installment amount must be greater than 0."))
        
        if not self.due_date:
            frappe.throw(_("Due date is required for each installment."))

    def on_payment_received(self, payment_amount):
        # Handle different payment scenarios
        if payment_amount < self.installment_amount:
            frappe.throw(_("Payment amount is less than the installment amount."))
        elif payment_amount == self.installment_amount:
            self.status = "Paid"
        elif payment_amount > self.installment_amount:
            frappe.throw(_("Payment amount exceeds the installment amount."))

        self.db_update()
        frappe.msgprint(_("Installment marked as paid."))
