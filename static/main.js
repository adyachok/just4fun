var init = function() {
    var t = $('#presentations');

    $("#presentationSearch")
        .on("keyup", function(evt) {onPresentationsSearch(evt, t)});

    $("#sortPoint")
        .on("click", function(evt) {onPresentationsSortClick(evt, t)})

    getPresentations("/presentations", t);
}

var buildTable = function(table, data) {
    var result = data.data,
        processedData = '';

    for(var i=0; i < result.length; i++) {
        var dataCells = '<tr><th scope="row">' + (i + 1) + '</th>',
            arr = [result[i].thumbnail, result[i].title, result[i].creator, result[i].createdAt];

        for (var j=0; j < arr.length; j++) {
            var cell = '<td>' + arr[j] + '</td>';
            dataCells += cell;
        };
        dataCells += '</tr>';
        processedData += dataCells;
    };
    if (!processedData) {
        processedData = "<h3 id='no-match'>No match found</h3>"
    }
    table.find("tbody").empty();
    table.find("tbody").append(processedData);
};

var getPresentations = function(url, table) {
    $.get(url, function () {})
        .done(function(data){buildTable(table, data)})
        .fail(function(data){console.log("error")});
};

var onPresentationsSearch = function (evt, table) {
    var searchString = $(evt.target).val(),
        baseUrl = "/presentations";

    if (searchString.length > 2) {
        url = searchString ? (baseUrl + "/" + searchString) : baseUrl;
        getPresentations(url, table);
    }
    if (searchString.length == 0) {
        getPresentations(baseUrl, table);
    }
};

var onPresentationsSortClick = function (evt, table) {
    var order = "",
        glyphClasses = $(evt.target).attr("class").split(" ");

    if (glyphClasses[1] == "glyphicon-arrow-down") {
        glyphClasses[1] = "glyphicon-arrow-up";
        order = "desc";
    }
    else {
        glyphClasses[1] = "glyphicon-arrow-down";
        order = "asc"
    }
    $(evt.target).attr("class", glyphClasses.join(" "));

    var url = "/presentations/order/" + order;
        getPresentations(url, table);
};
