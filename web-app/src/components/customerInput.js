import 'bootstrap/dist/css/bootstrap.min.css';
import React, {useState, useEffect, Fragment} from 'react';
import { Dropdown} from 'react-bootstrap';
import {brand_and_flags, specialty_service, revenue_period, profit_type} from '../input_fields.py'

export  const CustInputPage = ({}) => {
    const [name, setName] = useState('')
    const [brand, setBrand] = useState('')
    const [flag, setFlag] = useState('')
    const [roomNumber, setRoomNumber] = useState(0)
    const [specialType, setSpecialType] = useState()
    const [occupancyRate, setOccupancyRate] = useState(0)
    const [revenue, setRevenue] = useState(0)
    const [revenuePeriod, setRevenuePeriod] = useState(0)
    const [profit, setProfit] = useState(0)
    const [profitType, setProfitType] = useState('')
    const [profitPeriod, setProfitPeriod] = useState('')
    const [email, setEmail] = useState('')



    useEffect(() => {

    }, [])
    
    const onSubmit = () => {


    }
    console.log(brand_and_flags)

    const brandOption = (e) => {

        
        return (
            <Fragment>
                <Dropdown.Item href="#/action-1">Action</Dropdown.Item>
            </Fragment>
        )
    }
    
    return (
        <div className="formCont">
            <form >
                <div class="form-group">
                    <label className="inputTitle" for="inputHotelName">Name of hotel</label>
                    <input type="text" class="form-control" id="inputHotelName" onChange={e => setName(e)} placeholder="Enter hotel name"/>
                </div>
                <Dropdown>
                <label className="inputTitle" >Brand of hotel</label>
                    <Dropdown.Toggle variant="secondary" id="dropdown-basic">
                        Choose your hotel brand
                    </Dropdown.Toggle>
                    <Dropdown.Menu>
                        <Dropdown.Item href="#/action-1">Action</Dropdown.Item>
                    </Dropdown.Menu>
                </Dropdown>
                <div class="form-group">
                    <label className="inputTitle" for="numberOfRooms">Number of rooms</label>
                    <input type="number" class="form-control" id="numberOfRooms" onChange={e => setRoomNumber(e)} placeholder="Enter number of rooms"/>
                </div>
                <Dropdown>
                <label className="inputTitle" >Specialty type</label>
                    <Dropdown.Toggle variant="secondary" id="dropdown-basic">
                        Choose your specialty
                    </Dropdown.Toggle>
                    <Dropdown.Menu>
                        <Dropdown.Item href="#/action-1">Action</Dropdown.Item>
                        <Dropdown.Item href="#/action-2">Another action</Dropdown.Item>
                        <Dropdown.Item href="#/action-3">Something else</Dropdown.Item>
                    </Dropdown.Menu>
                </Dropdown>
                <div class="form-group">
                    <label className="inputTitle" for="averageOccupancyRate">Average occupancy rate</label>
                    <input type="number" class="form-control" id="averageOccupancyRate" onChange={e => setOccupancyRate(e)} placeholder="Enter the average occupancy rate of your hotel"/>
                </div>
                <div class="form-group">
                    <label className="inputTitle" for="revenue">Revenue</label>
                    <input type="number" class="form-control" id="revenue"  onChange={e => setRevenue(e)} placeholder="Enter revenue"/>
                </div>
                <Dropdown>
                <label className="inputTitle">Revenue period</label>
                    <Dropdown.Toggle variant="secondary" id="dropdown-basic">
                        Choose your revenue period
                    </Dropdown.Toggle>
                    <Dropdown.Menu>
                        <Dropdown.Item href="#/action-1">Action</Dropdown.Item>
                        <Dropdown.Item href="#/action-2">Another action</Dropdown.Item>
                        <Dropdown.Item href="#/action-3">Something else</Dropdown.Item>
                    </Dropdown.Menu>
                </Dropdown>
                <div class="form-group">
                    <label className="inputTitle" for="profit">Profit</label>
                    <input type="number" class="form-control" id="profit"  onChange={e => setProfit(e)} placeholder="Enter profit"/>
                </div>
                <Dropdown>
                <label className="inputTitle">Profit type</label>
                    <Dropdown.Toggle variant="secondary" id="dropdown-basic">
                        Choose your profit type
                    </Dropdown.Toggle>
                    <Dropdown.Menu>
                        <Dropdown.Item href="#/action-1">Action</Dropdown.Item>
                        <Dropdown.Item href="#/action-2">Another action</Dropdown.Item>
                        <Dropdown.Item href="#/action-3">Something else</Dropdown.Item>
                    </Dropdown.Menu>
                </Dropdown>
                <Dropdown>
                <label className="inputTitle" for="inputHotelName">Profit period</label>
                    <Dropdown.Toggle variant="secondary" id="dropdown-basic">
                        Choose your profit period
                    </Dropdown.Toggle>
                    <Dropdown.Menu>
                        <Dropdown.Item href="#/action-1">Action</Dropdown.Item>
                        <Dropdown.Item href="#/action-2">Another action</Dropdown.Item>
                        <Dropdown.Item href="#/action-3">Something else</Dropdown.Item>
                    </Dropdown.Menu>
                </Dropdown>
                <div class="form-group">
                    <label className="inputTitle" for="inputEmail1">Email address</label>
                    <input type="email" class="form-control" id="exampleInputEmail1" onChange={e => setEmail(e)} aria-describedby="emailHelp" placeholder="Enter email"/>
                    <small id="emailHelp" class="form-text">We'll never share your email with anyone else.</small>
                </div>
                <button type="submit" onClick={onSubmit()} class="btn btn-primary">Submit</button>
            </form>
       </div>
    )
    
}