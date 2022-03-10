
var labels1 = [
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
];

var data = {
    labels: labels1,
    datasets: [{
      label: 'My First dataset',
      backgroundColor: 'rgb(255, 99, 132)',
      borderColor: 'rgb(255, 99, 132)',
      data: [0, 10, 5, 2, 20, 30, 45],
    }]
};

var config = {
    type: 'line',
    data: data,
    options: {}
};


$("#draw_graph").click(function(event){
    
    var ric = $('#ric').val()
    var sd = $('#start_date').val()
    var ed = $('#end_date').val()
    var interval = $('#interval').val()

    $.ajax(
        {
            url: "/graphs_control",
            type: "POST",
            contentType: "application/json",
            data: JSON.stringify({button_id: "draw_graph", RIC: ric, start_date: sd, end_date: ed, interval: interval}),
            success: function(response_data){ 
                alert(response_data)
                data.datasets.data = response_data.y
                data.labels = response_data.x
                const myChart = new Chart( document.getElementById("myChart"), config);
            },
            error: function(err) { alert(err.statusText);console.log(err.responseText); }
        }
    );
});




