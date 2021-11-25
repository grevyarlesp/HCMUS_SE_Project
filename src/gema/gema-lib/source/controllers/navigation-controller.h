#ifndef NAVIGATIONCONTROLLER_H
#define NAVIGATIONCONTROLLER_H

#include <QObject>

#include <gema-lib_global.h>
#include <models/client.h>

namespace gema {
namespace controllers {

class GEMALIBSHARED_EXPORT NavigationController : public QObject
{
    Q_OBJECT

public:
    explicit NavigationController(QObject* parent = nullptr) : QObject(parent){}

signals:
    void goCreateClientView();
    void goDashboardView();
    void goEditClientView(gema::models::Client* client);
    void goFindClientView();

};
}

}

#endif // NAVIGATIONCONTROLLER_H
