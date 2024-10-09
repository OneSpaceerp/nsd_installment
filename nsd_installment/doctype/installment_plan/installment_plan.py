import frappe
from frappe.model.document import Document
from frappe import _

class InstallmentPlan(Document):
    def validate(self):
        # Validate installment months and advance payment
        if self.installment_months <= 0:
            frappe.throw(_("Installment months must be greater than 0."))
        
        if self.advance_payment < 0:
            frappe.throw(_("Advance payment cannot be negative."))

        # Ensure total amount is calculated before proceeding
        self.calculate_total()

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

    def on_submit(self):
        # Trigger invoice creation when the installment plan is submitted
        self.create_invoices_for_all_installments()

    def create_invoices_for_all_installments(self):
        # Create a sales invoice for each installment in the payment schedule
        for schedule in self.payment_schedule:
            invoice = frappe.get_doc({
                'doctype': 'Sales Invoice',
                'customer': self.customer,
                'installment_plan': self.name,
                'posting_date': frappe.utils.today(),
                'due_date': schedule.due_date,
                'items': [{'item_name': item.item_name, 'qty': item.qty, 'rate': item.rate} for item in self.sales_order_items],
                'total': schedule.installment_amount
            })
            invoice.insert()
            invoice.submit()
            frappe.msgprint(_("Sales Invoice created for installment due on {0}.").format(schedule.due_date))
