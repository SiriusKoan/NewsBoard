function respond(r) {
    if (r.status == 200) {
        alert("OK.");
        location.reload();
    }
    else {
        alert("Error.");
    }
}

function addDirectory() {
    let value = document.getElementById("directory_name").value;
    $.ajax({
        url: "/dashboard/backend",
        type: "post",
        data: JSON.stringify({ "type": "directory", "value": value }),
        dataType: "json",
    })
        .always(function (r) { respond(r); })
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
    let directory_id = parseInt(identifier[0]);
    let keyword = identifier[1];
    $.ajax({
        url: "/dashboard/backend",
        type: "delete",
        data: JSON.stringify({ "type": "keyword", "directory_id": directory_id, "keyword": keyword }),
        dataType: "json",
    })
        .always(function (r) { respond(r); })
}

function addKeyword(id) {
    let keyword = prompt("Enter the keyword");
    if (keyword) {
        $.ajax({
            url: "/dashboard/backend",
            type: "post",
            data: JSON.stringify({ "type": "keyword", "directory_id": id, "keyword": keyword }),
            dataType: "json",
        })
            .always(function (r) { respond(r); })
    }
}

function show_hide(element) {
    if (window.innerWidth < 600) {
        let children = element.parentElement.children;
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