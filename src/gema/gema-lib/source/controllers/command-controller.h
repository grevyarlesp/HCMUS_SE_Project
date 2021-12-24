#ifndef COMMANDCONTROLLER_H
#define COMMANDCONTROLLER_H

#include <QObject>
#include <QtQml/QQmlListProperty>
#include <gema-lib_global.h>
#include <framework/command.h>

namespace gema {
namespace controllers {

class GEMALIBSHARED_EXPORT CommandController : public QObject
{
    Q_OBJECT

    Q_PROPERTY(QQmlListProperty<gema::framework::Command> ui_createClientViewContextCommands READ ui_createClientViewContextCommands CONSTANT)
public:
    explicit CommandController(QObject* _parent = nullptr);
    ~CommandController();

    QQmlListProperty<framework::Command> ui_createClientViewContextCommands();

public slots:
    void onCreateClientSaveExecuted();

private:
    class Implementation;
    QScopedPointer<Implementation> implementation;
};

}}

#endif
