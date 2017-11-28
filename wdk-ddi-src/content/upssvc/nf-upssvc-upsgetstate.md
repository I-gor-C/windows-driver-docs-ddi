---
UID: NF.upssvc.UPSGetState
title: UPSGetState
author: windows-driver-content
description: The UPSGetState function returns the operational state of the UPS.
old-location: battery\upsgetstate.htm
old-project: battery
ms.assetid: c60284ff-ebbd-455d-949c-e6d31ce65d5d
ms.author: windowsdriverdev
ms.date: 11/16/2017
ms.keywords: UPSGetState
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: upssvc.h
req.include-header: Upssvc.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: UPSGetState
req.alt-loc: Upssvc.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
req.iface: 
req.product: Windows 10 or later.
---

# UPSGetState function



## -description
<p>The <b>UPSGetState</b> function returns the operational state of the UPS.</p>


## -syntax

````
DWORD UPSGetState(
   void 
);
````


## -parameters
<dl>

### -param <i></i> 

<dd>
<p>None</p>
</dd>
</dl>

## -returns
<p>The <b>UPSGetState</b> function returns one of the following DWORD values:</p><dl>
<dt><b>UPS_ONLINE </b></dt>
</dl><p>Utility-supplied power is normal.</p><dl>
<dt><b>UPS_ONBATTERY</b></dt>
</dl><p>Utility-supplied power is inadequate, and the UPS batteries are discharging.</p><dl>
<dt><b>UPS_LOWBATTERY</b></dt>
</dl><p>Utility-supplied power is inadequate, and the UPS batteries are critically low.</p><dl>
<dt><b>UPS_NOCOMM</b></dt>
</dl><p>Communication with the UPS is not currently established.</p>

<p> </p>

## -remarks
<p>This is a nonblocking call. </p>

<p>This is a nonblocking call. </p>

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
<dt>Upssvc.h (include Upssvc.h)</dt>
</dl>
</td>
</tr>
</table>