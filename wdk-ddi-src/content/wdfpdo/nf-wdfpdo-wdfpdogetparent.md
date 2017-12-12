---
UID: NF.wdfpdo.WdfPdoGetParent
title: WdfPdoGetParent function
author: windows-driver-content
description: The WdfPdoGetParent method returns a handle to the framework device object that represents the parent device of a specified device.
old-location: wdf\wdfpdogetparent.htm
old-project: wdf
ms.assetid: 62a2a316-afb4-4133-b256-933ea04c0994
ms.author: windowsdriverdev
ms.date: 12/7/2017
ms.keywords: WdfPdoGetParent
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdfpdo.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 
req.alt-api: WdfPdoGetParent
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
req.irql: <= DISPATCH_LEVEL
req.product: Windows 10 or later.
---

# WdfPdoGetParent function



## -description
<p class="CCE_Message">[Applies to KMDF only]

The <b>WdfPdoGetParent</b> method returns a handle to the framework device object that represents the parent device of a specified device.



## -syntax

````
WDFDEVICE WdfPdoGetParent(
  _In_ WDFDEVICE Device
);
````


## -parameters

### -param Device [in]

A handle to a framework device object that represents the device's physical device object (PDO).


## -returns
The method returns a handle to the framework device object that represents the specified device's parent, or <b>NULL</b> if the <i>Device</i> value does not represent a PDO. 

A system bug check occurs if the driver supplies an invalid object handle.

The following code example obtains a handle to the framework device object that represents a specified device's parent device.


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
<dt>Wdfpdo.h (include Wdf.h)</dt>
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
&lt;= DISPATCH_LEVEL

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