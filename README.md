# WaterKiosk Theme

Brand colours for the Raven staff chat on erp.waterkiosk.africa: ocean-blue to aqua
headers and buttons, a light water-drop chat background, coloured icons per channel
(announcements, general, technical, operators, hr-admin, accounts-finance, management),
and WhatsApp-style blue bubbles for your own messages.

It touches **only** the `/raven` pages. Desk, ERPNext, the Hub and the ESS app are not affected.

## Install on Frappe Cloud (private bench)

1. Push this folder to a GitHub repository (private is fine), e.g. `waterkiosk/waterkiosk_theme`.
2. Frappe Cloud → your bench group → **Apps** → **Add App** → **GitHub** → pick the repo, branch `main`.
3. **Deploy** the bench group.
4. Site `erp.waterkiosk.africa` → **Apps** → **Install App** → *WaterKiosk Theme*.
5. Open `/raven` and refresh (on phones: close and reopen the installed app).

## Change colours

Edit `waterkiosk_theme/public/css/raven_theme.css` (the `--wk-*` values at the top), bump
`__version__` in `waterkiosk_theme/__init__.py` so phones fetch the new file, push, and redeploy.

## Remove

Uninstall the app from the site. Raven returns to its normal grey look; no data is changed.

Note: Raven updates can rename internal page elements. If part of the theme stops
showing after a Raven upgrade, the CSS selectors need a small refresh.
