document.addEventListener('DOMContentLoaded', function() {

    // Function to update total price based on current values of price, tax, and discount
    function updateTotalPrice() {
        var price = parseInt(document.getElementById('id_price').value);
        var tax = parseFloat(document.getElementById('id_tax').value);
        var discount = parseInt(document.getElementById('id_discount').value);

        // Calculate total price
        var total = (price * (1 - discount / 100)) * tax;

        // Round total price to the nearest whole number
        total = Math.ceil(total);

        // Update the total price field
        document.getElementById('id_total_price').value = total;
    }

    // Attach event handlers to fields for real-time updates
    var fields = document.querySelectorAll('#id_price, #id_tax, #id_discount');
    fields.forEach(function(field) {
        field.addEventListener('change', updateTotalPrice);
    });

    // Call the function initially to set the initial value of total price
    updateTotalPrice();

});