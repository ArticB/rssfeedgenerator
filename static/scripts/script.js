$('#exampleModal2').on('show.bs.modal', function (e) {
    // do something...
    console.log('asdfasdf')
})

function newfile() {

    var rsstitle = document.getElementById("new_rss_title").value
    console.log(rsstitle)
    var request = $.ajax({
        url: $SCRIPT_ROOT + '/createnewrss',
        method: "POST",
        data: {
            'title': rsstitle
        },
        dataType: "json"
    });

    request.done(function (msg) {
        if (msg.message === "done")
            showSuccessAlert('1')
        else
            showErrorAlert('1')
    });

    // request.fail(function (jqXHR, textStatus) {
    //     alert("Request failed: " + textStatus);
    // });
    // let myRequest = new Request($SCRIPT_ROOT + '/getall');

    // fetch(myRequest)
    // .then(function(response) {
    //   if (!response.ok) {
    //     throw new Error('HTTP error, status = ' + response.status);
    //   }
    //   return response.blob();
    // })
    // .then(function(response) {
    //     console.log(response)
    // });
}

function newitem() {
    fileid = $Object_id
    var itemtitle = document.getElementById("new_item_title").value
    var itemlink = document.getElementById("new_item_link").value

    var request = $.ajax({
        url: $SCRIPT_ROOT + '/createnewitem',
        method: "POST",
        data: {
            '_id': fileid,
            'title': itemtitle,
            'link': itemlink
        },
        dataType: "json"
    });

    request.done((response) => {
        console.log(response.message)
        if (response.message === "done") {
            console.log('asdfa')
            showSuccessAlert('2')
        } else
            showErrorAlert('2')
    })

}

function getAll(option) {
    var request = $.ajax({
        url: $SCRIPT_ROOT + '/getall',
        method: "POST",
        data: {
            'option': option,
            '_id': $Object_id
        },
        dataType: "json"
    });

    request.done((msg) => {
        if (option == 'add')
            $('#stbody').html(msg.template)
        if (option == 'view')
            $('#stbody2').html(msg.template)
        if (option == 'items')
            $('#stbody3').html(msg.template)
    })
}

function getxml() {
    var request = $.ajax({
        url: $SCRIPT_ROOT + '/geta',
        method: "POST",
        data: {
            '_id': $Object_id
        },
        dataType: "json"
    });
    request.done((response) => {
        elemt = response.template
        console.log(elemt)
        $('#a_id').html(elemt)
    })

}

function setid(id) {
    $Object_id = id
    console.log($Object_id)
}

function setiditem(id) {
    $Object_id = id
    getAll('items')
    getxml()
    console.log($Object_id)
}


function showSuccessAlert(n) {
    var t = '#success-alert'.concat(n)
    $(t).show()
    hideSuccessAlert()
}

function showErrorAlert(n) {
    var t = '#error-alert'.concat(n)
    $(t).show()
    hideErrorAlert()
}

function hideSuccessAlert() {
    setTimeout(function () {
        $('.alert').hide()
    }, 3000);
}

function hideErrorAlert(n) {
    setTimeout(function () {
        $('.alert').hide()
    }, 3000);
}