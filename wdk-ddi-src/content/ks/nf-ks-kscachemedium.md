---
UID: NF.ks.KsCacheMedium
title: KsCacheMedium
author: windows-driver-content
description: The KsCacheMedium function improves graph building performance of pins that use Mediums to define connectivity.
old-location: stream\kscachemedium.htm
old-project: stream
ms.assetid: d0e9c146-5d73-49e8-92a8-c453f5bbbfe9
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: KsCacheMedium
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ks.h
req.include-header: Ks.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KsCacheMedium
req.alt-loc: Ks.lib,Ks.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ks.lib
req.dll: 
req.irql: 
req.iface: 
---

# KsCacheMedium function



## -description
<p>The <b>KsCacheMedium</b> function improves graph building performance of pins that use Mediums to define connectivity.</p>


## -syntax

````
NTSTATUS KsCacheMedium(
  _In_ PUNICODE_STRING SymbolicLink,
  _In_ PKSPIN_MEDIUM   Medium,
  _In_ ULONG           PinDirection
);
````


## -parameters
<dl>

### -param <i>SymbolicLink</i> [in]

<dd>
<p>The symbolic link used to open the device interface.</p>
</dd>

### -param <i>Medium</i> [in]

<dd>
<p>Points to the medium to cache.</p>
</dd>

### -param <i>PinDirection</i> [in]

<dd>
<p>Contains the direction of the Pin.  1 is output, 0 is input.</p>
</dd>
</dl>

## -returns
<p><b>KsCacheMedium</b> returns STATUS_SUCCESS if the caching operation is successful, failure if it is not.</p>

## -remarks
<p><b>KsCacheMedium</b> improves graph building performance by creating a registry key at: </p>

<p><b>\System\CurrentControlSet\Control\MediumCache\GUID\DWORD\DWORD </b></p>

<p>This enables fast lookup of connected filters in TvTuner and other complex graphs.  Note that the GUID identifies the Medium of the connection, and that the DWORDs denote the device instance.  The value name is the SymbolicLink for the driver, and ActualValue is the pin direction.turning. </p>

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
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ks.h (include Ks.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Ks.lib</dt>
</dl>
</td>
</tr>
</table>