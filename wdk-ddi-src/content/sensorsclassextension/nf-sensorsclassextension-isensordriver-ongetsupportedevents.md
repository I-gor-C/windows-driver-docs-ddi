---
UID: NF.sensorsclassextension.ISensorDriver.OnGetSupportedEvents
title: ISensorDriver::OnGetSupportedEvents
author: windows-driver-content
description: The ISensorDriver::OnGetSupportedEvents method retrieves the list of events that the specified sensor can raise.
old-location: sensors\isensordriver_ongetsupportedevents.htm
old-project: sensors
ms.assetid: b323f803-56fb-44db-9b88-be25062c08ff
ms.author: windowsdriverdev
ms.date: 11/26/2017
ms.keywords: ISensorDriver, OnGetSupportedEvents, ISensorDriver::OnGetSupportedEvents
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
req.alt-api: OnGetSupportedEvents
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

# ISensorDriver::OnGetSupportedEvents method



## -description
<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/ff545623">ISensorDriver::OnGetSupportedEvents</a> method retrieves the list of events that the specified sensor can raise.</p>


## -syntax

````
HRESULT OnGetSupportedEvents(
   LPWSTR  pwszSensorID,
   GUID ** ppSupportedEvents,
   ULONG * pulEventCount
);
````


## -parameters
<dl>

### -param <i>pwszSensorID</i> 

<dd>
<p>LPWSTR that contains the ID for the sensor from which the client application is requesting the events list.</p>
</dd>

### -param <i>ppSupportedEvents</i> 

<dd>
<p>Address of a GUID pointer that receives the array of supported event IDs. If the driver does not support events, return a buffer containing a single GUID that has its value set to GUID_NULL.</p>
</dd>

### -param <i>pulEventCount</i> 

<dd>
<p>Address of a ULONG that receives the count of event IDs in the buffer returned through ppSupportedEvents. If the driver does not support events, set this value to zero.</p>
</dd>
</dl>

## -returns
<p>If the operation succeeds, this method returns S_OK. Otherwise, this method returns one of the error codes that are defined in Winerror.h.</p>

## -remarks
<p>Event IDs are represented by <b>GUID</b>s. Platform-defined events are defined in sensors.h. </p>

<p>You must use CoTaskMemAlloc to create the event ID buffer. The sensor class extension frees this memory.</p>

<p>Event IDs are represented by <b>GUID</b>s. Platform-defined events are defined in sensors.h. </p>

<p>You must use CoTaskMemAlloc to create the event ID buffer. The sensor class extension frees this memory.</p>

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