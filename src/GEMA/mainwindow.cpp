#include "mainwindow.h"
#include "ui_mainwindow.h"
#include "controller.h"
#include <QHBoxLayout>
#include "widgetmanager.h"

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    // , ui(new Ui::MainWindow)
{

    // ui->setupUi(this);
    this->resize(1000, 500);
    Controller *controller = new Controller;
    WidgetManager *widgetManager = new WidgetManager(controller);


    QWidget* widget = new QWidget(this);
    setCentralWidget(widget);
    QVBoxLayout *layout = new QVBoxLayout;
    widget->setLayout(layout);

    QHBoxLayout* hboxlayout1 = new QHBoxLayout, *hboxlayout2  = new QHBoxLayout;
    layout->addLayout(hboxlayout1,90);
    layout->addLayout(hboxlayout2,20);

    widgetManager->addButton("add", "Add");
    hboxlayout1->addWidget(widgetManager->getButton("add"));

    widgetManager->addButton("delete", "Delete");
    hboxlayout1->addWidget(widgetManager->getButton("delete"));

    widgetManager->addButton("modify", "Modify");
    hboxlayout1->addWidget(widgetManager->getButton("modify"));

}

MainWindow::~MainWindow() {
    // delete ui;
}

