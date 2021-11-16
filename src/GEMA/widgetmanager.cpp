#include "widgetmanager.h"


WidgetManager::WidgetManager(Controller * controller) {
    this->controller = controller;
}

bool WidgetManager::addButton(string name, QString defaultText) {
    if (buttons[name] == nullptr) {
        buttons[name] = new QPushButton();
        buttons[name]->setText(defaultText);
        // qDebug("Yes");
        return true;
    }
    return false;
}


QPushButton* WidgetManager::getButton(string name) {
    return buttons[name];
}
