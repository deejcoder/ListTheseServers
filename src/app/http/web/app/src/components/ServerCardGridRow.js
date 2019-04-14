import React from 'react';

import { Grid } from '@material-ui/core';
import ServerCard from './ServerCard';


class ServerCardGridRow extends React.Component {

    render() {

        // create a card for each server
        let items = this.props.items;
        let servers = items.map((server, index) => {
            return (
                <Grid key={index} item xs={5}>
                    <ServerCard
                        serverName={server.server_name}
                        ipAddress={server.ip_address}
                        port={server.port}
                        description={server.description}
                        status={server.status}
                    />
                </Grid>
            );
        })

        return (
            <React.Fragment>
                {servers}
            </React.Fragment>
        );
    }
}

export default ServerCardGridRow;