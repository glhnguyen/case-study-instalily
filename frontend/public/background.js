const SITE_ORIGIN = "https://www.partselect.com";

// Allows users to open the side panel by clicking on the action toolbar icon
chrome.sidePanel
  .setPanelBehavior({ openPanelOnActionClick: true })
  .catch((error) => console.error(error));

chrome.tabs.onUpdated.addListener(async (tabId, info, tab) => {
  if (!tab.url) return;
  const url = new URL(tab.url);
  if (url.origin === SITE_ORIGIN) {
    await chrome.sidePanel.setOptions({
      tabId,
      path: "index.html",
      enabled: true,
    });
  } else {
    // Disables the side panel on all other sites
    await chrome.sidePanel.setOptions({
      tabId,
      enabled: false,
    });
  }
});

function generateUUID() {
  return "xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx".replace(/[xy]/g, function (c) {
    var r = (Math.random() * 16) | 0,
      v = c === "x" ? r : (r & 0x3) | 0x8;
    return v.toString(16);
  });
}

chrome.cookies.set(
  {
    url: "http://localhost:8000",
    name: "session_id",
    value: generateUUID(),
    expirationDate: Math.floor(Date.now() / 1000) + 600,
    sameSite: "lax",
    secure: false,
  },
  function (cookie) {
    if (cookie) {
      console.log("Cookie retrieved: ", cookie.value);
    } else {
      console.log("No session cookie found.");
    }
  }
);
