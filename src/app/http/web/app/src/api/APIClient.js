import axios from 'axios';


const BASE_URL = 'http://ecology.thecodingkiwi.com:8000/api';


const client = axios.create({
    baseURL: BASE_URL,
    json: true
});


class APIClient {

    /**
     * Returns a list of servers
     */
    async getServers() {
        let data = await this._fetch('get', '/servers');
        return data.list;
    }

    /**
     * Returns a list of ping results
     * @param {*} id the server ID
     */
    getServerActivity(id) {
        //let activity = await getServerActivity(1); console.log(activity) :: used for testing
        return this._fetch('get',`/servers/${id}/activity`);
    }


    /**
     * Makes an API request
     * @param {string} method HTTP method
     * @param {string} resource URL
     * @param {*} payload body
     */
    async _fetch(method, resource, payload) {
        return client({
            method,
            url: resource,
            payload,
            headers: {}
        }).then(resp => {
            return resp.data ? resp.data : [];
        })
    }
}

export default APIClient;