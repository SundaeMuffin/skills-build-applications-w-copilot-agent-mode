import { useEffect } from 'react';

import ResourceView from './ResourceView';

const leaderboardEndpoint = process.env.REACT_APP_CODESPACE_NAME
  ? `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/leaderboard/`
  : 'http://localhost:8000/api/leaderboard/';

const columns = [
  { key: 'rank', label: 'Rank' },
  { key: 'hero_name', label: 'Hero' },
  { key: 'team_name', label: 'Team' },
  { key: 'points', label: 'Points' },
  { key: 'streak_days', label: 'Streak' },
];

export default function Leaderboard() {
  useEffect(() => {
    console.log('[Leaderboard] API endpoint', leaderboardEndpoint);
  }, []);

  return (
    <ResourceView
      columns={columns}
      endpoint={leaderboardEndpoint}
      resourceName="Leaderboard"
      subtitle="Friendly competition across Marvel and DC squads, sorted by points and streaks."
      title="Leaderboard"
    />
  );
}