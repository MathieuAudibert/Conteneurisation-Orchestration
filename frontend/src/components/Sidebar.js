import React from 'react';
import { Link, useLocation } from 'react-router-dom';
import { 
  Home, 
  Car, 
  ScrollText, 
  Database, 
  Activity,
  BarChart3
} from 'lucide-react';

const Sidebar = () => {
  const location = useLocation();

  const navItems = [
    { path: '/', label: 'Dashboard', icon: Home },
    { path: '/cars', label: 'Cars', icon: Car },
    { path: '/logs', label: 'Logs', icon: ScrollText },
    { path: '/etl', label: 'ETL Pipeline', icon: Activity },
    { path: '/analytics', label: 'Analytics', icon: BarChart3 },
  ];

  return (
    <div className="sidebar">
      <div className="sidebar-logo">
        <Database size={32} className="text-gradient" />
        <span className="text-gradient">ETL Manager</span>
      </div>
      
      <nav className="sidebar-nav">
        {navItems.map((item) => {
          const Icon = item.icon;
          const isActive = location.pathname === item.path;
          
          return (
            <Link
              key={item.path}
              to={item.path}
              className={`nav-item ${isActive ? 'active' : ''}`}
            >
              <Icon />
              <span>{item.label}</span>
            </Link>
          );
        })}
      </nav>

      <div className="glass-card" style={{ padding: '1rem' }}>
        <div style={{ fontSize: '0.875rem', color: 'var(--text-muted)' }}>
          <strong>MongoDB</strong>
          <div style={{ marginTop: '0.5rem' }}>
            Connected
            <span style={{ 
              display: 'inline-block', 
              width: '8px', 
              height: '8px', 
              borderRadius: '50%', 
              background: 'var(--success)', 
              marginLeft: '0.5rem' 
            }}></span>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Sidebar;
