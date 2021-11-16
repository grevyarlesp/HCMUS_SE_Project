#ifndef WIDGETMANAGER_H
#define WIDGETMANAGER_H

#include <QMainWindow>
#include <QObject>
#include <QWidget>
#include "controller.h"
#include "map"
#include "string"
#include <QLabel>
#include <QPushButton>
#include <QString>
#include <QDebug>

class Controller;

using std::map;
using std::string;

class WidgetManager {
private:
    map<string, QLabel*> labels;
    map<string, QPushButton*> buttons;
    Controller *controller;
public:
    WidgetManager(Controller * controller);
    bool addButton(string name, QString defaultText="Button");
    QPushButton* getButton(string name);
};

#endif // WIDGETMANAGER_H
