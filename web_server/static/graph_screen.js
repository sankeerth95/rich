

function cb(selection){
  $.getJSON({
    url: "/callback", 
    data: {'data': selection },
    success: function(result){
      alert(result.message)
      Plotly.newPlot('chart', result, {staticPlot: true})
    }
  })
}

$("#draw_graph").click(function(event){
    
    var ric = $('#ric').val()
    var sd = $('#start_date').val()
    var ed = $('#end_date').val()
    var interval = $('#interval').val()

    cb(interval);

    // $.ajax(
    //     {
    //         url: "/graphs_control",
    //         type: "POST",
    //         contentType: "application/json",
    //         data: JSON.stringify({button_id: "draw_graph", RIC: ric, start_date: sd, end_date: ed, interval: interval}),
    //         success: function(response_data){ 
    //             alert(response_data)
    //             data.datasets.data = response_data.y
    //             data.labels = response_data.x
    //             const myChart = new Chart( document.getElementById("myChart"), config);
    //         },
    //         error: function(err) { alert(err.statusText);console.log(err.responseText); }
    //     }
    // );
});




