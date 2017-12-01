---
UID: NF.sensorscx.SensorsCxStateChange
title: SensorsCxStateChange
author: windows-driver-content
description: Used to initialize a state change.
old-location: sensors\sensorscxstatechange.htm
old-project: sensors
ms.assetid: E6897994-51C7-4278-9CCE-9B7E9DD408D7
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: SensorsCxStateChange
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: sensorscx.h
req.include-header: 
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: SensorsCxStateChange
req.alt-loc: SensorsCx.h
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

# SensorsCxStateChange function



## -description
<p>Used to initialize a state change.</p>


## -syntax

````
FORCEINLINE VOID SensorsCxStateChange(
  _In_ SENSOROBJECT Sensor,
  _In_ SENSOR_STATE State
);
````


## -parameters
<dl>

### -param <i>Sensor</i> [in]

<dd>
<p>Holds information on the sensor being managed by the driver.</p>
</dd>

### -param <i>State</i> [in]

<dd>
<p>Holds information on the state of the sensor.</p>
</dd>
</dl>

## -returns
<p>This function does not return a value.</p>

## -remarks


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
<dt>SensorsCx.h</dt>
</dl>
</td>
</tr>
</table>