
var labels1 = [
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
];

var data1 = {
    labels: labels1,
    datasets: [{
      label: 'My First dataset',
      backgroundColor: 'rgb(255, 99, 132)',
      borderColor: 'rgb(255, 99, 132)',
      data: [0, 10, 5, 2, 20, 30, 45],
    }]
};

var config1 = {
    type: 'line',
    data: data1,
    options: {}
};


$("#draw_graph").click(function(event){
    
    var ric = 'a'
    var sd = 'a'
    var ed = 'a' //$('#end_date').data
    var interval = 'a'
    $.ajax(
        {
            url: "/graphs_control",
            type: "POST",
            contentType: "application/json",
            data: JSON.stringify({button_id: "draw_graph", RIC: ric, start_date: sd, end_date: ed, interval_id: interval}),
            success: function(response_data){ 
                // data.datasets.data = response_data
                const myChart = new Chart( document.getElementById("myChart"), config1);
            },
            error: function(err) { alert(err.statusText);console.log(err.responseText); }
        }
    );
});




