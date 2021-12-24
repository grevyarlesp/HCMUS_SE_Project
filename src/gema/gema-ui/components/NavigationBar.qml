import QtQuick 2.9
import assets 1.0

Item {
    anchors {
        top: parent.top
        bottom: parent.bottom
        left: parent.left
    }
    property bool isCollapsed: true

    width: isCollapsed ? Style.widthNavigationBarCollapsed : Style.heightNavigationBarExpanded
    Rectangle {
        anchors.fill: parent
        color: Style.colourNavigationBarBackground


        Column {
            NavigationButton {
                iconCharacter: "\uf0c9"
                description: ""
                hoverColour: "#993333"
                onNavigationButtonClicked: isCollapsed = !isCollapsed
            }
            NavigationButton {
                iconCharacter: "\uf015"
                description: "Dashboard"
                hoverColour: "#dc8a00"
                onNavigationButtonClicked: masterController.ui_navigationController.goDashboardView();
            }
            NavigationButton {
                iconCharacter: "\uf1c1"
                description: "All books"

                hoverColour: "#dc8a00"
                onNavigationButtonClicked: masterController.ui_navigationController.goCreateClientView();
            }
            NavigationButton {
                iconCharacter: "\uf647"
                description: "Collection"
                hoverColour: "#dc8a00"
                onNavigationButtonClicked: masterController.ui_navigationController.goCreateClientView();
            }
            NavigationButton {
                iconCharacter: "\uf1eb"
                description: "Client"
                hoverColour: "#dc8a00"
                onNavigationButtonClicked: masterController.ui_navigationController.goCreateClientView();
            }

            NavigationButton {
                iconCharacter: "\uf1e0"
                description: "Server"
                hoverColour: "#dc8a00"
                onNavigationButtonClicked: masterController.ui_navigationController.goCreateClientView();
            }
        }
    }
}
