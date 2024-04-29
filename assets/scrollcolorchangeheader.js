window.addEventListener('scroll', function() {

    var a = document.getElementById('navbar-edit')
    cssText = a.style.cssText

    var scrollTop = window.pageYOffset
    console.log(scrollTop)

    if(scrollTop == 0){
        a.style.cssText = cssText + 'background: transparent; box-shadow: none'
    }else{
        a.style.cssText = cssText + 'background: linear-gradient(to right, #00b7ff, #FFF); box-shadow: 0 0 8px #808080;'
    }

  })