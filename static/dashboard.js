function respond(r) {
    if (r.status == 200) {
        alert("OK.");
    }
    else {
        alert("Error.")
    }
}

function addKeyword(id) {
    alert(id)
    var keyword = prompt("Enter the keyword");
    if (keyword) {
        $.ajax({
            url: "/dashboard/backend",
            type: "post",
            data: JSON.stringify({ "id": id, "keyword": keyword }),
            dataType: "json",
        })
            .always(function (r) { respond(r) })
    }
}