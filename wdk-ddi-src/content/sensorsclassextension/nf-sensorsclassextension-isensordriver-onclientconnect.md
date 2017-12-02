---
UID: NF.sensorsclassextension.ISensorDriver.OnClientConnect
title: ISensorDriver::OnClientConnect
author: windows-driver-content
description: The ISensorDriver::OnClientConnect method notifies the sensor driver that a client application has connected.
old-location: sensors\isensordriver_onclientconnect.htm
old-project: sensors
ms.assetid: 0f64288b-5100-4529-af2f-3e867375da39
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: ISensorDriver, OnClientConnect, ISensorDriver::OnClientConnect
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
req.alt-api: OnClientConnect
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

# ISensorDriver::OnClientConnect method



## -description
<p>The <a href="sensors.isensordriver_onclientconnect">ISensorDriver::OnClientConnect</a> method notifies the sensor driver that a client application has connected.</p>


## -syntax

````
HRESULT OnClientConnect(
   IWDFFile * pClientFile,
   LPWSTR     pwszSensorID
);
````


## -parameters
<dl>

### -param pClientFile 

<dd>
<p>Pointer to an IWDFFile interface that represents the file object for the application requesting the connection.</p>
</dd>

### -param pwszSensorID 

<dd>
<p>LPWSTR that contains the ID for the sensor to which the client application is connecting.</p>
</dd>
</dl>

## -returns
<p>If the operation succeeds, this method returns S_OK. Otherwise, this method returns one of the error codes that are defined in Winerror.h.</p>

## -remarks
<p>The sensor class extension calls this method only if the specified client application has been given permission by the user to access the driver. If the user revokes this permission, the class extension immediately calls <a href="sensors.isensordriver_onclientdisconnect">ISensorDriver::OnClientDisconnect</a> for the same application/sensor pair.</p>

<p>The class extension always calls this method before calling <a href="sensors.isensordriver_onsetproperties">ISensorDriver::OnSetProperties</a> or <a href="sensors.isensordriver_ongetdatafields">ISensorDriver::OnGetDataFields</a> for a particular sensor. We recommend that you maintain a reference count of connected applications to help to anticipate when calls to these three methods are possible. If no client applications are connected, you may want to change the behavior of the driver, for example, by taking steps to reduce power consumption.</p>

<p>You can use the pointer value (the address pointed to) provided by <i>pClientFile</i> as a kind of ID to keep track of connected applications. However, you must track these IDs separately for each sensor, not for each device, because the class extension may provide the same pointer value to multiple sensors on the same device.</p>

<p>For more information about how to use this method, see <a href="https://msdn.microsoft.com/1895EC5C-08C1-4976-83F2-CD5A2B55338D">Filtering data</a>.</p>

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