import React from "react";
import Card from 'react-bootstrap/Card';
import ListGroup from 'react-bootstrap/ListGroup';

class Results extends React.Component {
    generateListGroup() {
        let results = [];
        for(var i = 0; i < this.props.results.length; i++) {
            results.push(<ListGroup.Item key={i}>{this.props.results[i]}</ListGroup.Item>)
        }

        return (
            <ListGroup variant='flush' style={{'text-align': 'left'}}>
                {results}
            </ListGroup>
        )
    }

    render() {
        return (
            <Card>
                <Card.Header as="h5">Possible Words</Card.Header>
                {this.generateListGroup()}
            </Card>
        )
    }
}

export default Results;