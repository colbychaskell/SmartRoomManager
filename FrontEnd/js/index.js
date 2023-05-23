$(document).ready(function() {
    $("button").click(function() {
        $.get("colbypi:5000/led-on", function(data, status) {
            alert("LED Status: " + data)
        });
    });
});