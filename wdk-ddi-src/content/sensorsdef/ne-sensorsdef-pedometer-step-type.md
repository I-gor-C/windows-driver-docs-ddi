---
UID: NE.sensorsdef.PEDOMETER_STEP_TYPE
title: PEDOMETER_STEP_TYPE
author: windows-driver-content
description: This enumeration represents the step types reported by the pedometer.
old-location: sensors\pedometer_step_type.htm
old-project: sensors
ms.assetid: 13ECDA33-2047-4F72-A8D4-5281C4BA8543
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
req.alt-api: PEDOMETER_STEP_TYPE
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

# PEDOMETER_STEP_TYPE enumeration



## -description
<p>This enumeration represents the step types reported by the pedometer.</p>


## -syntax

````
typedef enum _PEDOMETER_STEP_TYPE { 
  PedometerStepType_Unknown      = 0x00,
  PedometerStepType_Walking      = 0x01,
  PedometerStepType_Running      = 0x02,
  PedometerStepType_Max          = 1 << PedometerStepTypeCount,
  PedometerStepType_Force_Dword  = 0xFFFFFFFF
} PEDOMETER_STEP_TYPE;
````


## -enum-fields
<dl>

### -field <a id="PedometerStepType_Unknown"></a><a id="pedometersteptype_unknown"></a><a id="PEDOMETERSTEPTYPE_UNKNOWN"></a><b>PedometerStepType_Unknown</b>

<dd>
<p>The pedometer cannot determine the step type.</p>
</dd>

### -field <a id="PedometerStepType_Walking"></a><a id="pedometersteptype_walking"></a><a id="PEDOMETERSTEPTYPE_WALKING"></a><b>PedometerStepType_Walking</b>

<dd>
<p>Indicates a step type associated with walking.</p>
</dd>

### -field <a id="PedometerStepType_Running"></a><a id="pedometersteptype_running"></a><a id="PEDOMETERSTEPTYPE_RUNNING"></a><b>PedometerStepType_Running</b>

<dd>
<p>Indicates a step type associated with running.</p>
</dd>

### -field <a id="PedometerStepType_Max"></a><a id="pedometersteptype_max"></a><a id="PEDOMETERSTEPTYPE_MAX"></a><b>PedometerStepType_Max</b>

<dd>
<p>Indicates that the step type is generating maximum sensor values. In this scenario, the pedometer doesn't report the step type.</p>
</dd>

### -field <a id="PedometerStepType_Force_Dword"></a><a id="pedometersteptype_force_dword"></a><a id="PEDOMETERSTEPTYPE_FORCE_DWORD"></a><b>PedometerStepType_Force_Dword</b>

<dd>
<p>Used to force the PEDOMETER_STEP_TYPE enum to a 32-bit data type (a DWORD).</p>
</dd>
</dl>

## -remarks
<p>For more information about the sensor data fields that use this enumeration, see <a href="https://msdn.microsoft.com/library/windows/hardware/dn957076">Pedometer data fields</a>.</p>

<p>For more information about the sensor data fields that use this enumeration, see <a href="https://msdn.microsoft.com/library/windows/hardware/dn957076">Pedometer data fields</a>.</p>

<p>For more information about the sensor data fields that use this enumeration, see <a href="https://msdn.microsoft.com/library/windows/hardware/dn957076">Pedometer data fields</a>.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/dn957076">Pedometer data fields</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/mt138359">PEDOMETER_STEP_TYPE_COUNT</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [sensors\sensors]:%20PEDOMETER_STEP_TYPE enumeration%20 RELEASE:%20(11/26/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
