/**
 * Configuration file for Gas Leak Detection System
 * Contains all constants used in the web interface
 */

// API Endpoints
const CONFIG = {
    // API Base URLs
    API_BASE_URL: "https://vzrbxh0b-5000.inc1.devtunnels.ms", // Replace with your actual base URL
    LOCAL_API_BASE_URL: "http://127.0.0.1:5000",
    
    // Sensor API Endpoints
    SENSOR1_API: "/api/sensor1",
    SENSOR2_API: "/api/sensor2",
    
    // Buzzer Control Endpoints
    BUZZER1_ON_API: "/api/sensor1/buzzon",
    BUZZER1_OFF_API: "/api/sensor1/buzzoff",
    BUZZER2_ON_API: "/api/sensor2/buzzon",
    BUZZER2_OFF_API: "/api/sensor2/buzzoff",
    
    // Weather API
    WEATHER_API_URL: "https://wttr.in/Mangalore,Karnataka,India?format=j1",
    WEATHER_LOCATION: "Mangalore,Karnataka,India",
    
    // Update Intervals (milliseconds)
    SENSOR_UPDATE_INTERVAL: 1000,  // 1 second
    WEATHER_UPDATE_INTERVAL: 120000,  // 2 minutes
    
    // Chart Configuration
    MAX_CHART_POINTS: 20,
    
    // Thresholds
    AIR_QUALITY_POOR_THRESHOLD: 750,
    AIR_QUALITY_MODERATE_THRESHOLD: 650,
    
    // UI Configuration
    CHART_COLORS: {
        TEMPERATURE: {
            BORDER: '#0bda5e',
            BACKGROUND: 'rgba(11, 218, 94, 0.1)'
        },
        HUMIDITY: {
            BORDER: '#60a5fa',
            BACKGROUND: 'rgba(96, 165, 250, 0.1)'
        }
    },
    
    // Helper function to get full API URL
    getApiUrl: function(endpoint) {
        return this.API_BASE_URL + endpoint;
    },
    
    getLocalApiUrl: function(endpoint) {
        return this.LOCAL_API_BASE_URL + endpoint;
    }
};
