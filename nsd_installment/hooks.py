from . import __version__ as app_version

app_name = "nsd_installment"
app_title = "NSD Installment"
app_publisher = "Nest Software Development"
app_description = "Manage installment payments for sales orders."
app_icon = "octicon octicon-file-directory"
app_color = "green"
app_email = "info@nsd-eg.com"
app_license = "MIT"

# Doctype event hooks
doc_events = {
"Installment Plan": {
    "on_submit": "nsd_installment.nsd_installment.doctype.installment_plan.installment_plan.create_invoice_for_installment"
}
}

