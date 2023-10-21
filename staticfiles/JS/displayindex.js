document.addEventListener("DOMContentLoaded", function () {
    const categoryFilter = document.getElementById("category-filter");
    const productList = document.getElementById("product-list");
    //Checkbox 'que les promotions'
    const promochek = document.getElementById("sel-promo");

    function fillCategories() {
        // Sélécteur de catégorie
        $.ajax({
            url: '/promo/api/categories',
            method: "GET",
            dataType: "json",
            success: function (data) {
                var i = 0;
                data.forEach(category => {
                    const option = document.createElement("option");
                    //option.value = data[i].id;
                    option.textContent = data[i].label;
                    categoryFilter.appendChild(option);
                    i++
                });
            },
            error: function (xhr, status, error) {
                console.error("Problème de récupération des catégories :", xhr, status, error);
            }
        });

    }

    fillCategories()

    //affichage produit courant
    function fillOneProduct(prodid, prodcat, prodlab, prodimg, proddsc, prodprice, prodpromo) {
        if (categoryFilter.value == 'all' || prodcat == categoryFilter.value) {

            if ((promochek.checked == false) || (promochek.checked == true && prodpromo == "promo")) {
                var productHtml = `
                    <div class="col-2" id="${prodid}">
                        <div class="border border-dark vignette " id="XXXXXXX" >
                            <ul class="ul-vignette border list-unstyled" >
                                <li>
                                    <div id="id_vignettexx">
                                        <div class="text-center" id="id_vignette1">
                                            <span>${prodlab}</span>
                                        </div>
                                        <div class="text-justify text-center" id="id_vignette2">
                                            <span class="${prodpromo}">${prodprice}</span>
                                        </div>
                                        
                                        <div class="mx-auto text-center" id="id_vignette3">
                                            <img class="img_product" src="https://ik.imagekit.io/kpvotazbj/${prodimg}">
                                            
                                        </div>
                                        <div class="descript" id="id_vignette4">
                                            <span>${proddsc}</span>
                                        </div>
                                    </div>
                                </li>
                            </ul>
                        </div>
                    </div>
                    `;
                //display new current product
                $(".gallery").append(productHtml);
            }
        }
    }

    // Fonction de remplissage de la liste des produits en fonction de la catégorie sélectionnée et de la checkbox
    function fillProducts() {
        const selectedCategoryId = categoryFilter.value;
        //effacement gallerie
        while (productList.hasChildNodes()) {
            productList.removeChild(productList.firstChild);
        }
        //recuperation et traitement des produits
        $.ajax({
            url: `/promo/api/products`,
            method: "GET",
            dataType: "json",
            success: function (data) {
                data.forEach(product => {
                    // alert("product")
                    prod_id = product.id
                    prod_cat = product.category.label;
                    prod_lab = product.product_label;
                    prod_img = product.image;
                    prod_desc = product.description;
                    prod_price = product.price;
                    prod_begin = product.begin_promo
                    prod_end = product.end_promo
                    if (product.reduction == 0) {
                        prod_promo = "paspromo"
                    } else {
                        prod_price = product.price*(1-product.reduction/100);
                        prod_price = Number(prod_price).toFixed(2);
                        var dateDuJour = new Date();
                        var date1 = new Date(product.begin_promo);
                        var date2 = new Date(product.end_promo);
                        if (date1 <= dateDuJour && date2 >= dateDuJour) {
                            prod_promo = "promo";
                        } else {
                            prod_promo = "paspromo"
                        }
                    }
                    fillOneProduct(prod_id, prod_cat, prod_lab , prod_img, prod_desc, prod_price, prod_promo);
                })
            },
            error: function (error) {
                console.error("Erreur lors de la récupération des produits :", error);
            }
        })
    }

    //A la modification du selecteur de catégorie
    categoryFilter.addEventListener('change', function () {
        fillProducts();
    });

    //A la modification de la checkbox 'Que des promotions'
    promochek.addEventListener('change', function () {
        fillProducts();
    });

    // execution Gallerie
    fillProducts()
})