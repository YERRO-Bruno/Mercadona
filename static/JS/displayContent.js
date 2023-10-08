document.addEventListener("DOMContentLoaded", function () {
    const categoryFilter = document.getElementById("category-filter");
    const productList = document.getElementById("product-list");
    //Checkbox 'que les promotions'
    const promochek = document.getElementById("sel-promo");

    function fillCategories(categr) {
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

    //Affichage d'un produit
    function fillOneProduct(prodcat, prodlab, prodimg, proddsc, prodprice, prodpromo) {
        if (categoryFilter.value == 'all' || prodcat == categoryFilter.value) {
            if ((promochek.checked == false) || (promochek.checked == true && prodpromo == "promo")) {

                var productHtml = `

                    <div class="col-2">
                        <ul class="list-unstyled">
                            <li>
                                <div class="text-center" style="height: 20%">
                                    <span>${prodlab}</span>
                                </div>
                                <div class="text-justify text-center">
                                    <span class="${prodpromo}">${prodprice}</span>
                                </div>
                                <div class="mx-auto vignette text-center">
                                    <img class="img_product" src=" http://localhost:8080/images/${prodimg}">
                                </div>
                            </li>
                        </ul>
                        <div class="text-justify">
                            <span>${proddsc}</span>
                        </div>
                    `;
                $(".row").append(productHtml);
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
                    prod_cat = product.category;
                    prod_lab = product.product_label;
                    prod_img = product.image;
                    prod_desc = product.description;
                    prod_price = product.price;

                    if (product.promo === null || product.promo === undefined) {
                        prod_promo = "paspromo"
                    } else {
                        prod_price = product.price*(1-product.promo.percent_promo/100);
                        prod_price = Number(prod_price).toFixed(2);
                        var dateDuJour = new Date();
                        var date1 = new Date(product.promo.begin_date);
                        var date2 = new Date(product.promo.end_date);
                        if (date1 <= dateDuJour && date2 >= dateDuJour) {
                            prod_promo = "promo";
                        } else {
                            prod_promo = "paspromo"
                        }
                    }
                    fillOneProduct(prod_cat, prod_lab , prod_img, prod_desc, prod_price);
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