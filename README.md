# DIP225projekts Laikapstākļu/Radio programma
## Autori - Raitis Regža (231RDB286), Jānis Zeidmans (231RDB265)

### Izmantotās bibliotēkas un resursi
**Selenium**

* **Webdriver**
    * Bibliotēka, kurā ir dažādu tīmekļa pārlūkprogrammu vadīšanas klases, kas tālāk tiek aprakstītas zemāk.
        * **By**
            * Šo bibliotēku izmanto lai atrastu elementus, kurus izmanto, lai veiktu komandas, kuras tiek izvadītas mājaslapā.
        * **WebDriverWait**
            * Šīs bibliotēkas uzdevums ir sagaidīt, kamēr kāds nosacījums ir piepildīts, piemēram, lai komanda sagaida pogu, kuru vajag nospiest, vai arī textu, kuru vajag ievadīt.
        * **ExpectedConditions**
            * Līdzīgi kā iepriekš minētā biblioteka, tiek izmantota, lai radītu apstākļus, kas Selenium WebDriver ir jānogaida pirms turpmāku darbību veikšanas. Šīs bibliotēkas savā starpā sadarbojas.
* **TimeoutException**
    * Bibliotēka, kas piefiksē, ja netiek izpildītas komandas noteiktā perioda laikā, un tad tas tiek uzkatīts par kļūdu.

**Time**
* Izmantojot reāllaiku, ļauj veikt pazues, kuras vajdzīgas, lai tīmeklis spētu veikt nepieciešamās darbības, pirms tam tiek nosūtītas jaunas instrukcijas.

**Pandas**
* Izmanto datu analīzei un apstrādei, šajā programmā, lai varētu apstrādāt iegūtos datus par laikapstākļiem tabulas veidā

**WebBrowser**
* Izmantota, lai atvērtu saiti interneta pārlūkā, šajā gadījumā, lai jaunā cilnē atvērtos izvēlētā radio stacija.

**PyAutoGUI** 
* Ar šīs bibliotēkas palidzību ir iespejams automatizēt peles kustības un klikšķus, kas šajā gadījumā tiek pielietots, lai pelītes kursors nonāktu nepieciešamajā lokācijā uz ekrāna.

Kā viens no informācijas resursem tika izmantots geeksforgeeks.com, kur tiek aprakstītas metodes, kuras bija noderīgas šajā programā - PyAutoGUI funkcijas, WebDriver funkcijas -, kā arī noderēja arī StackOverflow noderīgie padomi un dažādie veidi, kā izpildīt kādu funciju. Kā piemēram - *from selenium.common.exceptions import TimeoutException* bibliotēka, kura palīdz negaidīt bezgalīgi, bet tikai konkrētu laiku, kā arī, ja jātiek galā ar lietotāja izraisītu kļūdu, tad izvada izvelētu kļūdas paziņojumu, nevis kļūdas pārakstu.

### Programmatūras izmantošanas metodes

Programma ir noderīga lietošanai ikdienā jebkuram lietotājam, kas ikdienā klausās rādio. Programma noteikti varētu tikt optimizēta un paplašināta nākotnē, lai nodrošinātu tās lietotājus ar papildus funkcijām un informāciju. Pažreizējo informāciju jebkurš students var pielietot, piemēram, lai uzzinātu pašreizējo gaisa temperatūru un saģērbtos attiecīgi laika apstākļiem, tikmēr radio funkcija ļauj klausīties jebkuru vēlamo rādio staciju, kamēr tiek pildīti ikdienas uzdevumi u.t.t.

### Projekta uzdevums

Sākumā lielotājs izvēlas starp laikapstākļu vai laikapstākļu funkciju. Ja tiek izvelēti laikapstākļi, programma prasīs ievadīt konkrētu pilsētu vai reģionu (piem. Sidneja), par kuru lietotājs vēlas uzzināt noteikto informāciju. Izmantojot mājaslapu https://www.yr.no/en, tiek atrasta konkrētā pilsēta, nolasīti dati un izvadīti uz ekrāna tabulas formā. Programma izvada informāciju par gaisa temperatūru, vēja stiprumu un mitruma līmeni.

Ja lietotājs gadījumā ievada pilsētu, kas neeksistē vai nav atrodama sarakstā, tiks izvadīts kļūdas paziņojums, kas norāda, ka pilsēta nav atrasta.

Līdzigi kā laikapstākļu funkcija, ja lietotājs izvēlas rādio funkciju, lietotājam tiks prasīts ievādīt vēlamās radio stacijas nosaukumu (piem. (bez atsarpēm - skonto). Kad stacija ievadīta, programma atvērs saiti (http://radio.lv/' + izveletais_radio +'/') jaunā cilnē, un pelīte tiks automātiski aizvadīta līdz pogai 'atskaņot'.

Ievades kļūdas gadījumā programma atkal izvadīs kļūdas paziņojumu, ka konkrētā ievadītā radio stacija neeksistē vai nav atrodama.

Ņemot vērā, ka lietotāju monitoru izmēri ir dažādi, pogas 'atskaņot' atrašanās vieta uz ekrāna var atšķirties, kas nozīmē, ka lietotājam var nākties labot orģināli ievadītās pelītes kursora koordinātas, lai tas trāpītu pogai 'atskaņot'.