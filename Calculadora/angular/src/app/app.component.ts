import { Component, ViewEncapsulation } from '@angular/core';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { RouterOutlet } from '@angular/router';
import { InputTextModule } from 'primeng/inputtext';
import { ButtonModule } from 'primeng/button';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, ButtonModule, InputTextModule, ReactiveFormsModule, FormsModule],
  templateUrl: './app.component.html',
  styleUrl: './app.component.scss',
  encapsulation: ViewEncapsulation.None
})
export class AppComponent {
  
  buttonLayout=[
    [{label: '1', type: 'number'}, {label: '2', type: 'number'}, {label: '3', type: 'number'}, {label: '+', type: 'operator'}],
    [{label: '4', type: 'number'}, {label: '5', type: 'number'}, {label: '6', type: 'number'}, {label: '-', type: 'operator'}],
    [{label: '7', type: 'number'}, {label: '8', type: 'number'}, {label: '9', type: 'number'}, {label: '*', type: 'operator'}],
    [{label: 'C', type: 'clear'}, {label: '0', type: 'number'}, {label: '=', type: 'equal'}, {label: '/', type: 'operator'}]
  ]

  value = '0'
  firstOperand: number | null = null
  operator: string | null = null
  waitingForSecondOperand = false


  onButtonClick(button: {label:string, type: string}) {
   
    switch(button.type) {
      case 'number':
        this.assignNumber(button.label)
        break;
      case 'operator':
        this.assignOperator(button.label)
        break;
      case 'clear':
        this.clear()
        break;
      case 'equal':
        this.calculateResult()
        break;
    }

  }

  assignNumber(num: string) {
    if(this.waitingForSecondOperand){
      this.value = num
      this.waitingForSecondOperand = false
    }
    else{
      this.value === '0' ? this.value = num : this.value += num
    }
  }

  assignOperator(op: string) {
    const currentValue = parseFloat(this.value)
    
    if(this.operator && this.waitingForSecondOperand){
      this.operator = op
      return
    }

    if(this.firstOperand === null){
      this.firstOperand = currentValue
    }
    else if(this.operator){
      const result = this.calculate(this.firstOperand, currentValue, this.operator)
      this.value = String(result)
      this.firstOperand = result
    }

    this.operator = op
    this.waitingForSecondOperand = true
  }

  calculate(firstOperand: number, secondOperand: number, operator: string) {
    switch(operator){
      case '+':
        return firstOperand + secondOperand
      case '-':
        return firstOperand - secondOperand
      case '*':
        return firstOperand * secondOperand
      case '/':
        return firstOperand / secondOperand
      default:
        return secondOperand
    }
  }

  calculateResult() {
    if(this.firstOperand === null || this.operator === null){
      return
    }

    const secondOperand = parseFloat(this.value)
    const result = this.calculate(this.firstOperand, secondOperand, this.operator)
    
    this.value = `${result}`
    this.firstOperand = null
    this.operator = null
    this.waitingForSecondOperand = false
  }

  clear() {
    this.value = '0'
    this.firstOperand = null
    this.operator = null
    this.waitingForSecondOperand = false
  }



}
