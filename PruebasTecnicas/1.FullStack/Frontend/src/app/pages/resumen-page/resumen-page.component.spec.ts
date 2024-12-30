import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ResumenPageComponent } from './resumen-page.component';

describe('ResumenPageComponent', () => {
  let component: ResumenPageComponent;
  let fixture: ComponentFixture<ResumenPageComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ResumenPageComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ResumenPageComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
