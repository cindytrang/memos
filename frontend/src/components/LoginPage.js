import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { useAuth } from './AuthContext';
import axios from 'axios';  // Import axios

const LoginPage = () => {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const navigate = useNavigate();
    const { setUserEmail, setToken } = useAuth();
    const [error, setError] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();
    
        try {
            const response = await axios.post("http://127.0.0.1:8000/auth/login/", {
                email: email,
                password: password
            }, {
                headers: {
                    'Content-Type': 'application/json',
                }
            });

            // setToken(response.data.token);
            // setUserEmail(email);
            // localStorage.setItem('token', response.data.token);
    
            navigate('/diary');
        } catch (err) {
            console.error('Login error:', err.response ? err.response.data : err.message);
            setError('Login failed. Please check your credentials.');
        }
    };

    return (
        <div className="login-page">
            <form onSubmit={handleSubmit} className="login-form">
                <h1>Login Page</h1>
                {error && <p style={{ color: 'red' }}>{error}</p>}
                
                <label htmlFor="email">Email:</label>
                <input 
                    type="email" 
                    id="email"
                    value={email} 
                    onChange={(e) => setEmail(e.target.value)} 
                    required 
                />
                
                <label htmlFor="password">Password:</label>
                <input 
                    type="password" 
                    id="password"
                    value={password} 
                    onChange={(e) => setPassword(e.target.value)} 
                    required 
                />
                
                <input type="submit" value="Login" />
                
                <p>Don't have an account? <a href="/register">Register</a></p>
            </form>
        </div>
    );
};

export default LoginPage;