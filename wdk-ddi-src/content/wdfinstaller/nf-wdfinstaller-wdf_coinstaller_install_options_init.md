---
UID: NF.wdfinstaller.WDF_COINSTALLER_INSTALL_OPTIONS_INIT
title: WDF_COINSTALLER_INSTALL_OPTIONS_INIT function
author: windows-driver-content
description: The WDF_COINSTALLER_INSTALL_OPTIONS_INIT function initializes a WDF_COINSTALLER_INSTALL_OPTIONS structure.
old-location: wdf\wdf_coinstaller_install_options_init.htm
old-project: wdf
ms.assetid: 65fd2c27-7d9e-4dad-adef-8cb2bea9d9f2
ms.author: windowsdriverdev
ms.date: 12/7/2017
ms.keywords: WDF_COINSTALLER_INSTALL_OPTIONS_INIT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdfinstaller.h
req.include-header: Wdfinstaller.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.9
req.umdf-ver: 
req.alt-api: WDF_COINSTALLER_INSTALL_OPTIONS_INIT
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

# WDF_COINSTALLER_INSTALL_OPTIONS_INIT function



## -description
<p class="CCE_Message">[Applies to KMDF only]

The <b>WDF_COINSTALLER_INSTALL_OPTIONS_INIT</b> function initializes a <a href="wdf.wdf_coinstaller_install_options">WDF_COINSTALLER_INSTALL_OPTIONS</a> structure.



## -syntax

````
VOID WDF_COINSTALLER_INSTALL_OPTIONS_INIT(
  _Out_ PWDF_COINSTALLER_INSTALL_OPTIONS ClientOptions
);
````


## -parameters

### -param ClientOptions [out]

A pointer to a <a href="wdf.wdf_coinstaller_install_options">WDF_COINSTALLER_INSTALL_OPTIONS</a> structure.


## -returns
None.


## -remarks
The <b>WDF_COINSTALLER_INSTALL_OPTIONS_INIT</b> function zeros the specified <a href="wdf.wdf_coinstaller_install_options">WDF_COINSTALLER_INSTALL_OPTIONS</a> structure and sets the structure's <b>Size</b> member.

The following code example initializes a <a href="wdf.wdf_coinstaller_install_options">WDF_COINSTALLER_INSTALL_OPTIONS</a> structure.


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
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
<a href="wdf.wdf_coinstaller_install_options">WDF_COINSTALLER_INSTALL_OPTIONS</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WDF_COINSTALLER_INSTALL_OPTIONS_INIT function%20 RELEASE:%20(12/7/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

