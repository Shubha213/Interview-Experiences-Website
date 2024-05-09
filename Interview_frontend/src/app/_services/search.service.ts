import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { blog } from '../models/users';

@Injectable({
  providedIn: 'root'
})
export class SearchService {

  constructor(private httpClient: HttpClient) { }

  private searchURL = "http://localhost:8884/Blogapi/search-similar-blogs";

  serachData(key:string) : Observable<blog[]>
  {
    return this.httpClient.post<blog[]>(`${this.searchURL}/${key}`,key);
  }
}
 