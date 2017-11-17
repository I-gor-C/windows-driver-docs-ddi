---
UID: NF.sensorscx.SensorsCxStateChange
title: SensorsCxStateChange
author: windows-driver-content
description: Used to initialize a state change.
old-location: sensors\sensorscxstatechange.htm
ms.assetid: E6897994-51C7-4278-9CCE-9B7E9DD408D7
ms.author: windowsdriverdev
ms.date: 10/23/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: sensors
req.header: sensorscx.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: SensorsCxStateChange
req.alt-loc: sensorscx.h
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
ms.keywords: SensorsCxStateChange
req.iface: 
req.product: Windows 10 or later.
---

# SensorsCxStateChange function



## -description
<p class="CCE_Message">[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.]</p>
<p>Used to initialize a state change.</p>


## -syntax

````
VOID WDFAPI SensorsCxStateChange(
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
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Sensorscx.h</dt>
</dl>
</td>
</tr>
</table>