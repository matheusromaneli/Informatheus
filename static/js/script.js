//logica like
$(".btnlike").click( function(){
    let idNum = $(this)[0].id.match(/\d+/)[0]
    let icon = $(this).children().first()
    let span = $(this).children().next()
    //dar like
    if(icon[0].className.includes("far")){
        icon.addClass("fas")
        icon.removeClass("far")
        span[0].innerHTML = parseInt(span[0].innerHTML) + 1
        //desdar dislike
        let dislike = $("#" + idNum + "btndislike").children()
        if (dislike[0].className.includes("fas")){
            dislike.first().addClass("far")
            dislike.first().removeClass("fas")
            let dislikespan = $("#" + idNum + "dislike")
            dislikespan[0].innerHTML = parseInt(dislikespan[0].innerHTML) - 1
        }

    }
    else{//desdar like
        icon.addClass("far")
        icon.removeClass("fas")
        span[0].innerHTML = parseInt(span[0].innerHTML) - 1
    }
})

//logica dislike
$(".btndislike").click( function(){
    let idNum = $(this)[0].id.match(/\d+/)[0]
    let icon = $(this).children().first()
    let span = $(this).children().next()
    //dar dislike
    if(icon[0].className.includes("far")){
        icon.addClass("fas")
        icon.removeClass("far")
        span[0].innerHTML = parseInt(span[0].innerHTML) + 1
        //desdar like
        let like = $("#" + idNum + "btnlike").children()
        if (like[0].className.includes("fas")){
            like.first().addClass("far")
            like.first().removeClass("fas")
            let likespan = $("#" + idNum + "like")
            likespan[0].innerHTML = parseInt(likespan[0].innerHTML) - 1
        }

    }
    else{//desdar dislike
        icon.addClass("far")
        icon.removeClass("fas")
        span[0].innerHTML = parseInt(span[0].innerHTML) - 1
    }
})

document.getElementById("adicionar-carrinho").onclick = function() {
    var toastEl = document.getElementById("toast-compra")
    var toast = new bootstrap.Toast(toastEl)
    toast.show()

    carItems++
    carrinho = document.getElementById("car-items")
    carrinho.innerText = carItems
    carrinho.style.display = "inline-block"
}