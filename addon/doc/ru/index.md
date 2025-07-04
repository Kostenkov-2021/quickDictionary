# NVDA Quick Dictionary (Быстрый словарь)

Добро пожаловать в дополнение NVDA Quick Dictionary, которое позволит вам быстро получить словарную статью с переводом слова или словосочетания на выбранный язык при помощи комбинации клавиш. Основных клавишных команд немного и все они интуитивно понятны и удобны поэтому вы быстро их запомните.

Словарные статьи содержат подробную информацию о слове, такую как часть речи, род, число, варианты перевода, перечень значений, синонимы и подробные примеры. Такая информация будет полезной для людей, изучающих иностранные языки, или стремящихся использовать в общении все богатство и разнообразие собственного языка.

Дополнение поддерживает несколько сервисов онлайн словарей. Вы можете выбрать нужный удаленный словарь в соответствующем диалоговом окне или воспользовавшись клавишными командами. Каждый доступный сервис имеет собственную панель настроек.

Также присутствуют расширенные функции для работы с профилями голосовых синтезаторов. Вы можете связать профиль синтезатора голоса с определенным языком, после чего переводы на этот язык будут автоматически озвучиваться выбранным синтезатором.

Ниже приведены все возможности дополнения и сочетания клавиш для управления ими. По умолчанию все функции вызываются с использованием двухуровневых команд. Но для любого из этих методов вы всегда можете назначить удобные для вас сочетания клавиш. Вы можете сделать это в диалоговом окне NVDA "Параметры" -> "Жесты ввода...".

## Получение словарной статьи
Для того, чтобы получить статью из словаря необходимо сначала выделить слово, которое Вас интересует или скопировать его в буфер обмена. После чего достаточно дважды нажать комбинацию клавиш NVDA+Y.

Существует также другая возможность получения записи из словаря: одноразовое нажатие NVDA+Y переключает клавиатуру в режим управления дополнением, а дальше просто воспользуйтесь клавишей D.

Примечание: Перед тем как выполнить запрос к удаленному сервису дополнение должно получить слово или словосочетание, интересующее пользователя. Последовательность действий, которые дополнение выполняет каждый раз перед обращением к онлайн-словарю:

* Получает выделенный текст и выполняет запрос;
* Если нет выделенного текста - извлекается текстовое содержимое буфера обмена и выполняется удаленный запрос;
* Если буфер обмена пуст или его содержимое не является текстовыми данными - дополнение сообщает об этом пользователю и не выполняет дальнейших действий.

## Режим управления дополнением
Для доступа ко всем функциям дополнения нужно переключиться в режим управления дополнением, это можно сделать нажав однократно NVDA+Y. Вы услышите низкий звуковой сигнал и сможете воспользоваться другими клавишными командами, которые будут описаны ниже. При нажатии клавиши, которая не используется в дополнении, вы услышите другой сигнал, который сообщит об ошибочной команде и режим управления дополнением будет автоматически выключен.

## Анонс выбранной пары языков при работе со словарем
Чтобы узнать текущие исходный язык и язык назначения выполните следующие действия:

1. Включите режим управления дополнением с помощью комбинации клавиш NVDA+Y.
2. Нажмите A, чтобы прослушать, какие языки выбраны для получения данных из словаря.

## Изменение порядка языков для получения перевода
Это можно быстро сделать следующим образом:

1. Выделить слово или словосочетание, которое Вас интересует.
2. Включить режим управления дополнением с помощью NVDA+Y, после чего нажать S.

Вы услышите сообщение о том, что языки изменены и полученную из словаря информацию.

Примечание: Каждый раз при изменении языков дополнение выполняет проверку доступна ли новая пара языков для перевода в используемом онлайн-словаре. Если такое сочетание языков отсутствует - вы услышите соответствующее предупреждение.

## Отображение словарной статьи в отдельном окне в виде веб-страницы
Статью из словаря можно открыть в отдельном окне в виде отформатированной веб-страницы:

1. Выделить слово или словосочетание.
2. Включить режим управления дополнением - NVDA+Y.
3. Нажать W.

Примечание: В этом окне можно использовать стандартные команды навигации элементами веб-страницы. Чтобы закрыть окно достаточно нажать Escape или Alt+F4.

## Подготовка текста
Иногда возникает необходимость изменить текст перед отправкой его на перевод или просто ввести текст самостоятельно.

Для этого вы можете воспользоваться командой предварительного редактирования текста - нажмите клавишу E в режиме управления дополнением (NVDA+Y). Откроется диалоговое окно с многострочным полем для редактирования текста. После правки просто нажмите Ctrl+Enter или соответствующую кнопку.

В поле для редактирования также доступны следующие команды:

* Ctrl+A - выделить все;
* Ctrl+E - очистить текст от не буквенных символов;
* Ctrl+R - очистить поле редактора;
* Ctrl+U - восстановить исходный текст.

Примечание: Если перед вызовом диалога для правки текста был предварительно выделен текст или скопирован в буфер обмена, то он будет помещен в поле редактора в этом диалоговом окне.

## Копирование результатов последнего запроса в буфер обмена
Это можно сделать выполнив следующую последовательность действий:

1. Включить режим управления дополнением - NVDA+Y.
2. Нажать клавишу C.

После этого вы услышите сообщение о том, что данные успешно скопированы и саму словарную статью.

Примечание: Если перед этим еще не выполнялось запросов к удаленному словарю - вы услышите соответствующее предупреждение.

Если в настройках дополнения включена опция копирования словарных статей в буфер обмена, данные будут автоматически копироваться после каждого успешного запроса.

## Загрузка актуального списка доступных языков
Воспользуйтесь клавишей U в режиме управления дополнением для того, чтобы загрузить с онлайн-словаря и сохранить актуальный список исходящих языков и языков назначения.

После этого вы услышите сообщение о состоянии выполнения команды.

## Выбор онлайн-сервиса
Есть несколько способов выбрать удаленный словарь, к которому будет обращаться дополнение.

* Воспользовавшись меню NVDA: нажмите NVDA+N, перейдите в подменю "Сервис", далее - "Быстрый словарь" и активируйте команду "Выбрать онлайн-сервис...". Появится диалоговое окно выбора удаленного сервиса. В этом окне клавишами вверх или вниз перейдите на нужный пункт и нажмите Enter. Или же просто нажмите цифру, которая соответствует порядковому номеру интересующего вас онлайн-сервиса.
* Диалог выбора сервиса также можно вызвать нажав клавишу F в режиме управления дополнением.
* За каждым доступным сервисом также закреплена функциональная клавиша начиная от F1 в режиме управления дополнением.
* И наконец сервис можно выбрать непосредственно в панели настроек дополнения.

Примечание: Каждый онлайн-сервис имеет собственную панель настроек и все его параметры хранятся отдельно.

## Информация о выбранном сервисе
Нажав Q в режиме управления дополнением можно прослушать следующие данные:

* название выбранного онлайн-сервиса;
* количество поддерживаемых языков;
* раздел словаря (если поддерживается);
* статистику и лимиты использования текущего сервиса;
* состояние кэша запросов (попадания/промахи/размер/использовано).

## Диалоговое окно настроек дополнения
Чтобы изменить параметры дополнения, нужно открыть диалоговое окно его настроек. Это можна сделать следующим образом: нажмите NVDA+Y, а затем - клавишу O.

На экране появится стандартное диалоговое окно настроек NVDA с открытым разделом дополнения "Быстрый словарь".

Также этот диалог можно открыть через меню NVDA: нажмите NVDA+N, перейдите в подменю "Сервис", далее - "Быстрый словарь" и активируйте пункт "Параметры...".

### Выбор онлайн-сервиса
При открытии диалогового окна настроек дополнения, курсор NVDA сразу устанавливается на выпадающий список выбора онлайн-сервиса. Вы можете выбрать нужный вам сервис из списка и нажать Enter, или Tab для перехода к следующему параметру.

Как уже отмечалось выше - каждый сервис имеет собственную панель настроек. Поэтому все последующие параметры для каждого сервиса могут отличаться. Рассмотрим наиболее общие из них.

### Выбор языков для получения переводов
Перейдя в список исходных языков, клавишами вверх или вниз выберите нужный язык и нажмите Tab для перехода к выбору языка назначения.

Примечание:

* Список доступных языков назначения зависит от выбранного исходного языка, поэтому язык назначения нужно выбирать только после установки исходного языка.
* В некоторых сервисах списки доступных языков зависят от выбранного раздела словаря.

### Опция "Копировать в буфер обмена"
После установки этой галочки, полученные от словаря данные будут копироваться в буфер обмена после каждого запроса.

### Опция "Автоматически менять порядок языков"
После включения этой опции, дополнение при неуспешных запросах к словарю будет пытаться получить данные повторно поменяв местами исходный язык и язык назначения.

Примечание: Если обратная комбинация языков недоступна - вы будете слышать соответствующее предупреждение об этом каждый раз.

### Опция "Использовать альтернативный сервер"
При включении этой опции, дополнение будет отправлять запросы не напрямую к онлайн-словарю, а использовать альтернативный промежуточный сервер, который перенаправляет все запросы дальше.

### Код доступа к онлайн-словарю
Для использования сервиса онлайн-словарей рекомендуется получить собственный код доступа. По умолчанию в дополнении уже задан предварительно зарегистрированный код доступа. Но используемый в дополнении сервис онлайн-словарей накладывает определенные ограничения и лимиты запросов на каждого бесплатного пользователя. Поэтому при массовом использовании одного кода доступа - рано или поздно его могут заблокировать. Во избежание этого рекомендуется зарегистрировать собственный код доступа и указать его в настройках дополнения.

Ссылку для регистрации вы найдете ниже поля для ввода кода доступа, нажав на нее вы перейдете на соответствующую веб-страницу.

Примечание: Ссылка для регистрации отображается только при использовании кода доступа по умолчанию. После того, как вы укажете в настройках собственный код доступа, эта ссылка будет скрыто. Для того, чтобы восстановить код доступа по умолчанию, просто очистите поле для его ввода и нажмите "OK". Исходный код доступа будет восстановлен в конфигурации дополнения и вы увидите его открыв следующий раз диалоговое окно настроек.

## Добавление и управление профилями голосовых синтезаторов
В дополнении реализована возможность озвучивать полученные словарные статьи с помощью связанных с ними и заранее настроенных голосовых синтезаторов.

Чтобы воспользоваться этой возможностью, сначала необходимо создать и сохранить профили голосовых синтезаторов, а затем в диалоговом окне настройки дополнения связать эти профили с языками для которых они будут активироваться.

После этого при получении перевода для каждого заданного языка будет автоматически включаться связанный с ним голосовой синтезатор.

Управлять профилями можно с помощью клавишных команд или через соответствующее диалоговое окно. Чтобы открыть диалоговое окно со списком профилей голосовых синтезаторов - нажмите NVDA+N, перейдите в подменю "Сервис", далее - "Быстрый словарь" и активируйте команду "Профили голосовых синтезаторов..." или просто нажмите клавишу P в режиме управления дополнением (NVDA+Y).

### Создание профиля голосового синтезатора
Можно создать до 9 профилей настроек для различных голосовых синтезаторов которые доступны в NVDA.

Переключаться между профилями можно с помощью цифровых клавиш от 1 до 9 в режиме управления дополнением.

Например, чтобы создать профиль под номером 5 следует выполнить следующие действия:

1. Перейти в режим управления дополнением с помощью NVDA+Y.
2. Нажать клавишу 5. Вы услышите сообщение о том, что выбранный профиль под номером 5.
3. Перейти в раздел "Речь" настроек NVDA с помощью комбинации клавиш NVDA+Ctrl+V и настроить нужный голосовой синтезатор, который будет сохранен в выбранном профиле. После чего нажать кнопку "ОК".
4. Сохранить настроенный синтезатор в выбранном профиле - нажав NVDA+Y и затем клавишу V. Вы услышите сообщение об успешном сохранении профиля голосового синтезатора.

Примечание: Эту и другие операции также можно выполнить в диалоговом окне "Профили голосовых синтезаторов...".

### Активация голосового синтезатора по умолчанию
Чтобы вернуться к использованию первоначального голосового синтезатора нажмите NVDA+Y, после чего - клавишу R. Это восстановит работу голосового синтезатора, который был установлен при запуске NVDA, и вы услышите его название и выбранный голос.

### Переключение между профилями
Как уже упоминалось ранее - переключаться между профилями голосовых синтезаторов можно с помощью цифровых клавиш в режиме управления дополнением.

При этом если в профиле уже имеются настройки голосового синтезатора, то будет активирован соответствующий голос и вы услышите сообщение с информацией о номере активированного профиля и название синтезатора и голоса. Если же выбранный профиль еще не содержит никаких данных - будет выведено сообщение только о его номер и переключения синтезатора не произойдет.

Примечание: В любом случае вы можете вернуться к использованию голоса по умолчанию с помощью клавиши R (в режиме управления дополнением NVDA+Y).

### Переключение к предыдущему синтезатору голоса
Быстро вернуться к предыдущему синтезатору голоса можно нажав клавишу B в режиме управления дополнением.

### Сообщение о выбранном в данный момент профиле
Чтобы услышать какой профиль выбран в данный момент используется клавиша G (в режиме управления дополнением NVDA+Y).

Если профиль содержит настройки голосового синтезатора, то кроме номера будет также объявлено название синтезатора и имя настроенного голоса. В противном случае вы услышите только номер активного профиля.

### Удаление настроек из выбранного профиля
Чтобы удалить настройки голосового синтезатора из выбранного в данный момент профиля нужно воспользоваться клавишей Delete в режиме управления дополнением NVDA+Y.

Вы услышите сообщение об успешном удалении профиля и его номер.

### Сохранение изменений
После каждой манипуляции с профилем (создание/обновление/удаление) необходимо сохранять изменения с помощью клавиши V (в режиме управления дополнением NVDA+Y).

Нажав эту клавишу вы услышите соответствующее сообщение.

### Диалоговое окно "Профили голосовых синтезаторов"
Открыть диалоговое окно со списком профилей голосовых синтезаторов можно из меню NVDA - нажмите NVDA+N, перейдите в подменю "Сервис", далее - "Быстрый словарь" и активируйте пункт "Профили голосовых синтезаторов..." или просто нажмите клавишу P в режиме управления дополнением.

Для каждого профиля в списке указан его номер, название синтезатора, имя голоса и язык, связанный с ним.

Чтобы активировать профиль - перейдите к нему с помощью клавиш вверх или вниз и нажмите Enter или просто нажмите цифру, соответствующую номеру профиля.

В указанном диалоговом окне доступны также и другие операции с профилями голосовых синтезаторов. Чтобы выполнить одно из следующих действий - перейдите к соответствующей кнопки в диалоговом окне или воспользуйтесь клавишей, указанной в скобках:

* создать новый профиль (F7)
* изменить выбранный профиль (F4)
* удалить выбранный профиль (F8 или Delete)
* обновить список (F5)
* сохранить изменения (F2)

Примечание: По умолчанию связанный язык устанавливается как "- универсальный язык -". Это означает, что переключение на этот синтезатор не будет осуществляться. Процесс изменения связанного языка для каждого профиля будет рассмотрен ниже.

### Выбор связанного языка
Чтобы связать определенный профиль с нужным языком необходимо выполнить следующие действия:

1. Открыть диалоговое окно настроек дополнения - комбинация клавиш NVDA+Y, затем - O.
2. Найти и отметить галочку "Переключаться между голосовыми синтезаторами для выбранных языков".
3. Перейти табуляцией до нужного профиля и из списка рядом с ним выбрать язык, для которого он будет применяться.
4. Нажать "OK".

Примечание:

* Если ни одного профиля предварительно не было создано, в диалоговом окне настроек дополнения вы увидите предупреждение об этом.
* Каждый язык можно связать только с одним профилем. Если вы выбрали язык для одного из профилей, он автоматически будет удален из выпадающих списков для других профилей.
* Чтобы не использовать профиль для переключения синтезаторов - свяжите его с первым пунктом "- универсальный язык -".

### Процесс переключения голосовых синтезаторов
После выполнения указанных выше настроек, при получении данных из словаря будет автоматически включаться выбранный вами голосовой синтезатор. А после окончания объявления статьи снова активируется предыдущий голос.

Примечание: Если по какой-то причине переключение к предыдущему голосовому синтезатору не произошло - вы можете сделать это вручную нажав клавишу B или R в режиме управления дополнением.

## Справка по командам дополнения
Ознакомиться со списком всех команд, используемых в дополнении можно следующим образом:

* Через меню NVDA - нажав NVDA+N, перейти к подменю "Сервис", далее - "Быстрый словарь" и активировать пункт меню "Справка по командам дополнения".
* Нажать клавишу H в режиме управления дополнением (NVDA+Y).

## Справка
Чтобы открыть справку по дополнению - нажмите NVDA+N, перейдите в подменю "Сервис", далее - "Быстрый словарь" и активируйте пункт меню "Справка".

## Благодарности
Мы очень благодарны всем, кто прикладывает усилия в разработке, переводе и поддержке дополнения:

* Cagri Dogan - перевод на турецкий язык;
* Wafiqtaher - перевод на арабский язык.

В дополнении Quick Dictionary было использовано несколько хороших решений из других разработок. Благодарим авторов следующих дополнений:

* Instant Translate - Alexy Sadovoy, Beqa Gozalishvili, Mesar Hameed, Alberto Buffolino и другие соавторы.
* Для работы с профилями синтезаторов голоса были использованы идеи из дополнения Switch Synth (автор Tyler Spivey).

## Журнал изменений

### Версия 2.1.5
* дополнение протестировано на совместимость с NVDA 2022.1;
* исходный код значительно оптимизирован и добавлены MyPy подсказки типов;
* дополнение адаптировано для поддержки Python версий 3.7 и 3.8;
* исправлены ошибки форматирования в Markdown-файлах;
* добавлено диалоговое окно для редактирования текста перед отправкой его на удаленный сервис;
* отделена справка дополнения от ReadMe;
* обновлен перевод на турецкий язык (благодарность Cagri Dogan).

### Версия 2.0
* добавлена возможность подключения других сервисов онлайн-словарей;
* добавлен сервис Lexicala и его панель настроек;
* добавлено диалоговое окно выбора онлайн-сервиса из списка доступных;
* добавлена ​​команда для получения информации о выбранном сервисе;
* добавлено диалоговое окно для работы с профилями голосовых синтезаторов;
* реализована процедура переключения к предыдущему голосовому синтезатору;
* реализован параллельный поток для контроля состояния синтезатора;
* из-за увеличения количества функций в дополнении - справка по командам теперь отображается в отдельном окне;
* обновлено процедуру кэширования запросов к онлайн-сервисам;
* добавлено подменю дополнения в меню NVDA;
* обновлено ReadMe.

### Версия 1.2
* добавлена возможность автоматического переключения голосовых синтезаторов для выбранных языков;
* добавлена возможность загрузки актуального списка языков, доступных в Интернет-словаре;
* добавлен перевод на турецкий язык, благодарность Cagri Dogan;

### Версия 1.1
* изменены сочетания клавиш, которые конфликтовали с другими дополнениями;
* несколько сочетаний клавиш было отключено и дана возможность пользователю самостоятельно назначать их для функций дополнения;
* обновлено описание основных функций дополнения;
* обновлена справка и переводы дополнения;
* исправлена ошибка в украинском переводе (спасибо Владимиру Перогу);
* добавлен русский перевод.

### Версия 1.0: особенности реализации
* выполнение запросов к удаленному серверу в отдельном потоке, чтобы не блокировать работу NVDA;
* вывод сигналов при ожидании ответа от сервера;
* кеширование последних 100 запросов для снижения нагрузки на службу онлайн-словаря;
* реализован переход в режим управления дополнением;
* добавлена возможность использования альтернативного сервера;
* диалоговое окно настроек дополнения.

## Внесение изменений в NVDA QuickDictionary
Вы можете клонировать этот репозиторий, чтобы внести изменения в NVDA Quick Dictionary.

### Сторонние зависимости
Следующие модули могут быть установлены при помощи pip:

- markdown
- scons
- python-gettext

### Упаковка дополнения для распространения
1. Откройте командную строку, перейдите в корневой каталог этого репозитория.
2. Запустите команду **scons**. Созданное дополнение при отсутствии ошибок будет помещено в текущий каталог.
