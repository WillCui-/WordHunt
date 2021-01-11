import React from "react";
import Card from 'react-bootstrap/Card';

class Results extends React.Component {
    render() {
        return (
            <Card>
                <Card.Header as="h5">Possible Words</Card.Header>
                <Card.Body  className="d-flex align-items-start">
                    <Card.Text>
                        Words
                    </Card.Text>
                </Card.Body>
            </Card>
        )
    }
}

export default Results;