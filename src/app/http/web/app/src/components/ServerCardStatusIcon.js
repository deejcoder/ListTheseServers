import React from 'react';

import { Tooltip } from '@material-ui/core';
import { CheckCircle, OfflineBolt } from '@material-ui/icons';


class ServerStatusIcon extends React.Component {

    render() {

        const onlineStyle = {
            color: 'green',
        }

        const offlineStyle = {
            color: 'orange',
        }

        if(!this.props.status) {
            return (
                <Tooltip title="Offline" placement="top">
                    <OfflineBolt style={offlineStyle} />
                </Tooltip>
            )
        }
        
        else {
            return(
                <Tooltip title="Online" placement="top">
                    <CheckCircle style={onlineStyle} />
                </Tooltip>
            )
        }
    }
}

export default ServerStatusIcon;