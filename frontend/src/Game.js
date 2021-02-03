import React, { useState, useEffect } from "react";
import axios from 'axios';

import Board from './Board.js';
import Results from './Results.js';


import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Card from "react-bootstrap/Card";

function Game(props) {
    const [letters, setLetters] = useState([]);
    const [results, setResults] = useState([]);

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
        axios.post(`http://localhost:5000/api/letters`, formData)
            .then(res => {
                setResults(res.data['results']);
            }).catch(error => {
                console.log(error.response);
            });
    }

    return (
        <Card style={{
            width: '100%', 
        }}>
            <Card.Header as="h5">WordHunt Helper</Card.Header>
            <Card.Body style={{
                paddingBottom: '50px',
            }}>
                <Container fluid>
                    <Row className="justify-content-md-center" style={{padding: '50px'}}>
                        <Col md='auto'>
                            <Board 
                                letters={ letters }
                            />
                        </Col>
                    </Row>
                    <Row>
                        <Col>
                            <Results 
                                results={ results }
                            />
                        </Col>
                    </Row>
                </Container>
            </Card.Body>
        </Card>
    );
}

export default Game;