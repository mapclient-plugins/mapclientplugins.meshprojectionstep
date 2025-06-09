# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'configuredialog.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QDialog,
    QDialogButtonBox, QDoubleSpinBox, QFormLayout, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_ConfigureDialog(object):
    def setupUi(self, ConfigureDialog):
        if not ConfigureDialog.objectName():
            ConfigureDialog.setObjectName(u"ConfigureDialog")
        ConfigureDialog.resize(467, 457)
        self.gridLayout = QGridLayout(ConfigureDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.configGroupBox = QGroupBox(ConfigureDialog)
        self.configGroupBox.setObjectName(u"configGroupBox")
        self.verticalLayout = QVBoxLayout(self.configGroupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.labelIdentifier = QLabel(self.configGroupBox)
        self.labelIdentifier.setObjectName(u"labelIdentifier")

        self.horizontalLayout.addWidget(self.labelIdentifier)

        self.lineEditIdentifier = QLineEdit(self.configGroupBox)
        self.lineEditIdentifier.setObjectName(u"lineEditIdentifier")

        self.horizontalLayout.addWidget(self.lineEditIdentifier)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.checkBoxStandardisedXYPlaneOutput = QCheckBox(self.configGroupBox)
        self.checkBoxStandardisedXYPlaneOutput.setObjectName(u"checkBoxStandardisedXYPlaneOutput")

        self.verticalLayout.addWidget(self.checkBoxStandardisedXYPlaneOutput)

        self.groupBoxFixedProjection = QGroupBox(self.configGroupBox)
        self.groupBoxFixedProjection.setObjectName(u"groupBoxFixedProjection")
        self.groupBoxFixedProjection.setCheckable(True)
        self.groupBoxFixedProjection.setChecked(False)
        self.formLayout = QFormLayout(self.groupBoxFixedProjection)
        self.formLayout.setObjectName(u"formLayout")
        self.labelPoint = QLabel(self.groupBoxFixedProjection)
        self.labelPoint.setObjectName(u"labelPoint")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.labelPoint)

        self.labelPointX = QLabel(self.groupBoxFixedProjection)
        self.labelPointX.setObjectName(u"labelPointX")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.labelPointX)

        self.doubleSpinBoxPointX = QDoubleSpinBox(self.groupBoxFixedProjection)
        self.doubleSpinBoxPointX.setObjectName(u"doubleSpinBoxPointX")
        self.doubleSpinBoxPointX.setDecimals(4)
        self.doubleSpinBoxPointX.setMinimum(-999999.999900000053458)
        self.doubleSpinBoxPointX.setMaximum(999999.999900000053458)
        self.doubleSpinBoxPointX.setSingleStep(0.100000000000000)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.doubleSpinBoxPointX)

        self.labelPointY = QLabel(self.groupBoxFixedProjection)
        self.labelPointY.setObjectName(u"labelPointY")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.labelPointY)

        self.doubleSpinBoxPointY = QDoubleSpinBox(self.groupBoxFixedProjection)
        self.doubleSpinBoxPointY.setObjectName(u"doubleSpinBoxPointY")
        self.doubleSpinBoxPointY.setDecimals(4)
        self.doubleSpinBoxPointY.setMinimum(-999999.999900000053458)
        self.doubleSpinBoxPointY.setMaximum(999999.999900000053458)
        self.doubleSpinBoxPointY.setSingleStep(0.100000000000000)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.doubleSpinBoxPointY)

        self.labelPointZ = QLabel(self.groupBoxFixedProjection)
        self.labelPointZ.setObjectName(u"labelPointZ")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.labelPointZ)

        self.doubleSpinBoxPointZ = QDoubleSpinBox(self.groupBoxFixedProjection)
        self.doubleSpinBoxPointZ.setObjectName(u"doubleSpinBoxPointZ")
        self.doubleSpinBoxPointZ.setDecimals(4)
        self.doubleSpinBoxPointZ.setMinimum(-999999.999900000053458)
        self.doubleSpinBoxPointZ.setMaximum(999999.999900000053458)
        self.doubleSpinBoxPointZ.setSingleStep(0.100000000000000)
        self.doubleSpinBoxPointZ.setValue(0.000000000000000)

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.doubleSpinBoxPointZ)

        self.labelNormal = QLabel(self.groupBoxFixedProjection)
        self.labelNormal.setObjectName(u"labelNormal")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.labelNormal)

        self.labelNormalX = QLabel(self.groupBoxFixedProjection)
        self.labelNormalX.setObjectName(u"labelNormalX")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.labelNormalX)

        self.doubleSpinBoxNormalX = QDoubleSpinBox(self.groupBoxFixedProjection)
        self.doubleSpinBoxNormalX.setObjectName(u"doubleSpinBoxNormalX")
        self.doubleSpinBoxNormalX.setDecimals(4)
        self.doubleSpinBoxNormalX.setMinimum(-999999.999900000053458)
        self.doubleSpinBoxNormalX.setMaximum(999999.999900000053458)
        self.doubleSpinBoxNormalX.setSingleStep(0.100000000000000)

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.doubleSpinBoxNormalX)

        self.labelNormalY = QLabel(self.groupBoxFixedProjection)
        self.labelNormalY.setObjectName(u"labelNormalY")

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.labelNormalY)

        self.doubleSpinBoxNormalY = QDoubleSpinBox(self.groupBoxFixedProjection)
        self.doubleSpinBoxNormalY.setObjectName(u"doubleSpinBoxNormalY")
        self.doubleSpinBoxNormalY.setDecimals(4)
        self.doubleSpinBoxNormalY.setMinimum(-999999.999900000053458)
        self.doubleSpinBoxNormalY.setMaximum(999999.999900000053458)
        self.doubleSpinBoxNormalY.setSingleStep(0.100000000000000)

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.doubleSpinBoxNormalY)

        self.labelNormalZ = QLabel(self.groupBoxFixedProjection)
        self.labelNormalZ.setObjectName(u"labelNormalZ")

        self.formLayout.setWidget(9, QFormLayout.LabelRole, self.labelNormalZ)

        self.doubleSpinBoxNormalZ = QDoubleSpinBox(self.groupBoxFixedProjection)
        self.doubleSpinBoxNormalZ.setObjectName(u"doubleSpinBoxNormalZ")
        self.doubleSpinBoxNormalZ.setDecimals(4)
        self.doubleSpinBoxNormalZ.setMinimum(-999999.999900000053458)
        self.doubleSpinBoxNormalZ.setMaximum(999999.999900000053458)
        self.doubleSpinBoxNormalZ.setSingleStep(0.100000000000000)
        self.doubleSpinBoxNormalZ.setValue(1.000000000000000)

        self.formLayout.setWidget(9, QFormLayout.FieldRole, self.doubleSpinBoxNormalZ)

        self.labelMeshCoordinates = QLabel(self.groupBoxFixedProjection)
        self.labelMeshCoordinates.setObjectName(u"labelMeshCoordinates")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.labelMeshCoordinates)

        self.labelDatapointCoordinates = QLabel(self.groupBoxFixedProjection)
        self.labelDatapointCoordinates.setObjectName(u"labelDatapointCoordinates")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.labelDatapointCoordinates)

        self.lineEditMeshCoordinates = QLineEdit(self.groupBoxFixedProjection)
        self.lineEditMeshCoordinates.setObjectName(u"lineEditMeshCoordinates")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEditMeshCoordinates)

        self.lineEditDatapointCoordinates = QLineEdit(self.groupBoxFixedProjection)
        self.lineEditDatapointCoordinates.setObjectName(u"lineEditDatapointCoordinates")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEditDatapointCoordinates)


        self.verticalLayout.addWidget(self.groupBoxFixedProjection)


        self.gridLayout.addWidget(self.configGroupBox, 0, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(ConfigureDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)


        self.retranslateUi(ConfigureDialog)
        self.buttonBox.accepted.connect(ConfigureDialog.accept)
        self.buttonBox.rejected.connect(ConfigureDialog.reject)

        QMetaObject.connectSlotsByName(ConfigureDialog)
    # setupUi

    def retranslateUi(self, ConfigureDialog):
        ConfigureDialog.setWindowTitle(QCoreApplication.translate("ConfigureDialog", u"Configure Mesh Projection", None))
        self.configGroupBox.setTitle("")
        self.labelIdentifier.setText(QCoreApplication.translate("ConfigureDialog", u"Identifier:  ", None))
#if QT_CONFIG(tooltip)
        self.checkBoxStandardisedXYPlaneOutput.setToolTip(QCoreApplication.translate("ConfigureDialog", u"Rotate the projected mesh from its arbitrary 2D plane onto the X-Y plane for standardised output.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxStandardisedXYPlaneOutput.setText(QCoreApplication.translate("ConfigureDialog", u"Output to X-Y Plane", None))
        self.groupBoxFixedProjection.setTitle(QCoreApplication.translate("ConfigureDialog", u"Fixed Projection", None))
        self.labelPoint.setText(QCoreApplication.translate("ConfigureDialog", u"Point", None))
        self.labelPointX.setText(QCoreApplication.translate("ConfigureDialog", u"x:", None))
        self.labelPointY.setText(QCoreApplication.translate("ConfigureDialog", u"y:", None))
        self.labelPointZ.setText(QCoreApplication.translate("ConfigureDialog", u"z:", None))
        self.labelNormal.setText(QCoreApplication.translate("ConfigureDialog", u"Normal", None))
        self.labelNormalX.setText(QCoreApplication.translate("ConfigureDialog", u"x:", None))
        self.labelNormalY.setText(QCoreApplication.translate("ConfigureDialog", u"y:", None))
        self.labelNormalZ.setText(QCoreApplication.translate("ConfigureDialog", u"z:", None))
        self.labelMeshCoordinates.setText(QCoreApplication.translate("ConfigureDialog", u"Mesh coordinates:", None))
        self.labelDatapointCoordinates.setText(QCoreApplication.translate("ConfigureDialog", u"Datapoint coordinates:", None))
        self.lineEditMeshCoordinates.setText(QCoreApplication.translate("ConfigureDialog", u"coordinates", None))
        self.lineEditDatapointCoordinates.setText(QCoreApplication.translate("ConfigureDialog", u"coordinates", None))
    # retranslateUi

