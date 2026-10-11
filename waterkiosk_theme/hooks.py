app_name = "waterkiosk_theme"
app_title = "WaterKiosk Theme"
app_publisher = "WaterKiosk Ltd"
app_description = "WaterKiosk brand colours for the Raven staff chat"
app_email = "info@waterkiosk.africa"
app_license = "mit"

required_apps = ["raven"]

# Adds the WaterKiosk stylesheet to Raven's /raven pages (web + installed phone app).
after_request = ["waterkiosk_theme.raven_theme.inject_theme"]
