---
UID: NF.wdffileobject.WdfFileObjectGetDevice
title: WdfFileObjectGetDevice function
author: windows-driver-content
description: The WdfFileObjectGetDevice method returns the framework device object that is associated with a specified framework file object.
old-location: wdf\wdffileobjectgetdevice.htm
old-project: wdf
ms.assetid: 10bb8bbd-0347-4ceb-844e-87f049813684
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: WdfFileObjectGetDevice
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdffileobject.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
req.alt-api: WdfFileObjectGetDevice
req.alt-loc: Wdf01000.sys,Wdf01000.sys.dll,WUDFx02000.dll,WUDFx02000.dll.dll
req.ddi-compliance: DriverCreate, KmdfIrql, KmdfIrql2
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Wdf01000.sys (KMDF); WUDFx02000.dll (UMDF)
req.dll: 
req.irql: <=DISPATCH_LEVEL
req.product: Windows 10 or later.
---

# WdfFileObjectGetDevice function



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]
The <b>WdfFileObjectGetDevice</b> method returns the framework device object that is associated with a specified framework file object.


## -syntax

````
WDFDEVICE WdfFileObjectGetDevice(
  _In_ WDFFILEOBJECT FileObject
);
````


## -parameters

### -param FileObject [in]

A handle to a framework file object.

## -returns
<b>WdfFileObjectGetDevice</b> returns a handle to the framework device object that is associated with the specified framework file object.

A bug check occurs if the driver supplies an invalid object handle.



## -remarks
For more information about framework file objects, see <a href="wdf.framework_file_objects">Framework File Objects</a>.

The following code example shows how an <a href="..\wdfdevice\nc-wdfdevice-evt_wdf_file_close.md">EvtFileClose</a> callback function can obtain the framework device object that is associated with a specified framework file object.

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
Minimum UMDF version
</th>
<td width="70%">
2.0
</td>
</tr>
<tr>
<th width="30%">
Header
</th>
<td width="70%">
<dl>
<dt>Wdffileobject.h (include Wdf.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library
</th>
<td width="70%">
<dl>
<dt>Wdf01000.sys (KMDF); </dt>
<dt>WUDFx02000.dll (UMDF)</dt>
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