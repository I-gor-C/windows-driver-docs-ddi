---
UID: NF.ndis.NdisMResetMiniport
title: NdisMResetMiniport
author: windows-driver-content
description: A miniport driver calls the NdisMResetMiniport function to trigger a later reset operation from NDIS.
old-location: netvista\ndismresetminiport.htm
ms.assetid: 614C6E21-00D0-4F57-9E09-D1BAB166BA42
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: netvista
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Universal
req.target-min-winverclnt: Supported in NDIS 6.30 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdisMResetMiniport
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
req.irql: <= DISPATCH_LEVEL
ms.keywords: NdisMResetMiniport
req.iface: 
---

# NdisMResetMiniport function



## -description
<p>A miniport driver calls the <b>NdisMResetMiniport</b> function to trigger a later reset operation from NDIS.</p>


## -syntax

````
void NdisMResetMiniport(
  _In_ NDIS_HANDLE MiniportAdapterHandle
);
````


## -parameters
<dl>

### -param <i>MiniportAdapterHandle</i> [in]

<dd>
<p>The miniport adapter handle that NDIS passed to the <i>MiniportAdapterHandle</i> parameter of <a href="https://msdn.microsoft.com/b146fa81-005b-4a6c-962d-4cb023ea790e">MiniportInitializeEx</a>.</p>
</dd>
</dl>

## -returns
<p>This function does not return a value.</p>

## -remarks
<p>A miniport driver calls <b>NdisMResetMiniport</b> when it determines that the device requires a hardware reset.</p>

<p>As a result, NDIS schedules a work item for calling the miniport driver's <a href="https://msdn.microsoft.com/15f82163-a1b5-4cef-a53e-8a97adb2cd92">MiniportResetEx</a> function asynchronously.</p>

<p><b>NdisMResetMiniport</b> must be called at IRQL &lt;= DISPATCH_LEVEL.</p>

<p>A miniport driver calls <b>NdisMResetMiniport</b> when it determines that the device requires a hardware reset.</p>

<p>As a result, NDIS schedules a work item for calling the miniport driver's <a href="https://msdn.microsoft.com/15f82163-a1b5-4cef-a53e-8a97adb2cd92">MiniportResetEx</a> function asynchronously.</p>

<p><b>NdisMResetMiniport</b> must be called at IRQL &lt;= DISPATCH_LEVEL.</p>

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
<p>Supported in NDIS 6.30 and later.</p>
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
<p>&lt;= DISPATCH_LEVEL</p>
</td>
</tr>
</table>