import { CanActivateFn } from '@angular/router';
import { Injectable } from '@angular/core';

export const authGuard: CanActivateFn = (route, state) => {
  // uname: any= sessionStorage.getItem('username');
  if(sessionStorage.getItem('username') == null)
  {
    return false;
  }
  return true;
};
