import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Todo } from './todo';

const API_URL = '/api/';
const HEADERS = {
  headers: new HttpHeaders().append('Content-Type', 'application/json'),
};

@Injectable({ providedIn: 'root' })
export class TodoService {
  constructor(private readonly http: HttpClient) {}

  list(): Observable<Todo[]> {
    return this.http.get<Todo[]>(API_URL + 'list');
  }

  create(task: string): Observable<Todo> {
    // Partial to make all fields of Todo optional so we can omit the id field.
    const todo: Partial<Todo> = {
      task,
      completed: false,
    };

    return this.http.post<Todo>(API_URL + 'create/', todo, HEADERS);
  }
}
