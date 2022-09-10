

const listPreguntas = (tp) =>{
    $.ajax({
        type:'GET',
        url: 'http://127.0.0.1:8000/json/'+tp,
        contentType: 'application/json',
        async: true,
        success: function(data) {
            $('.tbPreguntas').empty();
            $.each(data,function (i, item){
                if(item.ticket==1){
                    $('#tablaArticulos').append(
                        $('<tr>'),
                        $('<td>').text(item.nombre),
                        $('<td> <input type="checkbox" checked name="check'+i+'" onclick="return false" />')
                    );
                }
                else {
                    $('#tablaArticulos').append(
                        $('<tr>'),
                        $('<td>').text(item.nombre),
                        $('<td> <input type="checkbox" name="check'+i+'" onclick="return false" />')
                    )
                }
             
            });

        }
    })
}

$(document).ready(function ($){
    listPreguntas();
})

