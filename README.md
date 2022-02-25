Pierwszym etapem projektu było stworzenie własnej kaskady haar. Aby to zrobić wsparłem się toturialem z poniższej strony internetowe:

https://medium.com/@vipulgote4/guide-to-make-custom-haar-cascade-xml-file-for-object-detection-with-opencv-6932e22c3f0e

Użyłem do tego programu  Cascade-Trainer-GUI.

Aby pobrać odpowiednią ilość danych pozytywowych i negatywowych użyłem kodu:

from icrawler.builtin import BingImageCrawler
classes=['znak informacyjny przejście dla pieszych'] 
number=100
for c in classes:
    bing_crawler=BingImageCrawler(storage={'root_dir':f'p/{c.replace(" ",".")}'})
    bing_crawler.crawl(keyword=c,filters=None,max_num=number,offset=0)

Gdy kaskada została stworzona, w programie pycharm napisałem program który pobiera kolejne zdjęcia z folderu testowego a następnie wyszukuje 
na nich elementu zawartego w kaskadzie haar. W przypadku wykrycia program wypisuje lokalizaję z nazwą zdjęcia, ilość i współrzędne wykrytych 
znaków oraz wyświetla zdjęcie z zaznaczonym ramką wykrytym elementem

Gotowy program wykrywa wszystkie znaki przejścia dla obiektów testowych. Jednak wykrywa też niektóre obiekty w tle. Pomimo zastosowaniu 200 danych 
pozytywowych i 784 danych negatywowych algorytm wykrywa nieporządane elementy. Prawdopodobnie konieczne jest zwiększenie ilości danych. Mimo tych niedociągnięć 
algorytm bardzo dokładnie wyszukuje znaków których miał szukać.

Aby zmniejszyć rozmiar pliku dane treningowe umieściłem pod linkiem:

https://drive.google.com/drive/folders/1TBNxHts8eoS5Dyyod_5SZkYx4zbycGo8?usp=sharing
