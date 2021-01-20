# File download in Web Server

[Ref](https://stackoverflow.com/questions/54983080/return-file-from-graphql-resolve)

GraphQL uses JSON format, which represents as text format, not as binary.  

So the right architecture design is add a file link in the GraphQL response and use  browser for downloading/rendering the file.

If you don't want to download files with REST, then you should:

1. Encode your file content into base64 string in the backend
2. Send this string as part of query response
3. Save encoded base64 string as a file in frontend.

## Send file stream in the backend

#### Express backend

1. As data stream

   ```js
   res.attachment('pdffile.pdf');
   pdfStream.pipe(res);
   ```

2. Send file on disk

   ```js
   res.download('/path/to/file.pdf')
   ```

   Or download with a custom file name

   ```js
   res.download('/path/to/file.pdf', 'newname.pdf')
   ```

## Save data as a file in frontend

### HTML download link

```html
<a href="/downloads/archive.zip" download="archive.zip"
   [target="_blank" rel="noopener noreferer"]
   >Download File</a>
```

`target="_blank" rel="noopener noreferer"` is intended to open download link in new browser tab.

### Download file with HttpClient

#### Naive JS implementation

```js
var sampleBytes = new Int8Array(4096);

var savedByteArray = (function () {
    var a = document.createElement('a');
    document.body.appendChild('a');
    a.style = 'display: none';
    return function (data, name) {
        var blob = new Blod(data, {type: 'octect/stream'});
        var url = window.URL.createObjectURL(blob);
        a.href = url;
        a.download = name;
        a.click();
        window.URL.revokeObjectURL(url);
    };
});

saveByteArray([sampleBytes], 'example.txt');
```

It creates an `a` tag which reads in byte array and save it as specified filename.

#### Angular Implementation

##### Create a `DownloadService`

```js
@Injectable({providedIn: 'root'})
export class DownloadService {
    constructor(private http: httpClient) {}
    
    download(url: string): Observable<Blob> {
        return this.http.get(url, {
       		responseType: 'blob' 
    	});
    }
}
```

##### Call `DownloadService` in page component

```js
@Component({...})
export class MyComponent {
	constructor(private downloads: DownloadService) {}

	download(): void {
        this.downloads
        	.download('/downloads/archive.zip')
            .subscribe(blob => {
                const a = document.createElement('a');
                const objectUrl = URL.createObjectURL(blob);
                a.href = objectURL;
                a.download = 'archive.zip';
                a.click();
                URL.revokeObjectURL(objectUrl);
            })
    }
}
```

It does basically the same thing as naive JS implementation, but separate code in dedicated classes.

