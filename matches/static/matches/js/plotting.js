function drawChart(){
var chartContainer = document.getElementById('chart-container')
var chartDataAttribute = chartContainer.getAttribute('data-chart-data')

var chartData = JSON.parse(chartDataAttribute)

var ctx = document.getElementById('myChart').getContext('2d')
var myChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: Object.keys(chartData),
        datasets: [{
            label: 'Values',
            data: Object.values(chartData),
            backgroundColor: 'rgba(75, 192, 192, 0.2)',
            borderColor: 'rgba(75, 192, 192, 1)',
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
}

document.addEventListener('DOMContentLoaded', drawChart);