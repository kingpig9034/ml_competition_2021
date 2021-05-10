
Keen.ready(function () {

  // Pageviews by browser

  const pageviews_timeline = new KeenDataviz({
    container: '#chart-01',
    title: 'Pageviews by browser',
    type: 'area',
    stacked: true,
    sortGroups: 'desc'
  });

  client
    .query('count', {
      event_collection: 'pageviews',
      interval: 'hourly',
      group_by: 'user.device_info.browser.family',
      timeframe: {
        start: '2014-05-04T00:00:00.000Z',
        end: '2014-05-05T00:00:00.000Z'
      }
    })
    .then(res => {
      pageviews_timeline
        .data(res)
        .render();
    })
    .catch(err => {
      pageviews_timeline.message(err.message)
    });


  // Pageviews by browser (pie)

  const pageviews_pie = new KeenDataviz({
    container: '#chart-02',
    type: 'pie',
    title: 'Pageviews by browser',
    sortGroups: 'desc'
  });
  const data = {
    "result": [{
      "color": "Blue",
      "result": 2
    }, {
      "color": "Red",
      "result": 1
    }]
  }
  
  pageviews_pie
    .render(data);
  


  // Impressions timeline

  const impressions_timeline = new KeenDataviz({
    container: '#chart-03',
    title: 'Impressions by advertiser',
    type: 'bar',
    stacked: true,
    sortGroups: 'desc'
  });

  client
    .query('count', {
      event_collection: 'impressions',
      group_by: 'ad.advertiser',
      interval: 'hourly',
      timeframe: {
        start: '2014-05-04T00:00:00.000Z',
        end: '2014-05-05T00:00:00.000Z'
      }
    })
    .then(res => {
      impressions_timeline
        .data(res)
        .render();
    })
    .catch(err => {
      impressions_timeline.message(err.message)
    });

  // Impressions by device

  const impressions_by_device = new KeenDataviz({
    container: '#chart-04',
    title: 'Impressions by device',
    type: 'bar',
    stacked: true,
    sortGroups: 'desc'
  });

  client
    .query('count', {
      event_collection: 'impressions',
      group_by: 'user.device_info.device.family',
      interval: 'hourly',
      timeframe: {
        start: '2014-05-04T00:00:00.000Z',
        end: '2014-05-05T00:00:00.000Z'
      }
    })
    .then(res => {
      impressions_by_device
        .data(res)
        .render();
    })
    .catch(err => {
      impressions_by_device.message(err.message)
    });


  // Impressions by country

  const impressions_by_country = new KeenDataviz({
    container: '#chart-05',
    title: 'Impressions by country',
    type: 'bar',
    stacked: true,
    sortGroups: 'desc'
  });

  client
    .query('count', {
      event_collection: 'impressions',
      group_by: 'user.geo_info.country',
      interval: 'hourly',
      timeframe: {
        start: '2014-05-04T00:00:00.000Z',
        end: '2014-05-05T00:00:00.000Z'
      }
    })
    .then(res => {
      impressions_by_country
        .data(res)
        .render();
    })
    .catch(err => {
      impressions_by_country.message(err.message)
    });

});