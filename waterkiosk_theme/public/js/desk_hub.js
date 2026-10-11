// WaterKiosk: a "Hub" button on every desk page, to jump back to the WaterKiosk Hub.
(function () {
	var STYLE =
		".wk-hub-switch{position:fixed;right:16px;bottom:16px;z-index:1040;display:inline-flex;" +
		"align-items:center;gap:6px;padding:7px 14px 7px 8px;border-radius:999px;color:#fff !important;" +
		"font-weight:600;font-size:13px;text-decoration:none !important;" +
		"background:linear-gradient(120deg,#0a4a85 0%,#0b74c4 50%,#10b4cf 100%);" +
		"box-shadow:0 4px 14px rgba(10,74,133,.35);transition:transform .15s ease,box-shadow .15s ease}" +
		".wk-hub-switch:hover{transform:translateY(-1px);box-shadow:0 6px 18px rgba(10,74,133,.45)}" +
		".wk-hub-switch img{width:22px;height:22px;border-radius:50%;background:#fff;padding:2px}" +
		"@media print{.wk-hub-switch{display:none}}";

	function addHubButton() {
		if (!document.body || document.querySelector(".wk-hub-switch")) return;
		if (!document.getElementById("wk-hub-switch-style")) {
			var s = document.createElement("style");
			s.id = "wk-hub-switch-style";
			s.textContent = STYLE;
			document.head.appendChild(s);
		}
		var a = document.createElement("a");
		a.className = "wk-hub-switch";
		a.href = "/hub";
		a.title = "Go to the WaterKiosk Hub";
		a.innerHTML = '<img src="/files/waterkiosk-icon.png" alt=""><span>Hub</span>';
		document.body.appendChild(a);
	}

	if (document.readyState === "loading") {
		document.addEventListener("DOMContentLoaded", addHubButton);
	} else {
		addHubButton();
	}
	if (window.jQuery) {
		window.jQuery(document).on("app_ready", addHubButton);
	}
})();
