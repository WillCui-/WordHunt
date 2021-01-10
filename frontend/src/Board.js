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
            <Tile value = {this.state.letters}/>
        )
    }

    renderRow() {
        let rowItems = [];
        for (var i = 0; i < 4; i++) {
            rowItems.push(this.renderTile());
        }

        return (
                <div>{rowItems}</div>
            
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

function Square(props) {
    return (
      <div className="square-big" background-color="lightblue"></div>
    );
  }

export default Board;