import React from "react";
import Board from './Board.js';
import Results from './Results.js';

import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Card from "react-bootstrap/Card";

class Game extends React.Component {
    render() {
        return (
            <Card>
                <Card.Header as="h5">WordHunt Helper</Card.Header>
                <Card.Body style={{padding: '50px'}}>
                    <Container>
                        <Row>
                            <Col><Board /></Col>
                            <Col><Results /></Col>
                        </Row>
                    </Container>
                </Card.Body>
            </Card>
        )
    }
}

export default Game;