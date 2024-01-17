# DIP225projekts

bibliotēkas

from selenium import webdriver
// bibliotēka, kurā ir dažādu tīmekļa pārlūkprogrammu vadīšanas klases

from selenium.webdriver.common.by import By
// šo bibliotēku izmanto lai atrastu elementus, kurus izmanto, lai veiktu komandas, kuras tiek izvadītas mājaslapā

from selenium.webdriver.support.ui import WebDriverWait
// izmanto, lai komanda sagaida pogi, kuru vajag nospiest, vai arī textu, kuru vajag ievadīt

from selenium.webdriver.support import expected_conditions as EC
//šis ir ka augšēj minētā bibliotēka, bet lai viņa funkcionētu, ir vajadzīgas abas bibliotēkas

from selenium.common.exceptions import TimeoutException
// ja netiek izpildītas komandas noteiktā perioda laikā, tad tas tiek uzkatīts par kļūdu

import time
// ļauj veikt pazues, kuras vajdzīgas, lai tīmeklis spētu ielādēties pirms nākamās darbības

import pandas as pd
// lai varētu apstrādāt iegūtos datus par laikapstākļiem tabulas veidā

import webbrowser
// lai jaunā cilnē atvērtos izvēlētā radio stacija

import pyautogui
// lai pelītes kursors nonāktu vajadzīgaja pozīcijā





aprakstīsies programmatūras izmantošanas metodes

tika izmantots geeksforgeeks.com, kur tiek aprakstītas dažas metodes, kuras bija noderīgas šajā programā - pyautogui funkcijas, webdriver funkcijas - noderēja arī stack overflow noderīgie padomi un dažādie veidi, kā izpildīt kādu funciju, kā piemēram - from selenium.common.exceptions import TimeoutException bibliotēka, kura palīdz kodam neilgt mūzību, bet konkrētu laiku, kā arī, ja ir kļūda, tad izvada izvelēto ziņu, nevis kļūdas parakstu.

detalizēti aprakstīsiet projekta uzdevumu

ar dažu atslēgvārdiem ir iespējams uzzināt temperatūru sidnejā, kā arī vēja ātrumu un mitruma līmeni, vai arī izvēlēto radiostaciju.

laikapstākļu programma:

tiek izmantots laikapstākļu saits - https://www.yr.no/en -, kurā tiek ievadīta izvēlētas pilsētas nosaukums, un izvēlētas pilsētas laikapstākļi tiek izvadīti terminālī.

radio:

šī programma prasa, lai ievadi izvelētās radio stacijas nosaukumu (piem. (bez atsarpēm - skonto), (radio staciajs ar atsarpēm tiek rakstītas bez - swhrock - vai arī tiek saīsinātas - lr1, (ehr latvišu hiti ==> ehrlatviesu)))

pēc tam tiek atvērta cilne ar izvēlēto radio staciju un pelīte tiek aizvadita uz 'play' pogas, ar kuru tiek atskaņots radio