import React from "react";
import Tile from "./Tile.js";

function Board(props) {
    
    function renderTile(key) {
        return (
            <Tile 
                value = {props.letters[key]}
                key = {key}
                tabIndex="0"
            />
        )
    }

    function renderRow(row) {
        let rowItems = [];
        for(var i = 0; i < 4; i++) {
            rowItems.push(renderTile(row * 4 + i));
        }

        return (
            <div key={row}>
                {rowItems}
            </div>
        )
    }

    function renderBoard() {
        let items = [];
        for(var i = 0; i < 4; i++) {
            items.push(renderRow(i))
        }

        return (
            <Square
                value={items}> 
            </Square>
        )
    }

    return (
        <div>
            {renderBoard()}
        </div>
    );
}

function Square(props) {
    return (
        <div style={{
            background: 'rgb(117, 38, 38)',
            border: '3px solid yellowgreen',
            'borderRadius': '10px',
            height: '220px',
            'paddingTop': '7px',
            width: '220px',
            'zIndex': -999,
        }}>
            {props.value}
        </div>
    );
}

export default Board;