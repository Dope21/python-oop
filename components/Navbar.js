import React, { useState, useEffect } from 'react';
import axios from 'axios';
import "./NavbarStyles.css";


const Navbar = () => {
  const [showDropdown, setShowDropdown] = useState(false);
  const [catagory, setcatagory] = useState([]);

  useEffect(() => {
    axios.get('http://localhost:8000/api/catagory/')
      .then(response => {
        setcatagory(response.data);
      })
      .catch(error => {
        console.error(error);
      });
  }, []);


  return (
<>
  <p class="fourday">All the products will be shipped within 4 business days.</p>

<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"></link>
    
    <div class="Navbar">
    <a><img src="//cdn.shopify.com/s/files/1/0328/6034/0364/files/Keychron-logo-black_140x.png?v=1663761190" srcset="//cdn.shopify.com/s/files/1/0328/6034/0364/files/Keychron-logo-black_140x.png?v=1663761190 1x, //cdn.shopify.com/s/files/1/0328/6034/0364/files/Keychron-logo-black_140x@2x.png?v=1663761190 2x" alt="Keychron" itemprop="logo" /></a>
        <div class="dropdown">
          
            <button class="dropbtn">All Products 
              <i class="fa fa-caret-down"></i>
            </button>
            <div class="dropdown-content">
              <a href="#">Service 1</a>
              <a href="#">Service 2</a>
              <a href="#">Service 3</a>
            </div>
          </div> 

          <div class="dropdown">
            <button class="dropbtn">All Keyboards 
              <i class="fa fa-caret-down"></i>
            </button>
            <div class="dropdown-content">
              <a href="#">Service 1</a>
              <a href="#">Service 2</a>
              <a href="#">Service 3</a>
            </div>
          </div> 
      
          <div class="dropdown">
            <button class="dropbtn">Custom Keyboards 
            <i class="fa fa-caret-down"></i>
            </button>
            <div class="dropdown-content">
              <a href="#">Service 1</a>
              <a href="#">Service 2</a>
              <a href="#">Service 3</a>
            </div>
          </div> 
      

          <div class="dropdown">
            <button class="dropbtn">Low profile Keyboards
            <i class="fa fa-caret-down"></i>
            </button>
            <div class="dropdown-content">
              <a href="#">Service 1</a>
              <a href="#">Service 2</a>
              <a href="#">Service 3</a>
            </div>
          </div> 
          <div class="dropdown">
            <button class="dropbtn">Accessories 
              <i class="fa fa-caret-down"></i>
            </button>
            <div class="dropdown-content">
              <a href="#">Service 1</a>
              <a href="#">Service 2</a>
              <a href="#">Service 3</a>
            </div>
            
          </div> 
            <div class="navbar-right">
                <a href="#" class="icon-link">
                  <div class="visible">
                    <i class="fa fa-user" aria-hidden="true"></i>
                  </div></a>
                <a href="#" class="icon-link"><i class="fa fa-search" aria-hidden="true"></i></a>
                <a href="#" class="icon-link"><i class="fa fa-suitcase" aria-hidden="true"></i></a>
          </div>

    </div>
 
</>

  );
};

export default Navbar;