
document.addEventListener("DOMContentLoaded", function () {
    const categoryFilter = document.getElementById("category-filter");
    const productList = document.getElementById("product-list");
    //Checkbox 'que les promotions'
    const promochek = document.getElementById("sel-promo");
    // liste categorie du bloc  administration produit
    const currentCategory = document.getElementById("id_category");
    const imgcour = document.getElementById("currentimg")
    // alert("admin")
    console.log("admin")

    function fillcurrentCategories() {
        alert("fillcat")
        // Sélécteur de catégorie
        $.ajax({
            url: '/promo/api/categories',
            method: "GET",
            dataType: "json",
            success: function (data) {
                var i = 0;
                data.forEach(category => {
                    const option = document.createElement("option");

                    // option.value = data[i].id;
                    option.textContent = data[i].label;
                    // optionc.textContent = data[i].label;
                    currentCategory.appendChild(option);
                    //$(".categc").append(categc);
                    i++
                });
                document.getElementById("id_category").value = null
            },
            error: function (xhr, status, error) {
                console.error("Problème de récupération des catégories :", xhr, status, error);
            }
        });
    }

    fillcurrentCategories()

    const gallery = document.getElementById("product-list");
    gallery.addEventListener("click", function (event) {
        var imgfils = (document.getElementById("currentimg"))
        imgfils.remove()
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
        fillcurrentproduct(id_prod)
    })

    window.addEventListener("load", function() {
    // Code JavaScript à exécuter après le chargement complet de toutes les ressources
        var idx = document.getElementById("id_prodid").value
        fillcurrentproduct(parseInt(idx))
    });


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
                    <img class="imgproduct" id="currentimg" src="/static/images/${product.image}">
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
    document.getElementById("imageInput").addEventListener("change", function (e) {
        e.preventDefault();
        var boutonimg = document.getElementById("btnimage");
        uploadimage()
    })

    async function uploadimage() {
        var fileInput = document.getElementById("imageInput");
        var file = fileInput.files[0];
        // alert("image1")
        if (file) {
            var formData = new FormData();
            formData.append("image", file);
            var csrfToken = getCookie('csrftoken');
            // fetch("http://127.0.0.1:8000/promo/administration/upload_image/", {
            await fetch("/promo/administration/upload_image/", {
                method: "POST",
                body: formData,
                headers: {
                    "X-CSRFToken": csrfToken // Inclure le jeton CSRF dans l'en-tête
                },
            })
                .then(response => response.json())
                .then(data => {
                    // suppression image actuellement affiché
                    var imgfils = (document.getElementById("currentimg"))
                        imgfils.remove()
                    //recupération nom de fichier
                    const fileimg = document.getElementById("imageInput").files[0].name;
                    alert(fileimg)
                    //affichage image téléchargé
                    document.getElementById("id_fileimage").value =fileimg
                    var imghtml = `
                    <img class="imgproduct" id="currentimg" src="/static/images/${fileimg}">
                    `;
                    imgnew = $(".imgcour").append(imghtml)

                })
                .catch(error => {
                    console.error(error);
                    alert(error)
                });
        }
    }

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



