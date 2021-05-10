

$( document ).ready(function(){
  // image gallery
  // init the state from the input
  $(".image-checkbox").each(function () {
    if ($(this).find('input[type="checkbox"]').first().attr("checked")) {
      $(this).addClass('image-checkbox-checked');
    }
    else {
      $(this).removeClass('image-checkbox-checked');
    }
  });

  // sync the state to the input
  $(".image-checkbox").on("click", function (e) {
    $(this).toggleClass('image-checkbox-checked');
    var $checkbox = $(this).find('input[type="checkbox"]');
    $checkbox.prop("checked",!$checkbox.prop("checked"))

    e.preventDefault();
  });

  $('.test').click(function(){
      console.log(checked_cell)
      checked_cell = {}
      $('#timeSlider-div').html('');
      var cam_id = $('.cam_id').val()
      var date_from = $('.date_from').val()
      var date_to = $('.date_to').val()
      var url_to = "http://localhost:9030/api/v1/getTimeline/"
      $.ajax({
          url : url_to,
          type: "POST",
          contentType: "text/plain",
          crossDomain: true,
          dataType: "json",
          data: JSON.stringify({
              cam_id : cam_id,
              date_from : date_from,
              date_to : date_to,
          }),
          
          success: function(response) { 
              //console.log(response.timelines)
              var timelines = response.timelines
              var timeline_list = []
              

              for(var i=0; i< timelines.length; i++){
                  
                  //console.log(timelines[i])
                  year_from = timelines[i].fromDateTime.split("-")[0]
                  //console.log(year_from)
                  month_from = timelines[i].fromDateTime.split("-")[1]
                  day_from = timelines[i].fromDateTime.split("-")[2].split("T")[0]
                  hour_from = timelines[i].fromDateTime.split("T")[1].split(":")[0]
                  minute_from = timelines[i].fromDateTime.split("T")[1].split(":")[1]
                  second_from = timelines[i].fromDateTime.split("T")[1].split(":")[2].split("+")[0]
                  
                  year_to = timelines[i].toDateTime.split("-")[0]
                  //console.log(year_to)
                  month_to = timelines[i].toDateTime.split("-")[1]
                  day_to = timelines[i].toDateTime.split("-")[2].split("T")[0]
                  hour_to = timelines[i].toDateTime.split("T")[1].split(":")[0]
                  minute_to = timelines[i].toDateTime.split("T")[1].split(":")[1]
                  second_to = timelines[i].toDateTime.split("T")[1].split(":")[2].split("+")[0]
                  timeline_list.push({
                      checked : false,
                      year_from : year_from, 
                      month_from : month_from,
                      day_from : day_from,
                      hour_from : hour_from,
                      minute_from : minute_from,
                      second_from : second_from,
                      year_to : year_to,
                      month_to : month_to,
                      day_to : day_to,
                      hour_to : hour_to,
                      minute_to : minute_to,
                      second_to : second_to,
                  })
              }

              var current_year = timeline_list[0].year_from
              var current_month = timeline_list[0].month_from
              var current_day = timeline_list[0].day_from
              //console.log(current_year)
              //console.log(current_month)
              //console.log(current_day)
              var timeSlider_params = []
              
              var init_cells_temp = []
              var date_day_start = Date.parse(new Date(current_year, current_month-1, current_day,0,0,0)) + 3600*9*1000
              //console.log(new Date(current_year, current_month-1, current_day,0,0,0))
              for(var i=0; i< timeline_list.length; i++){
                  //console.log(i)
                  
                  init_cells_temp.push({
                      '_id' : i,
                      'start' : date_day_start + timeline_list[i].hour_from*3600*1000 + timeline_list[i].minute_from*60*1000 + timeline_list[i].second_from*1000,
                      'stop' : date_day_start + timeline_list[i].hour_to*3600*1000 + timeline_list[i].minute_to*60*1000 + timeline_list[i].second_to*1000,
                      'style':{
                                  'background-color': '#76C4FF'
                              }
                  })

                  if(current_year != timeline_list[i].year_from ||
                      current_month != timeline_list[i].month_from ||
                      current_day != timeline_list[i].day_from ||
                      i == timeline_list.length - 1){
                          var zoomDiv = document.createElement('div');
                          zoomDiv.id = 'zoom-'.concat(i.toString());
                          zoomDiv.style = "width:300px;margin-bottom:10px;margin:10px 30px;";

                          $('#timeSlider-div').append(zoomDiv);
                          var iDiv = document.createElement('div');
                          iDiv.id = i;
                          iDiv.className = 'time-slider';
                          iDiv.style = "margin: 10px 30px;";
                          $('#timeSlider-div').append(iDiv);
                      
                          //$('body').append('<div id="asdf" class="time-slider" style="width: 65%"></div>');
                          
                          //console.log(date_day_start)
                          $('#'.concat(i.toString())).TimeSlider({
                              start_timestamp: date_day_start,
                              init_cells: init_cells_temp,
                          });
                          $('#zoom-'.concat(i.toString())).slider({
                              min: 1,
                              max: 24,
                              value: 24,
                              step: 0.2,
                              slide: function(event, ui) {
                                  id = $(this).attr("id").split('-')[1];
                                  $('#'.concat(id)).TimeSlider({hours_per_ruler: ui.value});
                              }
                          });
                          current_year = timeline_list[i].year_from;
                          current_month = timeline_list[i].month_from;
                          current_day = timeline_list[i].day_from;
                          date_day_start = Date.parse(new Date(current_year, current_month-1, current_day,0,0,0)) + 3600*9*1000
                          init_cells_temp = []
                      }
              }
              //console.log(timeline_list)

              
              
          },
          error: function(ts) { 
              alert("error");
          }
      })
      
  });
});
