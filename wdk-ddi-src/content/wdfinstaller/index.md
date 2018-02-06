---
UID: NA:wdfinstaller
ms.assetid: 7d20668c-a0dd-32f7-aeef-8188b28028fb
ms.author: windowsdriverdev
ms.date: 01/18/18
ms.keywords: 
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: portal
---

# wdfinstaller.h header



wdfinstaller.h contains the following programming interfaces:





## Functions
| Title | Description |
| ---- |:---- |
| [WDF_COINSTALLER_INSTALL_OPTIONS_INIT](nf-wdfinstaller-wdf_coinstaller_install_options_init.md) | The WDF_COINSTALLER_INSTALL_OPTIONS_INIT function initializes a WDF_COINSTALLER_INSTALL_OPTIONS structure. |
| [WdfPostDeviceInstall](nf-wdfinstaller-wdfpostdeviceinstall.md) | The co-installer's WdfPostDeviceInstall function performs any operations that the co-installer might require after a non-Plug and Play (PnP) driver's installer has created the driver's kernel-mode service. |
| [WdfPostDeviceRemove](nf-wdfinstaller-wdfpostdeviceremove.md) | The co-installer's WdfPostDeviceRemove function performs any operations that the co-installer might require after a non-Plug and Play (PnP) driver's installer has deleted the driver's kernel-mode service. |
| [WdfPreDeviceInstall](nf-wdfinstaller-wdfpredeviceinstall.md) | The co-installer's WdfPreDeviceInstall function performs any operations that the co-installer might require before a non-Plug and Play (PnP) driver's installer creates the driver's kernel-mode service. |
| [WdfPreDeviceInstallEx](nf-wdfinstaller-wdfpredeviceinstallex.md) | The co-installer's WdfPreDeviceInstallEx function performs any operations that the co-installer might require before a non-Plug and Play (PnP) driver's installer creates the driver's kernel-mode service. |
| [WdfPreDeviceRemove](nf-wdfinstaller-wdfpredeviceremove.md) | The co-installer's WdfPreDeviceRemove function performs any operations that the co-installer might require before a non-Plug and Play (PnP) driver's installer deletes the driver's kernel-mode service. |



## Structures
| Title | Description |
| ---- |:---- |
| [_WDF_COINSTALLER_INSTALL_OPTIONS](ns-wdfinstaller-_wdf_coinstaller_install_options.md) | The WDF_COINSTALLER_INSTALL_OPTIONS structure contains installation options that a framework-based driver's installer can specify to the framework's co-installer. |