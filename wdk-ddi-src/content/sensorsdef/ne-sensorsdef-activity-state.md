---
UID: NE.sensorsdef.ACTIVITY_STATE
title: ACTIVITY_STATE
author: windows-driver-content
description: This enumeration represents the activity states reported by the activity detection sensor.
old-location: sensors\activity_states.htm
old-project: sensors
ms.assetid: E602F16A-AFD8-4698-AC90-1686887FFEA6
ms.author: windowsdriverdev
ms.date: 11/26/2017
ms.keywords: SENSOR_CONTROLLER_CONFIG, SENSOR_CONTROLLER_CONFIG, *PSENSOR_CONTROLLER_CONFIG
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
req.alt-api: ACTIVITY_STATE
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

# ACTIVITY_STATE enumeration



## -description
<p>This enumeration represents the activity states reported by the activity detection sensor.</p>


## -syntax

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


## -enum-fields
<dl>

### -field <a id="ActivityState_Unknown"></a><a id="activitystate_unknown"></a><a id="ACTIVITYSTATE_UNKNOWN"></a><b>ActivityState_Unknown</b>

<dd>
<p>The sensor cannot accurately determine the current activity.</p>
</dd>

### -field <a id="ActivityState_Stationary"></a><a id="activitystate_stationary"></a><a id="ACTIVITYSTATE_STATIONARY"></a><b>ActivityState_Stationary</b>

<dd>
<p>Indicates that the sensor is currently stationary.</p>
</dd>

### -field <a id="ActivityState_Fidgeting"></a><a id="activitystate_fidgeting"></a><a id="ACTIVITYSTATE_FIDGETING"></a><b>ActivityState_Fidgeting</b>

<dd>
<p>Describes the current activity as "fidgeting."</p>
</dd>

### -field <a id="ActivityState_Walking"></a><a id="activitystate_walking"></a><a id="ACTIVITYSTATE_WALKING"></a><b>ActivityState_Walking</b>

<dd>
<p>Describes the current activity as "walking."</p>
</dd>

### -field <a id="ActivityState_Running"></a><a id="activitystate_running"></a><a id="ACTIVITYSTATE_RUNNING"></a><b>ActivityState_Running</b>

<dd>
<p>Describes the current activity as "running."</p>
</dd>

### -field <a id="ActivityState_InVehicle"></a><a id="activitystate_invehicle"></a><a id="ACTIVITYSTATE_INVEHICLE"></a><b>ActivityState_InVehicle</b>

<dd>
<p>Describes the current activity as "traveling in a vehicle."</p>
</dd>

### -field <a id="ActivityState_Biking"></a><a id="activitystate_biking"></a><a id="ACTIVITYSTATE_BIKING"></a><b>ActivityState_Biking</b>

<dd>
<p>Describes the current activity as "biking."</p>
</dd>

### -field <a id="ActivityState_Idle"></a><a id="activitystate_idle"></a><a id="ACTIVITYSTATE_IDLE"></a><b>ActivityState_Idle</b>

<dd>
<p>Describes the current activity as "idle."</p>
</dd>

### -field <a id="ActivityState_Max"></a><a id="activitystate_max"></a><a id="ACTIVITYSTATE_MAX"></a><b>ActivityState_Max</b>

<dd>
<p>Indicates that the current activity state is generating maximum sensor values. In this scenario the sensor doesn't indicate what the activity is.</p>
</dd>

### -field <a id="ActivityState_Force_Dword"></a><a id="activitystate_force_dword"></a><a id="ACTIVITYSTATE_FORCE_DWORD"></a><b>ActivityState_Force_Dword</b>

<dd>
<p>Used to force the ACTIVITY_STATE enum to a 32-bit data type (a DWORD).</p>
</dd>
</dl>

## -remarks
<p>For more information about the sensor data fields that use this enumeration, see <a href="https://msdn.microsoft.com/library/windows/hardware/dn957013">Activity detection sensor data fields</a>.</p>

<p>For more information about the sensor data fields that use this enumeration, see <a href="https://msdn.microsoft.com/library/windows/hardware/dn957013">Activity detection sensor data fields</a>.</p>

<p>For more information about the sensor data fields that use this enumeration, see <a href="https://msdn.microsoft.com/library/windows/hardware/dn957013">Activity detection sensor data fields</a>.</p>

## -requirements
<table>
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

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn957013">Activity detection sensor data fields</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [sensors\sensors]:%20ACTIVITY_STATE enumeration%20 RELEASE:%20(11/26/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
