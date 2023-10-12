const gallery= document.getElementById("product-list");
    gallery.addEventListener("click", function (event) {
        const currentproduct = document.getElementById("currentproduct")
        const tabid = []
        alert("clic")
        idClicked =event.target
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

        for (var i = 0; i < 7; i++) {
            if (tabid[i] == "XXXXXXX") {
                id_prod = tabelement[i].parentNode.id
                //alert(id_prod)
            }
        }
        //recuperation et traitement du produit courant
        $.ajax({
            url: `/promo/api/products/${id_prod}`,
            method: "GET",
            dataType: "json",
            success: function (data) {
                product = data
                prod_id = product.id
                prod_cat = product.category.label;
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

                //display current product
                fillCurentProduct(prod_id, prod_cat, prod_lab , prod_img, prod_desc, prod_price, prod_promo);
            },
            error: function (error) {
                console.error("Erreur lors de la récupération des produits :", error);
            }
        })

    })