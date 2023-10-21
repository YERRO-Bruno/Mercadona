
alert("admin")
document.addEventListener("DOMContentLoaded", function () {
    const categoryFilter = document.getElementById("category-filter");
    const productList = document.getElementById("product-list");
    //Checkbox 'que les promotions'
    const promochek = document.getElementById("sel-promo");
    // liste categorie du bloc  administration produit
    const currentCategory = document.getElementById("id_category");
    const imgcour = document.getElementById("currentimg")
       function fillcurrentCategories() {
        // Sélécteur de catégorie
        $.ajax({
            url: '/promo/api/categories',
            method: "GET",
            dataType: "json",
            success: function (data) {
                var i = 0;
                data.forEach(category => {
                    const option = document.createElement("option");
                    option.textContent = data[i].label;
                    currentCategory.appendChild(option);
                    i++
                });
                document.getElementById("id_category").value = data[0].label
                document.getElementById("id_addcat").value = data[0].label
            },
            error: function (xhr, status, error) {
                console.error("Problème de récupération des catégories :", xhr, status, error);
            }
        });
    }

    fillcurrentCategories()

    const gallery = document.getElementById("product-list");
    gallery.addEventListener("click", function (event) {
        alert("click")
        var imgfils = (document.getElementById("currentimg"))
        if (imgfils) {
            imgfils.remove()
        }
        const currentproduct = document.getElementById("currentproduct")
        const tabid = []
        idClicked = event.target
        tabid.push(idClicked.id)
        idClicked1 = idClicked.parentNode
        tabid.push(idClicked1.id)
        idClicked2 = idClicked1.parentNode
        tabid.push(idClicked2.id)
        idClicked3 = idClicked2.parentNode
        tabid.push(idClicked3.id)
        idClicked4 = idClicked3.parentNode
        tabid.push(idClicked4.id)
        idClicked5 = idClicked4.parentNode
        tabid.push(idClicked5.id)
        idClicked6 = idClicked5.parentNode
        tabid.push(idClicked6.id)
        tabelement = [idClicked, idClicked1, idClicked2, idClicked3, idClicked4, idClicked5, idClicked6]
        //recherche id de l'element avec l'id XXXXXXX dont le parent a comme id product.id
        for (var i = 0; i < 7; i++) {
            if (tabid[i] == "XXXXXXX") {
                id_prod = tabelement[i].parentNode.id
            }
        }
        alert("trouvé")
        fillcurrentproduct(id_prod)
    })

    //recuperation et traitement du produit courant
    function fillcurrentproduct(idprod) {
        $.ajax({
            url: `/promo/api/products/${idprod}`,
            method: "GET",
            dataType: "json",
            success: function (data) {
                product = data
                document.getElementById("id_prodid").value = product.id

                var imghtml = `
                    <img class="imgproduct" id="currentimg" src="https://ik.imagekit.io/kpvotazbj/${product.image}">
                `;
                imgnew = $(".imgcour").append(imghtml)
                document.getElementById("id_fileimage").value = product.image
                document.getElementById("id_label").value = product.product_label
                document.getElementById("id_description").value = product.description
                document.getElementById("id_category").value = product.category.label
                document.getElementById("id_price").value = product.price
                document.getElementById("id_promo").value = product.reduction
                document.getElementById("id_begin").value = product.begin_promo
                document.getElementById("id_end").value = product.end_promo
                document.getElementById("imageInput").value = product.image
                if (product.reduction == 0.00) {
                    // alert("pas promo")
                    document.getElementById("id_price_reduc").value = product.price
                } else {
                    // alert("promo")
                    document.getElementById("id_price_reduc").value =
                        Math.round(product.price * (1 - product.reduction / 100) * 100) / 100
                }
            },
            error: function (error) {
                console.error("Erreur lors de la récupération des produits :", error);
            }
        })
    }
    // gallery.addEventListener("click", function (event) {
    btnimg = document.getElementById("imageInput");
    btnimg.addEventListener("click", function (e) {
        e.preventDefault()
        alert("click")
    })


    document.getElementById("btnraz").addEventListener("click", function (e) {
        e.preventDefault();
        alert("raz")
        document.getElementById("id_prodid").value = 0
        document.getElementById("id_fileimage").value = null
        document.getElementById("id_label").value = null
        document.getElementById("id_description").value = null
        document.getElementById("id_category").value = null
        document.getElementById("id_price").value = null
        document.getElementById("id_price_reduc").value = null
        document.getElementById("id_promo").value = null
        document.getElementById("id_begin").value = null
        document.getElementById("id_end").value = null
        document.getElementById("currentimg").src = null
        // document.getElementById("id_label").value = null
    })

    function getCookie(name) {
        var value = "; " + document.cookie;
        var parts = value.split("; " + name + "=");
        if (parts.length === 2) return parts.pop().split(";").shift();
    }

})



