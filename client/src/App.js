import React, { useEffect } from 'react';
import axios from 'axios';
import { createContext, useState } from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import { BrowserView } from 'react-device-detect';
import { ToastContainer } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';

// Desktop version:
import Header from './desktop/components/Header';

import MainPage from './desktop/Pages/MainPage';
import LoginPage from './desktop/Pages/LoginPage';
import RegisterPage from './desktop/Pages/RegisterPage';
import LogoutPage from './desktop/Pages/LogoutPage';
import ForgotPasswordPage from './desktop/Pages/ForgotPasswordPage';
import LandingPage from './desktop/Pages/LandingPage';
import SettingsPage from './desktop/Pages/SettingPage';


const Data = createContext(null);

function App() {
  const [data, setData] = useState({
    auth: localStorage.getItem("auth") === "true" || false,
    access_token: localStorage.getItem("access_token"),
    avatar: localStorage.getItem("avatar"),
    username: localStorage.getItem("username"),
    user_id: localStorage.getItem('user_id')
  })

  axios.defaults.baseURL = "ANY SERVER URL";
  axios.defaults.headers.post['Content-Type'] = 'application/json';
  
  useEffect(() => {
    axios.defaults.headers.common['Authorization'] = `Bearer ${data.access_token}`
  }, [data])
  
  const setterWithObserver = (data) => {
    setData({...data});
    console.log("Observer: ", data);
    localStorage.setItem("auth", data.auth);
    localStorage.setItem("access_token", data.access_token);
    localStorage.setItem("avatar", data.avatar);
    localStorage.setItem("username", data.username);
    localStorage.setItem("user_id", data.user_id)
  }

  return (
    <>
      <BrowserView>
      <BrowserRouter>
        {/* desktop version */}
        <Data.Provider value={{user: data, setter: setterWithObserver}}>
          <Header />
          <Routes>
            <Route path="/*" element={<LandingPage />} />
            <Route path='/login' element={<LoginPage />} />
            <Route path="/logout" element={<LogoutPage />} />
            <Route path="/register" element={<RegisterPage />} />
            <Route path="/forgot-password" element={<ForgotPasswordPage />} />
            <Route path='/dialogs' element={<MainPage />} />            
            <Route path="/settings" element={<SettingsPage />} />

          </Routes>
        </Data.Provider>
      </BrowserRouter>
      </BrowserView>
      
      {/* toastify container for notifications */}
      <ToastContainer
				position="bottom-right"
				autoClose={5000}
				hideProgressBar={false}
				newestOnTop={false}
				closeOnClick
				rtl={false}
				pauseOnFocusLoss
				draggable
				pauseOnHover
				theme="colored" />
    </>
  );
}

export default App;
export {Data};