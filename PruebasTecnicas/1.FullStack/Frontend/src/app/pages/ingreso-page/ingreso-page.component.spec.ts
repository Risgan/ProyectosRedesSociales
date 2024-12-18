import { ComponentFixture, TestBed } from '@angular/core/testing';

import { IngresoPageComponent } from './ingreso-page.component';

describe('IngresoPageComponent', () => {
  let component: IngresoPageComponent;
  let fixture: ComponentFixture<IngresoPageComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [IngresoPageComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(IngresoPageComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
