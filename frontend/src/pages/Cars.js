import React, { useState, useEffect } from 'react';
import { AgGridReact } from 'ag-grid-react';
import 'ag-grid-community/styles/ag-grid.css';
import 'ag-grid-community/styles/ag-theme-alpine.css';
import { Car, Download, RefreshCw, Search } from 'lucide-react';
import { carService } from '../services/api';

const Cars = () => {
    const [rowData, setRowData] = useState([]);
    const [loading, setLoading] = useState(true);
    const [searchText, setSearchText] = useState('');

    const columnDefs = [
        {
            headerName: 'Brand',
            field: 'brand',
            sortable: true,
            filter: true,
            flex: 1,
        },
        {
            headerName: 'Model',
            field: 'model',
            sortable: true,
            filter: true,
            flex: 1,
        },
        {
            headerName: 'Year',
            field: 'make_year',
            sortable: true,
            filter: true,
            width: 120,
        },
        {
            headerName: 'Price',
            field: 'price',
            sortable: true,
            filter: 'agNumberColumnFilter',
            valueFormatter: params => params.value ? `$${params.value.toLocaleString()}` : 'N/A',
            width: 150,
        },
        {
            headerName: 'Fuel Type',
            field: 'fuel_type',
            sortable: true,
            filter: true,
            width: 130,
        },
        {
            headerName: 'Transmission',
            field: 'transmission',
            sortable: true,
            filter: true,
            width: 140,
        },
        {
            headerName: 'KM Driven',
            field: 'km_driven',
            sortable: true,
            filter: 'agNumberColumnFilter',
            valueFormatter: params => params.value ? params.value.toLocaleString() : 'N/A',
            width: 130,
        },
        {
            headerName: 'Engine (cc)',
            field: 'engine_capacity_cc',
            sortable: true,
            filter: 'agNumberColumnFilter',
            width: 130,
        },
        {
            headerName: 'Ownership',
            field: 'ownership',
            sortable: true,
            filter: 'agNumberColumnFilter',
            width: 120,
        },
    ];

    const defaultColDef = {
        resizable: true,
        sortable: true,
        filter: true,
    };

    const fetchCars = async () => {
        setLoading(true);
        try {
            const response = await carService.getAllCars();
            setRowData(response.data || []);
        } catch (error) {
            console.error('Error fetching cars:', error);
        } finally {
            setLoading(false);
        }
    };

    useEffect(() => {
        fetchCars();
    }, []);

    const onExport = () => {
        // In a real application, you would implement CSV export
        console.log('Exporting data...');
    };

    if (loading) {
        return (
            <div className="loading-container">
                <div className="loading-spinner"></div>
                <p>Loading cars data...</p>
            </div>
        );
    }

    return (
        <div className="fade-in">
            <div className="header">
                <div>
                    <h1 className="header-title">Cars Database</h1>
                    <p style={{ color: 'var(--text-secondary)', marginTop: '0.5rem' }}>
                        {rowData.length} cars in database
                    </p>
                </div>
                <div className="header-actions">
                    <button className="btn btn-glass" onClick={fetchCars}>
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
                        <Car size={24} style={{ marginRight: '0.5rem' }} />
                        All Cars
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
                                placeholder="Search cars..."
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

export default Cars;
