import { Component, OnInit } from '@angular/core';
import { Subscription, timer } from 'rxjs';
import { webSocket } from 'rxjs/webSocket';
import { map, share } from "rxjs/operators";
import { OnDestroy } from '@angular/core';

@Component({
  selector: 'app-weather',
  templateUrl: './weather.component.html',
  styleUrls: ['./weather.component.css']
})
export class WeatherComponent implements OnInit, OnDestroy {

  private backend = webSocket("ws://localhost:8000/ws/weather/")
  weathers = '{ "Santiago": 0, "Zurich": 0, "Sydney": 0, "London": 0, "Georgia": 0, "Auckland": 0 }';
  weatherObject = JSON.parse(this.weathers);

  constructor() {
    this.backend.subscribe(
      (v) => this.weatherObject = (v)
    )
    this.sendMessage();
  }

  
  time = new Date();
  subscription!: Subscription;

  ngOnInit() {
    // Using RxJS Timer
    this.subscription = timer(0, 1000)
      .pipe(
        map(() => new Date()),
        share()
      )
      .subscribe(time => {
        this.time = time;
        if (this.time.getSeconds() % 10 == 0) {
          this.sendMessage();
        }
      });
  }

  sendMessage() {
    this.backend.next({message: "update"});
  }

  ngOnDestroy() {
    if (this.subscription) {
      this.subscription.unsubscribe();
    }
  }

}
