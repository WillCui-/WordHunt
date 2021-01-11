import React from "react";
import Button from 'react-bootstrap/Button';

class Tile extends React.Component {
    
    render() {
        return (
            <Button 
                variant="light"
                onKeyDown={this.props.onKeyDown}
                style={{
                    background: '#caa472',
                    'font-size': '20px',
                    'font-weight': 600,
                    height: '50px', 
                    width: '50px',}}>
                {this.props.value}
            </Button>
        )
    }
}

export default Tile;