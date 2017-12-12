---
UID: NF.wdfdpc.WdfDpcGetParentObject
title: WdfDpcGetParentObject function
author: windows-driver-content
description: The WdfDpcGetParentObject method returns the parent object of a specified DPC object.
old-location: wdf\wdfdpcgetparentobject.htm
old-project: wdf
ms.assetid: 77ebca0f-3056-4f11-9d59-fbd166967ed3
ms.author: windowsdriverdev
ms.date: 12/7/2017
ms.keywords: WdfDpcGetParentObject
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdfdpc.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 
req.alt-api: WdfDpcGetParentObject
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
req.irql: Any level
req.product: Windows 10 or later.
---

# WdfDpcGetParentObject function



## -description
<p class="CCE_Message">[Applies to KMDF only]

The <b>WdfDpcGetParentObject</b> method returns the parent object of a specified DPC object.



## -syntax

````
WDFOBJECT WdfDpcGetParentObject(
  _In_ WDFDPC Dpc
);
````


## -parameters

### -param Dpc [in]

A handle to a framework DPC object.


## -returns
<b>WdfDpcGetParentObject</b> returns a handle to the parent object of a specified DPC object.

A bug check occurs if the driver supplies an invalid object handle.




## -remarks
A driver might call <b>WdfDpcGetParentObject</b> from within its <a href="wdf.evtdpcfunc">EvtDpcFunc</a> callback function.

The following code example returns a handle to the parent object of a specified DPC object. The <a href="wdf.wdfdpccreate">WdfDpcCreate</a> code example shows how the specified DPC object was created.


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
<dt>Wdfdpc.h (include Wdf.h)</dt>
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
Any level

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
<a href="wdf.evtdpcfunc">EvtDpcFunc</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfDpcGetParentObject method%20 RELEASE:%20(12/7/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

