import React, { useState, useEffect } from "react";
import Tile from "./Tile.js";
import axios from 'axios';

function Board(props) {
    let data;
    // axios.get(`http://localhost:5000/letters`).then(res => {
    //     data = res.data;
    // });
    // console.log(data)
    // // let lets = DataService.getLetters();
    const [letters, setLetters] = useState([]);

    useEffect(() => {
        function handleKey(e) {
            const c = e.key;
            if (e.keyCode === 8) {
                setLetters(l => l.slice(0, l.length - 1));
            } else if (letters.length < 16 && c.length === 1 && c.match(/[a-zA-Z]/i)) {
                setLetters(l => l.concat([c.toUpperCase()]));
                
            }
        };

        document.addEventListener('keydown', handleKey);

        return function cleanup() {
            document.removeEventListener('keydown', handleKey);
        }
    }, [letters]);

    if (letters.length === 16) {
        const formData = new FormData();
        let messages = '';
        letters.forEach(l => {
            messages += l;
        });
        formData.append("letters", messages);
        axios.post(`http://localhost:5000/letters`, formData)
            .then(res => {
                console.log("posting", res.data['results']);
            }).catch(error => {
                console.log(error.response);
            });
    }

    function renderTile(key) {
        return (
            <Tile 
                value = {letters[key]}
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
            'border-radius': '10px',
            height: '220px',
            'padding-top': '7px',
            width: '220px',
            'z-index': -999,
        }}>
            {props.value}
        </div>
    );
}

export default Board;