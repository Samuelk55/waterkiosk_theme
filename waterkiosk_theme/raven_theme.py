import frappe

from waterkiosk_theme import __version__

THEME_URL = "/assets/waterkiosk_theme/css/raven_theme.css"


def inject_theme(response=None, request=None):
	"""Add the WaterKiosk stylesheet to the HTML of Raven's /raven pages.

	Raven's page template has no hook for custom CSS, so the link is added to
	the finished response. Every other page and API call is left untouched.
	"""
	if response is None or request is None:
		return

	try:
		path = request.path or ""
		if path != "/raven" and not path.startswith("/raven/"):
			return
		if path.endswith((".js", ".json", ".webmanifest", ".png", ".svg", ".ico")):
			return
		if response.status_code != 200 or response.mimetype != "text/html":
			return
		if response.direct_passthrough or response.is_streamed:
			return

		html = response.get_data(as_text=True)
		if THEME_URL in html or "</head>" not in html:
			return

		link = f'<link rel="stylesheet" href="{THEME_URL}?v={__version__}">'
		response.set_data(html.replace("</head>", f"{link}\n</head>", 1))
	except Exception:
		frappe.logger().error("WaterKiosk theme: could not add Raven stylesheet", exc_info=True)
