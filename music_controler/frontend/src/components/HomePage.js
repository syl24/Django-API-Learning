import React, { Component } from 'react';
import RoomJoinPage from "./RoomJoinPage";
import CreateRoomPage from "./CreateRoomPage";
import { BrowserRouter as Router , Switch, Link, Redirect, Route } from "react-router-dom";
import Room from "./Room";

export default class HomePage extends Component{
    constructor(props){
        super(props);
    }

    renderHomePage(){
        return(
            
        );
    }

    render(){
        return (
            <Router>

                <Switch>

                    <Route exact path="/"> <p>This is the Home Page</p> </Route>
                    <Route path="/join" component={RoomJoinPage}/>
                    <Route path="/create" component={CreateRoomPage}/>
                    <Route path="/room/:roomCode" component={Room} />

                </Switch>

            </Router>
        );
    }
}