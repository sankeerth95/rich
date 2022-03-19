



window.onload = function () {
  var dataPoints1 = [], dataPoints2 = [];
  var stockChart = new CanvasJS.StockChart("chartContainer",{
    exportEnabled: true,
    title:{
      text:"StockChart with Annotation"
    },
    subtitles: [{
      text: "Litecoin Price"
    }],
    charts: [{
      axisX: {
        crosshair: {
          enabled: true,
          snapToDataPoint: true
        }
      },
      axisY: {
        prefix: "$",
        lineThickness: 0
      },
      data: [{
        name: "Price (in USD)",
        yValueFormatString: "$#,###.##",
        type: "candlestick",
        dataPoints : dataPoints1
      }]
    }],
    navigator: {
      data: [{
        dataPoints: dataPoints2
      }],
      slider: {
        minimum: new Date(2018, 10, 01),
        maximum: new Date(2018, 11, 20)
      }
    }
  });
  $.getJSON("https://canvasjs.com/data/docs/ltceur2018.json", function(data) {
    var lowestCloseDate = data[0].date, lowestClosingPrice = data[0].close;
    for(var i = 0; i < data.length; i++) {
      if(data[i].close < lowestClosingPrice) {
        lowestClosingPrice = data[i].close;
        lowestCloseDate = data[i].date;
      }
    }
    for(var i = 0; i < data.length; i++){
      dataPoints1.push({x: new Date(data[i].date), y: [Number(data[i].open), Number(data[i].high), Number(data[i].low), Number(data[i].close)]});
      dataPoints2.push({x: new Date(data[i].date), y: Number(data[i].close)});
      if(data[i].date === lowestCloseDate){
        dataPoints1[i].indexLabel = "Lowest Closing";
        dataPoints1[i].indexLabelFontColor = "red";
        dataPoints1[i].indexLabelOrientation = "vertical"
      }
    }
    stockChart.render();
  });
}

















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




