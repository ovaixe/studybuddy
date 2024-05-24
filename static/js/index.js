main();

function main() {
  let profileMenuButton = document.getElementById("profile-menuButton");
  let browseButton = document.getElementById("browse-button");
  let browseCloseButton = document.getElementById("browse-close-button");
  let activityButton = document.getElementById("activity-button");
  let activityCloseButton = document.getElementById("activity-close-button");

  media();

  window.addEventListener("resize", () => {
    media();
  });

  profileMenuButton.addEventListener("click", () => {
    let profileMenu = document.getElementById("profile-menu");
    toogle(profileMenu);
  });

  browseButton.addEventListener("click", () => {
    let topicsSidebarMobile = document.getElementById("topics-sidebar-mobile");
    toogle(topicsSidebarMobile);
  });

  browseCloseButton.addEventListener("click", () => {
    let topicsSidebarMobile = document.getElementById("topics-sidebar-mobile");
    toogle(topicsSidebarMobile);
  });

  activityButton.addEventListener("click", () => {
    let activitySidebarMobile = document.getElementById(
      "activity-sidebar-mobile"
    );
    toogle(activitySidebarMobile);
  });

  activityCloseButton.addEventListener("click", () => {
    let activitySidebarMobile = document.getElementById(
      "activity-sidebar-mobile"
    );
    toogle(activitySidebarMobile);
  });
}

function toogle(element) {
  if (element.style.display === "none") {
    element.style.display = "flex";
  } else {
    element.style.display = "none";
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
  let navSearchBar = document.getElementById("nav-search-bar");
  let mainSearchBar = document.getElementById("main-search-bar");
  let topicsSidebar = document.getElementById("topics-sidebar");
  let activitySidebar = document.getElementById("activity-sidebar");
  let participants = document.getElementById("participants");
  let roomSearchbar = document.getElementById("room-searchbar");
  let browseButton = document.getElementById("browse-button");
  let activityButton = document.getElementById("activity-button");


  if (deviceWidth < 900) {
    logoName.style.display = "none";
    if (profileUsername) profileUsername.style.display = "none";
    if (profileLogout) profileLogout.style.display = "none";
    if (profileLogin) profileLogin.style.display = "none";
    if (profileRegister) profileRegister.style.display = "none";
    if (profileMenuButton) profileMenuButton.style.display = "flex";
    if (navSearchBar) navSearchBar.style.display = "none";
    if (mainSearchBar) mainSearchBar.style.display = "flex";
    if (topicsSidebar) topicsSidebar.style.display = "none";
    if (activitySidebar) activitySidebar.style.display = "none";
    if (participants) participants.style.display = "none";
    if (roomSearchbar) roomSearchbar.style.display = "flex";
    if (browseButton) browseButton.style.display = "flex";
    if (activityButton) activityButton.style.display = "flex";
  } else {
    logoName.style.display = "flex";
    if (profileUsername) profileUsername.style.display = "flex";
    if (profileLogout) profileLogout.style.display = "flex";
    if (profileLogin) profileLogin.style.display = "flex";
    if (profileRegister) profileRegister.style.display = "flex";
    if (profileMenuButton) profileMenuButton.style.display = "none";
    if (navSearchBar) navSearchBar.style.display = "flex";
    if (mainSearchBar) mainSearchBar.style.display = "none";
    if (topicsSidebar) topicsSidebar.style.display = "flex";
    if (activitySidebar) activitySidebar.style.display = "flex";
    if (participants) participants.style.display = "flex";
    if (roomSearchbar) roomSearchbar.style.display = "none";
    if (browseButton) browseButton.style.display = "none";
    if (activityButton) activityButton.style.display = "none";
  }
}
