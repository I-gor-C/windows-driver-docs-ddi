---
UID: NE:sensorsdef.SENSOR_STATE
title: SENSOR_STATE
author: windows-driver-content
description: This enumeration represents the valid states of a sensor.
old-location: sensors\sensor_state.htm
old-project: sensors
ms.assetid: F1E869AE-2FAF-402F-9C50-58D81E0EFF69
ms.author: windowsdriverdev
ms.date: 2/22/2018
ms.keywords: SENSOR_STATE, SENSOR_STATE enumeration [Sensor Devices], SensorState_Active, SensorState_Error, SensorState_Idle, SensorState_Initializing, sensors.sensor_state, sensorsdef/SENSOR_STATE, sensorsdef/SensorState_Active, sensorsdef/SensorState_Error, sensorsdef/SensorState_Idle, sensorsdef/SensorState_Initializing
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
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	Sensorsdef.h
api_name:
-	SENSOR_STATE
product: Windows
targetos: Windows
req.typenames: SENSOR_STATE
req.product: Windows 10 or later.
---

# SENSOR_STATE Enumeration
This enumeration represents the valid states of a sensor.

## Syntax
````
typedef enum _SENSOR_STATE { 
  SensorState_Initializing  = 0,
  SensorState_Idle,
  SensorState_Active,
  SensorState_Error
} SENSOR_STATE;
````

## Constants

<table>
            
                <tr>
                    <td>SensorState_Initializing</td>
                    <td>Indicates that the sensor is initializing.</td>
                </tr>
            
                <tr>
                    <td>SensorState_Idle</td>
                    <td>Indicates that the sensor is idle</td>
                </tr>
            
                <tr>
                    <td>SensorState_Active</td>
                    <td>Indicates that the sensor is active.</td>
                </tr>
            
                <tr>
                    <td>SensorState_Error</td>
                    <td>Indicates that the sensor is in an error state.</td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8.1 Windows 8.1 |
| **Header** | sensorsdef.h |