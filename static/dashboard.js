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
            data: JSON.stringify({ "type": "directory", "id": id }),
            dataType: "json",
        })
            .always(function (r) { respond(r); })
    }
}

function deleteKeyword(identifier) {
    identifier = identifier.split("_");
    var directory_id = parseInt(identifier[0]);
    var keyword = identifier[1];
    $.ajax({
        url: "/dashboard/backend",
        type: "delete",
        data: JSON.stringify({ "type": "keyword", "directory_id": directory_id, "keyword": keyword }),
        dataType: "json",
    })
        .always(function (r) { respond(r); })
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

function show_hide(element) {
    if (window.innerWidth > 600) {
        var children = element.children;
        if (children[1].style.display == "none") {
            for (i = 1; i < children.length; i++) {
                children[i].style.display = "block";
            }
        }
        else {
            for (i = 1; i < children.length; i++) {
                children[i].style.display = "none";
            }
        }
    }
}