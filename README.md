# Деплой ML сервиса в Kubernetes
В рамках задания было выполнено:
1. Поднят локальный kubernetes кластер с помощью minikube
2. Запущен как 3 экземпляра подов flask сервис с инференсом простой GradientBoostingClassifier модели, обученной на датасете iris
3. Настроен service для взаимодействия с подами
4. Настроен Ingress (nginx)

### Запущенные поды:
<img src="https://github.com/VictoriaKlyueva/kubernetes_task/blob/master/images/Running%20pods.png">

### Запущенный Ingress (nginx):
<img src="https://github.com/VictoriaKlyueva/kubernetes_task/blob/master/images/Configured%20ingress.png">

### Работающий эндпоинт:
<img src="https://github.com/VictoriaKlyueva/kubernetes_task/blob/master/images/REST%20request%20to%20service%20in%20cluster.png">

### Анализ возникших проблем
Была проблема с запуском кластера. При первой попытке запуска кластер поднялся успешно, но позже упал. Как оказалось, были проблемы с виртуализацией в Windows. После обновления операционной системы и включения вирутализации удалось снова поднять кластер.\
При попытке запустить поды возникали проблемы с обращением к docker-registry, но проблема решилась натсройкой созданием secrets.
