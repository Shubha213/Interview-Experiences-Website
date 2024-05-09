import { Component, ViewChild } from '@angular/core';
import { FormControl, NgForm } from '@angular/forms';
import { Router } from '@angular/router';
import { UsersService } from 'src/app/_services/users.service';
import { Users } from 'src/app/models/users';

@Component({
  selector: 'app-edit-profile',
  templateUrl: './edit-profile.component.html',
  styleUrls: ['./edit-profile.component.css']
})
export class EditProfileComponent {
  @ViewChild('f') form!: NgForm;

  userData: Users = new Users();


  temp_gender = sessionStorage.getItem('gender');
  temp_name = sessionStorage.getItem('name');
  temp_userName = sessionStorage.getItem('username');
  temp_userEmail = sessionStorage.getItem('email');
  temp_userPass = "";
  temp_userProf = sessionStorage.getItem('proff');
  ageString = sessionStorage.getItem('age');
  temp_userAge = parseInt(this.ageString || '')
  uidString = sessionStorage.getItem('userid')
  temp_userId = parseInt(this.uidString || '')

  constructor(private usersService: UsersService, private router: Router) { }

  x: any = undefined;
  saveUpdatedData() {
    this.usersService.updateUser(this.userData, this.temp_userId).subscribe();
    console.log("Done");
  }
  ProfileRoute() {
    this.router.navigate(['profile']);
  }

  // s: number = 0;

  onSubmit(form: NgForm) {
    if (form.invalid) {
      alert('Invalid');
    } else {
      if (this.form.value.name == "")
        this.userData.name = this.temp_name!;
      else
        this.userData.name = this.form.value.name;

      // this.userData.gender = this.form.value.gender;
      this.userData.gender = this.temp_gender!;
      console.log(this.userData.gender);
      // this.userData.userName = sessionStorage.getItem('name');
      this.userData.userName = this.temp_name!;
      console.log(this.userData.userName);

      if (this.form.value.userEmail == "")
        this.userData.userEmail = this.temp_userEmail!;
      else
        this.userData.userEmail = this.form.value.userEmail;

      this.userData.userPass = this.form.value.userPass;

      if (this.form.value.userProf == "")
        this.userData.userProf == this.temp_userProf;
      else
        this.userData.userProf = this.form.value.userProf;

      if (this.form.value.userAge == "")
        this.userData.userAge = this.temp_userAge;
      else
        this.userData.userAge = this.form.value.userAge;
      // console.log(this.form.value.userAge);


      this.saveUpdatedData();

      alert("Changes are updated Successfully.");

      this.ProfileRoute();
    }
  }

  usernameClicked() {
    alert("user name can not be updated !!");
  }
}
