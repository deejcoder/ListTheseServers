import React from 'react';

import { Grid } from '@material-ui/core';
import ServerCard from './ServerCard';


class ServerCardGridRow extends React.Component {

    render() {

        // create a card for each server
        let servers = []
        Object.values(this.props.items).map((server, index) => {
            servers.push(
                <Grid item xs={5}>
                    <ServerCard
                        key={index}
                        serverName={server.server_name}
                        ipAddress={server.ip_address}
                        port={server.port}
                        description={server.description}
                        status={server.status}
                    />
                </Grid>
            )
        })

        return (
            <React.Fragment>
                {servers}
            </React.Fragment>
        );
    }
}

export default ServerCardGridRow;