import React from 'react';

import Visavail from 'visavail';
import d3 from 'd3';


class ServerActivityChart extends React.Component {

    render() {

        let chart = Visavail.visavailChart().width(200);
        d3.select("#activity-chart")
            .datum(dataset)
            .call(chart);

        return (
            <div id="activity-chart"></div>
        );
    }
}