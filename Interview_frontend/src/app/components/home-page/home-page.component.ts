import { Component, OnInit } from '@angular/core';
import { blog } from 'src/app/models/users';
import { BlogService } from 'src/app/_services/blog.service';
import { UsersService } from 'src/app/_services/users.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-home-page',
  templateUrl: './home-page.component.html',
  styleUrls: ['./home-page.component.css']
})
export class HomePageComponent {


  public p = 1;
  constructor(private blogService: BlogService, private router: Router) { }
  clickedTag: string = "";
  s: string = "";
  // ngOnInit(): void {
  //   console.log(tag);
  // }
  sendTag(value: string) {
    this.clickedTag = value;
  }
  removeTag() {
    this.clickedTag = "";
  }
  arr: String[] = ["hee", "helo", "h"];
  blogs: blog[] = [];
  count: number = 16;
  maxNo: number = 0;
  pageNo: number = 1;
  pages: number[] = [];


  // stripHtmlTags(html: string): string {
  //   return html.replace(/<[^>]*>/g, '');
  // }


  nextPage() {
    // console.log("next");
    this.blogService.setPage(this.blogService.getPage() + 1);
    this.p = this.blogService.getPage();
    console.log(this.blogService.getPage());
  }

  // setVal(){
  //   this.maxNo = this.count/10;
  //   for(let i =1;i<=this.maxNo+1;i++){
  //     this.pages.push(i);
  //   }  
  // }

  prevPage() {
    BlogService.total = 1;
    this.blogService.setPage(this.blogService.getPage() - 1);
    this.p = this.blogService.getPage();
    console.log(this.p);
  }

  getId() {
    let vl = sessionStorage.getItem('userid');
    let vs = parseInt(vl || '')
    return vs;
  }

  isloggedin(): boolean {
    let vs = this.getId();
    console.log("checking login or not: " + sessionStorage.getItem('userid'));

    if (isNaN(vs)) {
      return false;
    }
    return true;
  }

  // checkloginForWriteBlog(){
  //   let vs = this.getId();
  //   console.log("it is " + sessionStorage.getItem('userid'));

  //   if(isNaN(vs)){
  //     vs=0;
  //     this.router.navigate(['/login']);
  //   }
  //   else{
  //     this.router.navigate(['/create-blog']);
  //   }
  // }

  // checkloginForProfile(){
  //   let vs = this.getId();
  //   console.log("it is " + sessionStorage.getItem('userid'));

  //   if(isNaN(vs)){
  //     vs=0;
  //     this.router.navigate(['/login']);
  //   }
  //   else{
  //     this.router.navigate(['/profile']);
  //   }
  // }


}
