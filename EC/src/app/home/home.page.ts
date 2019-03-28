import { Component } from '@angular/core';
import {Router, ActivatedRoute, Params} from '@angular/router';
import { ShopItem } from './shopitem';
import { Item } from '../models/item.model';
@Component({
  selector: 'app-home',
  templateUrl: 'home.page.html',
  styleUrls: ['home.page.scss'],
})
export class HomePage {
  item:Item[]=[];
  constructor(private shopitem:ShopItem){}
  ngOnInit():void{
    this.shopitem.getAllItem().then(items=>this.item=items);
  }
}
