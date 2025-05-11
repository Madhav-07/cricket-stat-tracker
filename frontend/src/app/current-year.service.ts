import { Injectable } from '@angular/core';
import { environment } from '../environments/environment';
import type { Observable } from 'rxjs';
import { HttpClient } from '@angular/common/http';

type CurrentYearResponse = {
  current_year: number;
}

@Injectable({
  providedIn: 'root'
})
export class CurrentYearService {
  private apiUrl = environment.apiUrl;

  constructor(private httpClient: HttpClient) {}

  getCurrentYear(): Observable<CurrentYearResponse> {
    console.log(`${this.apiUrl}`);
    return this.httpClient.get<CurrentYearResponse>(`${this.apiUrl}/year`)
  }
}
