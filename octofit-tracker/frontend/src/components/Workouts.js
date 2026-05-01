import { useEffect } from 'react';

import ResourceView from './ResourceView';

const workoutsEndpoint = process.env.REACT_APP_CODESPACE_NAME
  ? `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/workouts/`
  : 'http://localhost:8000/api/workouts/';

const columns = [
  { key: 'title', label: 'Workout' },
  { key: 'focus_area', label: 'Focus Area' },
  { key: 'difficulty', label: 'Difficulty' },
  { key: 'duration_minutes', label: 'Minutes' },
  { key: 'assigned_to', label: 'Assigned To' },
];

export default function Workouts() {
  useEffect(() => {
    console.log('[Workouts] API endpoint', workoutsEndpoint);
  }, []);

  return (
    <ResourceView
      columns={columns}
      endpoint={workoutsEndpoint}
      resourceName="Workouts"
      subtitle="Personalized training plans, focus areas, and duration targets for each superhero profile."
      title="Workouts"
    />
  );
}