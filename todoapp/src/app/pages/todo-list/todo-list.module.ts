import { CommonModule } from '@angular/common';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';

import { TodoListComponent } from './todo-list.component';

@NgModule({
  imports: [CommonModule, FormsModule],
  exports: [TodoListComponent],
  declarations: [TodoListComponent],
  providers: [],
})
export class TodoListModule { }
