# Cracking PBKDF2HMAC

During a penetration test, me and the team i worked with were able to access a Liferay Database.
The *'USER_'* table, contained various information about the users registered on the tenant, and the password hash too.

Liferay version 6.2 and above, upgraded the password encryption algorithm to PBKDF2WithHmacSHA1/160/128000; referring to the official Liferay Knowledge base:

>   By default, Liferay encrypts the passwords that go into the database. 
>   The default algorithm is SHA-1 in 6.0 and 6.1 versions, which changed to PBKDF2WithHmacSHA1/160/128000 in version 6.2. 
>   The encryption algorithm can be changed and even turned off via the portal-ext.properties. 

To check if the passwords where compliant to the Client's Password Policy, we where authorized to crack them.

After some researches i wasn't able to find an utility to bulk convert the *"PBKDF2HMAC" hash*  to a suitable version for hashcat, then i created mine.

### Usage 

-  *hashlist* is the list of pbkdf2hmac hashes to convert into hashcat suitable format
-  *outfile* is the filename where the list will be written

```
pbk2hmac2hashcat.py hashlist outfile
```

##### Provided example file

The provided example hash which is *'AAAAoAAB9AD36DwJyq+Wu+wpiL4s1P/HsTQvI5AgKWr2oxzS'* is the PBKDF2WithHmacSHA1/160/128000 for *'password'*

```
pbk2hmac2hashcat.py examples/password_hash outfile
```


Then you are able to crack the list using hashcat command

```
hashcat -m 12000 -a 0 -w 3 outfile wordlist
```




## License

MIT
**Keep on Cracking.**

