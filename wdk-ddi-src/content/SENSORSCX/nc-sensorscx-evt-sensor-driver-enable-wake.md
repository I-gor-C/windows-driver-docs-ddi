---
UID: NC.sensorscx.EVT_SENSOR_DRIVER_ENABLE_WAKE
title: EVT_SENSOR_DRIVER_ENABLE_WAKE
author: windows-driver-content
description: Callback to enable wake for the sensor.
old-location: sensors\evt_sensor_driver_enable_wake.htm
ms.assetid: 969E08D1-0D4A-4FED-9722-4EDA067C522C
ms.author: windowsdriverdev
ms.date: 10/23/2017
ms.topic: callback
ms.prod: windows-hardware
ms.technology: sensors
req.header: sensorscx.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: EVT_SENSOR_DRIVER_ENABLE_WAKE
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
req.irql: _requires_same_
ms.keywords: SDP_TREE_ROOT_NODE, SDP_TREE_ROOT_NODE, *PSDP_TREE_ROOT_NODE
req.iface: 
req.product: Windows 10 or later.
---

# EVT_SENSOR_DRIVER_ENABLE_WAKE callback



## -description
<p class="CCE_Message">[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.]</p>
<p>Callback to enable wake for the sensor. </p>


## -prototype

````
NTSTATUS CALLBACK EVT_SENSOR_DRIVER_ENABLE_WAKE(
  _In_ SENSOROBJECT Sensor
);
````


## -parameters
<dl>

### -param <i>Sensor</i> [in]

<dd>
<p>A reference to the sensor object</p>
</dd>
</dl>

## -returns
<p>This function returns STATUS_SUCCESS when completed successfully.</p>

## -remarks
<p>This DDSI function does not compulsorily have to be implemented by the driver because it is expected that some sensor drivers do not care about enabling wake on the sensor. If it not implemented the enable call is ignored and a STATUS_SUCCESS is returned. This is primarily because PKEY_Sensor_WakeCapable is implemented today and used by some sensors such as the accelerometer and the proximity sensor, and for backward compatibility, implementing this DDSI is optional.</p>

<p>This DDSI function does not compulsorily have to be implemented by the driver because it is expected that some sensor drivers do not care about enabling wake on the sensor. If it not implemented the enable call is ignored and a STATUS_SUCCESS is returned. This is primarily because PKEY_Sensor_WakeCapable is implemented today and used by some sensors such as the accelerometer and the proximity sensor, and for backward compatibility, implementing this DDSI is optional.</p>

## -requirements
<table>
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
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>_requires_same_</p>
</td>
</tr>
</table>