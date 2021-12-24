#include "command-controller.h"

#include <QList>
#include <QDebug>

using namespace gema	::framework;

namespace gema {
namespace controllers {

class CommandController::Implementation
{
public:
    Implementation(CommandController* _commandController)
        : commandController(_commandController)
    {
        Command* createClientSaveCommand = new Command( commandController, QChar( 0xf0c7 ), "Save" );
        Command* addCommand = new Command( commandController, QChar( 0xf055 ), "Add Item" );
        Command* deleteCommand = new Command( commandController, QChar( 0xf056 ), "Delete Item" );

        Command* addCategory = new Command( commandController, QChar( 0xf055 ), "Add Cat" );
        Command* deleteCategory = new Command( commandController, QChar( 0xf056 ), "Delete Cat" );
        Command* Search = new Command( commandController, QChar( 0xf002 ), "Search" );
        Command* FavoriteCommand = new Command( commandController, QChar( 0xf00c ), "Favorite" );
        Command* viewCommand = new Command( commandController, QChar( 0xf144 ), "View" );

        QObject::connect( createClientSaveCommand, &Command::executed, commandController, &CommandController::onCreateClientSaveExecuted );

        createClientViewContextCommands.append(addCommand);
        createClientViewContextCommands.append(deleteCommand);
        createClientViewContextCommands.append(addCategory);
        createClientViewContextCommands.append(deleteCategory);
        createClientViewContextCommands.append( createClientSaveCommand );
        createClientViewContextCommands.append( Search );
        createClientViewContextCommands.append( FavoriteCommand );
        createClientViewContextCommands.append( viewCommand );
    }

    CommandController* commandController{nullptr};

    QList<Command*> createClientViewContextCommands{};
};

CommandController::CommandController(QObject* parent)
    : QObject(parent)
{
    implementation.reset(new Implementation(this));
}

CommandController::~CommandController()
{
}

QQmlListProperty<Command> CommandController::ui_createClientViewContextCommands()
{
    return QQmlListProperty<Command>(this, implementation->createClientViewContextCommands);
}

void CommandController::onCreateClientSaveExecuted()
{
    qDebug() << "You executed the Save command!";
}

}}
