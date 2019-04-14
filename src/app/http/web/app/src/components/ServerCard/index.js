import React from 'react';

import { Card, CardHeader, CardContent, CardActions } from '@material-ui/core';
import { Typography, Button, Tooltip } from '@material-ui/core';

import ServerStatusIcon from './ServerStatusIcon';


class ServerCard extends React.Component {
    /**
     * Represents a single server; each server will regularly
     * be updated using a tick function
     * @param {*} props 
     */

    constructor(props) {
        super(props);
    }

    render() {

        return (
            <Card>
                <CardHeader
                    action={
                        <ServerStatusIcon status={this.props.status} />
                    }
                    title={this.props.serverName}
                    subheader={`${this.props.ipAddress}:${this.props.port}`}

                />
                <CardContent>
                    <Typography component="p">
                        {this.props.description}
                    </Typography>
                </CardContent>
                <CardActions>
                    <Button size="small" color="primary">View</Button>
                    <Button size="small" color="primary">Copy</Button>
                </CardActions>
            </Card>
        );
    }
}


export default ServerCard;
