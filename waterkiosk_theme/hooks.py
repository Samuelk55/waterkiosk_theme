app_name = "waterkiosk_theme"
app_title = "WaterKiosk Theme"
app_publisher = "WaterKiosk Ltd"
app_description = "WaterKiosk brand colours for the Raven staff chat, and Hub-first access"
app_email = "info@waterkiosk.africa"
app_license = "mit"

required_apps = ["raven"]

# WaterKiosk Hub tile on the desk home screen (staff only).
add_to_apps_screen = [
	{
		"name": "waterkiosk_theme",
		"logo": "/files/waterkiosk-icon.png",
		"title": "WaterKiosk Hub",
		"route": "/hub",
		"has_permission": "waterkiosk_theme.access.can_see_hub_tile",
	}
]

# "Hub" button on every desk page.
app_include_js = "/assets/waterkiosk_theme/js/desk_hub.js"

# /hub always shows the Hub page (it lives at /me), including when it is the home page.
website_route_rules = [
	{"from_route": "/hub", "to_route": "me"},
]

# Operators, riders and technicians are kept on the Hub: desk and office apps redirect there.
before_request = ["waterkiosk_theme.access.keep_field_staff_on_hub"]

# Adds the WaterKiosk stylesheet to Raven's /raven pages (web + installed phone app).
after_request = ["waterkiosk_theme.raven_theme.inject_theme"]
