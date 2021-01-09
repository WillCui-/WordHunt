import React from "react";

class Tile extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            value: '1'
        };
    }


    render() {
        return <h1>{this.state.value}</h1>
    }
}

export default Tile;