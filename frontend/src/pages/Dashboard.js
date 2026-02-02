import React, { useState, useEffect } from 'react';
import { 
  Car, 
  ScrollText, 
  TrendingUp, 
  Database,
  Activity,
  RefreshCw
} from 'lucide-react';
import { carService, logService } from '../services/api';

const Dashboard = () => {
  const [stats, setStats] = useState({
    totalCars: 0,
    totalLogs: 0,
    avgPrice: 0,
  });
  const [loading, setLoading] = useState(true);
  const [recentCars, setRecentCars] = useState([]);

  const fetchDashboardData = async () => {
    setLoading(true);
    try {
      const [carsResponse, logsResponse] = await Promise.all([
        carService.getAllCars(),
        logService.getAllLogs(),
      ]);

      const cars = carsResponse.data || [];
      const logs = logsResponse.data || [];

      const avgPrice = cars.length > 0 
        ? cars.reduce((sum, car) => sum + (car.price || 0), 0) / cars.length 
        : 0;

      setStats({
        totalCars: carsResponse.count || 0,
        totalLogs: logsResponse.count || 0,
        avgPrice: avgPrice,
      });

      setRecentCars(cars.slice(-5).reverse());
    } catch (error) {
      console.error('Error fetching dashboard data:', error);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchDashboardData();
  }, []);

  const statCards = [
    {
      icon: Car,
      value: stats.totalCars,
      label: 'Total Cars',
      color: 'linear-gradient(135deg, #6366f1 0%, #4f46e5 100%)',
      change: '+12%',
      positive: true,
    },
    {
      icon: ScrollText,
      value: stats.totalLogs,
      label: 'System Logs',
      color: 'linear-gradient(135deg, #ec4899 0%, #db2777 100%)',
      change: '+5%',
      positive: true,
    },
    {
      icon: TrendingUp,
      value: `$${stats.avgPrice.toFixed(0)}`,
      label: 'Average Price',
      color: 'linear-gradient(135deg, #14b8a6 0%, #0d9488 100%)',
      change: '+8%',
      positive: true,
    },
    {
      icon: Database,
      value: '100%',
      label: 'Database Health',
      color: 'linear-gradient(135deg, #10b981 0%, #059669 100%)',
      change: 'Optimal',
      positive: true,
    },
  ];

  if (loading) {
    return (
      <div className="loading-container">
        <div className="loading-spinner"></div>
        <p>Loading dashboard...</p>
      </div>
    );
  }

  return (
    <div className="fade-in">
      <div className="header">
        <div>
          <h1 className="header-title">Dashboard</h1>
          <p style={{ color: 'var(--text-secondary)', marginTop: '0.5rem' }}>
            Welcome to your ETL management dashboard
          </p>
        </div>
        <div className="header-actions">
          <button className="btn btn-glass" onClick={fetchDashboardData}>
            <RefreshCw size={20} />
            Refresh
          </button>
          <button className="btn btn-primary">
            <Activity size={20} />
            Run ETL
          </button>
        </div>
      </div>

      <div className="stats-grid">
        {statCards.map((stat, index) => {
          const Icon = stat.icon;
          return (
            <div key={index} className="stat-card glass-card">
              <div className="stat-card-header">
                <div className="stat-card-icon" style={{ background: stat.color }}>
                  <Icon />
                </div>
              </div>
              <div className="stat-card-value">{stat.value}</div>
              <div className="stat-card-label">{stat.label}</div>
              <div className={`stat-card-change ${stat.positive ? 'positive' : 'negative'}`}>
                <TrendingUp size={16} />
                <span>{stat.change}</span>
              </div>
            </div>
          );
        })}
      </div>

      <div className="grid grid-2">
        <div className="glass-card">
          <h2 style={{ marginBottom: '1rem', display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
            <Car size={24} />
            Recent Cars
          </h2>
          {recentCars.length > 0 ? (
            <div style={{ display: 'flex', flexDirection: 'column', gap: '0.75rem' }}>
              {recentCars.map((car, index) => (
                <div 
                  key={index} 
                  style={{ 
                    padding: '1rem', 
                    background: 'var(--glass-bg)', 
                    borderRadius: 'var(--radius-sm)',
                    border: '1px solid var(--glass-border)'
                  }}
                >
                  <div style={{ fontWeight: 600, marginBottom: '0.25rem' }}>
                    {car.brand} {car.model}
                  </div>
                  <div style={{ fontSize: '0.875rem', color: 'var(--text-secondary)' }}>
                    ${car.price?.toLocaleString()} • {car.make_year}
                  </div>
                </div>
              ))}
            </div>
          ) : (
            <div className="empty-state">
              <Car size={48} />
              <p>No cars available</p>
            </div>
          )}
        </div>

        <div className="glass-card">
          <h2 style={{ marginBottom: '1rem', display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
            <Activity size={24} />
            System Activity
          </h2>
          <div style={{ display: 'flex', flexDirection: 'column', gap: '0.75rem' }}>
            <div style={{ 
              padding: '1rem', 
              background: 'var(--glass-bg)', 
              borderRadius: 'var(--radius-sm)',
              border: '1px solid var(--glass-border)'
            }}>
              <div style={{ fontWeight: 600, marginBottom: '0.25rem' }}>ETL Pipeline</div>
              <div style={{ fontSize: '0.875rem', color: 'var(--success)' }}>Running smoothly</div>
            </div>
            <div style={{ 
              padding: '1rem', 
              background: 'var(--glass-bg)', 
              borderRadius: 'var(--radius-sm)',
              border: '1px solid var(--glass-border)'
            }}>
              <div style={{ fontWeight: 600, marginBottom: '0.25rem' }}>Database Connection</div>
              <div style={{ fontSize: '0.875rem', color: 'var(--success)' }}>Connected</div>
            </div>
            <div style={{ 
              padding: '1rem', 
              background: 'var(--glass-bg)', 
              borderRadius: 'var(--radius-sm)',
              border: '1px solid var(--glass-border)'
            }}>
              <div style={{ fontWeight: 600, marginBottom: '0.25rem' }}>Last Backup</div>
              <div style={{ fontSize: '0.875rem', color: 'var(--text-secondary)' }}>2 hours ago</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Dashboard;
