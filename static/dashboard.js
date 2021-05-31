function respond(r) {
    if (r.status == 200) {
        alert("OK.");
        location.reload();
    }
    else {
        alert("Error.");
    }
}

function deleteDirectory(id) {
    if (window.confirm("Are you sure to delete this directory?")) {
        $.ajax({
            url: "/dashboard/backend",
            type: "delete",
            data: JSON.stringify({ "id": id }),
            dataType: "json",
        })
            .always(function (r) { respond(r); })
    }
}

function addKeyword(id) {
    var keyword = prompt("Enter the keyword");
    if (keyword) {
        $.ajax({
            url: "/dashboard/backend",
            type: "post",
            data: JSON.stringify({ "id": id, "keyword": keyword }),
            dataType: "json",
        })
            .always(function (r) { respond(r); })
    }
}