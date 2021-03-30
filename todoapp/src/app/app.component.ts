import { Component, OnDestroy, OnInit } from '@angular/core';
import { Subscription } from 'rxjs';
import { Todo } from './core/todo';
import { TodoService } from './core/todo.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss'],
})
export class AppComponent implements OnInit, OnDestroy {
  private subscription?: Subscription;

  items: Todo[] = [];

  constructor(private readonly todoService: TodoService) {}

  ngOnInit() {
    this.subscription = this.todoService.list().subscribe((data) => {
      this.items = data;
    });
  }

  ngOnDestroy() {
    // IMPORTANT TO NOT CREATE MEMORY LEAKS
    this.subscription?.unsubscribe();
  }

  async create(task: string) {
    this.items.push(
      await this.todoService.create(task).toPromise()
    );
  }
}
