$(document).ready(function() {
    console.log("ASD");
    $("#shortify").click(function() {
        let url = $("#url").val();

        $.ajax({
            url: '/shortify',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({'url': url}),
            dataType: 'json',
            success: function (data) {
                $("#short_link").val(data['short_link'])
                                .removeAttr("hidden");
            }
        });
    });
});