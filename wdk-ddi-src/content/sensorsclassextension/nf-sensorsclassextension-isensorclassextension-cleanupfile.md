---
UID: NF.sensorsclassextension.ISensorClassExtension.CleanupFile
title: ISensorClassExtension::CleanupFile
author: windows-driver-content
description: The ISensorClassExtension::CleanupFile method notifies the class extension about a file handle that closes and cancels all pending I/O requests, for the specified application.
old-location: sensors\isensorclassextension_cleanupfile.htm
old-project: sensors
ms.assetid: eeade123-fb83-478f-99e3-e79bbbb1919b
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: ISensorClassExtension, CleanupFile, ISensorClassExtension::CleanupFile
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
req.alt-api: CleanupFile
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

# ISensorClassExtension::CleanupFile method



## -description
<p>The <a href="sensors.isensorclassextension_cleanupfile">ISensorClassExtension::CleanupFile</a> method notifies the class extension about a file handle that closes and cancels all pending I/O requests, for the specified application.</p>


## -syntax

````
HRESULT CleanupFile(
   IWDFFile * pWdfFile
);
````


## -parameters
<dl>

### -param <i>pWdfFile</i> 

<dd>
<p>Pointer to an IWDFFile interface that represents the file object for the application being closed.</p>
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
<p>Your driver must call this method to forward <a href="umdf.ifilecallbackcleanup_oncleanupfile">IFileCallbackCleanup::OnCleanupFile</a> method calls from UMDF. You receive this call any time that a file handle closes. Typically, you receive this call after an application stops responding.</p>

<p>When finished, the sensor class extension calls the driver in <a href="sensors.isensordriver_onclientdisconnect">ISensorDriver::OnClientDisconnect</a>, and <a href="sensors.isensordriver_onclientunsubscribefromevents">ISensorDriver::OnClientUnsubscribeFromEvents</a>, if applicable.</p>

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