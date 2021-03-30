import { Component, EventEmitter, Input, OnInit, Output } from '@angular/core';
import { Todo } from 'src/app/core/todo';

@Component({
  selector: 'app-todo-list',
  templateUrl: './todo-list.component.html',
  styleUrls: ['./todo-list.component.scss']
})
export class TodoListComponent implements OnInit {
  @Input() items: Todo[] = [];
  @Output() create = new EventEmitter<string>();

  task = "";

  ngOnInit(): void {
  }

  onClick() {
    this.create.emit(this.task);
  }

}
