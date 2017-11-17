---
UID: NS.sensorscx._SENSOR_CONTROLLER_CONFIG
title: SENSOR_CONTROLLER_CONFIG
author: windows-driver-content
description: This structure contains pointers to callback functions that must be implemented by the driver, and passed on to the class extension to call.
old-location: sensors\sensor_controller_config.htm
ms.assetid: EEAC4D16-D0B8-4147-AD2D-7EE60853EBDD
ms.author: windowsdriverdev
ms.date: 10/23/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: sensors
req.header: sensorscx.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 8.1
req.target-min-winversvr: Windows Server 2012 R2
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: SENSOR_CONTROLLER_CONFIG
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
ms.keywords: SENSOR_CONTROLLER_CONFIG, SENSOR_CONTROLLER_CONFIG, *PSENSOR_CONTROLLER_CONFIG
req.iface: 
req.product: Windows 10 or later.
---

# SENSOR_CONTROLLER_CONFIG structure



## -description
<p>This structure contains pointers to callback functions that must be implemented by the driver, and passed on to the class extension to call.</p>


## -syntax

````
typedef struct _SENSOR_CONTROLLER_CONFIG {
  ULONG                                       Size;
  WDF_TRI_STATE                               DriverIsPowerPolicyOwner;
  PFN_SENSOR_DRIVER_START_SENSOR              EvtSensorStart;
  PFN_SENSOR_DRIVER_STOP_SENSOR               EvtSensorStop;
  PFN_SENSOR_DRIVER_GET_SUPPORTED_DATA_FIELDS EvtSensorGetSupportedDataFields;
  PFN_SENSOR_DRIVER_GET_DATA_FIELD_PROPERTIES EvtSensorGetDataFieldProperties;
  PFN_SENSOR_DRIVER_GET_DATA_INTERVAL         EvtSensorGetDataInterval;
  PFN_SENSOR_DRIVER_SET_DATA_INTERVAL         EvtSensorSetDataInterval;
  PFN_SENSOR_DRIVER_GET_DATA_THRESHOLDS       EvtSensorGetDataThresholds;
  PFN_SENSOR_DRIVER_SET_DATA_THRESHOLDS       EvtSensorSetDataThresholds;
  PFN_SENSOR_DRIVER_GET_PROPERTIES            EvtSensorGetProperties;
  PFN_SENSOR_DRIVER_DEVICE_IO_CONTROL         EvtSensorDeviceIoControl;
} SENSOR_CONTROLLER_CONFIG, *PSENSOR_CONTROLLER_CONFIG;
````


## -struct-fields
<dl>

### -field <b>Size</b>

<dd>
<p>The allocated size of this structure (in bytes).</p>
</dd>

### -field <b>DriverIsPowerPolicyOwner</b>

<dd>
<p>Indicates whether or not driver owns the power policy. This value must be either WdfFalse, WdfUseDefault, or WdfTrue. For partners to take advantage of pep-based power management, they must set this flag to WdfFalse or WdfUseDefault and remove any _PSx method in their ACPI tables.</p>
</dd>

### -field <b>EvtSensorStart</b>

<dd>
<p>See <a href="https://msdn.microsoft.com/library/windows/hardware/dn957040">EvtSensorStart</a> for implementation guidelines.</p>
</dd>

### -field <b>EvtSensorStop</b>

<dd>
<p>See <a href="https://msdn.microsoft.com/library/windows/hardware/dn957041">EvtSensorStop</a> for implementation guidelines.</p>
</dd>

### -field <b>EvtSensorGetSupportedDataFields</b>

<dd>
<p>See <a href="https://msdn.microsoft.com/library/windows/hardware/dn957033">EvtSensorGetSupportedDataFields</a> for implementation guidelines.</p>
</dd>

### -field <b>EvtSensorGetDataFieldProperties</b>

<dd>
<p>See <a href="https://msdn.microsoft.com/library/windows/hardware/dn957029">EvtSensorGetDataFieldProperties</a> for implementation guidelines.</p>
</dd>

### -field <b>EvtSensorGetDataInterval</b>

<dd>
<p>See <a href="https://msdn.microsoft.com/library/windows/hardware/dn957030">EvtSensorGetDataInterval</a> for implementation guidelines.</p>
</dd>

### -field <b>EvtSensorSetDataInterval</b>

<dd>
<p>See <a href="https://msdn.microsoft.com/library/windows/hardware/dn957038">EvtSensorSetDataInterval</a> for implementation guidelines.</p>
</dd>

### -field <b>EvtSensorGetDataThresholds</b>

<dd>
<p>See <a href="https://msdn.microsoft.com/library/windows/hardware/dn957031">EvtSensorGetDataThresholds</a> for implementation guidelines.</p>
</dd>

### -field <b>EvtSensorSetDataThresholds</b>

<dd>
<p>See <a href="https://msdn.microsoft.com/library/windows/hardware/dn957039">EvtSensorSetDataThresholds</a> for implementation guidelines.</p>
</dd>

### -field <b>EvtSensorGetProperties</b>

<dd>
<p>See <a href="https://msdn.microsoft.com/library/windows/hardware/dn957032">EvtSensorGetProperties</a> for implementation guidelines.</p>
</dd>

### -field <b>EvtSensorDeviceIoControl</b>

<dd>
<p>See  <a href="https://msdn.microsoft.com/library/windows/hardware/dn957028">EvtSensorDeviceIoControl</a> for implementation guidelines.</p>
</dd>
</dl>

## -remarks
<p>This structure is given to the class extension using the <a href="https://msdn.microsoft.com/library/windows/hardware/dn957086">SensorsCxDeviceInitialize</a> function. If any of the following function pointers are not set, the driver will fail to load:</p>

<p>This structure is given to the class extension using the <a href="https://msdn.microsoft.com/library/windows/hardware/dn957086">SensorsCxDeviceInitialize</a> function. If any of the following function pointers are not set, the driver will fail to load:</p>

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
<dt>SensorsCx.h</dt>
</dl>
</td>
</tr>
</table>