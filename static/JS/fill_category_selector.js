document.addEventListener("DOMContentLoaded", function () {
    const categoryFilter = document.getElementById("category-filter");
    const productList = document.getElementById("product-list");

    // remplissage du selecteur de categorie
    function fillCategories(categr) {
        $.ajax({
            url: '/promo/api/categories',
            method: "GET",
            dataType: "json",
            success: function (data) {
                var i =0;
                data.forEach(category => {
                    const option = document.createElement("option");
                    option.value = data[i].id;
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
    fillCategories();

    // remplir la liste des produits en fonction de la catégorie sélectionnée
    function fillProducts() {
        const selectedCategoryId = categoryFilter.value;
        $.ajax({
            url: `/promo/api/products`,
            method: "GET",
            dataType: "json",
            success: function (data) {
                var i =0;
                data.forEach(product => {
                    //var imageurl = "{% static 'images/' %}"
                    //var imagefile= ${product.image}
                    //imageurl=imageurl + imagefile
                    var productHtml = `
                        <div class="col-2 border border-2 border-primary">
                            <ul class="list-unstyled">
                                <li>
                                    <div class=" text-center" style="height: 20%">
                                        <span>${product.product_label}</span>
                                    </div>
                                    <div class="mx-auto vignette text-center">
                                        <img class="img_product" src=" http://localhost:8080/images/${product.image}">
                                    </div>
                                </li>
                            </ul>
                            <div class="text-justify">
                                <span>${product.description}</span>
                            </div>
                        </div>
                    `;
                    $(".row").append(productHtml);
                    i++
                })
            },
            error: function (error) {
                console.error("Erreur lors de la récupération des produits :", error);
            }
        });
    }
    fillProducts()
});