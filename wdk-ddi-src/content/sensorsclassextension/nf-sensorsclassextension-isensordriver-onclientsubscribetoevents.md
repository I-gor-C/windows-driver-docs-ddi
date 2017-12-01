---
UID: NF.sensorsclassextension.ISensorDriver.OnClientSubscribeToEvents
title: ISensorDriver::OnClientSubscribeToEvents
author: windows-driver-content
description: The ISensorDriver::OnClientSubscribeToEvents method notifies the sensor driver that an authorized client application is requesting event notifications.
old-location: sensors\isensordriver_onclientsubscribetoevents.htm
old-project: sensors
ms.assetid: b0528932-d7a8-46d7-bd94-6fd729a9d7f2
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: ISensorDriver, OnClientSubscribeToEvents, ISensorDriver::OnClientSubscribeToEvents
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
req.alt-api: OnClientSubscribeToEvents
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

# ISensorDriver::OnClientSubscribeToEvents method



## -description
<p>The <a href="sensors.isensordriver_onclientsubscribetoevents">ISensorDriver::OnClientSubscribeToEvents</a> method notifies the sensor driver that an authorized client application is requesting event notifications.</p>


## -syntax

````
HRESULT OnClientSubscribeToEvents(
   IWDFFile * pClientFile,
   LPWSTR     pwszSensorID
);
````


## -parameters
<dl>

### -param <i>pClientFile</i> 

<dd>
<p>Pointer to an IWDFFile interface that represents the file object for the application requesting event notifications.</p>
</dd>

### -param <i>pwszSensorID</i> 

<dd>
<p>LPWSTR that contains the ID for the sensor from which the client application is requesting event notifications.</p>
</dd>
</dl>

## -returns
<p>If the operation succeeds, this method returns S_OK. Otherwise, this method returns one of the error codes that are defined in Winerror.h.</p>

## -remarks
<p>When a client application requests event notifications, the driver raises all events to the sensor class extension for the specified object ID. The class extension then forwards these events to the Sensor API as event notifications for applications. </p>

<p>You can maintain a reference count of connected applications for each sensor to avoid making event callbacks when not required. </p>

<p>Platform-defined events are defined in sensors.h.</p>

<p>For more information about how to use this method, see <a href="NULL">Filtering data</a>.</p>

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