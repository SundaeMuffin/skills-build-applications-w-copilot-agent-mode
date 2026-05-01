import { useEffect } from 'react';

import ResourceView from './ResourceView';

const activitiesEndpoint = process.env.REACT_APP_CODESPACE_NAME
  ? `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/activities/`
  : 'http://localhost:8000/api/activities/';

const columns = [
  { key: 'hero_name', label: 'Hero' },
  { key: 'activity_type', label: 'Activity' },
  { key: 'duration_minutes', label: 'Minutes' },
  { key: 'calories_burned', label: 'Calories' },
  { key: 'completed_at', label: 'Completed' },
];

export default function Activities() {
  useEffect(() => {
    console.log('[Activities] API endpoint', activitiesEndpoint);
  }, []);

  return (
    <ResourceView
      columns={columns}
      endpoint={activitiesEndpoint}
      resourceName="Activities"
      subtitle="Workout logs, intensity snapshots, and completed sessions pulled from the Django REST API."
      title="Activities"
    />
  );
}