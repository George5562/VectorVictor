# TLS/SSL Connections


# TLS/SSL Connections

[TLS/SSL Connections](#tlsssl-connections)


Mongoose supports connecting toMongoDB clusters that require TLS/SSL connections. Setting thetlsoption totrueinmongoose.connect()or your connection string is enough to connect to a MongoDB cluster using TLS/SSL:

[MongoDB clusters that require TLS/SSL connections](https://www.mongodb.com/docs/manual/tutorial/configure-ssl/)

`tls`
`true`
[mongoose.connect()](../api/mongoose.html#mongoose_Mongoose-connect)

`mongoose.connect()`

```javascript
mongoose.connect('mongodb://127.0.0.1:27017/test', {tls:true});// Equivalent:mongoose.connect('mongodb://127.0.0.1:27017/test?tls=true');
```


Thetlsoption defaults tofalsefor connection strings that start withmongodb://. However,
thetlsoption defaults totruefor connection strings that start withmongodb+srv://. So if you are using an srv connection string to connect toMongoDB Atlas, TLS/SSL is enabled by default.

`tls`
`false`
`mongodb://`
`tls`
`true`
`mongodb+srv://`
[MongoDB Atlas](https://www.mongodb.com/cloud/atlas)


If you try to connect to a MongoDB cluster that requires TLS/SSL without enabling thetls/ssloption,mongoose.connect()will error out with the below error:

`tls`
`ssl`
`mongoose.connect()`

## TLS/SSL Validation

[TLS/SSL Validation](#tlsssl-validation)


By default, Mongoose validates the TLS/SSL certificate against acertificate authorityto ensure the TLS/SSL certificate is valid. To disable this validation, set thetlsAllowInvalidCertificates(ortlsInsecure) option totrue.

[certificate authority](https://en.wikipedia.org/wiki/Certificate_authority)

`tlsAllowInvalidCertificates`
`tlsInsecure`
`true`

```javascript
mongoose.connect('mongodb://127.0.0.1:27017/test', {tls:true,tlsAllowInvalidCertificates:true,
});
```


In most cases, you should not disable TLS/SSL validation in production. However,tlsAllowInvalidCertificates: trueis often helpful
for debugging SSL connection issues. If you can connect to MongoDB withtlsAllowInvalidCertificates: true, but not withtlsAllowInvalidCertificates: false, then you can confirm Mongoose can connect to the server and the server is configured to use
TLS/SSL correctly, but there's some issue with the certificate.

`tlsAllowInvalidCertificates: true`
`tlsAllowInvalidCertificates: true`
`tlsAllowInvalidCertificates: false`

For example, a common issue is the below error message:


This error is often caused byself-signed MongoDB certificatesor other situations where the certificate sent by the MongoDB
server is not registered with an established certificate authority. The solution is to set thetlsCAFileoption, which essentially sets a list of allowed SSL certificates.

[self-signed MongoDB certificates](https://medium.com/@rajanmaharjan/secure-your-mongodb-connections-ssl-tls-92e2addb3c89)

`tlsCAFile`

```javascript
awaitmongoose.connect('mongodb://127.0.0.1:27017/test', {tls:true,// For example, see https://medium.com/@rajanmaharjan/secure-your-mongodb-connections-ssl-tls-92e2addb3c89// for where the `rootCA.pem` file comes from.tlsCAFile:`${__dirname}/rootCA.pem`,
});
```


Another common issue is the below error message:


The SSL certificate'scommon namemustline up with the host name
in your connection string. If the SSL certificate is forhostname2.mydomain.com, your connection string must connect tohostname2.mydomain.com, not any other hostname or IP address that may be equivalent tohostname2.mydomain.com. For replica sets, this also means that the SSL certificate's common name must line up with themachine'shostname. To disable this validation, set thetlsAllowInvalidHostnamesoption totrue.

[common name](https://knowledge.digicert.com/solution/SO7239.html)

`hostname2.mydomain.com`
`hostname2.mydomain.com`
`hostname2.mydomain.com`
[machine'shostname](../connections.html#replicaset-hostnames)

`hostname`
`tlsAllowInvalidHostnames`
`true`

## X.509 Authentication

[X.509 Authentication](#x509-authentication)


If you're usingX.509 authentication, you should set the user name in the connection string,nottheconnect()options.

[X.509 authentication](https://www.mongodb.com/docs/drivers/node/current/fundamentals/authentication/mechanisms/#x.509)

`connect()`

```javascript
// Do this:constusername ='myusername';awaitmongoose.connect(`mongodb://${encodeURIComponent(username)}@127.0.0.1:27017/test`, {tls:true,tlsCAFile:`${__dirname}/rootCA.pem`,authMechanism:'MONGODB-X509',
});// Not this:awaitmongoose.connect('mongodb://127.0.0.1:27017/test', {tls:true,tlsCAFile:`${__dirname}/rootCA.pem`,authMechanism:'MONGODB-X509',auth: { username },
});
```


## X.509 Authentication with MongoDB Atlas

[X.509 Authentication with MongoDB Atlas](#x509-authentication-with-mongodb-atlas)


With MongoDB Atlas, X.509 certificates are not Root CA certificates and will not work with thetlsCAFileparameter as self-signed certificates would. If thetlsCAFileparameter is used an error similar to the following would be raised:

`tlsCAFile`
`tlsCAFile`

To connect to a MongoDB Atlas cluster using X.509 authentication the correct option to set istlsCertificateKeyFile. The connection string already specifies theauthSourceandauthMechanism, however they're included below asconnect()options for completeness:

`tlsCertificateKeyFile`
`authSource`
`authMechanism`
`connect()`

```javascript
consturl ='mongodb+srv://xyz.mongodb.net/test?authSource=%24external&authMechanism=MONGODB-X509';awaitmongoose.connect(url, {tls:true,// location of a local .pem file that contains both the client's certificate and keytlsCertificateKeyFile:'/path/to/certificate.pem',authMechanism:'MONGODB-X509',authSource:'$external',
});
```


NoteThe connection string options must be URL escaped correctly.


[Source](https://mongoosejs.com/docs/tutorials/ssl.html)