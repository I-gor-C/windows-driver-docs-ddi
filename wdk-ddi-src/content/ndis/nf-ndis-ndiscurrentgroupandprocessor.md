---
UID: NF.ndis.NdisCurrentGroupAndProcessor
title: NdisCurrentGroupAndProcessor
author: windows-driver-content
description: The NdisCurrentGroupAndProcessor function returns the group-relative processor number and group number of the current processor.
old-location: netvista\ndiscurrentgroupandprocessor.htm
old-project: netvista
ms.assetid: 056f7f4b-152b-426a-b59e-0f6663b386a8
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: NdisCurrentGroupAndProcessor
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Universal
req.target-min-winverclnt: Supported in NDIS 6.20 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdisCurrentGroupAndProcessor
req.alt-loc: ndis.lib,ndis.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ndis.lib
req.dll: 
req.irql: >= DISPATCH_LEVEL
req.iface: 
---

# NdisCurrentGroupAndProcessor function



## -description
<p>The
  <b>NdisCurrentGroupAndProcessor</b> function returns the group-relative processor number and group number of
  the current processor.</p>


## -syntax

````
PROCESSOR_NUMBER NdisCurrentGroupAndProcessor(void);
````


## -parameters


## -returns
<p><b>NdisCurrentGroupAndProcessor</b> returns a PROCESSOR_NUMBER value that contains the group-relative
     processor number and group number of the current processor.</p>

<p><b>NdisCurrentGroupAndProcessor</b> returns a PROCESSOR_NUMBER value that contains the group-relative
     processor number and group number of the current processor.</p>

<p><b>NdisCurrentGroupAndProcessor</b> returns a PROCESSOR_NUMBER value that contains the group-relative
     processor number and group number of the current processor.</p>

## -remarks
<p>NDIS drivers call the 
    <b>NdisCurrentGroupAndProcessor</b> function to obtain the group-relative processor number and group
    number of the current processor.</p>

<p>The PROCESSOR_NUMBER structure contains a 
    <b>Group</b> member of type USHORT and a 
    <b>Number</b> member of type UCHAR for group and processor numbers, respectively. The group and processor
    numbers are zero-based values.</p>

<p>NDIS drivers call the 
    <b>NdisCurrentGroupAndProcessor</b> function to obtain the group-relative processor number and group
    number of the current processor.</p>

<p>The PROCESSOR_NUMBER structure contains a 
    <b>Group</b> member of type USHORT and a 
    <b>Number</b> member of type UCHAR for group and processor numbers, respectively. The group and processor
    numbers are zero-based values.</p>

<p>NDIS drivers call the 
    <b>NdisCurrentGroupAndProcessor</b> function to obtain the group-relative processor number and group
    number of the current processor.</p>

<p>The PROCESSOR_NUMBER structure contains a 
    <b>Group</b> member of type USHORT and a 
    <b>Number</b> member of type UCHAR for group and processor numbers, respectively. The group and processor
    numbers are zero-based values.</p>

<p>NDIS drivers call the 
    <b>NdisCurrentGroupAndProcessor</b> function to obtain the group-relative processor number and group
    number of the current processor.</p>

<p>The PROCESSOR_NUMBER structure contains a 
    <b>Group</b> member of type USHORT and a 
    <b>Number</b> member of type UCHAR for group and processor numbers, respectively. The group and processor
    numbers are zero-based values.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported in NDIS 6.20 and later.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ndis.h (include Ndis.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Ndis.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&gt;= DISPATCH_LEVEL</p>
</td>
</tr>
</table>