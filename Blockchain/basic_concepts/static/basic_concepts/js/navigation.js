// Get the button, and when the user clicks on it, execute myFunction
document.getElementById("openSidebar").onclick = function() {
    openSidebar()
};

document.getElementById("closeSidebar").onclick = function() {
    closeSidebar()
};

document.getElementById("sidebar").style.animationFillMode = "forwards";

/* myFunction toggles between adding and removing the show class, which is used to hide and show the dropdown content */
function openSidebar(){
    
    const links = document.getElementsByClassName("link")
    for(i=0; i<links.length; i++){
        links[i].animate([
            // keyframes
            { opacity: '1' }
          ],{
            // timing options
            duration: 500,
            delay: 850,
            easing: "cubic-bezier(0.42, 0, 0.58, 1)",
            fill: "forwards",
          });
    };

    document.getElementById("sidebar").animate([
        // keyframes
        { height: '100vh' }
      ],{
        // timing options
        duration: 800,
        easing: "cubic-bezier(0.42, 0, 0.58, 1)",
        fill: "forwards",
      });

    document.getElementById("closeSidebar").style.display = "flex";
};

function closeSidebar(){

    const links = document.getElementsByClassName("link")
    for(i=0; i<links.length; i++){
        links[i].animate([
            // keyframes
            {opacity: '0' }
          ],{
            // timing options
            duration: 0,
            fill: "forwards",
          });
    };

    document.getElementById("sidebar").animate([
        // keyframes
        { height: '0vh' }
      ],{
        // timing options
        duration: 800,
        easing: "cubic-bezier(0.42, 0, 0.58, 1)",
        fill: "forwards",
      });

    document.getElementById("closeSidebar").style.display = "none";
};

