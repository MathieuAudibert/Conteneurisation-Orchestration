import axios from 'axios';

const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

export const carService = {
  getAllCars: async () => {
    const response = await api.get('/api/v1/data/cars');
    return response.data;
  },
  
  getCarsStats: async () => {
    const response = await api.get('/api/v1/data/cars/stats');
    return response.data;
  },
};

export const logService = {
  getAllLogs: async () => {
    const response = await api.get('/api/v1/data/logs');
    return response.data;
  },
  
  getRecentLogs: async (limit = 10) => {
    const response = await api.get(`/api/v1/data/logs/recent?limit=${limit}`);
    return response.data;
  },
};

export const etlService = {
  extract: async () => {
    const response = await api.get('/api/v1/etl/extract');
    return response.data;
  },
  
  transform: async () => {
    const response = await api.get('/api/v1/etl/transform');
    return response.data;
  },
  
  load: async () => {
    const response = await api.get('/api/v1/etl/load');
    return response.data;
  },
  
  runWorkflow: async () => {
    const response = await api.get('/api/v1/etl/workflow');
    return response.data;
  },
};

export const datasetService = {
  getDataset: async () => {
    const response = await api.get('/api/v1/dataset');
    return response.data;
  },
};

export default api;
