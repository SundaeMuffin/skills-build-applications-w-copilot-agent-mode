import { useEffect } from 'react';

import ResourceView from './ResourceView';

const teamsEndpoint = process.env.REACT_APP_CODESPACE_NAME
  ? `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/teams/`
  : 'http://localhost:8000/api/teams/';

const columns = [
  { key: 'name', label: 'Team' },
  { key: 'universe', label: 'Universe' },
  { key: 'captain', label: 'Captain' },
  { key: 'motto', label: 'Motto' },
];

export default function Teams() {
  useEffect(() => {
    console.log('[Teams] API endpoint', teamsEndpoint);
  }, []);

  return (
    <ResourceView
      columns={columns}
      endpoint={teamsEndpoint}
      resourceName="Teams"
      subtitle="Team rosters and squad identity cards coming straight from the backend REST collection."
      title="Teams"
    />
  );
}