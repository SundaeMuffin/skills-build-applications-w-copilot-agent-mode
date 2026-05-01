import { NavLink, Navigate, Route, Routes } from 'react-router-dom';

import './App.css';
import Activities from './components/Activities';
import Leaderboard from './components/Leaderboard';
import Teams from './components/Teams';
import Users from './components/Users';
import Workouts from './components/Workouts';
import octofitLogo from './assets/octofitapp-small.png';

const navItems = [
  { to: '/users', label: 'Users' },
  { to: '/teams', label: 'Teams' },
  { to: '/activities', label: 'Activities' },
  { to: '/leaderboard', label: 'Leaderboard' },
  { to: '/workouts', label: 'Workouts' },
];

function HomePanel() {
  return (
    <section className="hero-card card border-0 shadow-lg overflow-hidden">
      <div className="card-body p-4 p-lg-5">
        <div className="row g-4 align-items-center">
          <div className="col-lg-7">
            <span className="eyebrow">Mergington High School Fitness Network</span>
            <h1 className="display-title mt-3">OctoFit Tracker keeps every squad moving.</h1>
            <p className="hero-copy mt-3 mb-4">
              Track superhero workouts, compare team momentum, and route every screen to the live Django REST API.
            </p>
            <div className="d-flex flex-wrap gap-2">
              {navItems.map((item) => (
                <NavLink key={item.to} className="btn btn-octofit" to={item.to}>
                  Open {item.label}
                </NavLink>
              ))}
            </div>
          </div>
          <div className="col-lg-5">
            <div className="row g-3">
              <div className="col-sm-6">
                <div className="metric-card h-100">
                  <div className="metric-label">Tracked Teams</div>
                  <div className="metric-value">2</div>
                  <p className="metric-copy">Marvel and DC squads seeded from MongoDB.</p>
                </div>
              </div>
              <div className="col-sm-6">
                <div className="metric-card h-100">
                  <div className="metric-label">Live Collections</div>
                  <div className="metric-value">5</div>
                  <p className="metric-copy">Users, teams, activities, leaderboard, workouts.</p>
                </div>
              </div>
              <div className="col-12">
                <div className="metric-card accent-card h-100">
                  <div className="metric-label">Frontend Goal</div>
                  <p className="metric-copy mb-0">
                    Fast navigation, readable tables, and a clean route to the Codespaces API on port 8000.
                  </p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}

function App() {
  return (
    <div className="app-shell">
      <nav className="navbar navbar-expand-lg octofit-navbar">
        <div className="container-xxl align-items-center gap-3">
          <NavLink className="navbar-brand brand-mark d-flex align-items-center gap-3" to="/">
            <img src={octofitLogo} alt="OctoFit Tracker" className="brand-logo" />
            <span>
              <strong>OctoFit Tracker</strong>
              <small>Competitive fitness dashboard</small>
            </span>
          </NavLink>

          <div className="navbar-nav nav-pills-wrap ms-lg-auto">
            <NavLink end className={({ isActive }) => `nav-link nav-pill ${isActive ? 'active' : ''}`} to="/">
              Home
            </NavLink>
            {navItems.map((item) => (
              <NavLink
                key={item.to}
                className={({ isActive }) => `nav-link nav-pill ${isActive ? 'active' : ''}`}
                to={item.to}
              >
                {item.label}
              </NavLink>
            ))}
          </div>
        </div>
      </nav>

      <main className="container-xxl py-4 py-lg-5">
        <Routes>
          <Route path="/" element={<HomePanel />} />
          <Route path="/users" element={<Users />} />
          <Route path="/teams" element={<Teams />} />
          <Route path="/activities" element={<Activities />} />
          <Route path="/leaderboard" element={<Leaderboard />} />
          <Route path="/workouts" element={<Workouts />} />
          <Route path="*" element={<Navigate replace to="/" />} />
        </Routes>
      </main>
    </div>
  );
}

export default App;
