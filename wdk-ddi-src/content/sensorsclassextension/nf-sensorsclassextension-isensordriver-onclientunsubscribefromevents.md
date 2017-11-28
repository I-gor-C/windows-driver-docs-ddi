---
UID: NF.sensorsclassextension.ISensorDriver.OnClientUnsubscribeFromEvents
title: ISensorDriver::OnClientUnsubscribeFromEvents
author: windows-driver-content
description: The ISensorDriver::OnClientUnsubscribeFromEvents method notifies the sensor driver that a client application no longer requests event notifications.
old-location: sensors\isensordriver_onclientunsubscribefromevents.htm
old-project: sensors
ms.assetid: f51f1091-232f-4e41-9cc2-9938870aeef8
ms.author: windowsdriverdev
ms.date: 11/26/2017
ms.keywords: ISensorDriver, OnClientUnsubscribeFromEvents, ISensorDriver::OnClientUnsubscribeFromEvents
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
req.alt-api: OnClientUnsubscribeFromEvents
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

# ISensorDriver::OnClientUnsubscribeFromEvents method



## -description
<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/ff545598">ISensorDriver::OnClientUnsubscribeFromEvents</a> method notifies the sensor driver that a client application no longer requests event notifications.</p>


## -syntax

````
HRESULT OnClientUnsubscribeFromEvents(
   IWDFFile * pClientFile,
   LPWSTR     pwszSensorID
);
````


## -parameters
<dl>

### -param <i>pClientFile</i> 

<dd>
<p> Pointer to an IWDFFile interface that represents the file object for the application requesting cancellation of event notifications.</p>
</dd>

### -param <i>pwszSensorID</i> 

<dd>
<p>LPWSTR that contains the ID for the sensor from which the client application is requesting cancellation of event notifications.</p>
</dd>
</dl>

## -returns
<p>If the operation succeeds, this method returns S_OK. Otherwise, this method returns one of the error codes that are defined in Winerror.h.</p>

## -remarks
<p>The sensor class extension calls this method in the following instances:</p>

<p>An application unsubscribes from events.</p>

<p>An application closes normally.</p>

<p>The user revokes permission for an application to access the device that contains the specified sensor.</p>

<p>The sensor class extension is shutting down.</p>

<p>The cleanup work from a call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff545512">ISensorClassExtension::CleanupFile</a> has completed.</p>

<p>You can use this call as a signal to update the reference count of applications requesting events for the specified sensor.</p>

<p>For more information about how to use this method, see <a href="NULL">Filtering data</a>.</p>

<p>The ClientData structure is defined as follows.</p>

<p>The sensor class extension calls this method in the following instances:</p>

<p>An application unsubscribes from events.</p>

<p>An application closes normally.</p>

<p>The user revokes permission for an application to access the device that contains the specified sensor.</p>

<p>The sensor class extension is shutting down.</p>

<p>The cleanup work from a call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff545512">ISensorClassExtension::CleanupFile</a> has completed.</p>

<p>You can use this call as a signal to update the reference count of applications requesting events for the specified sensor.</p>

<p>For more information about how to use this method, see <a href="NULL">Filtering data</a>.</p>

<p>The ClientData structure is defined as follows.</p>

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