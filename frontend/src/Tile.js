import React from "react";
import Button from 'react-bootstrap/Button';

class Tile extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            value: '111'
        };
    }

    render() {
        return <Button className="square" variant="light">{this.state.value}</Button>
    }
}

export default Tile;