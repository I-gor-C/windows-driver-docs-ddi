---
UID: NF.sensorsclassextension.ISensorClassExtension.PostStateChange
title: ISensorClassExtension::PostStateChange
author: windows-driver-content
description: The ISensorClassExtension::PostStateChange method notifies the sensor class extension about a change in the operational state of the sensor.
old-location: sensors\isensorclassextension_poststatechange.htm
old-project: sensors
ms.assetid: ae3bc846-df63-4186-9554-f4600e1f2066
ms.author: windowsdriverdev
ms.date: 11/26/2017
ms.keywords: ISensorClassExtension, PostStateChange, ISensorClassExtension::PostStateChange
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: sensorsclassextension.h
req.include-header: 
req.target-type: Desktop
req.target-min-winverclnt: Windows 7,Available in Windows 7.
req.target-min-winversvr: None supported
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ISensorClassExtension.PostStateChange
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

# ISensorClassExtension::PostStateChange method



## -description
<p>The <b>ISensorClassExtension::PostStateChange</b> method notifies the sensor class extension about a change in the operational state of the sensor.</p>


## -syntax

````
HRESULT PostStateChange(
  [in] LPWSTR      pwszSensorID,
  [in] SensorState State
);
````


## -parameters
<dl>

### -param <i>pwszSensorID</i> [in]

<dd>
<p><b>LPWSTR</b> that contains the ID for the sensor for which the driver is raising the event.</p>
</dd>

### -param <i>State</i> [in]

<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545708">SensorState</a> value that indicates the new state.</p>
</dd>
</dl>

## -returns
<p>This method returns an HRESULT. Possible values include, but are not limited to, one of the following values.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method succeeded.</p><dl>
<dt><b>E_POINTER</b></dt>
</dl><p>A required pointer argument was <b>NULL</b>.</p><dl>
<dt><b>HRESULT_FROM_WIN32(ERROR_CAN_NOT_COMPLETE)</b></dt>
</dl><p>The class extension is not initialized.</p>

<p> </p>

## -remarks
<p>Sensor state information is also available through the <a href="https://msdn.microsoft.com/a9f88dad-a81d-45dc-b607-e7b4c5036774">SENSOR_PROPERTY_STATE</a> property key.</p>

<p>The following example code demonstrates a function that posts a state-changed event.</p>

<p>Sensor state information is also available through the <a href="https://msdn.microsoft.com/a9f88dad-a81d-45dc-b607-e7b4c5036774">SENSOR_PROPERTY_STATE</a> property key.</p>

<p>The following example code demonstrates a function that posts a state-changed event.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 7</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>None supported</p>
</td>
</tr>
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
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows 7.</p>
</td>
</tr>
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

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545589">ISensorDriver::OnClientSubscribeToEvents</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545598">ISensorDriver::OnClientUnsubscribeFromEvents</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [sensors\sensors]:%20ISensorClassExtension::PostStateChange method%20 RELEASE:%20(11/26/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
