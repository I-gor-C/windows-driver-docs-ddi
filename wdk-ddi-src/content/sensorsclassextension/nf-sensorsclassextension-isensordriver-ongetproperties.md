---
UID: NF.sensorsclassextension.ISensorDriver.OnGetProperties
title: ISensorDriver::OnGetProperties
author: windows-driver-content
description: The ISensorDriver::OnGetProperties method retrieves values for the specified properties from the specified sensor.
old-location: sensors\isensordriver_ongetproperties.htm
old-project: sensors
ms.assetid: 8c7f378c-b4e6-4074-8b6a-571068b5ab80
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: ISensorDriver, OnGetProperties, ISensorDriver::OnGetProperties
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
req.alt-api: OnGetProperties
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

# ISensorDriver::OnGetProperties method



## -description
<p>The <a href="sensors.isensordriver_ongetproperties">ISensorDriver::OnGetProperties</a> method retrieves values for the specified properties from the specified sensor.</p>


## -syntax

````
HRESULT OnGetProperties(
   IWDFFile *                     pClientFile,
   LPWSTR                         pwszSensorID,
   IPortableDeviceKeyCollection * pProperties,
   IPortableDeviceValues **       ppPropertyValues
);
````


## -parameters
<dl>

### -param <i>pClientFile</i> 

<dd>
<p> Pointer to an IWDFFile interface that represents the file object for the application requesting property values.</p>
</dd>

### -param <i>pwszSensorID</i> 

<dd>
<p>LPWSTR that contains the ID for the sensor from which the client application is requesting property values.</p>
</dd>

### -param <i>pProperties</i> 

<dd>
<p> Pointer to an IPortableDeviceKeyCollection that contains the list of PROPERTYKEY values that represent the properties being requested. </p>
</dd>

### -param <i>ppPropertyValues</i> 

<dd>
<p>Address of an IPortableDeviceValues pointer that receives the requested property values.</p>
</dd>
</dl>

## -returns
<p>If the operation succeeds, this method returns S_OK. Otherwise, this method returns one of the error codes that are defined in Winerror.h.</p>

## -remarks
<p>Properties describe the sensor device, as opposed to data fields, which contain sensor-generated data. Platform-defined properties are defined in sensors.h.</p>

<p>Applications can access some sensor property information before the user grants permission for the sensor. These items are limited to the following IDs defined in sensors.h:</p>

<p>Any <b>PROPERTYKEY</b> that starts with "SENSOR_PROPERTY_".</p>

<p>Any category <b>GUID</b> that starts with "SENSOR_CATEGORY_".</p>

<p>Each <a href="http://go.microsoft.com/fwlink/p/?linkid=131486">IPortableDeviceValues</a> object returned in this collection must contain values for the required properties, as described in the <a href="https://msdn.microsoft.com/library/windows/hardware/dn946698">Sensor Properties</a> reference section.</p>

<p>The sensor class extension is responsible for freeing any <b>PROPVARIANT</b> structures returned by this method.</p>

<p>Sensor properties must not contain information that can be used to identify the user. For more information about user privacy, see <a href="NULL">Privacy and Security in the Sensor and Location Platform</a>.</p>

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