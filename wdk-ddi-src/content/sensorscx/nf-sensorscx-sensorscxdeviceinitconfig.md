---
UID: NF.sensorscx.SensorsCxDeviceInitConfig
title: SensorsCxDeviceInitConfig
author: windows-driver-content
description: This function configures the sensor device.
old-location: sensors\sensorscxdeviceinitconfig.htm
old-project: sensors
ms.assetid: E347F2E1-5AF5-411A-8F05-DA4826240E02
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: SensorsCxDeviceInitConfig
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
req.alt-api: SensorsCxDeviceInitConfig
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

# SensorsCxDeviceInitConfig function



## -description
<p>This function configures the sensor device.</p>


## -syntax

````
FORCEINLINE NTSTATUS SensorsCxDeviceInitConfig(
  _Inout_ PWDFDEVICE_INIT        pFxDeviceInit,
  _Inout_ PWDF_OBJECT_ATTRIBUTES pFdoAttributes,
  _In_    ULONG                  Flags
);
````


## -parameters
<dl>

### -param <i>pFxDeviceInit</i> [in, out]

<dd>
<p>A reference to WDFDEVICE_INIT.</p>
</dd>

### -param <i>pFdoAttributes</i> [in, out]

<dd>
<p>A reference to WDF_OBJECT_ATTRIBUTES.</p>
</dd>

### -param <i>Flags</i> [in]

<dd>
<p>The flags for the sensor driver. Reserved set to 0.</p>
</dd>
</dl>

## -returns
<p>This function returns STATUS_SUCCESS when completed successfully. When an invalid parameter is supplied or this function fails, STATUS_INVALID_PARAMETER is returned. This function can also return other NTSTATUS values.

</p>

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