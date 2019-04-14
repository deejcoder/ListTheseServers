import React from 'react';

import { Grid } from '@material-ui/core';

import APIClient from '../../api/APIClient';
import ServerCardGridRow from './ServerCardGridRow';

class ServerCardGrid extends React.Component {
    constructor(props) {
        super(props)

        this.state = {
            servers: [],
        }
    }

    async componentDidMount() {
        // initially get the servers
        this.apiClient = new APIClient()
        await this.updateServerList();

        // update the servers every 5s
        this.timerID = setInterval(() => this.tick(), 5000);
    }

    componentWillUnmount() {
        // stop updating servers
        clearInterval(this.timerID);
    }

    tick() {
        // note this isn't awaited for a reason
        this.updateServerList();
    }

    async updateServerList() {
        let data = await this.apiClient.getServers();

        // if there is a connection error, [] will be returned, avoid updating
        if(data) {
            this.setState({...this.state, servers: data})
        }
    }

    render() {

        // organize cards into a grid (e.g 4xN matrix)
        let grid = [], servers = this.state.servers;
        while(servers.length) grid.push(servers.splice(0, 4));

        let output = grid.map((row, index) => {
            return (
                <Grid key={index} container spacing={8}>
                    <Grid container item xs={5} spacing={24}>
                        <ServerCardGridRow items={row} />
                    </Grid>
                </Grid>
            );
        });
        return (
            <div id="serverlist">
                {output}
            </div>
        );
    }
}

export default ServerCardGrid;