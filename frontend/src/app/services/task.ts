import { Injectable, inject } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

export interface Task {
  id: number;
  title: string;
  description?: string;
  priority: number;
  deadline?: string;
  created_at: string;
}

export interface TaskCreate {
  title: string;
  description?: string;
  priority?: number;
  deadline?: string;
}

@Injectable({
  providedIn: 'root'
})
export class TaskService {
  private http = inject(HttpClient);
  // In production, this URL should be in environment files
  private apiUrl = 'http://localhost:8000/api/v1/tasks';

  getTasks(): Observable<Task[]> {
    return this.http.get<Task[]>(this.apiUrl + '/');
  }

  createTask(task: TaskCreate): Observable<Task> {
    return this.http.post<Task>(this.apiUrl + '/', task);
  }
}
