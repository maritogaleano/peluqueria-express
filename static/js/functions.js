var localPk = null;
function submit_with_ajax(pk) {
    console.log(pk);
    $.confirm({
        theme: 'modern',
        title: 'Eliminar cliente',
        icon: 'fa fa-info',
        content: 'Desea eliminar el cliente seleccionado?',
        columnClass: 'small',
        typeAnimated: true,
        cancelButtonClass: 'btn-primary',
        draggable: true,
        dragWindowBorder: false,
        buttons: {
            info: {
                text: "Si",
                btnClass: 'btn-primary',
                action: function () {
                    
                    $.ajax({
                        url: '/clientes/delete/',
                        data: {
                            'id': pk,
                        },
                        method: 'POST',
                        dataType: 'json',
                        success: function (request) {
                            console.log(request);
                            if (!request.hasOwnProperty('error')) {
                                location.href = '/clientes/listado/';
                                return false;
                            }
                            alert(request.error);
                        },
                        error: function (jqXHR, textStatus, errorThrown) {
                            alert(errorThrown + ' ' + textStatus);
                        }
                    });
                }
            },
            danger: {
                text: "No",
                btnClass: 'btn-red',
                action: function () {

                }
            },
        }
    })
}