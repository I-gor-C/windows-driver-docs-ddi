---
UID: NF.sensorsclassextension.ISensorClassExtension.PostEvent
title: ISensorClassExtension::PostEvent
author: windows-driver-content
description: The ISensorClassExtension::PostEvent method raises one or more driver events in the sensor class extension.
old-location: sensors\isensorclassextension_postevent.htm
old-project: sensors
ms.assetid: 201a4558-8755-4a28-9982-c02ce5b5d8e7
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: ISensorClassExtension, PostEvent, ISensorClassExtension::PostEvent
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
req.alt-api: PostEvent
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
req.iface: ISensorClassExtension
req.product: Windows 10 or later.
---

# ISensorClassExtension::PostEvent method



## -description
<p>The <a href="sensors.isensorclassextension_postevent">ISensorClassExtension::PostEvent</a> method raises one or more driver events in the sensor class extension.</p>


## -syntax

````
HRESULT PostEvent(
   LPWSTR                            pwszSensorID,
   IPortableDeviceValuesCollection * pEventCollection
);
````


## -parameters
<dl>

### -param <i>pwszSensorID</i> 

<dd>
<p>LPWSTR that contains the ID for the sensor for which the driver is raising the event.</p>
</dd>

### -param <i>pEventCollection</i> 

<dd>
<p>Pointer to an IPortableDeviceValuesCollection interface that contains the list of events being posted and their associated data.</p>
</dd>
</dl>

## -returns
<p>This method returns an HRESULT. Possible values include, but are not limited to, one of the following values.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method succeeded.</p><dl>
<dt><b>S_FALSE</b></dt>
</dl><p>The method succeeded, but no client programs are currently subscribed to events. Do not post events when no clients are subscribed.</p><dl>
<dt><b>E_INVALIDARG</b></dt>
</dl><p>The event collection was empty.</p><dl>
<dt><b>E_POINTER</b></dt>
</dl><p>A required pointer argument was <b>NULL</b>.</p><dl>
<dt><b>HRESULT_FROM_WIN32(ERROR_CAN_NOT_COMPLETE)</b></dt>
</dl><p>The class extension is not initialized.</p><dl>
<dt><b>HRESULT_FROM_WIN32(ERROR_INTERNAL_DB_CORRUPTION</b></dt>
</dl><p>A serialization error occurred.</p><dl>
<dt><b>HRESULT_FROM_WIN32(ERROR_OBJECT_NOT_FOUND)</b></dt>
</dl><p>No client programs are currently subscribed to events. Do not post events when no clients are subscribed.</p>

<p> </p>

## -remarks
<p>The sensor class extension forwards these events to the Sensor API and Location API, which in turn, raise events in client programs.</p>

<p>The collection passed through <i>pEventCollection</i> can contain one or more events. Represent each event and its associated data by using one <a href="http://go.microsoft.com/fwlink/p/?linkid=131486">IPortableDeviceValues</a> object. Platform-defined <b>PROPERTYKEY</b>s for events and data types are defined in sensors.h.</p>

<p>Each <a href="http://go.microsoft.com/fwlink/p/?linkid=131486">IPortableDeviceValues</a> object returned by this method must contain a time stamp, as described in <a href="https://msdn.microsoft.com/library/windows/hardware/ff545725">SENSOR_CATEGORY_ALL</a>.</p>

<p>The sensor class extension is responsible for freeing any <b>PROPVARIANT</b> structures provided by this method.</p>

<p>To specify the event type, use the SENSOR_EVENT_PARAMETER_EVENT_ID <b>PROPERTYKEY</b> with the appropriate <b>GUID</b> value. </p>

<p>For an example of a class that creates an event thread, see <a href="NULL">Raising sensor events</a>
</p>

<p><a href="http://go.microsoft.com/fwlink/p/?linkid=131486">IPortableDeviceValues</a> and <a href="http://go.microsoft.com/fwlink/p/?linkid=131487">IPortableDeviceValuesCollection</a> are documented in Windows Portable Devices.</p>

<p>Raise state change events by calling <a href="sensors.isensorclassextension_poststatechange">ISensorClassExtension::PostStateChange</a>.</p>

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