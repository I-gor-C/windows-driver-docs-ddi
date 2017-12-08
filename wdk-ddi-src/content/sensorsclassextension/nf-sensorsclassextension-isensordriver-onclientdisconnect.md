---
UID: NF.sensorsclassextension.ISensorDriver.OnClientDisconnect
title: ISensorDriver::OnClientDisconnect
author: windows-driver-content
description: The ISensorDriver::OnClientDisconnect method notifies the sensor driver that a client application has disconnected.
old-location: sensors\isensordriver_onclientdisconnect.htm
old-project: sensors
ms.assetid: 9484610b-4cbd-4c4e-9e60-ef052702325c
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: ISensorDriver, OnClientDisconnect, ISensorDriver::OnClientDisconnect
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
req.alt-api: ISensorDriver.OnClientDisconnect
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

# ISensorDriver::OnClientDisconnect method



## -description
<p>The <b>ISensorDriver::OnClientDisconnect</b> method notifies the sensor driver that a client application has disconnected.</p>


## -syntax

````
HRESULT OnClientDisconnect(
  [in] IWDFFile           *pClientFile,
  [in] __in_string LPWSTR pwszSensorID
);
````


## -parameters
<dl>

### -param pClientFile [in]

<dd>
<p>Pointer to an <a href="..\wudfddi\nn-wudfddi-iwdffile.md">IWDFFile</a> interface that represents the file object for the client that disconnected.</p>
</dd>

### -param pwszSensorID [in]

<dd>
<p><b>LPWSTR</b> that contains the ID for the sensor from which the client application is disconnecting.</p>
</dd>
</dl>

## -returns
<p>If the operation succeeds, this method returns S_OK. Otherwise, this method returns one of the error codes that are defined in Winerror.h.</p>

## -remarks
<p>The sensor class extension calls this method in the following instances:</p>

<p>An application closes normally.</p>

<p>The user revokes permission for an application to access the device that contains the specified sensor.</p>

<p>The cleanup work from a call to <a href="sensors.isensorclassextension_cleanupfile">ISensorClassExtension::CleanupFile</a> has completed.</p>

<p>You can use this call as a signal to update lists and reference counts of connected applications. </p>

<p>For more information about how to use this method, see <a href="https://msdn.microsoft.com/1895EC5C-08C1-4976-83F2-CD5A2B55338D">Filtering data</a>.</p>

<p>The following example code demonstrates an implementation of <b>ISensorDriver::OnClientDisconnect</b>. This function uses an ATL simple map, named Clients, to keep track of connected clients. See <a href="sensors.isensordriver_onclientconnect">ISensorDriver::OnClientConnect</a> for an example of how connected clients are added to the map.</p>

<p>The ClientData structure is defined as follows.</p>

<p>The function definition follows.</p>

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
<a href="sensors.isensordriver_onclientconnect">ISensorDriver::OnClientConnect</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [sensors\sensors]:%20ISensorDriver::OnClientDisconnect method%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
