
app_name = "nsd_installment"
app_title = "NSD Installment"
app_publisher = "Your Name"
app_description = "Manage installment payments for sales orders."
app_icon = "octicon octicon-file-directory"
app_color = "green"
app_email = "your.email@example.com"
app_license = "MIT"
app_include_js = []  # No JavaScript to include
app_include_css = []  # No CSS to include

# Doctype event hooks
doc_events = {
    "Installment Plan": {
        "on_submit": "nsd_installment.nsd_installment.doctype.installment_plan.installment_plan.create_invoice_for_installment"
    }
}
            
