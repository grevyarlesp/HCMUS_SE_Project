#ifndef MASTERCONTROLLER_H
#define MASTERCONTROLLER_H


#include <QObject>
#include <QString>
#include <QScopedPointer>

#include <gema-lib_global.h>
#include <controllers/navigation-controller.h>
#include <controllers/command-controller.h>

namespace gema {
namespace controllers {

class GEMALIBSHARED_EXPORT MasterController : public QObject {
    Q_OBJECT

    Q_PROPERTY( QString ui_welcomeMessage READ welcomeMessage CONSTANT )
    Q_PROPERTY(gema::controllers::NavigationController* ui_navigationController READ navigationController CONSTANT)
    Q_PROPERTY(gema::controllers::CommandController* ui_commandController READ commandController CONSTANT )

public:
    explicit MasterController(QObject* parent = nullptr);
    ~MasterController();

    NavigationController* navigationController();
    CommandController* commandController();
    const QString& welcomeMessage() const;

private:
    class Implementation;
    QScopedPointer<Implementation> implementation;
};

}}

#endif // MASTER-CONTROLLER_H
