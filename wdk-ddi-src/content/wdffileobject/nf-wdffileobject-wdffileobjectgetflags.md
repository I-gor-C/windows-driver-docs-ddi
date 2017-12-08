---
UID: NF.wdffileobject.WdfFileObjectGetFlags
title: WdfFileObjectGetFlags function
author: windows-driver-content
description: The WdfFileObjectGetFlags method returns the flags that a specified framework file object contains.
old-location: wdf\wdffileobjectgetflags.htm
old-project: wdf
ms.assetid: f2f30acb-cab7-444a-8b86-6001a8a325b9
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: WdfFileObjectGetFlags
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdffileobject.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 
req.alt-api: WdfFileObjectGetFlags
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

# WdfFileObjectGetFlags function



## -description
<p class="CCE_Message">[Applies to KMDF only]
The <b>WdfFileObjectGetFlags</b> method returns the flags that a specified framework file object contains.


## -syntax

````
ULONG WdfFileObjectGetFlags(
  _In_ WDFFILEOBJECT FileObject
);
````


## -parameters

### -param FileObject [in]

A handle to a framework file object.

## -returns
<b>WdfFileObjectGetFlags</b> returns a bitwise OR of file object flags. The flag names have a format of FO_<i>XXX</i> and are defined in <i>Wdm.h</i>. 

A bug check occurs if the driver supplies an invalid object handle.



## -remarks
For more information about framework file objects, see <a href="wdf.framework_file_objects">Framework File Objects</a>.

The following code example obtains the flags that a specified framework file object contains.

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