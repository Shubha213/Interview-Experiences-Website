import { AUTO_STYLE } from '@angular/animations';
import { Component, OnInit } from '@angular/core';
import { AngularEditorConfig } from '@kolkov/angular-editor';
import { delay } from 'rxjs';
import { blogd, userN } from 'src/app/models/create-blog';
import { BlogService } from 'src/app/_services/blog.service';
import { ActivatedRoute } from '@angular/router';
import { visited } from 'src/app/models/users';

@Component({
  selector: 'app-show-blog',
  templateUrl: './show-blog.component.html',
  styleUrls: ['./show-blog.component.css'],
})
export class ShowBlogComponent implements OnInit {
  constructor(
    private blogService: BlogService,
    private activatedRoute: ActivatedRoute
  ) {}

  blogtitle = '';
  blogtxt = `lorem`;
  name = '';
  f = 0;
  numlike = 0;
  // id =0;
  nid = 0;
  bdata: blogd = new blogd();
  visit: visited = new visited();
  ngOnInit(): void {
    const id = this.activatedRoute.snapshot.paramMap.get('blogid');
    this.showblog(id);
  }

  startDelay(id: any): void {
    setTimeout(() => {
      this.viewed(id);
    }, 2000); // Delay of 5 seconds (5000 milliseconds)
  }

  viewed(id: any) {
    this.nid = id;
    delay(2000);
    this.blogService.viewUpdate(id).subscribe(
      (data) => {}
    );
    this.blogService.visiting(this.visit).subscribe((data) => {
      console.log("my in upate " + data);
    });
  }

  likein() {
    if (this.f == 1) {
      this.f = 0;
      this.numlike--;
      this.blogService.liked(this.nid).subscribe((data) => {
        console.log(data);
      });
    } else {
      this.f = 1;
      this.numlike++;
      this.blogService.likein(this.nid).subscribe((data) => {
        console.log(data);
      });
    }
  }

  x: any = undefined;
  showblog(id: any) {
    this.blogService.getBlog(id).subscribe((data) => {
      console.log(data);
      this.x = data;
      this.bdata = this.x;
      console.log(this.bdata.blog_title);
      this.blogtxt = this.bdata.blog_text;
      this.blogtitle = this.bdata.blog_title;
      this.numlike = this.bdata.likes;
      this.UserName(id);
    });

    this.visit.blogId = parseInt(id || '');
    this.visit.userId = parseInt(sessionStorage.getItem('userid') || '');
    console.log(this.visit.blogId + ' ' + this.visit.userId);
  }
  y: any = undefined;
  u: userN = new userN();
  UserName(id: any) {
    // console.log(this.bdata.user_id);

    this.blogService.getName(this.bdata.user_id).subscribe((data) => {
      console.log(data);
      this.y = data;
      this.u = this.y;
      this.name = this.u.name;
      this.startDelay(id);
    });
  }

  config: AngularEditorConfig = {
    editable: false,
    showToolbar: false,
    height: 'auto',
    minHeight: 'auto',
    width: '100%',
  };

  // config: AngularEditorConfig = {
  //   editable: false,
  //   spellcheck: true,
  //   height: '50%',
  //   minHeight: '28rem',
  //   width: '90%',
  //   enableToolbar:false,
  //   showToolbar: false
  // };
  uploadImage(event: any) {
    const file = event.target.files[0];
  }
}
