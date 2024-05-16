export class Users{
    gender!: string;
    name!: string;
    userName!: string;
    userEmail!: string;
    userPass!: string;
    userProf!: string;
    userAge!: number;
    userId!:number;
}
export class login{
    userName!:string ;
    userPass!: string;
}
export class blog{
    blog_id!:number;
	blog_title!:string;
	blog_text!:string;
	tags!:string;
	views!:number;
	likes!:number;
}
export class visited{
    blogId!: number;
    userId!: number;
    rating = 3.5;
}