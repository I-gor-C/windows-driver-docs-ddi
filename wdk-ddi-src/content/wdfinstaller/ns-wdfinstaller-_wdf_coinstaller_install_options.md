---
UID: NS.WDFINSTALLER._WDF_COINSTALLER_INSTALL_OPTIONS
title: _WDF_COINSTALLER_INSTALL_OPTIONS
author: windows-driver-content
description: The WDF_COINSTALLER_INSTALL_OPTIONS structure contains installation options that a framework-based driver's installer can specify to the framework's co-installer.
old-location: wdf\wdf_coinstaller_install_options.htm
old-project: wdf
ms.assetid: be8867e4-42be-4f11-bf4b-1b0fd29daa06
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: _WDF_COINSTALLER_INSTALL_OPTIONS, PWDF_COINSTALLER_INSTALL_OPTIONS, *PWDF_COINSTALLER_INSTALL_OPTIONS, WDF_COINSTALLER_INSTALL_OPTIONS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: wdfinstaller.h
req.include-header: Wdfinstaller.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.9
req.umdf-ver: 
req.alt-api: WDF_COINSTALLER_INSTALL_OPTIONS
req.alt-loc: wdfinstaller.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
req.product: Windows 10 or later.
---

# _WDF_COINSTALLER_INSTALL_OPTIONS structure



## -description
<p class="CCE_Message">[Applies to KMDF only]

The <b>WDF_COINSTALLER_INSTALL_OPTIONS</b> structure contains installation options that a framework-based driver's installer can specify to the framework's co-installer.



## -syntax

````
typedef struct _WDF_COINSTALLER_INSTALL_OPTIONS {
  ULONG Size;
  BOOL  ShowRebootPrompt;
} WDF_COINSTALLER_INSTALL_OPTIONS, *PWDF_COINSTALLER_INSTALL_OPTIONS;
````


## -struct-fields

### -field Size

The size, in bytes, of this structure.


### -field ShowRebootPrompt

A Boolean value. If this value is <b>TRUE</b>, and if the co-installer determines that the computer must be restarted to complete the driver installation, <a href="wdf.wdfpredeviceinstallex">WdfPreDeviceInstallEx</a> informs the Plug and Play (PnP) manager, and the PnP manager prompts the user that a restart is necessary.  

If this value is <b>FALSE</b>, and if the co-installer determines that the computer must be restarted to complete the driver installation, <a href="wdf.wdfpredeviceinstallex">WdfPreDeviceInstallEx</a> does not inform the PnP manager. 


## -remarks
The <b>WDF_COINSTALLER_INSTALL_OPTIONS</b> structure is used as an input parameter to <a href="wdf.wdfpredeviceinstallex">WdfPreDeviceInstallEx</a>.

Your installer should initialize the <b>WDF_COINSTALLER_INSTALL_OPTIONS</b> structure by calling <a href="wdf.wdf_coinstaller_install_options_init">WDF_COINSTALLER_INSTALL_OPTIONS_INIT</a>.


## -requirements
<table>
<tr>
<th width="30%">
Minimum KMDF version

</th>
<td width="70%">
1.9

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Wdfinstaller.h (include Wdfinstaller.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="wdf.wdf_coinstaller_install_options_init">WDF_COINSTALLER_INSTALL_OPTIONS_INIT</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WDF_COINSTALLER_INSTALL_OPTIONS structure%20 RELEASE:%20(12/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

