import React from "react";
import Button from 'react-bootstrap/Button';

class Tile extends React.Component {
    
    render() {
        return (
            <Button 
                className="square" 
                variant="light"
                onKeyDown={this.props.onKeyDown}>
                {this.props.value}
            </Button>
        )
    }
}

export default Tile;