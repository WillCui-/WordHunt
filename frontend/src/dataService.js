import axios from 'axios';

class DataService {
    getLetters() {
        let data;
        axios.get(`http://localhost:5000/letters`).then(res => {
            data = res.data;
        })
        return data;
    }
}

export default DataService;