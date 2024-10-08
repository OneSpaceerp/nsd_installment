
# Desktop config for nsd_installment
from frappe import _

def get_data():
    return [
        {
            "module_name": "NSD Installment",
            "category": "Modules",
            "label": _("NSD Installment"),
            "color": "green",
            "icon": "octicon octicon-file-directory",
            "type": "module",
            "description": _("Module to manage installment payments.")
        }
    ]
