import React, { useState } from 'react';
import {
    Activity,
    Download,
    Upload,
    RefreshCw,
    Play,
    CheckCircle,
    AlertCircle,
    Clock
} from 'lucide-react';
import { etlService } from '../services/api';

const ETL = () => {
    const [loading, setLoading] = useState({
        extract: false,
        transform: false,
        load: false,
        workflow: false,
    });

    const [status, setStatus] = useState({
        extract: null,
        transform: null,
        load: null,
        workflow: null,
    });

    const runETLStep = async (step) => {
        setLoading(prev => ({ ...prev, [step]: true }));
        setStatus(prev => ({ ...prev, [step]: 'running' }));

        try {
            let response;
            switch (step) {
                case 'extract':
                    response = await etlService.extract();
                    break;
                case 'transform':
                    response = await etlService.transform();
                    break;
                case 'load':
                    response = await etlService.load();
                    break;
                case 'workflow':
                    response = await etlService.runWorkflow();
                    break;
                default:
                    throw new Error('Invalid step');
            }

            setStatus(prev => ({ ...prev, [step]: 'success' }));
            console.log(`${step} completed:`, response);
        } catch (error) {
            setStatus(prev => ({ ...prev, [step]: 'error' }));
            console.error(`Error in ${step}:`, error);
        } finally {
            setLoading(prev => ({ ...prev, [step]: false }));
        }
    };

    const getStatusIcon = (stepStatus) => {
        if (stepStatus === 'running') return <Clock className="loading" size={20} />;
        if (stepStatus === 'success') return <CheckCircle size={20} style={{ color: 'var(--success)' }} />;
        if (stepStatus === 'error') return <AlertCircle size={20} style={{ color: 'var(--danger)' }} />;
        return null;
    };

    const etlSteps = [
        {
            id: 'extract',
            title: 'Extract',
            description: 'Extract data from the source CSV file',
            icon: Download,
            color: 'linear-gradient(135deg, #6366f1 0%, #4f46e5 100%)',
        },
        {
            id: 'transform',
            title: 'Transform',
            description: 'Clean and transform the extracted data',
            icon: RefreshCw,
            color: 'linear-gradient(135deg, #ec4899 0%, #db2777 100%)',
        },
        {
            id: 'load',
            title: 'Load',
            description: 'Load transformed data into MongoDB',
            icon: Upload,
            color: 'linear-gradient(135deg, #14b8a6 0%, #0d9488 100%)',
        },
    ];

    return (
        <div className="fade-in">
            <div className="header">
                <div>
                    <h1 className="header-title">ETL Pipeline</h1>
                    <p style={{ color: 'var(--text-secondary)', marginTop: '0.5rem' }}>
                        Extract, Transform, and Load your data
                    </p>
                </div>
                <div className="header-actions">
                    <button
                        className="btn btn-primary"
                        onClick={() => runETLStep('workflow')}
                        disabled={loading.workflow}
                    >
                        {loading.workflow ? (
                            <>
                                <div className="loading"></div>
                                Running...
                            </>
                        ) : (
                            <>
                                <Play size={20} />
                                Run Full Pipeline
                            </>
                        )}
                    </button>
                </div>
            </div>

            {status.workflow && (
                <div
                    className="glass-card"
                    style={{
                        marginBottom: 'var(--spacing-lg)',
                        padding: 'var(--spacing-md)',
                        display: 'flex',
                        alignItems: 'center',
                        gap: 'var(--spacing-sm)',
                    }}
                >
                    {getStatusIcon(status.workflow)}
                    <div>
                        <strong>Full Pipeline Status:</strong>{' '}
                        {status.workflow === 'running' && 'Running...'}
                        {status.workflow === 'success' && 'Completed successfully!'}
                        {status.workflow === 'error' && 'Failed. Check logs for details.'}
                    </div>
                </div>
            )}

            <div className="grid grid-3">
                {etlSteps.map((step) => {
                    const Icon = step.icon;
                    return (
                        <div key={step.id} className="glass-card stat-card">
                            <div className="stat-card-header">
                                <div className="stat-card-icon" style={{ background: step.color }}>
                                    <Icon />
                                </div>
                                {getStatusIcon(status[step.id])}
                            </div>
                            <h3 style={{ fontSize: '1.5rem', marginBottom: '0.5rem' }}>{step.title}</h3>
                            <p style={{ color: 'var(--text-secondary)', marginBottom: '1rem' }}>
                                {step.description}
                            </p>
                            <button
                                className="btn btn-glass"
                                style={{ width: '100%' }}
                                onClick={() => runETLStep(step.id)}
                                disabled={loading[step.id]}
                            >
                                {loading[step.id] ? (
                                    <>
                                        <div className="loading"></div>
                                        Processing...
                                    </>
                                ) : (
                                    <>
                                        <Play size={16} />
                                        Run {step.title}
                                    </>
                                )}
                            </button>
                        </div>
                    );
                })}
            </div>

            <div className="glass-card" style={{ marginTop: 'var(--spacing-lg)' }}>
                <h2 style={{ marginBottom: '1rem', display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
                    <Activity size={24} />
                    Pipeline Information
                </h2>
                <div className="grid grid-2">
                    <div>
                        <h3 style={{ fontSize: '1rem', marginBottom: '0.5rem', color: 'var(--primary)' }}>
                            Extract Phase
                        </h3>
                        <ul style={{ color: 'var(--text-secondary)', paddingLeft: '1.5rem' }}>
                            <li>Reads data from CSV file</li>
                            <li>Validates data structure</li>
                            <li>Handles missing values</li>
                        </ul>
                    </div>
                    <div>
                        <h3 style={{ fontSize: '1rem', marginBottom: '0.5rem', color: 'var(--secondary)' }}>
                            Transform Phase
                        </h3>
                        <ul style={{ color: 'var(--text-secondary)', paddingLeft: '1.5rem' }}>
                            <li>Cleans and normalizes data</li>
                            <li>Applies business rules</li>
                            <li>Enriches data with calculations</li>
                        </ul>
                    </div>
                    <div>
                        <h3 style={{ fontSize: '1rem', marginBottom: '0.5rem', color: 'var(--accent)' }}>
                            Load Phase
                        </h3>
                        <ul style={{ color: 'var(--text-secondary)', paddingLeft: '1.5rem' }}>
                            <li>Connects to MongoDB</li>
                            <li>Inserts transformed data</li>
                            <li>Creates indexes for performance</li>
                        </ul>
                    </div>
                    <div>
                        <h3 style={{ fontSize: '1rem', marginBottom: '0.5rem', color: 'var(--success)' }}>
                            Full Workflow
                        </h3>
                        <ul style={{ color: 'var(--text-secondary)', paddingLeft: '1.5rem' }}>
                            <li>Runs all phases sequentially</li>
                            <li>Handles errors gracefully</li>
                            <li>Logs all operations</li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default ETL;
