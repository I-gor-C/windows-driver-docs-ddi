---
UID: NF.wdfwmi.WdfWmiProviderGetDevice
title: WdfWmiProviderGetDevice function
author: windows-driver-content
description: The WdfWmiProviderGetDevice method returns a handle to the framework device object that is the parent of a specified WMI provider object.
old-location: wdf\wdfwmiprovidergetdevice.htm
old-project: wdf
ms.assetid: 8d934e44-c6f9-42f7-81a6-202b6c97aca2
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: WdfWmiProviderGetDevice
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdfwmi.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 
req.alt-api: WdfWmiProviderGetDevice
req.alt-loc: Wdf01000.sys,Wdf01000.sys.dll
req.ddi-compliance: DriverCreate, KmdfIrql, KmdfIrql2
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Wdf01000.sys (see Framework Library Versioning.)
req.dll: 
req.irql: <=DISPATCH_LEVEL
req.product: Windows 10 or later.
---

# WdfWmiProviderGetDevice function



## -description
<p class="CCE_Message">[Applies to KMDF only]
The <b>WdfWmiProviderGetDevice</b> method returns a handle to the framework device object that is the parent of a specified WMI provider object.


## -syntax

````
WDFDEVICE WdfWmiProviderGetDevice(
  _In_ WDFWMIPROVIDER WmiProvider
);
````


## -parameters

### -param WmiProvider [in]

A handle to a WMI provider object that the driver obtained by calling <a href="wdf.wdfwmiprovidercreate">WdfWmiProviderCreate</a> or <a href="wdf.wdfwmiinstancegetprovider">WdfWmiInstanceGetProvider</a>.

## -returns
<b>WdfWmiProviderGetDevice</b> returns a handle to a framework device object.

A bug check occurs if the driver supplies an invalid object handle.



The following code example obtains a handle to the framework device object that is the parent of a specified WMI provider object.

## -remarks


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
1.0
</td>
</tr>
<tr>
<th width="30%">
Header
</th>
<td width="70%">
<dl>
<dt>Wdfwmi.h (include Wdf.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library
</th>
<td width="70%">
<dl>
<dt>Wdf01000.sys (see <a href="wdf.framework_library_versioning">Framework Library Versioning</a>.)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL
</th>
<td width="70%">
&lt;=DISPATCH_LEVEL
</td>
</tr>
<tr>
<th width="30%">
DDI compliance rules
</th>
<td width="70%">
<a href="devtest.kmdf_drivercreate">DriverCreate</a>, <a href="devtest.kmdf_kmdfirql">KmdfIrql</a>, <a href="devtest.kmdf_kmdfirql2">KmdfIrql2</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="wdf.wdfwmiinstancegetprovider">WdfWmiInstanceGetProvider</a>
</dt>
<dt>
<a href="wdf.wdfwmiprovidercreate">WdfWmiProviderCreate</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfWmiProviderGetDevice method%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
