---
UID: NE:sensorsdef.ACTIVITY_STATE
title: ACTIVITY_STATE
author: windows-driver-content
description: This enumeration represents the activity states reported by the activity detection sensor.
old-location: sensors\activity_states.htm
old-project: sensors
ms.assetid: E602F16A-AFD8-4698-AC90-1686887FFEA6
ms.author: windowsdriverdev
ms.date: 2/8/2018
ms.keywords: sensors.activity_states, sensorsdef/ActivityState_Running, ActivityState_Fidgeting, ActivityState_Unknown, sensorsdef/ActivityState_Max, sensorsdef/ActivityState_Stationary, sensorsdef/ActivityState_Force_Dword, sensorsdef/ActivityState_Biking, ActivityState_Running, ActivityState_InVehicle, sensorsdef/ActivityState_InVehicle, sensorsdef/ActivityState_Idle, sensorsdef/ActivityState_Unknown, ActivityState_Idle, ActivityState_Biking, ActivityState_Max, ActivityState_Walking, sensorsdef/ACTIVITY_STATE, ACTIVITY_STATE enumeration [Sensor Devices], ActivityState_Force_Dword, sensorsdef/ActivityState_Walking, sensorsdef/ActivityState_Fidgeting, ActivityState_Stationary, ACTIVITY_STATE
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
topictype:
-	APIRef
-	kbSyntax
apitype:
-	HeaderDef
apilocation:
-	Sensorsdef.h
apiname:
-	ACTIVITY_STATE
product: Windows
targetos: Windows
req.typenames: ACTIVITY_STATE
req.product: Windows 10 or later.
---

# ACTIVITY_STATE Enumeration
This enumeration represents the activity states reported by the activity detection sensor.

## Syntax
````
typedef enum _ACTIVITY_STATES { 
  ActivityState_Unknown      = 0x00000001,
  ActivityState_Stationary   = 0x00000002,
  ActivityState_Fidgeting    = 0x00000004,
  ActivityState_Walking      = 0x00000008,
  ActivityState_Running      = 0x00000010,
  ActivityState_InVehicle    = 0x00000020,
  ActivityState_Biking       = 0x00000040,
  ActivityState_Idle         = 0x00000080,
  ActivityState_Max          = 0x00000100,
  ActivityState_Force_Dword  = 0xFFFFFFFF
} ACTIVITY_STATE;
````

## Constants

<table>
            
                <tr>
                    <td>ActivityState_Biking</td>
                    <td>Describes the current activity as "biking."</td>
                </tr>
            
                <tr>
                    <td>ActivityState_Fidgeting</td>
                    <td>Describes the current activity as "fidgeting."</td>
                </tr>
            
                <tr>
                    <td>ActivityState_Force_Dword</td>
                    <td>Used to force the ACTIVITY_STATE enum to a 32-bit data type (a DWORD).</td>
                </tr>
            
                <tr>
                    <td>ActivityState_Idle</td>
                    <td>Describes the current activity as "idle."</td>
                </tr>
            
                <tr>
                    <td>ActivityState_InVehicle</td>
                    <td>Describes the current activity as "traveling in a vehicle."</td>
                </tr>
            
                <tr>
                    <td>ActivityState_Max</td>
                    <td>Indicates that the current activity state is generating maximum sensor values. In this scenario the sensor doesn't indicate what the activity is.</td>
                </tr>
            
                <tr>
                    <td>ActivityState_Running</td>
                    <td>Describes the current activity as "running."</td>
                </tr>
            
                <tr>
                    <td>ActivityState_Stationary</td>
                    <td>Indicates that the sensor is currently stationary.</td>
                </tr>
            
                <tr>
                    <td>ActivityState_Unknown</td>
                    <td>The sensor cannot accurately determine the current activity.</td>
                </tr>
            
                <tr>
                    <td>ActivityState_Walking</td>
                    <td>Describes the current activity as "walking."</td>
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



 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [sensors\sensors]:%20ACTIVITY_STATE enumeration%20 RELEASE:%20(2/8/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>