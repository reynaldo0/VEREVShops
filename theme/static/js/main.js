$(document).ready(function() {
    $('.plus-cart').off('click').on('click', function() { 
        var id = $(this).attr("pid").toString();
        var eml = (this.parentNode.children[2]);
        console.log("PID :", id);
        $.ajax({
            type: "GET",
            url: "/pluscart",
            data: {
                prod_id: id
            },
            success: function(data) {
                console.log("data : ", data);
                eml.innerText = data.quantity;
                document.getElementById("amount").innerText = data.amount;
                document.getElementById("totalamount").innerText = data.totalamount;
            },
            error: function(xhr, status, error) {
                console.log("Error: ", error);
                console.log("Status: ", status);
                console.log("Response: ", xhr.responseText);
            }
        });
    });
});

$(document).ready(function() {
    $('.minus-cart').off('click').on('click', function() { 
        var id = $(this).attr("pid").toString();
        var eml = (this.parentNode.children[2]);
        console.log("PID :", id);
        $.ajax({
            type: "GET",
            url: "/minuscart",
            data: {
                prod_id: id
            },
            success: function(data) {
                console.log("data : ", data);
                eml.innerText = data.quantity;
                document.getElementById("amount").innerText = data.amount;
                document.getElementById("totalamount").innerText = data.totalamount;
            },
            error: function(xhr, status, error) {
                console.log("Error: ", error);
                console.log("Status: ", status);
                console.log("Response: ", xhr.responseText);
            }
        });
    });
});

$(document).ready(function() {
    $('.remove-cart').off('click').on('click', function() { 
        var id = $(this).attr("pid").toString();
        var eml = this
        $.ajax({
            type: "GET",
            url: "/removecart",
            data: {
                prod_id: id
            },
            success: function(data) {
                document.getElementById("amount").innerText = data.amount;
                document.getElementById("totalamount").innerText = data.totalamount;
                eml.parentNode.parentNode.parentNode.remove()
            }
        });
    });
});
