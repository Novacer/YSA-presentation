import { Component } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
	
	public genders : string[];
	public selectedClass : number;
	public age: number;
	public siblings : number;
	public parents : number;
	public fare : number;
	
	public survived : boolean;
	
	private selectedGender : number;
	
	constructor(private http: HttpClient) {
		this.genders = ["Male", "Female"];
		
		this.selectedGender = 0;
		
		this.selectedClass = 1;
		this.age = 1;
		this.siblings = 0;
		this.parents = 2;
		this.fare = 100;
		
		this.survived = null;
	}
	
	
	onGenderClick(index: number) {
		this.selectedGender = index;
	}
	
	onSubmitClick() {
		let body = {
			pclass : this.selectedClass,
			sex : this.selectedGender,
			age : this.age,
			siblings : this.siblings,
			parents : this.parents,
			fare_price : this.fare
		};
		
		let headers = new HttpHeaders({ 'Content-Type': 'application/json' });

		
		this.http.post("/api/post/survived-titanic", body, {headers: headers}).subscribe((response : any) => {
			if (response) {
				this.survived = response.survived;
			}
		});
	}
}
