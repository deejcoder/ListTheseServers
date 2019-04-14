import React from 'react';
import APIClient from '../../apiClient';
import ServerCard from '../ServerCard';


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

        let servers = []
        Object.values(this.state.servers).map((server, index) => {
            servers.push(
                <ServerCard
                    key={index}
                    serverName={server.server_name}
                    ipAddress={server.ip_address}
                    port={server.port}
                    description={server.description}
                    status={server.status}
                />
            )
        })
        return (
            <div id="serverlist">
                {servers}
            </div>
        );
    }
}

export default ServerCardGrid;