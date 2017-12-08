---
UID: NF.sensorsclassextension.ISensorDriver.OnGetSupportedProperties
title: ISensorDriver::OnGetSupportedProperties
author: windows-driver-content
description: The ISensorDriver::OnGetSupportedProperties method retrieves the list of properties that the specified sensor provides.
old-location: sensors\isensordriver_ongetsupportedproperties.htm
old-project: sensors
ms.assetid: 8712fe85-0af1-4552-9351-aca4fe5430d1
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: ISensorDriver, OnGetSupportedProperties, ISensorDriver::OnGetSupportedProperties
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
req.alt-api: OnGetSupportedProperties
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

# ISensorDriver::OnGetSupportedProperties method



## -description
<p>The <a href="sensors.isensordriver_ongetsupportedproperties">ISensorDriver::OnGetSupportedProperties</a> method retrieves the list of properties that the specified sensor provides.</p>


## -syntax

````
HRESULT OnGetSupportedProperties(
   LPWSTR                          pwszSensorID,
   IPortableDeviceKeyCollection ** ppSupportedProperties
);
````


## -parameters
<dl>

### -param pwszSensorID 

<dd>
<p>LPWSTR that contains the ID for the sensor from which the client application is requesting the properties list.</p>
</dd>

### -param ppSupportedProperties 

<dd>
<p> Address of an IPortableDeviceKeyCollection pointer that receives the list of PROPERTYKEY values that represent the supported properties.</p>
</dd>
</dl>

## -returns
<p>If the operation succeeds, this method returns S_OK. Otherwise, this method returns one of the error codes that are defined in Winerror.h.</p>

## -remarks
<p>Properties describe the sensor device, as opposed to data fields, which contain sensor-generated data. Platform-defined properties are defined in sensors.h.</p>

<p>Each <a href="http://go.microsoft.com/fwlink/p/?linkid=131484">IPortableDeviceKeyCollection</a> object returned in this collection must contain <b>PROPERTYKEY</b>s for the  required properties, as described in the <a href="https://msdn.microsoft.com/library/windows/hardware/dn946698">Sensor Properties</a> reference section.</p>

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