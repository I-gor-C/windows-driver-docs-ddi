---
UID: NF.ndis.NdisGetVersion
title: NdisGetVersion function
author: windows-driver-content
description: The NdisGetVersion function returns the version number of NDIS.
old-location: netvista\ndisgetversion.htm
old-project: netvista
ms.assetid: d3e2c799-f789-499f-9948-f41d7576296e
ms.author: windowsdriverdev
ms.date: 12/8/2017
ms.keywords: NdisGetVersion
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Universal
req.target-min-winverclnt: Supported for NDIS 6.0 and NDIS 5.1 drivers (see    NdisGetVersion (NDIS 5.1)) in   Windows Vista. Supported for NDIS 5.1 drivers (see    NdisGetVersion (NDIS 5.1)) in   Windows XP.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdisGetVersion
req.alt-loc: ndis.lib,ndis.dll
req.ddi-compliance: Irql_Miscellaneous_Function
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ndis.lib
req.dll: 
req.irql: <= DISPATCH_LEVEL
---

# NdisGetVersion function



## -description
The 
  <b>NdisGetVersion</b> function returns the version number of NDIS.



## -syntax

````
UINT NdisGetVersion(void);
````


## -parameters


## -returns
Returns the major and minor numbers for the NDIS version in the high and low halves of the
     unsigned integer respectively.

Returns the major and minor numbers for the NDIS version in the high and low halves of the
     unsigned integer respectively.

Returns the major and minor numbers for the NDIS version in the high and low halves of the
     unsigned integer respectively.


## -remarks
System support for 
    <b>NdisGetVersion</b> is available in Windows XP and later versions.


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
Version

</th>
<td width="70%">
Supported for NDIS 6.0 and NDIS 5.1 drivers (see 
   <a href="https://msdn.microsoft.com/library/windows/hardware/ff552120">NdisGetVersion (NDIS 5.1)</a>) in
   Windows Vista. Supported for NDIS 5.1 drivers (see 
   <b>NdisGetVersion (NDIS 5.1)</b>) in
   Windows XP.

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Ndis.h (include Ndis.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library

</th>
<td width="70%">
<dl>
<dt>Ndis.lib</dt>
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
<a href="devtest.ndis_irql_miscellaneous_function">Irql_Miscellaneous_Function</a>
</td>
</tr>
</table>