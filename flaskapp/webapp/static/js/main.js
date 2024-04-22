document.addEventListener("DOMContentLoaded", (event)=>{
    const nav = document.getElementById("nav");
    const nav_items = document.querySelectorAll(".nav-items .nav-item");

    nav_items.forEach(function(item){
        item.addEventListener('click', function(){
            var url = item.getAttribute("data-url");
            window.location.href = url;
        });
    });
});

document.addEventListener("DOMContentLoaded", ()=>{
    var element = document.getElementById("center");
    
    var elementWidth = element.clientWidth;
    var elementHeight = element.clientHeight;
    
    var viewportWidth = window.innerWidth;
    var viewportHeight = window.innerHeight;

    var leftPosition = (viewportWidth - elementWidth) / 2;
    var topPosition = (viewportHeight - elementHeight) / 2;

    element.style.left = leftPosition + 'px';
    element.style.top = topPosition + 'px';
});
