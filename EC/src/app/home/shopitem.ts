import { Injectable } from '@angular/core';
import { Http,Headers } from '@angular/http';
import { Item } from '../models/item.model';
import 'rxjs/add/operator/toPromise';
@Injectable()
export class ShopItem {
    item:Item[]=[];
    private Url='http://localhost:3000/server/shop';
    private headers =new Headers({'Content-Type':'application/json'});

    constructor(private http:Http){}

    getAllItem():Promise<Item[]>{
        return this.http.get(this.Url)
        .toPromise()
        .then(res=>res.json() as Item[])        
    }
}