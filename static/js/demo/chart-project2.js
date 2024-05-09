$("#kospi-chart-button").click(function(){
    var chart = c3.generate({
        bindto: '#chart-exercise',
        data: {
            columns: [],
            type: 'bar',
            labels: true
        },
        color: {
            pattern: ['#e76e6e'] // 데이터 시리즈별 색상 패턴 지정
        }
    });

    $.ajax({
        method: "GET",
        url: "/kospi"
    }).done(function(response) {
        chart.load({
          columns: [ response[1]]
        });
    });
});

$("#kosdaq-chart-button").click(function(){
    var chart = c3.generate({
        bindto: '#chart-exercise',
        data: {
            columns: [],
            type: 'bar',
            labels: true
        },
        color: {
            pattern: ['#1974a3'] // 데이터 시리즈별 색상 패턴 지정
        }
    });

    $.ajax({
        method: "GET",
        url: "/kosdaq"
    }).done(function(response) {
        chart.load({
          columns: [ response[1]]
        });
    });
});


var chart = c3.generate({
        bindto: '#chart-exercise',
        data: {
            columns: [],
            type: 'bar',
            labels: true
        },
        color: {
            pattern: ['#e76e6e'] // 데이터 시리즈별 색상 패턴 지정
        }
    });

$.ajax({
    method: "GET",
    url: "/kospi"
}).done(function(response) {
    chart.load({
        columns: [response[1]],
        });
});
