
var red = '#ff6c62';
var yellow= '#f9f781';
var green = '#c1ee6e';

/*
This values are used to define the bar charts limits
You may change this values
 */
var rpm_bar_max_value = 7000; // max value for the rpm bar axis
var rpm_low = 4500; // rpm:first limit value (separates the yellow and green ranges)
var rpm_high = 5000; // rpm: second limit value (separates green and red ranges)
var soc_low = 33; // soc: first limit value (separates red and yellow ranges)
var soc_high = 66; // soc: second limit value (separates yellow and green ranges)

/*Given a value, a lower and higher limit and three colors
* returns the pertinent color
* */
function get_color(value,low,high,c1,c2,c3){
    if(value < low ){
        color = c1;
    }
    else if(value >= low && value <= high){
        color = c2;
    }
    else{
        color = c3;
    }
    return color;
}

function rmp_chart(rpmValue){
    var color = get_color(rpmValue,rpm_low,rpm_high,yellow,green,red)
    var ctx = document.getElementById("rpm_chart").getContext('2d');
    var rpmChart = new Chart(ctx, {
      type: 'horizontalBar',
      data: {
        datasets: [{
            data: [rpmValue],
            backgroundColor: [
              color
            ],
            borderColor: [
              '#d1cad0'
            ],
            borderWidth: 2
          },
          {
            data: [rpm_bar_max_value-rpmValue],
            backgroundColor: [
              '#d1cad0'
            ],
            borderColor: [
              '#d1cad0'
            ],
            borderWidth: 2
          }
        ]
      },
      options: {
          maintainAspectRatio: false,
          animation: false,
          legend: {
                display: false
            },
            tooltips: {
                enabled: false
            },
        scales: {
          yAxes: [{
            stacked: true,
            ticks: {
              beginAtZero: true
            }
          }],
          xAxes: [{
            stacked: true,
            ticks: {
              beginAtZero: true
            }
          }]

        }
      }
    });
}

function soc_chart(socValue){
    var color = get_color(socValue,soc_low,soc_high,red,yellow,green);
    var ctx = document.getElementById("soc_chart").getContext('2d');
    var socChart = new Chart(ctx, {
      type: 'bar',
      data: {
        datasets: [{
            data: [socValue],
            backgroundColor: [
              color
            ],
            borderColor: [
              '#d1cad0'
            ],
            borderWidth: 2
          },
          {
            data: [100-socValue],
            backgroundColor: [
              '#d1cad0'
            ],
            borderColor: [
              '#d1cad0'
            ],
            borderWidth: 2
          }
        ]
      },
      options: {
          maintainAspectRatio: false,
          animation: false,
          legend: {
                display: false
            },
            tooltips: {
                enabled: false
            },
        scales: {
          yAxes: [{
            stacked: true,
            ticks: {
              display: false
            },
            gridLines: {
                display:false,
                drawBorder: false,
            }
          }],
          xAxes: [{
            stacked: true,
            ticks: {
              display: false
            },
            gridLines: {
                display:false,
                drawBorder: false,
            }
          }]

        },
        axes: {display:false}
      }
    });
}

function soc_chart_lv(socValue){
    var color = get_color(socValue,soc_low,soc_high,red,yellow,green);
    var ctx = document.getElementById("soc_chart_lv").getContext('2d');
    var socChart = new Chart(ctx, {
      type: 'bar',
      data: {
        datasets: [{
            data: [socValue],
            backgroundColor: [
              color
            ],
            borderColor: [
              '#d1cad0'
            ],
            borderWidth: 2
          },
          {
            data: [100-socValue],
            backgroundColor: [
              '#d1cad0'
            ],
            borderColor: [
              '#d1cad0'
            ],
            borderWidth: 2
          }
        ]
      },
      options: {
          maintainAspectRatio: false,
          animation: false,
          legend: {
                display: false
            },
            tooltips: {
                enabled: false
            },
        scales: {
          yAxes: [{
            stacked: true,
            ticks: {
              display: false
            },
            gridLines: {
                display:false,
                drawBorder: false,
            }
          }],
          xAxes: [{
            stacked: true,
            ticks: {
              display: false
            },
            gridLines: {
                display:false,
                drawBorder: false,
            }
          }]

        },
        axes: {display:false}
      }
    });
}

function written_values(data){
    document.getElementById("soc_value_lv").textContent = data['SOC_LV'];
    document.getElementById("soc_value").textContent = data['SOC'];
    document.getElementById("rpm_value").textContent = data['RPM'];
    document.getElementById("vmincell_value").textContent = data['Vmincell'];
    document.getElementById("vmaxvcell_value").textContent = data['Vmaxcell'];
    document.getElementById("tmincell_value").textContent = data['Tmincell'];
    document.getElementById("tmaxcell_value").textContent = data['Tmaxcell'];
    document.getElementById("tbat_value").textContent = data['Tbat'];
    document.getElementById("tengine_value").textContent = data['Tengine'];
    document.getElementById("tdriver_value").textContent = data['Tdriver'];
    document.getElementById("imax_value").textContent = data['Imax'];
    document.getElementById("vbat_value").textContent = data['Vbat'];
    document.getElementById("tbat_value_lv").textContent = data['Tbat_LV'];
    document.getElementById("speed_value").textContent = data['Speed'];

}