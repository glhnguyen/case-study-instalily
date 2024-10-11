// Event listener to handle cookie access after the extension is installed
chrome.runtime.onInstalled.addListener(() => {
  console.log("Extension installed.");

  // Access the cookie from the backend
  chrome.cookies.get(
    {
      url: "http://localhost:8000", // The domain where the cookie is set
      name: "session_id", // Name of the cookie you want to access
    },
    function (cookie) {
      if (cookie) {
        // If the cookie exists, log it and perform any necessary action
        console.log("Cookie retrieved:", cookie.value);

        // Example: Store the session ID in chrome.storage for later use
        chrome.storage.local.set({ session_id: cookie.value }, function () {
          console.log("Session ID stored in chrome.storage:", cookie.value);
        });
      } else {
        // If no cookie is found
        console.log("No session cookie found.");
      }
    }
  );
});

// Example of accessing the cookie when the background.js file runs
chrome.runtime.onStartup.addListener(() => {
  chrome.cookies.get(
    {
      url: "http://localhost:8000",
      name: "session_id",
    },
    function (cookie) {
      if (cookie) {
        console.log("Cookie found on startup:", cookie.value);
      } else {
        console.log("No cookie found on startup.");
      }
    }
  );
});
