import { Component, OnInit, signal, inject, ChangeDetectionStrategy } from '@angular/core';
import { CommonModule } from '@angular/common';
import { TaskService, Task } from '../../services/task';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-task-list',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './task-list.html',
  styleUrl: './task-list.css',
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class TaskListComponent implements OnInit {
  private taskService = inject(TaskService);
  tasks = signal<Task[]>([]);
  newTaskTitle = signal('');

  ngOnInit() {
    this.loadTasks();
  }

  loadTasks() {
    this.taskService.getTasks().subscribe({
      next: (tasks) => this.tasks.set(tasks),
      error: (err) => console.error('Error fetching tasks', err)
    });
  }

  addTask() {
    if (!this.newTaskTitle()) return;
    this.taskService.createTask({ title: this.newTaskTitle() }).subscribe({
      next: (task) => {
        this.tasks.update(tasks => [...tasks, task]);
        this.newTaskTitle.set('');
      },
      error: (err) => console.error('Error creating task', err)
    });
  }
}
