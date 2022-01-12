import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-slideshow',
  templateUrl: './slideshow.component.html',
  styleUrls: ['./slideshow.component.scss']
})
export class SlideshowComponent implements OnInit {
  images = ['Hintergrund-Laptop.jpg','Hintergrund-Laptop2.jpg','Hintergrund-Laptop3.jpg'];
  headlines = ['Bring engineering to next level!', 'IoT is the future','PNG is oldschool'];
  currentImage = 0;
  showImage = true;

  ngOnInit() {
    this.updateImage();
  }
  updateImage() {
    setInterval(() =>{
      this.currentImage++;
      this.currentImage = this.currentImage % this.images.length;
      this.showImage = false;
      setTimeout(() =>{
        this.showImage=true;
      },100);
    },8000);
  }

}
