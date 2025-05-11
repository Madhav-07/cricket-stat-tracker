import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { PlayerModel } from '../models/player-model';
import { environment } from '../../environments/environment.development';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})

export class HomeService {
  private apiUrl = environment.apiUrl;

  constructor(private httpClient: HttpClient) { }

  getCurrentYearPlayers(): Observable<PlayerModel[]> {
    return this.httpClient.get<PlayerModel[]>(`${this.apiUrl}/players`);
  }
}
