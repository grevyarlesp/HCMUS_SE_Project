#include "master-controller.h"

namespace gema {
namespace controllers {

class MasterController::Implementation
{
public:
    Implementation(MasterController* _masterController) : masterController(_masterController) {
        navigationController = new NavigationController(masterController);
    }

    MasterController* masterController{nullptr};
    NavigationController* navigationController{nullptr};
    QString welcomeMessage = "This is master controller";
};

MasterController::MasterController(QObject* parent) : QObject(parent) {
    implementation.reset(new Implementation(this));
}

MasterController::~MasterController() {

}

NavigationController* MasterController::navigationController() {
    return implementation->navigationController;
}

const QString& MasterController::welcomeMessage() const {
    return implementation->welcomeMessage;
}

}

}
