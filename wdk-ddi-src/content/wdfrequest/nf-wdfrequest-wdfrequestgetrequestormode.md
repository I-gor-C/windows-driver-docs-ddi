---
UID: NF.wdfrequest.WdfRequestGetRequestorMode
title: WdfRequestGetRequestorMode function
author: windows-driver-content
description: The WdfRequestGetRequestorMode method returns the processor access mode of the originator of a specified I/O request.
old-location: wdf\wdfrequestgetrequestormode.htm
old-project: wdf
ms.assetid: 63fc77c8-756c-4872-b608-539d8419154b
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: WdfRequestGetRequestorMode
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdfrequest.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
req.alt-api: WdfRequestGetRequestorMode
req.alt-loc: Wdf01000.sys,Wdf01000.sys.dll,WUDFx02000.dll,WUDFx02000.dll.dll
req.ddi-compliance: DriverCreate, InvalidReqAccess, InvalidReqAccessLocal, KmdfIrql, KmdfIrql2
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

# WdfRequestGetRequestorMode function



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]

The <b>WdfRequestGetRequestorMode</b> method returns the processor access mode of the originator of a specified I/O request.



## -syntax

````
KPROCESSOR_MODE WdfRequestGetRequestorMode(
  _In_ WDFREQUEST Request
);
````


## -parameters

### -param Request [in]

A handle to a framework request object.


## -returns
<b>WdfRequestGetRequestorMode</b> returns <b>KernelMode</b> if the originator of the I/O request is executing in kernel mode. Otherwise, this method returns <b>UserMode</b>. The <b>KernelMode</b> and <b>UserMode</b> constants are defined in <i>wdm.h</i>.

A bug check occurs if the driver supplies an invalid object handle.




## -remarks
For more information about <b>WdfRequestGetRequestorMode</b>, see <a href="wdf.obtaining_information_about_an_i_o_request">Obtaining Information About an I/O Request</a>.

The following code example is from the <a href="wdf.sample_kmdf_drivers">NDISProt</a> sample driver. This example checks for a valid MAC address if the I/O request came from a user-mode application.


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
<dt>Wdfrequest.h (include Wdf.h)</dt>
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
<a href="devtest.kmdf_drivercreate">DriverCreate</a>, <a href="devtest.kmdf_invalidreqaccess">InvalidReqAccess</a>, <a href="devtest.kmdf_invalidreqaccesslocal">InvalidReqAccessLocal</a>, <a href="devtest.kmdf_kmdfirql">KmdfIrql</a>, <a href="devtest.kmdf_kmdfirql2">KmdfIrql2</a>
</td>
</tr>
</table>