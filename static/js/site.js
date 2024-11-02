
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


      // Function to animate the count
  function animateCount(target, duration, counter) {
        const start = 0;
        const range = target - start;
        const increment = target / (duration / 16); // Adjust for 60fps
  
        let current = start;
        const step = () => {
          current += increment;
          if (current >= target) {
            counter.textContent = target.toLocaleString();
          } else {
            counter.textContent = Math.floor(current).toLocaleString();
            requestAnimationFrame(step);
          }
        };
        step();
      }
  
const satisfy =  document.getElementById("counter");

const typeofpuja =  document.getElementById("typeofpuja");

const hours =  document.getElementById("hours");

const poojaperformed =  document.getElementById("poojaperformed");

      // Start the count animation to 5000 over 3 seconds

  const targetSection = document.getElementById('counts');

  if(targetSection){
    window.addEventListener('scroll', () => {
      const sectionTop = targetSection.getBoundingClientRect().top;
    
      if (sectionTop < window.innerHeight && sectionTop >= 0) {
        // Code to run when the section is visible
        animateCount(1500,1000,satisfy);
        animateCount(20,1000,typeofpuja);
        animateCount(24,1000,hours);
        animateCount(2000,1000,poojaperformed);
      }
    });
  }





