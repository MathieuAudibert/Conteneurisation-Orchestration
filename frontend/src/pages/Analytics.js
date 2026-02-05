import React, { useState, useEffect } from 'react';
import { 
  BarChart3, 
  TrendingUp, 
  DollarSign, 
  Fuel,
  Calendar,
  Award
} from 'lucide-react';
import { carService } from '../services/api';

const Analytics = () => {
  const [stats, setStats] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchAnalytics();
  }, []);

  const fetchAnalytics = async () => {
    setLoading(true);
    try {
      const response = await carService.getAllCars();
      const cars = response.data || [];
      
      // Calculate analytics
      const totalCars = cars.length;
      const avgPrice = cars.reduce((sum, car) => sum + (car.price || 0), 0) / totalCars;
      const maxPrice = Math.max(...cars.map(car => car.price || 0));
      const minPrice = Math.min(...cars.filter(car => car.price > 0).map(car => car.price || 0));
      
      // Fuel type distribution
      const fuelTypes = cars.reduce((acc, car) => {
        const fuel = car.fuel_type || 'Unknown';
        acc[fuel] = (acc[fuel] || 0) + 1;
        return acc;
      }, {});
      
      // Brand distribution
      const brands = cars.reduce((acc, car) => {
        const brand = car.brand || 'Unknown';
        acc[brand] = (acc[brand] || 0) + 1;
        return acc;
      }, {});
      
      const topBrands = Object.entries(brands)
        .sort((a, b) => b[1] - a[1])
        .slice(0, 5);
      
      // Year distribution
      const years = cars.reduce((acc, car) => {
        const year = car.make_year || 'Unknown';
        acc[year] = (acc[year] || 0) + 1;
        return acc;
      }, {});
      
      setStats({
        totalCars,
        avgPrice,
        maxPrice,
        minPrice,
        fuelTypes,
        topBrands,
        years,
      });
    } catch (error) {
      console.error('Error fetching analytics:', error);
    } finally {
      setLoading(false);
    }
  };

  if (loading) {
    return (
      <div className="loading-container">
        <div className="loading-spinner"></div>
        <p>Loading analytics...</p>
      </div>
    );
  }

  if (!stats) {
    return <div>No data available</div>;
  }

  return (
    <div className="fade-in">
      <div className="header">
        <div>
          <h1 className="header-title">Analytics Dashboard</h1>
          <p style={{ color: 'var(--text-secondary)', marginTop: '0.5rem' }}>
            Insights and statistics from your car database
          </p>
        </div>
      </div>

      <div className="stats-grid">
        <div className="glass-card stat-card">
          <div className="stat-card-header">
            <div className="stat-card-icon" style={{ background: 'linear-gradient(135deg, #6366f1 0%, #4f46e5 100%)' }}>
              <DollarSign />
            </div>
          </div>
          <div className="stat-card-value">${stats.avgPrice.toFixed(0)}</div>
          <div className="stat-card-label">Average Price</div>
        </div>

        <div className="glass-card stat-card">
          <div className="stat-card-header">
            <div className="stat-card-icon" style={{ background: 'linear-gradient(135deg, #10b981 0%, #059669 100%)' }}>
              <TrendingUp />
            </div>
          </div>
          <div className="stat-card-value">${stats.maxPrice.toLocaleString()}</div>
          <div className="stat-card-label">Highest Price</div>
        </div>

        <div className="glass-card stat-card">
          <div className="stat-card-header">
            <div className="stat-card-icon" style={{ background: 'linear-gradient(135deg, #ec4899 0%, #db2777 100%)' }}>
              <Award />
            </div>
          </div>
          <div className="stat-card-value">{stats.topBrands[0]?.[0] || 'N/A'}</div>
          <div className="stat-card-label">Most Popular Brand</div>
        </div>

        <div className="glass-card stat-card">
          <div className="stat-card-header">
            <div className="stat-card-icon" style={{ background: 'linear-gradient(135deg, #14b8a6 0%, #0d9488 100%)' }}>
              <BarChart3 />
            </div>
          </div>
          <div className="stat-card-value">{stats.totalCars}</div>
          <div className="stat-card-label">Total Vehicles</div>
        </div>
      </div>

      <div className="grid grid-2">
        <div className="glass-card">
          <h2 style={{ marginBottom: '1rem', display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
            <Fuel size={24} />
            Fuel Type Distribution
          </h2>
          <div style={{ display: 'flex', flexDirection: 'column', gap: '0.75rem' }}>
            {Object.entries(stats.fuelTypes).map(([fuel, count]) => (
              <div key={fuel}>
                <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '0.25rem' }}>
                  <span>{fuel}</span>
                  <span style={{ fontWeight: 600 }}>{count} ({((count / stats.totalCars) * 100).toFixed(1)}%)</span>
                </div>
                <div style={{ 
                  height: '8px', 
                  background: 'var(--glass-bg)', 
                  borderRadius: '4px',
                  overflow: 'hidden'
                }}>
                  <div style={{ 
                    width: `${(count / stats.totalCars) * 100}%`, 
                    height: '100%', 
                    background: 'linear-gradient(90deg, var(--primary) 0%, var(--primary-light) 100%)',
                    transition: 'width 0.5s ease'
                  }}></div>
                </div>
              </div>
            ))}
          </div>
        </div>

        <div className="glass-card">
          <h2 style={{ marginBottom: '1rem', display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
            <Award size={24} />
            Top 5 Brands
          </h2>
          <div style={{ display: 'flex', flexDirection: 'column', gap: '0.75rem' }}>
            {stats.topBrands.map(([brand, count], index) => (
              <div key={brand}>
                <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '0.25rem' }}>
                  <span>#{index + 1} {brand}</span>
                  <span style={{ fontWeight: 600 }}>{count} cars</span>
                </div>
                <div style={{ 
                  height: '8px', 
                  background: 'var(--glass-bg)', 
                  borderRadius: '4px',
                  overflow: 'hidden'
                }}>
                  <div style={{ 
                    width: `${(count / stats.totalCars) * 100}%`, 
                    height: '100%', 
                    background: 'linear-gradient(90deg, var(--secondary) 0%, #f472b6 100%)',
                    transition: 'width 0.5s ease'
                  }}></div>
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>

      <div className="glass-card" style={{ marginTop: 'var(--spacing-lg)' }}>
        <h2 style={{ marginBottom: '1rem', display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
          <Calendar size={24} />
          Manufacturing Year Distribution
        </h2>
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(120px, 1fr))', gap: '1rem' }}>
          {Object.entries(stats.years)
            .sort((a, b) => b[0] - a[0])
            .slice(0, 12)
            .map(([year, count]) => (
              <div 
                key={year}
                style={{ 
                  padding: '1rem', 
                  background: 'var(--glass-bg)', 
                  borderRadius: 'var(--radius-sm)',
                  border: '1px solid var(--glass-border)',
                  textAlign: 'center'
                }}
              >
                <div style={{ fontSize: '1.5rem', fontWeight: 700, marginBottom: '0.25rem' }}>
                  {year}
                </div>
                <div style={{ fontSize: '0.875rem', color: 'var(--text-secondary)' }}>
                  {count} cars
                </div>
              </div>
            ))}
        </div>
      </div>
    </div>
  );
};

export default Analytics;
