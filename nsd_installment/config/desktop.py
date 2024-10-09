# Desktop config for nsd_installment
from frappe import _

def get_data():
    return [
        {
            "module_name": "NSD Installment",
            "color": "green",
            "icon": "octicon octicon-file-directory",
            "type": "module",
            "label": _("NSD Installment"),
        }
    ]
