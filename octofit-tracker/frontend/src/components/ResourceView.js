import { useEffect, useState } from 'react';

function normalizeCollection(payload) {
  if (Array.isArray(payload)) {
    return payload;
  }

  if (Array.isArray(payload?.results)) {
    return payload.results;
  }

  return [];
}

function formatCellValue(value) {
  if (value === null || value === undefined || value === '') {
    return '—';
  }

  if (Array.isArray(value)) {
    return value.join(', ');
  }

  if (typeof value === 'string') {
    const parsed = Date.parse(value);
    if (!Number.isNaN(parsed) && value.includes('T')) {
      return new Date(parsed).toLocaleString();
    }
  }

  return String(value);
}

function matchesQuery(record, query) {
  if (!query) {
    return true;
  }

  return JSON.stringify(record).toLowerCase().includes(query.toLowerCase());
}

export default function ResourceView({ title, subtitle, resourceName, endpoint, columns }) {
  const [records, setRecords] = useState([]);
  const [query, setQuery] = useState('');
  const [selectedRecord, setSelectedRecord] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const [reloadKey, setReloadKey] = useState(0);

  useEffect(() => {
    let ignore = false;

    async function fetchRecords() {
      console.log(`[${resourceName}] endpoint`, endpoint);
      setLoading(true);
      setError('');

      try {
        const response = await fetch(endpoint);
        if (!response.ok) {
          throw new Error(`Request failed with ${response.status}`);
        }

        const payload = await response.json();
        console.log(`[${resourceName}] fetched data`, payload);

        if (!ignore) {
          setRecords(normalizeCollection(payload));
        }
      } catch (fetchError) {
        console.error(`[${resourceName}] fetch error`, fetchError);
        if (!ignore) {
          setError('Unable to load the collection right now. Check the Django API and try again.');
        }
      } finally {
        if (!ignore) {
          setLoading(false);
        }
      }
    }

    fetchRecords();

    return () => {
      ignore = true;
    };
  }, [endpoint, reloadKey, resourceName]);

  const visibleRecords = records.filter((record) => matchesQuery(record, query));

  return (
    <section className="resource-section">
      <div className="card resource-card border-0">
        <div className="card-body p-4 p-lg-5">
          <div className="resource-header">
            <div>
              <span className="eyebrow">Live Collection</span>
              <h2 className="resource-title mt-3">{title}</h2>
              <p className="resource-subtitle mt-2 mb-0">{subtitle}</p>
            </div>

            <div className="resource-actions">
              <span className="resource-badge">{visibleRecords.length} shown</span>
              <a className="btn btn-outline-octofit" href={endpoint} rel="noreferrer" target="_blank">
                Open API
              </a>
              <button className="btn btn-octofit" onClick={() => setReloadKey((current) => current + 1)} type="button">
                Refresh Data
              </button>
            </div>
          </div>

          <div className="row g-3 align-items-end mb-4">
            <div className="col-lg-8">
              <label className="form-label fw-semibold" htmlFor={`${resourceName}-search`}>
                Search {title}
              </label>
              <input
                className="form-control resource-search"
                id={`${resourceName}-search`}
                onChange={(event) => setQuery(event.target.value)}
                placeholder={`Filter ${title.toLowerCase()} by any visible field...`}
                type="search"
                value={query}
              />
            </div>
            <div className="col-lg-4">
              <div className="api-note">
                Endpoint in use:
                {' '}
                <a className="octofit-link" href={endpoint} rel="noreferrer" target="_blank">
                  {endpoint}
                </a>
              </div>
            </div>
          </div>

          {loading ? <div className="alert alert-info">Loading {title.toLowerCase()}...</div> : null}
          {!loading && error ? <div className="alert alert-danger">{error}</div> : null}

          {!loading && !error && visibleRecords.length === 0 ? (
            <div className="empty-state">No records match the current filter.</div>
          ) : null}

          {!loading && !error && visibleRecords.length > 0 ? (
            <div className="table-shell table-responsive">
              <table className="table octofit-table align-middle table-hover">
                <thead>
                  <tr>
                    {columns.map((column) => (
                      <th key={column.key} scope="col">
                        {column.label}
                      </th>
                    ))}
                    <th scope="col">Details</th>
                  </tr>
                </thead>
                <tbody>
                  {visibleRecords.map((record) => (
                    <tr key={record.id || record._id}>
                      {columns.map((column) => (
                        <td key={`${record.id || record._id}-${column.key}`}>
                          {column.render ? column.render(record) : formatCellValue(record[column.key])}
                        </td>
                      ))}
                      <td>
                        <button
                          className="btn btn-sm btn-outline-octofit"
                          onClick={() => setSelectedRecord(record)}
                          type="button"
                        >
                          View
                        </button>
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          ) : null}
        </div>
      </div>

      {selectedRecord ? (
        <>
          <div aria-hidden="true" className="modal-backdrop fade show" />
          <div aria-modal="true" className="modal fade show d-block octofit-modal" role="dialog" tabIndex="-1">
            <div className="modal-dialog modal-lg modal-dialog-centered">
              <div className="modal-content">
                <div className="modal-header">
                  <div>
                    <h3 className="modal-title h4 mb-1">{title} details</h3>
                    <p className="mb-0 text-muted">Structured view of the selected record.</p>
                  </div>
                  <button
                    aria-label="Close"
                    className="btn-close"
                    onClick={() => setSelectedRecord(null)}
                    type="button"
                  />
                </div>
                <div className="modal-body">
                  <div className="detail-grid">
                    {Object.entries(selectedRecord).map(([key, value]) => (
                      <div className="detail-card" key={key}>
                        <span className="detail-label">{key}</span>
                        <span>{formatCellValue(value)}</span>
                      </div>
                    ))}
                  </div>
                </div>
                <div className="modal-footer">
                  <button className="btn btn-outline-octofit" onClick={() => setSelectedRecord(null)} type="button">
                    Close
                  </button>
                </div>
              </div>
            </div>
          </div>
        </>
      ) : null}
    </section>
  );
}