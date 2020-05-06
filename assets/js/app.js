function toSearch(){
    var searchIcon = document.getElementById('searchForm');
    var toggleBtn = document.getElementById('form-toggle');
    var x = window.matchMedia("(max-width: 700px)")
    // searchIcon.style.display= 'block';
    searchIcon.classList.toggle('searchVisible')
    if(x.matches){
        toggleBtn.style.display = 'none';
    }
   
 }