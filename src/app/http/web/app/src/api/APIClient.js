import axios from 'axios';


const BASE_URL = 'http://ecology.thecodingkiwi.com:8000/api';


const client = axios.create({
    baseURL: BASE_URL,
    json: true
});


class APIClient {

    async getServers() {
        let data = await this.perform('get', '/servers');
        return data.list;
    }

    async perform(method, resource, payload) {
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