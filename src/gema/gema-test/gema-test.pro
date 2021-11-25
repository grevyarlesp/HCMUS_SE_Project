QT += testlib
QT -= gui

CONFIG += console c++14
CONFIG -= app_bundle

TEMPLATE = app
TARGET = client-tests

include(../qmake-target-platform.pri)
include(../qmake-destination-path.pri)

INCLUDEPATH += source

SOURCES += \
    source/model/client-tests.cpp


LIBS += -L$$PWD/../binaries/$$DESTINATION_PATH -lgema-lib


DESTDIR = $$PWD/../binaries/$$DESTINATION_PATH
OBJECTS_DIR = $$PWD/build/$$DESTINATION_PATH/.obj
MOC_DIR = $$PWD/build/$$DESTINATION_PATH/.moc
RCC_DIR = $$PWD/build/$$DESTINATION_PATH/.qrc
UI_DIR = $$PWD/build/$$DESTINATION_PATH/.ui
