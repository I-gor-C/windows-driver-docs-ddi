---
UID: NE.sensorsdef.MAGNETOMETER_ACCURACY
title: MAGNETOMETER_ACCURACY
author: windows-driver-content
description: This enumeration represents the accuracy states of the magnetometer.
old-location: sensors\magnetometer_accuracy.htm
old-project: sensors
ms.assetid: BC8D4FB1-69F4-4FAE-BA90-7CCB57D4A6C4
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
req.alt-api: MAGNETOMETER_ACCURACY
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

# MAGNETOMETER_ACCURACY enumeration



## -description
<p>This enumeration represents the accuracy states of the magnetometer.</p>


## -syntax

````
typedef enum _MAGNETOMETER_ACCURACY { 
  MagnetometerAccuracy_Unknown      = 0,
  MagnetometerAccuracy_Unreliable,
  MagnetometerAccuracy_Approximate,
  MagnetometerAccuracy_High
} MAGNETOMETER_ACCURACY;
````


## -enum-fields
<dl>

### -field <a id="MagnetometerAccuracy_Unknown"></a><a id="magnetometeraccuracy_unknown"></a><a id="MAGNETOMETERACCURACY_UNKNOWN"></a><b>MagnetometerAccuracy_Unknown</b>

<dd>
<p>Indicates that the magnetometer's accuracy cannot be determined.</p>
</dd>

### -field <a id="MagnetometerAccuracy_Unreliable"></a><a id="magnetometeraccuracy_unreliable"></a><a id="MAGNETOMETERACCURACY_UNRELIABLE"></a><b>MagnetometerAccuracy_Unreliable</b>

<dd>
<p>Indicates that the magnetometer readings are unreliable. The application can choose to prompt the user to calibrate the compass, to improve accuracy.</p>
</dd>

### -field <a id="MagnetometerAccuracy_Approximate"></a><a id="magnetometeraccuracy_approximate"></a><a id="MAGNETOMETERACCURACY_APPROXIMATE"></a><b>MagnetometerAccuracy_Approximate</b>

<dd>
<p>Indicates that the magnetometer readings are approximate values.</p>
</dd>

### -field <a id="MagnetometerAccuracy_High"></a><a id="magnetometeraccuracy_high"></a><a id="MAGNETOMETERACCURACY_HIGH"></a><b>MagnetometerAccuracy_High</b>

<dd>
<p>Indicates that the magnetometer accuracy is set to high.</p>
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