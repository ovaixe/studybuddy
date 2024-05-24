let deviceWidth = window.innerWidth;

media();

window.addEventListener("resize", () => {
  deviceWidth = window.innerWidth;
  media();
});

function media() {
  let logoName = document.getElementById("logo-name");
  let profileUsername = document.getElementById("profile-username");
  let profileLogout = document.getElementById("profile-logout");
  let profileLogin = document.getElementById("profile-login");
  let profileRegister = document.getElementById("profile-register");
  let profileMenu = document.getElementById("profile-menu");
  let navSearchBar = document.getElementById("nav-search-bar");
  let mainSearchBar = document.getElementById("main-search-bar");
  let topicsSidebar = document.getElementById("topics-sidebar");
  let activitySidebar = document.getElementById("activity-sidebar");
  let participants = document.getElementById("participants");
  let roomSearchbar = document.getElementById("room-searchbar");

  if (deviceWidth < 900) {
    logoName.style.display = "none";
    if (profileUsername) profileUsername.style.display = "none";
    if (profileLogout) profileLogout.style.display = "none";
    if (profileLogin) profileLogin.style.display = "none";
    if (profileRegister) profileRegister.style.display = "none";
    if (profileMenu) profileMenu.style.display = "flex";
    if (navSearchBar) navSearchBar.style.display = "none";
    if (mainSearchBar) mainSearchBar.style.display = "flex";
    if (topicsSidebar) topicsSidebar.style.display = "none";
    if (activitySidebar) activitySidebar.style.display = "none";
    if (participants) participants.style.display = "none";
    if (roomSearchbar) roomSearchbar.style.display = "flex";
  } else {
    logoName.style.display = "flex";
    if (profileUsername) profileUsername.style.display = "flex";
    if (profileLogout) profileLogout.style.display = "flex";
    if (profileLogin) profileLogin.style.display = "flex";
    if (profileRegister) profileRegister.style.display = "flex";
    if (profileMenu) profileMenu.style.display = "none";
    if (navSearchBar) navSearchBar.style.display = "flex";
    if (mainSearchBar) mainSearchBar.style.display = "none";
    if (topicsSidebar) topicsSidebar.style.display = "flex";
    if (activitySidebar) activitySidebar.style.display = "flex";
    if (participants) participants.style.display = "flex";
    if (roomSearchbar) roomSearchbar.style.display = "none";
  }
}
