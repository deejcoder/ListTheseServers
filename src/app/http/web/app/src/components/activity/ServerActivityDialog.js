import React from 'react';

import { Button, Dialog } from '@material-ui/core';
import {
    DialogTitle,
    DialogContent,
    DialogContentText,
    DialogActions
} from '@material-ui/core/Dialog';


/**
 * A dialog to show the downtime of a server
 */
class ServerActivityDialog extends React.Component {

    constructor(props) {
        super(props);
        
        this.state = {
            open: false,
            server_id: null,
            activity: [],
        }
    }

    handleClickOpen = () => {
        this.setState({ open: true });
    };

    handleClose = () => {
        this.setState({ open: false });
    };

    render() {
        return (
            <React.Fragment>
                <Button size="small" color="primary" onClick={this.handleClickOpen}>View</Button>

                <Dialog
                    open={this.state.open}
                    onClose={this.handleClose}
                    aria-labelledby="dialog-server-activity"
                >
                    <DialogTitle id="dialog-server-activity">{this.props.serverName}</DialogTitle>
                    <DialogContent>
                        <DialogContentText>
                            To be replaced with graph...
                        </DialogContentText>
                    </DialogContent>

                    <DialogActions>
                        <Button onclick={this.handleClose} color="primary">
                            Close
                        </Button>
                    </DialogActions>
                
                </Dialog>

            </React.Fragment>
        );
    }
}

export default ServerActivityDialog;