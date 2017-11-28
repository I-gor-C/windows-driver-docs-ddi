---
UID: NF.sensorsclassextension.ISensorDriver.OnGetSupportedDataFields
title: ISensorDriver::OnGetSupportedDataFields
author: windows-driver-content
description: The ISensorDriver::OnGetSupportedDataFields method retrieves the list of data fields that the specified sensor can provide.
old-location: sensors\isensordriver_ongetsupporteddatafields.htm
old-project: sensors
ms.assetid: 5020212e-9e3f-468f-8f7c-77d70a8f024b
ms.author: windowsdriverdev
ms.date: 11/26/2017
ms.keywords: ISensorDriver, OnGetSupportedDataFields, ISensorDriver::OnGetSupportedDataFields
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: sensorsclassextension.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: OnGetSupportedDataFields
req.alt-loc: SensorsClassExtension.lib,SensorsClassExtension.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: SensorsClassExtension.lib
req.dll: 
req.irql: <= PASSIVE_LEVEL
req.iface: ISensorDriver
req.product: Windows 10 or later.
---

# ISensorDriver::OnGetSupportedDataFields method



## -description
<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/ff545620">ISensorDriver::OnGetSupportedDataFields</a> method retrieves the list of data fields that the specified sensor can provide.</p>


## -syntax

````
HRESULT OnGetSupportedDataFields(
   LPWSTR                          pwszSensorID,
   IPortableDeviceKeyCollection ** ppSupportedDataFields
);
````


## -parameters
<dl>

### -param <i>pwszSensorID</i> 

<dd>
<p>LPWSTR that contains the ID for the sensor from which the client application is requesting the data fields list.</p>
</dd>

### -param <i>ppSupportedDataFields</i> 

<dd>
<p>Address of an IPortableDeviceKeyCollection pointer that receives the list of PROPERTYKEY values that represent the supported data fields.</p>
</dd>
</dl>

## -returns
<p>If the operation succeeds, this method returns S_OK. Otherwise, this method returns one of the error codes that are defined in Winerror.h.</p>

## -remarks
<p>Data fields contain sensor-generated data, as opposed to properties, which describe the sensor device. Platform-defined data fields are defined in sensors.h.</p>

<p>All drivers must support SENSOR_DATA_TYPE_TIMESTAMP as a required data field.</p>

<p><a href="http://go.microsoft.com/fwlink/p/?linkid=131484">IPortableDeviceKeyCollection</a> is documented in Windows Portable Devices.</p>

<p>Data fields contain sensor-generated data, as opposed to properties, which describe the sensor device. Platform-defined data fields are defined in sensors.h.</p>

<p>All drivers must support SENSOR_DATA_TYPE_TIMESTAMP as a required data field.</p>

<p><a href="http://go.microsoft.com/fwlink/p/?linkid=131484">IPortableDeviceKeyCollection</a> is documented in Windows Portable Devices.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Sensorsclassextension.h</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>SensorsClassExtension.lib</dt>
</dl>
</td>
</tr>
</table>