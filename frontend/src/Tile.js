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
                    'fontSize': '20px',
                    'fontWeight': '600',
                    height: '50px', 
                    width: '50px',}}>
                {this.props.value}
            </Button>
        )
    }
}

export default Tile;