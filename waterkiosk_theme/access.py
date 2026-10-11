import frappe
from werkzeug.exceptions import HTTPException
from werkzeug.utils import redirect

HUB_URL = "/hub"

# Pages that make up the ERP desk and the office apps. Field staff are sent to the Hub instead.
OFFICE_PAGES = ("/desk", "/app", "/apps", "/crm", "/helpdesk", "/insights")

# Field staff: Hub (and team chat) only.
HUB_ONLY_ROLES = {"Kiosk Operator", "WK Technician", "WK Rider"}
HUB_ONLY_DESIGNATIONS = {"Operator", "Rider", "Technician"}

# Anyone holding one of these keeps desk access, whatever their designation.
DESK_ROLES = {
	"System Manager",
	"WK Director",
	"Kiosk Supervisor",
	"WK Technical Supervisor",
	"HR Manager",
	"HR User",
	"Accounts Manager",
	"Accounts User",
}


class _GoToHub(HTTPException):
	"""Temporary (302) redirect, so a shared browser never caches it for office users."""

	code = 302

	def get_response(self, environ=None, scope=None):
		return redirect(HUB_URL, 302)


def is_hub_only(user=None):
	"""True for operators, riders and technicians: they use the Hub, not the desk."""
	user = user or frappe.session.user
	if not user or user in ("Guest", "Administrator"):
		return False

	roles = set(frappe.get_roles(user))
	if roles & DESK_ROLES:
		return False
	if roles & HUB_ONLY_ROLES:
		return True

	designation = frappe.db.get_value("Employee", {"user_id": user, "status": "Active"}, "designation")
	return designation in HUB_ONLY_DESIGNATIONS


def _is_office_page(path):
	path = (path or "").rstrip("/") or "/"
	return any(path == p or path.startswith(p + "/") for p in OFFICE_PAGES)


def keep_field_staff_on_hub():
	"""before_request: send field staff who open the desk or an office app to the Hub."""
	request = getattr(frappe.local, "request", None)
	if not request or request.method != "GET":
		return
	if not _is_office_page(request.path):
		return
	if is_hub_only():
		raise _GoToHub()


@frappe.whitelist()
def can_use_desk():
	"""Used by the Hub to decide whether to show its Desk button."""
	user = frappe.session.user
	if user == "Guest":
		return False
	if frappe.db.get_value("User", user, "user_type") != "System User":
		return False
	return not is_hub_only(user)


def can_see_hub_tile():
	"""Show the WaterKiosk Hub tile on the apps screen to staff only (not helpdesk customers)."""
	user = frappe.session.user
	if user == "Guest":
		return False
	if frappe.db.get_value("User", user, "user_type") == "System User":
		return True
	return bool(frappe.db.exists("Employee", {"user_id": user})) or is_hub_only(user)
