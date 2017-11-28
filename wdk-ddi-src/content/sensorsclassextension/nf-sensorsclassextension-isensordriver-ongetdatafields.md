---
UID: NF.sensorsclassextension.ISensorDriver.OnGetDataFields
title: ISensorDriver::OnGetDataFields
author: windows-driver-content
description: The ISensorDriver::OnGetDataFields method retrieves current sensor data.
old-location: sensors\isensordriver_ongetdatafields.htm
old-project: sensors
ms.assetid: a9233a0f-ac80-46be-9abe-7b87d25736f9
ms.author: windowsdriverdev
ms.date: 11/26/2017
ms.keywords: ISensorDriver, OnGetDataFields, ISensorDriver::OnGetDataFields
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
req.alt-api: OnGetDataFields
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

# ISensorDriver::OnGetDataFields method



## -description
<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/ff545607">ISensorDriver::OnGetDataFields</a> method retrieves current sensor data.</p>


## -syntax

````
HRESULT OnGetDataFields(
   IWDFFile *                     pClientFile,
   LPWSTR                         pwszSensorID,
   IPortableDeviceKeyCollection * pDataFields,
   IPortableDeviceValues **       ppDataValues
);
````


## -parameters
<dl>

### -param <i>pClientFile</i> 

<dd>
<p> Pointer to an IWDFFile interface that represents the file object for the application requesting the data.</p>
</dd>

### -param <i>pwszSensorID</i> 

<dd>
<p>LPWSTR that contains the ID for the sensor from which the client application is requesting data.</p>
</dd>

### -param <i>pDataFields</i> 

<dd>
<p>Pointer to an IPortableDeviceKeyCollection that contains the list of PROPERTYKEY values that represent the data fields being requested. </p>
</dd>

### -param <i>ppDataValues</i> 

<dd>
<p>Address of an IPortableDeviceValues pointer that receives the requested data.</p>
</dd>
</dl>

## -returns
<p>This method returns an HRESULT. Possible values include, but are not limited to, one of the following values.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method succeeded.</p><dl>
<dt><b>HRESULT_FROM_WIN32(ERROR_NO_DATA)</b></dt>
</dl><p>The sensor has no data to report. Each of the data fields returned in the <i>ppDataValues</i> parameter is VT_EMPTY.</p>

<p> </p>

## -remarks
<p>Data fields contain sensor-generated data, as opposed to properties, which describe the sensor device. Platform-defined data fields are defined in sensors.h.</p>

<p>Each <a href="http://go.microsoft.com/fwlink/p/?linkid=131486">IPortableDeviceValues</a> object returned by this method must contain a time stamp, as described in <a href="https://msdn.microsoft.com/library/windows/hardware/ff545725">SENSOR_CATEGORY_ALL</a>. </p>

<p>The sensor class extension is responsibile for freeing any <b>PROPVARIANT</b> structures returned by this method.</p>

<p>The sensor class extension calls this method only for sensors for which the user has granted permission through Control Panel.</p>

<p><a href="http://go.microsoft.com/fwlink/p/?linkid=131484">IPortableDeviceKeyCollection</a> and <a href="http://go.microsoft.com/fwlink/p/?linkid=131486">IPortableDeviceValues</a> are documented in Windows Portable Devices.</p>

<p>Data fields contain sensor-generated data, as opposed to properties, which describe the sensor device. Platform-defined data fields are defined in sensors.h.</p>

<p>Each <a href="http://go.microsoft.com/fwlink/p/?linkid=131486">IPortableDeviceValues</a> object returned by this method must contain a time stamp, as described in <a href="https://msdn.microsoft.com/library/windows/hardware/ff545725">SENSOR_CATEGORY_ALL</a>. </p>

<p>The sensor class extension is responsibile for freeing any <b>PROPVARIANT</b> structures returned by this method.</p>

<p>The sensor class extension calls this method only for sensors for which the user has granted permission through Control Panel.</p>

<p><a href="http://go.microsoft.com/fwlink/p/?linkid=131484">IPortableDeviceKeyCollection</a> and <a href="http://go.microsoft.com/fwlink/p/?linkid=131486">IPortableDeviceValues</a> are documented in Windows Portable Devices.</p>

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