---
UID: NE:sensorsdef.ACTIVITY_STATE
title: ACTIVITY_STATE
author: windows-driver-content
description: This enumeration represents the activity states reported by the activity detection sensor.
old-location: sensors\activity_states.htm
old-project: sensors
ms.assetid: E602F16A-AFD8-4698-AC90-1686887FFEA6
ms.author: windowsdriverdev
ms.date: 2/22/2018
ms.keywords: ACTIVITY_STATE, ACTIVITY_STATE enumeration [Sensor Devices], ActivityState_Biking, ActivityState_Fidgeting, ActivityState_Force_Dword, ActivityState_Idle, ActivityState_InVehicle, ActivityState_Max, ActivityState_Running, ActivityState_Stationary, ActivityState_Unknown, ActivityState_Walking, sensors.activity_states, sensorsdef/ACTIVITY_STATE, sensorsdef/ActivityState_Biking, sensorsdef/ActivityState_Fidgeting, sensorsdef/ActivityState_Force_Dword, sensorsdef/ActivityState_Idle, sensorsdef/ActivityState_InVehicle, sensorsdef/ActivityState_Max, sensorsdef/ActivityState_Running, sensorsdef/ActivityState_Stationary, sensorsdef/ActivityState_Unknown, sensorsdef/ActivityState_Walking
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: sensorsdef.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
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
-	ACTIVITY_STATE
product:
- Windows
targetos: Windows
req.typenames: ACTIVITY_STATE
req.product: Windows 10 or later.
---

# ACTIVITY_STATE Enumeration
This enumeration represents the activity states reported by the activity detection sensor.

## Syntax
```
typedef enum ACTIVITY_STATE {
  ActivityState_Unknown      ,
  ActivityState_Stationary   ,
  ActivityState_Fidgeting    ,
  ActivityState_Walking      ,
  ActivityState_Running      ,
  ActivityState_InVehicle    ,
  ActivityState_Biking       ,
  ActivityState_Idle         ,
  ActivityState_Max          ,
  ActivityState_Force_Dword
} ;
```

## Constants

<table>
            
                <tr>
                    <td>ActivityState_Unknown</td>
                    <td>The sensor cannot accurately determine the current activity.</td>
                </tr>
            
                <tr>
                    <td>ActivityState_Stationary</td>
                    <td>Indicates that the sensor is currently stationary.</td>
                </tr>
            
                <tr>
                    <td>ActivityState_Fidgeting</td>
                    <td>Describes the current activity as "fidgeting."</td>
                </tr>
            
                <tr>
                    <td>ActivityState_Walking</td>
                    <td>Describes the current activity as "walking."</td>
                </tr>
            
                <tr>
                    <td>ActivityState_Running</td>
                    <td>Describes the current activity as "running."</td>
                </tr>
            
                <tr>
                    <td>ActivityState_InVehicle</td>
                    <td>Describes the current activity as "traveling in a vehicle."</td>
                </tr>
            
                <tr>
                    <td>ActivityState_Biking</td>
                    <td>Describes the current activity as "biking."</td>
                </tr>
            
                <tr>
                    <td>ActivityState_Idle</td>
                    <td>Describes the current activity as "idle."</td>
                </tr>
            
                <tr>
                    <td>ActivityState_Max</td>
                    <td>Indicates that the current activity state is generating maximum sensor values. In this scenario the sensor doesn't indicate what the activity is.</td>
                </tr>
            
                <tr>
                    <td>ActivityState_Force_Dword</td>
                    <td>Used to force the ACTIVITY_STATE enum to a 32-bit data type (a DWORD).</td>
                </tr>
</table>

## Remarks

For more information about the sensor data fields that use this enumeration, see <a href="https://msdn.microsoft.com/library/windows/hardware/dn957013">Activity detection sensor data fields</a>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | sensorsdef.h |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/dn957013">Activity detection sensor data fields</a>