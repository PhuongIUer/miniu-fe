import ngrokDomain from './domain.json';

const EnvironmentConfig = {
  // Base URLs
  NGROK_BASE_URL: ngrokDomain.domain + "/api",

  // API Endpoints
  API_ENDPOINTS: {
    USERS: "/users",
    PRODUCTS: "/products",
    ORDERS: "/orders"
  },
};

export default EnvironmentConfig;
