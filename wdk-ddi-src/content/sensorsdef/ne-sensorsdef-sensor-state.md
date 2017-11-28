---
UID: NE.sensorsdef.SENSOR_STATE
title: SENSOR_STATE
author: windows-driver-content
description: This enumeration represents the valid states of a sensor.
old-location: sensors\sensor_state.htm
old-project: sensors
ms.assetid: F1E869AE-2FAF-402F-9C50-58D81E0EFF69
ms.author: windowsdriverdev
ms.date: 11/26/2017
ms.keywords: SENSOR_CONTROLLER_CONFIG, SENSOR_CONTROLLER_CONFIG, *PSENSOR_CONTROLLER_CONFIG
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: sensorsdef.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 8.1
req.target-min-winversvr: Windows Server 2012 R2
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: SENSOR_STATE
req.alt-loc: Sensorsdef.h
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

# SENSOR_STATE enumeration



## -description
<p>This enumeration represents the valid states of a sensor.</p>


## -syntax

````
typedef enum _SENSOR_STATE { 
  SensorState_Initializing  = 0,
  SensorState_Idle,
  SensorState_Active,
  SensorState_Error
} SENSOR_STATE;
````


## -enum-fields
<dl>

### -field <a id="SensorState_Initializing"></a><a id="sensorstate_initializing"></a><a id="SENSORSTATE_INITIALIZING"></a><b>SensorState_Initializing</b>

<dd>
<p>Indicates that the sensor is initializing.</p>
</dd>

### -field <a id="SensorState_Idle"></a><a id="sensorstate_idle"></a><a id="SENSORSTATE_IDLE"></a><b>SensorState_Idle</b>

<dd>
<p>Indicates that the sensor is idle</p>
</dd>

### -field <a id="SensorState_Active"></a><a id="sensorstate_active"></a><a id="SENSORSTATE_ACTIVE"></a><b>SensorState_Active</b>

<dd>
<p>Indicates that the sensor is active.</p>
</dd>

### -field <a id="SensorState_Error"></a><a id="sensorstate_error"></a><a id="SENSORSTATE_ERROR"></a><b>SensorState_Error</b>

<dd>
<p>Indicates that the sensor is in an error state.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 8.1</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2012 R2</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Sensorsdef.h</dt>
</dl>
</td>
</tr>
</table>