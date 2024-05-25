main();

function main() {
  let profileMenuButton = document.getElementById("profile-menuButton");
  let browseButton = document.getElementById("browse-button");
  let browseCloseButton = document.getElementById("browse-close-button");
  let activityButton = document.getElementById("activity-button");
  let activityCloseButton = document.getElementById("activity-close-button");
  let participantsButton = document.getElementById("participants-button");
  let participantsCloseButton = document.getElementById(
    "participants-close-button"
  );

  media();

  window.addEventListener("resize", () => {
    media();
  });

  if (profileMenuButton) {
    profileMenuButton.addEventListener("click", () => {
      let profileMenu = document.getElementById("profile-menu");
      toogle(profileMenu);
    });
  }

  if (browseButton) {
    browseButton.addEventListener("click", () => {
      let topicsSidebarMobile = document.getElementById(
        "topics-sidebar-mobile"
      );
      let body = document.body;

      body.style.overflow = "hidden";
      toogle(topicsSidebarMobile);
    });
  }

  if (browseCloseButton) {
    browseCloseButton.addEventListener("click", () => {
      let topicsSidebarMobile = document.getElementById(
        "topics-sidebar-mobile"
      );
      let body = document.body;
      body.style.overflow = "auto";
      toogle(topicsSidebarMobile);
    });
  }

  if (activityButton) {
    activityButton.addEventListener("click", () => {
      let activitySidebarMobile = document.getElementById(
        "activity-sidebar-mobile"
      );
      let body = document.body;
      body.style.overflow = "hidden";
      toogle(activitySidebarMobile);
    });
  }

  if (activityCloseButton) {
    activityCloseButton.addEventListener("click", () => {
      let activitySidebarMobile = document.getElementById(
        "activity-sidebar-mobile"
      );
      let body = document.body;
      body.style.overflow = "auto";
      toogle(activitySidebarMobile);
    });
  }

  if (participantsButton) {
    participantsButton.addEventListener("click", () => {
      let participantsSidebarMobile = document.getElementById(
        "participants-sidebar-mobile"
      );
      let body = document.body;
      body.style.overflow = "hidden";
      toogle(participantsSidebarMobile);
    });
  }

  if (participantsCloseButton) {
    participantsCloseButton.addEventListener("click", () => {
      let participantsSidebarMobile = document.getElementById(
        "participants-sidebar-mobile"
      );
      let body = document.body;
      body.style.overflow = "auto";
      toogle(participantsSidebarMobile);
    });
  }
}

function toogle(element) {
  if (element.style.display === "none") {
    element.style.display = "flex";
  } else {
    element.style.display = "none";
  }
}

function toogleHide(deviceWidth, element, hide = True) {
  if (element) {
    if (deviceWidth < 900) {
      if (hide) element.style.display = "none";
      else element.style.display = "flex";
    } else {
      if (hide) element.style.display = "flex";
      else element.style.display = "none";
    }
  }
}

function media() {
  let deviceWidth = window.innerWidth;

  let logoName = document.getElementById("logo-name");
  let profileUsername = document.getElementById("profile-username");
  let profileLogout = document.getElementById("profile-logout");
  let profileLogin = document.getElementById("profile-login");
  let profileRegister = document.getElementById("profile-register");
  let profileMenuButton = document.getElementById("profile-menuButton");
  let navSearchBar = document.getElementById("nav-searchbar");
  let searchBar = document.getElementById("searchbar");
  let topicsSidebar = document.getElementById("topics-sidebar");
  let activitySidebar = document.getElementById("activity-sidebar");
  let participantsSidebar = document.getElementById("participants-sidebar");
  let browseButton = document.getElementById("browse-button");
  let activityButton = document.getElementById("activity-button");
  let participantsButton = document.getElementById("participants-button");

  toogleHide(deviceWidth, logoName, true);
  toogleHide(deviceWidth, profileUsername, true);
  toogleHide(deviceWidth, profileLogout, true);
  toogleHide(deviceWidth, profileLogin, true);
  toogleHide(deviceWidth, profileRegister, true);
  toogleHide(deviceWidth, profileMenuButton, false);
  toogleHide(deviceWidth, navSearchBar, true);
  toogleHide(deviceWidth, searchBar, false);
  toogleHide(deviceWidth, topicsSidebar, true);
  toogleHide(deviceWidth, activitySidebar, true);
  toogleHide(deviceWidth, participantsSidebar, true);
  toogleHide(deviceWidth, browseButton, false);
  toogleHide(deviceWidth, activityButton, false);
  toogleHide(deviceWidth, participantsButton, false);
}
