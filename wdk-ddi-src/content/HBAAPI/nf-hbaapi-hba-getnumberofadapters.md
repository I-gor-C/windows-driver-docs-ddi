---
UID: NF.hbaapi.HBA_GetNumberOfAdapters
title: HBA_GetNumberOfAdapters
author: windows-driver-content
description: The HBA_GetNumberOfAdapters routine returns the number of HBAs supported by the library.
old-location: storage\hba_getnumberofadapters.htm
ms.assetid: 5864a535-4ff8-4c9a-abf9-f835c7fde305
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: Storage
req.header: hbaapi.h
req.include-header: Hbaapi.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: HBA_GetNumberOfAdapters
req.alt-loc: Hbaapi.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Hbaapi.lib
req.dll: Hbaapi.dll
req.irql: 
ms.keywords: HBA_GetNumberOfAdapters
req.iface: 
---

# HBA_GetNumberOfAdapters function



## -description
<p>The <b>HBA_GetNumberOfAdapters</b> routine returns the number of HBAs supported by the library. </p>


## -syntax

````
HBA_UINT32 HBA_API HBA_GetNumberOfAdapters(void);
````


## -parameters


## -returns
<p>The <b>HBA_GetNumberOfAdapters</b> routine returns the number of adapters supported by this library. If no adapters are supported, <b>HBA_GetNumberOfAdapters</b> returns 0.</p>

<p>The <b>HBA_GetNumberOfAdapters</b> routine returns the number of adapters supported by this library. If no adapters are supported, <b>HBA_GetNumberOfAdapters</b> returns 0.</p>

<p>The <b>HBA_GetNumberOfAdapters</b> routine returns the number of adapters supported by this library. If no adapters are supported, <b>HBA_GetNumberOfAdapters</b> returns 0.</p>

## -remarks
<p>The <b>HBA_GetNumberOfAdapters</b> routine allows the caller to dynamically determine the size of the HBA inventory without having to restart the system, the HBA drivers, or the library. </p>

<p>The <b>HBA_GetNumberOfAdapters</b> routine allows the caller to dynamically determine the size of the HBA inventory without having to restart the system, the HBA drivers, or the library. </p>

<p>The <b>HBA_GetNumberOfAdapters</b> routine allows the caller to dynamically determine the size of the HBA inventory without having to restart the system, the HBA drivers, or the library. </p>

<p>The <b>HBA_GetNumberOfAdapters</b> routine allows the caller to dynamically determine the size of the HBA inventory without having to restart the system, the HBA drivers, or the library. </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Hbaapi.h (include Hbaapi.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Hbaapi.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>Hbaapi.dll</dt>
</dl>
</td>
</tr>
</table>