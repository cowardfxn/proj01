
### save data with UTC offset

```JavaScript
var now = new Date();
db.data.save({
    date: now,
    offset: now.getTimezoneOffset()
});
```

### get the right date with UTC offset after get date from MongoDB

```JavaScript
var record = db.data.findOne();
var localNow = new Date( record.date.getTime() -  ( record.offset * 60000 ) );
```

