import React, { useState, useEffect } from 'react';
import { AgGridReact } from 'ag-grid-react';
import 'ag-grid-community/styles/ag-grid.css';
import 'ag-grid-community/styles/ag-theme-alpine.css';
import { ScrollText, Download, RefreshCw, Search, Filter } from 'lucide-react';
import { logService } from '../services/api';

const Logs = () => {
    const [rowData, setRowData] = useState([]);
    const [loading, setLoading] = useState(true);
    const [searchText, setSearchText] = useState('');

    const columnDefs = [
        {
            headerName: 'Timestamp',
            field: 'timestamp',
            sortable: true,
            filter: true,
            valueFormatter: params => {
                if (!params.value) return 'N/A';
                return new Date(params.value).toLocaleString();
            },
            width: 200,
        },
        {
            headerName: 'User ID',
            field: 'user_id',
            sortable: true,
            filter: 'agNumberColumnFilter',
            width: 120,
        },
        {
            headerName: 'Action',
            field: 'action',
            sortable: true,
            filter: true,
            flex: 1,
        },
        {
            headerName: 'Metadata',
            field: 'metadata',
            sortable: true,
            filter: true,
            flex: 2,
            cellRenderer: params => {
                const value = params.value;
                if (!value) return 'N/A';

                // Try to parse and format JSON metadata
                try {
                    if (typeof value === 'object') {
                        return JSON.stringify(value);
                    }
                    return value;
                } catch {
                    return value;
                }
            }
        },
        {
            headerName: 'Created At',
            field: 'created_at',
            sortable: true,
            filter: true,
            valueFormatter: params => {
                if (!params.value) return 'N/A';
                return new Date(params.value).toLocaleString();
            },
            width: 200,
        },
    ];

    const defaultColDef = {
        resizable: true,
        sortable: true,
        filter: true,
    };

    const fetchLogs = async () => {
        setLoading(true);
        try {
            const response = await logService.getAllLogs();
            setRowData(response.data || []);
        } catch (error) {
            console.error('Error fetching logs:', error);
        } finally {
            setLoading(false);
        }
    };

    useEffect(() => {
        fetchLogs();
    }, []);

    const onExport = () => {
        console.log('Exporting logs...');
    };

    if (loading) {
        return (
            <div className="loading-container">
                <div className="loading-spinner"></div>
                <p>Loading logs data...</p>
            </div>
        );
    }

    return (
        <div className="fade-in">
            <div className="header">
                <div>
                    <h1 className="header-title">System Logs</h1>
                    <p style={{ color: 'var(--text-secondary)', marginTop: '0.5rem' }}>
                        {rowData.length} log entries
                    </p>
                </div>
                <div className="header-actions">
                    <button className="btn btn-glass" onClick={fetchLogs}>
                        <RefreshCw size={20} />
                        Refresh
                    </button>
                    <button className="btn btn-primary" onClick={onExport}>
                        <Download size={20} />
                        Export
                    </button>
                </div>
            </div>

            <div className="table-container">
                <div className="table-header">
                    <h2 className="table-title">
                        <ScrollText size={24} style={{ marginRight: '0.5rem' }} />
                        All Logs
                    </h2>
                    <div className="table-actions">
                        <div style={{ position: 'relative' }}>
                            <Search
                                size={20}
                                style={{
                                    position: 'absolute',
                                    left: '1rem',
                                    top: '50%',
                                    transform: 'translateY(-50%)',
                                    color: 'var(--text-muted)'
                                }}
                            />
                            <input
                                type="text"
                                placeholder="Search logs..."
                                className="input-glass"
                                value={searchText}
                                onChange={(e) => setSearchText(e.target.value)}
                                style={{ paddingLeft: '3rem', width: '300px' }}
                            />
                        </div>
                    </div>
                </div>

                <div className="ag-theme-alpine-dark" style={{ height: 600, width: '100%' }}>
                    <AgGridReact
                        rowData={rowData}
                        columnDefs={columnDefs}
                        defaultColDef={defaultColDef}
                        pagination={true}
                        paginationPageSize={20}
                        quickFilterText={searchText}
                        animateRows={true}
                        rowSelection="multiple"
                    />
                </div>
            </div>
        </div>
    );
};

export default Logs;
