# Declarations in the wdfinstaller header
This header Wdfinstaller contains these programming interfaces:

Callback

| Title        | Description    |
| ------------- |:-------------:|
| [PFN_WDFPREDEVICEREMOVE callback function](nc-wdfinstaller-pfn-wdfpredeviceremove.md) | TBD |
| [PFN_WDFPOSTDEVICEINSTALL callback function](nc-wdfinstaller-pfn-wdfpostdeviceinstall.md) | TBD |
| [PFN_WDFPOSTDEVICEREMOVE callback function](nc-wdfinstaller-pfn-wdfpostdeviceremove.md) | TBD |
| [PFN_WDFPREDEVICEINSTALL callback function](nc-wdfinstaller-pfn-wdfpredeviceinstall.md) | TBD |
| [PFN_WDFPREDEVICEINSTALLEX callback function](nc-wdfinstaller-pfn-wdfpredeviceinstallex.md) | TBD |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [WdfPostDeviceInstall function](nf-wdfinstaller-wdfpostdeviceinstall.md) | The co-installer's WdfPostDeviceInstall function performs any operations that the co-installer might require after a non-Plug and Play (PnP) driver's installer has created the driver's kernel-mode service. |
| [WdfPreDeviceInstall function](nf-wdfinstaller-wdfpredeviceinstall.md) | The co-installer's WdfPreDeviceInstall function performs any operations that the co-installer might require before a non-Plug and Play (PnP) driver's installer creates the driver's kernel-mode service. |
| [WdfPreDeviceRemove function](nf-wdfinstaller-wdfpredeviceremove.md) | The co-installer's WdfPreDeviceRemove function performs any operations that the co-installer might require before a non-Plug and Play (PnP) driver's installer deletes the driver's kernel-mode service. |
| [WdfPostDeviceRemove function](nf-wdfinstaller-wdfpostdeviceremove.md) | The co-installer's WdfPostDeviceRemove function performs any operations that the co-installer might require after a non-Plug and Play (PnP) driver's installer has deleted the driver's kernel-mode service. |
| [WDF_COINSTALLER_INSTALL_OPTIONS_INIT function](nf-wdfinstaller-wdf-coinstaller-install-options-init.md) | The WDF_COINSTALLER_INSTALL_OPTIONS_INIT function initializes a WDF_COINSTALLER_INSTALL_OPTIONS structure. |
| [WdfPreDeviceInstallEx function](nf-wdfinstaller-wdfpredeviceinstallex.md) | The co-installer's WdfPreDeviceInstallEx function performs any operations that the co-installer might require before a non-Plug and Play (PnP) driver's installer creates the driver's kernel-mode service. |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [WDF_COINSTALLER_INSTALL_OPTIONS structure](ns-wdfinstaller--wdf-coinstaller-install-options.md) | The WDF_COINSTALLER_INSTALL_OPTIONS structure contains installation options that a framework-based driver's installer can specify to the framework's co-installer. |

This header is used in these topics:

- [wdf](..content/_wdf)
