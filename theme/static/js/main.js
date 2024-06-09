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
