import { Component } from '@angular/core';
import { SearchService } from 'src/app/_services/search.service';
import { blog } from 'src/app/models/users';

@Component({
  selector: 'app-search-bar',
  templateUrl: './search-bar.component.html',
  styleUrls: ['./search-bar.component.css']
})
export class SearchBarComponent {
  searchTerm: string = '';
  public p = 1;
  
  constructor(private serachService : SearchService) { }
  blogs: blog[] = [];

  search() {
    console.log('Searching for:', this.searchTerm);
    this.load();
  }

  load(){
    this.serachService.serachData(this.searchTerm).subscribe((data: blog[]) => {
      this.blogs = data;
    });
    console.log(this.blogs);
    
  }
}
