---
UID: NF.mrx.RxMakeLateDeviceAvailable
title: RxMakeLateDeviceAvailable
author: windows-driver-content
description: RxMakeLateDeviceAvailable modifies the device object to make a &#0034;late device&#0034; available. A late device is one that is not created in the driver's load routine.
old-location: ifsk\rxmakelatedeviceavailable.htm
old-project: ifsk
ms.assetid: 0818907f-3346-42a2-b123-3298ea8f9a1d
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: RxMakeLateDeviceAvailable
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: mrx.h
req.include-header: Mrx.h, Rxstruc.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RxMakeLateDeviceAvailable
req.alt-loc: mrx.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <= APC_LEVEL
req.iface: 
---

# RxMakeLateDeviceAvailable function



## -description
<p><b>RxMakeLateDeviceAvailable</b> modifies the device object to make a "late device" available. A late device is one that is not created in the driver's load routine.</p>


## -syntax

````
VOID RxMakeLateDeviceAvailable(
  _In_ PRDBSS_DEVICE_OBJECT RxDeviceObject
);
````


## -parameters
<dl>

### -param <i>RxDeviceObject</i> [in]

<dd>
<p>A pointer to the where the created device object is to be stored.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p><b>RxMakeLateDeviceAvailable</b> clears the DO_DEVICE_INITIALIZING bit in the <b>Flags</b> member of the device object. </p>

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
<dt>Mrx.h (include Mrx.h or Rxstruc.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;= APC_LEVEL</p>
</td>
</tr>
</table>