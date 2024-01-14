
function toggleMenu(){

if(document.getElementById("mobilenav").style.display == "none"){


    document.getElementById("mobilenav").style.display = "block";
    document.getElementById("mobilenav2").style.display = "block";
    document.getElementById("mobilenav2").style.paddingTop = "80px";
    addAnimation();

}
else{
  removeAnimation();
  document.getElementById("mobilenav").style.display = "none";
  document.getElementById("mobilenav2").style.display = "none";
}
document.getElementById("mobilenav").style.width = "224px";
document.getElementById("mobilenav").style.height = "1000px";
document.getElementById("mobilenav").style.position = "absolute";
document.getElementById("mobilenav").style.top = "-16px";
document.getElementById("mobilenav").style.right = "-24px";
document.getElementById("mobilenav").style.background = "#ffffff";
}


function addAnimation() {
    let content = document.getElementById("mobilenav");
    content.classList.add("animate");
    content.classList.remove("reanimate");
    setTimeout(() => {
      content.classList.remove("animate");
    }, 500); // 500 is the same time as the CSS animation
  }


  function removeAnimation() {
    let content = document.getElementById("mobilenav");
    content.classList.add("reanimate");
    content.classList.remove("animate");
    setTimeout(() => {
      content.classList.remove("reanimate");
    }, 500); // 500 is the same time as the CSS animation
  }