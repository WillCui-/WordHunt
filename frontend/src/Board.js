import React from "react";
import Tile from "./Tile.js";
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';

class Board extends React.Component {
    constructor(props) {
        super(props);
 
        this.state = {
            letters: "",
        }
    }

    renderTile() {
        return (
            <Col xs={1} md={1}>
                <Tile
                    value = {this.state.letters}
                />
            </Col>
        )
    }

    renderRow() {
        let rowItems = [];
        for (var i = 0; i <= 4; i++) {
            rowItems.push(this.renderTile());
        }

        return (
            <Container>
                <Row>{rowItems}</Row>
            </Container>
        )
    }

    render() { 
        return (
            <div>
                {this.renderRow()}
                {this.renderRow()}
                {this.renderRow()}
                {this.renderRow()}
            </div>
        )
    }
}

export default Board;