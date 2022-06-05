import React from 'react';
import { BrowserRouter, Switch, Redirect, Route } from 'react-router-dom';
import { routes } from '../routes';
import { Header } from './Header';
import { Footer } from './Footer';

export const App = () => (
  <BrowserRouter>
    <Header />
    <Switch>
      {routes.map((route) => (
        <Route key={route.path} path={route.path} exact={route.exact} component={route.component} />
      ))}
      <Redirect to="/" />
    </Switch>
    <Footer />
  </BrowserRouter>
);
