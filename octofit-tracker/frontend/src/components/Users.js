import { useEffect } from 'react';

import ResourceView from './ResourceView';

const usersEndpoint = process.env.REACT_APP_CODESPACE_NAME
  ? `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/users/`
  : 'http://localhost:8000/api/users/';

const columns = [
  { key: 'hero_name', label: 'Hero' },
  { key: 'full_name', label: 'Identity' },
  { key: 'team_name', label: 'Team' },
  { key: 'favorite_activity', label: 'Favorite Activity' },
  { key: 'points', label: 'Points' },
];

export default function Users() {
  useEffect(() => {
    console.log('[Users] API endpoint', usersEndpoint);
  }, []);

  return (
    <ResourceView
      columns={columns}
      endpoint={usersEndpoint}
      resourceName="Users"
      subtitle="Athlete profiles, team assignment, and score totals rendered from the Django API."
      title="Users"
    />
  );
}