import { Component } from '@angular/core';
import { CurrentYearService } from '../current-year.service';

@Component({
  selector: 'app-home',
  standalone: false,
  templateUrl: './home.component.html',
  styleUrl: './home.component.css'
})
export class HomeComponent {
  currentYear: number | undefined;

  constructor(private currentYearService: CurrentYearService) {}

  ngOnInit() {
    this.currentYearService
      .getCurrentYear()
      .subscribe((currentYearResponse) => {
        console.log(currentYearResponse);
        this.currentYear = currentYearResponse.current_year;
      })
  }
}
