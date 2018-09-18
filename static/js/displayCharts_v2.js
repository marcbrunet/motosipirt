function rpm_chart_old(value) {
    var rpm =value;
    var opts = {
      angle: 0.04, // The span of the gauge arc
      lineWidth: 0.44, // The line thickness
      radiusScale: 0.78, // Relative radius
      pointer: {
        length: 0.6, // // Relative to gauge radius
        strokeWidth: 0.035, // The thickness
        color: '#000000' // Fill color
      },
      limitMax: false,     // If false, max value increases automatically if value > maxValue
      limitMin: false,     // If true, the min value of the gauge will be fixed
      colorStart: '#6FADCF',   // Colors
      colorStop: '#8FC0DA',    // just experiment with them
      strokeColor: '#E0E0E0',  // to see which ones work best for you
      generateGradient: true,
      highDpiSupport: true,     // High resolution support
      staticLabels: {
          font: "15px sans-serif",  // Specifies font
          labels: [0,1000,2000,3000,4000,5000,6000],  // Print labels at these values
          color: "#000000",  // Optional: Label text color
          fractionDigits: 0  // Optional: Numerical precision. 0=round off.
        },

    };
    var target = document.getElementById('rpmChart'); // your canvas element
    var gauge = new Gauge(target).setOptions(opts); // create sexy gauge!
    gauge.maxValue = 6000; // set max gauge value
    gauge.setMinValue(0);  // Prefer setter over gauge.minValue = 0
    gauge.animationSpeed = 1; // set animation speed (32 is default value)
    gauge.set(rpm); // set actual value

    var rpm = document.getElementById("rpm_value");
    rpm.textContent = value;
}

function speed_chart(value){
    var speed = value;
    var opts = {
      angle: 0.04, // The span of the gauge arc
      lineWidth: 0.44, // The line thickness
      radiusScale: 0.78, // Relative radius
      pointer: {
        length: 0.6, // // Relative to gauge radius
        strokeWidth: 0.035, // The thickness
        color: '#000000' // Fill color
      },
      limitMax: false,     // If false, max value increases automatically if value > maxValue
      limitMin: false,     // If true, the min value of the gauge will be fixed
      colorStart: '#6FADCF',   // Colors
      colorStop: '#8FC0DA',    // just experiment with them
      strokeColor: '#E0E0E0',  // to see which ones work best for you
      generateGradient: true,
      highDpiSupport: true,     // High resolution support
      staticLabels: {
          font: "15px sans-serif",  // Specifies font
          labels: [10,30,50,70,90,110, 130, 150, 170,190,210,230,250,270,290,310],  // Print labels at these values
          color: "#000000",  // Optional: Label text color
          fractionDigits: 0  // Optional: Numerical precision. 0=round off.
},

    };
    var target = document.getElementById('speedChart'); // your canvas element
    var gauge = new Gauge(target).setOptions(opts); // create sexy gauge!
    gauge.maxValue = 310; // set max gauge value
    gauge.setMinValue(0);  // Prefer setter over gauge.minValue = 0
    gauge.animationSpeed = 1; // set animation speed (32 is default value)
    gauge.set(speed); // set actual value

    var speed = document.getElementById("speed_value");
    speed.textContent = value;
}

function rmp_chart(value){
    var rpmValue = value;
    var color;
    if(rpmValue < 4000 ){
        color = '#f9f5ab';
    }
    else if(rpmValue >= 4000 && rpmValue <= 5000){
        color = '#c1ee6e';
    }
    else{
        color = '#ff6c62';
    }
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
            data: [8000-rpmValue],
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
    var rpm = document.getElementById("rpm_value");
    rpm.textContent = value;
}

function motor_temp_value(value){
    var motor = document.getElementById("motor_temperature");
    motor.textContent = value;
}