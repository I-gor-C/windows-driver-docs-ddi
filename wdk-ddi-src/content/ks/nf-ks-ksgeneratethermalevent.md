---
UID: NF.ks.KsGenerateThermalEvent
title: KsGenerateThermalEvent
author: windows-driver-content
description: This function is used by clients (miniport drivers) that do not want to subscribe to the thermal manager, but want to do their own thermal management.
old-location: stream\ksgeneratethermalevent.htm
old-project: stream
ms.assetid: CE450017-1792-4B69-8289-902396D0D7B1
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: KsGenerateThermalEvent
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ks.h
req.include-header: 
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KsGenerateThermalEvent
req.alt-loc: ks.lib,ks.dll
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

# KsGenerateThermalEvent function



## -description
<p>This function is used by clients (miniport drivers) that do not want to subscribe to the thermal manager, but want to do their own thermal management. </p>
<p>There is a check that verifies whether the miniport driver has the query interface support for a thermal manager (for example, the device is actively managed by a thermal manager). In cases of devices managed by a thermal manager, this call is rejected.</p>


## -syntax

````
void KSDDKAPI NTSTATUS NTAPI KsGenerateThermalEvent(
  _In_ PVOID                  Object,
  _In_ KSDEVICE_THERMAL_STATE Value
);
````


## -parameters
<dl>

### -param <i>Object</i> [in]

<dd>
<p>Can be  <a href="https://msdn.microsoft.com/library/windows/hardware/ff561681">KSDEVICE</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff562522">KSFILTER</a>, or <a href="https://msdn.microsoft.com/library/windows/hardware/ff563483">KSPIN</a>. Depending on the object passed, the thermal notification is sent device-wide, filter-wide, or to the pin.</p>
</dd>

### -param <i>Value</i> [in]

<dd>
<p>KSDEVICE_THERMAL_STATE_LOW or KSDEVICE_THERMAL_STATE_HIGH</p>
</dd>
</dl>

## -returns
<p> Returns STATUS_SUCCESS for success and STATUS_INVALID_DEVICE_REQUEST if the parameters are incorrect.</p>

## -remarks


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
<dt>Ks.h</dt>
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