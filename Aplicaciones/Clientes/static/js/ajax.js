
// Peticion ajax para cargar cuestionario, por parametro se pasa el id del tipo calidad y carga las pregunta segun tipo calidad
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





//Peticion ajax para cargar los gráficos de Chartjs.org segun los distintos datos de la BD

const graficos = () => {
    const ctx = document.getElementById('myChart');
    const ctx1 = document.getElementById('myChart1');
    const ctx2 = document.getElementById('myChart2');
    const ctx3 = document.getElementById('myChart3');
    const ctx4 = document.getElementById('myChart4');
    const ctx5 = document.getElementById('myChartB').getContext('2d');



    $.ajax({
        type:'GET',
        url: 'http://127.0.0.1:8000/sexo/',
        contentType: 'application/json',
        async: true,
        success: function(data) {
            $.each(data,function (i,item){
                const myChart = new Chart(ctx5, {
                    type: 'bar',
                    data: {
                        labels: ['Hombre', 'Mujer','Prefiere no decir'],
                        datasets: [{
                            label: 'Personas',
                            data: [item.masculino, item.femenino, item.otro],
                            backgroundColor: [
                                'rgba(75, 192, 192, 0.2)',
                                'rgba(153, 102, 255, 0.2)',
                                'rgba(255, 159, 64, 0.2)'
                               
                            ],
                            borderColor: [
                                'rgba(75, 192, 192, 0.2)',
                                'rgba(153, 102, 255, 0.2)',
                                'rgba(255, 159, 64, 0.2)'
                              
                            ],
                            borderWidth: 1
                        }]
                    },
                    options: {
                        scales: {
                            y: {
                                beginAtZero: true
                            }
                        }
                    }
                });
                
            })
        }
    })

    

    $.ajax({
        type:'GET',
        url: 'http://127.0.0.1:8000/tickets/',
        contentType: 'application/json',
        async: true,
        success: function(data) {
            $.each(data,function (i, item){

              
                    const myChart = new Chart(ctx, {
                    type: 'pie',
                    data: {
                        labels: ['Completado', 'No Completado'],
                        datasets: [{
                            label: '# of Votes',
                            data: [item.ticket_true, item.ticket_false],
                            backgroundColor: [
                                'rgba(54, 162, 235, 0.2)',
                                'rgba(255, 99, 132, 0.2)',
                            ],
                            borderColor: [
                                'rgba(54, 162, 235, 1)',
                                'rgba(255, 99, 132, 1)',
                                
                            ],
                            borderWidth: 1
                        }]
                    },
                    options: {
                        responsive: true,
                        
                    }
                })
               
                const myChart1 = new Chart(ctx1, {
                    type: 'pie',
                    data: {
                        labels: ['Completado', 'No Completado'],
                        datasets: [{
                            label: '# of Votes',
                            data: [item.ticket_true_acce, item.ticket_false_acce],
                            backgroundColor: [
                                'rgba(54, 162, 235, 0.2)',
                                'rgba(255, 99, 132, 0.2)',
                            ],
                            borderColor: [
                                'rgba(54, 162, 235, 1)',
                                'rgba(255, 99, 132, 1)',
                                
                            ],
                            borderWidth: 1
                        }]
                    },
                    options: {
                        responsive: true,
                        
                    }
                })
                const myChart2 = new Chart(ctx2, {
                    type: 'pie',
                    data: {
                        labels: ['Completado', 'No Completado'],
                        datasets: [{
                            label: '# of Votes',
                            data: [item.ticket_true_usa, item.ticket_false_usa],
                            backgroundColor: [
                                'rgba(54, 162, 235, 0.2)',
                                'rgba(255, 99, 132, 0.2)',
                            ],
                            borderColor: [
                                'rgba(54, 162, 235, 1)',
                                'rgba(255, 99, 132, 1)',
                                
                            ],
                            borderWidth: 1
                        }]
                    },
                    options: {
                        responsive: true,
                        
                    }
                })
                const myChart3 = new Chart(ctx3, {
                    type: 'pie',
                    data: {
                        labels: ['Completado', 'No Completado'],
                        datasets: [{
                            label: '# of Votes',
                            data: [item.ticket_true_seg, item.ticket_false_seg],
                            backgroundColor: [
                                'rgba(54, 162, 235, 0.2)',
                                'rgba(255, 99, 132, 0.2)',
                            ],
                            borderColor: [
                                'rgba(54, 162, 235, 1)',
                                'rgba(255, 99, 132, 1)',
                                
                            ],
                            borderWidth: 1
                        }]
                    },
                    options: {
                        responsive: true,
                        
                    }
                })
                const myChart4 = new Chart(ctx4, {
                    type: 'pie',
                    data: {
                        labels: ['Completado', 'No Completado'],
                        datasets: [{
                            label: '# of Votes',
                            data: [item.ticket_true_rda, item.ticket_false_rda],
                            backgroundColor: [
                                'rgba(54, 162, 235, 0.2)',
                                'rgba(255, 99, 132, 0.2)',
                            ],
                            borderColor: [
                                'rgba(54, 162, 235, 1)',
                                'rgba(255, 99, 132, 1)',
                                
                            ],
                            borderWidth: 1
                        }]
                    },
                    options: {
                        responsive: true,
                        
                    }
                })
             
            });

        }
    })

}



//Se cargan las funciones al inicio
$(document).ready(function ($){
    listPreguntas();
    graficos();
})