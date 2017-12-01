---
UID: NE.wdm._DEVICE_INSTALL_STATE
title: DEVICE_INSTALL_STATE
author: windows-driver-content
description: The DEVICE_INSTALL_STATE enumeration describes a device's installation state.
old-location: kernel\device_install_state.htm
old-project: kernel
ms.assetid: 82b702ae-ea62-4bc1-ad92-467eba027e3d
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: WDI_TYPE_PMK_NAME, WDI_TYPE_PMK_NAME, *PWDI_TYPE_PMK_NAME
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: wdm.h
req.include-header: Wdm.h
req.target-type: Windows
req.target-min-winverclnt: Available in Microsoft Windows XP and later versions of the Windows operating system.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DEVICE_INSTALL_STATE
req.alt-loc: wdm.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# DEVICE_INSTALL_STATE enumeration



## -description
<p>The <b>DEVICE_INSTALL_STATE</b> enumeration describes a device's installation state.</p>


## -syntax

````
typedef enum _DEVICE_INSTALL_STATE { 
  InstallStateInstalled       = 0,
  InstallStateNeedsReinstall  = 1,
  InstallStateFailedInstall   = 2,
  InstallStateFinishInstall   = 3
} DEVICE_INSTALL_STATE, *PDEVICE_INSTALL_STATE;
````


## -enum-fields
<dl>

### -field <a id="InstallStateInstalled"></a><a id="installstateinstalled"></a><a id="INSTALLSTATEINSTALLED"></a><b>InstallStateInstalled</b>

<dd>
<p>The device is installed.</p>
</dd>

### -field <a id="InstallStateNeedsReinstall"></a><a id="installstateneedsreinstall"></a><a id="INSTALLSTATENEEDSREINSTALL"></a><b>InstallStateNeedsReinstall</b>

<dd>
<p>The system will try to reinstall the device on a later enumeration.</p>
</dd>

### -field <a id="InstallStateFailedInstall"></a><a id="installstatefailedinstall"></a><a id="INSTALLSTATEFAILEDINSTALL"></a><b>InstallStateFailedInstall</b>

<dd>
<p>The device did not install properly.</p>
</dd>

### -field <a id="InstallStateFinishInstall"></a><a id="installstatefinishinstall"></a><a id="INSTALLSTATEFINISHINSTALL"></a><b>InstallStateFinishInstall</b>

<dd>
<p>The installation of this device is not yet complete. </p>
</dd>
</dl>

## -remarks
<p>The <a href="..\wdm\nf-wdm-iogetdeviceproperty.md">IoGetDeviceProperty</a> routine supplies a <b>DEVICE_INSTALL_STATE</b> enumeration value when a driver requests <b>DevicePropertyInstallState</b>. The operating system uses the value as a hint about the install state of the device.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Microsoft Windows XP and later versions of the Windows operating system.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdm.h (include Wdm.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="kernel.device_registry_property">DEVICE_REGISTRY_PROPERTY</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-iogetdeviceproperty.md">IoGetDeviceProperty</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20DEVICE_INSTALL_STATE enumeration%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
