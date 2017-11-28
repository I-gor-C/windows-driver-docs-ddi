---
UID: NF.sensorsclassextension.ISensorClassExtension.ProcessIoControl
title: ISensorClassExtension::ProcessIoControl
author: windows-driver-content
description: The ISensorClassExtension::ProcessControl method sends Windows Portable Devices (WPD) I/O control requests to the sensor class extension for processing.
old-location: sensors\isensorclassextension_processiocontrol.htm
old-project: sensors
ms.assetid: bd886086-4e23-47c0-ae58-9234399e5a79
ms.author: windowsdriverdev
ms.date: 11/26/2017
ms.keywords: ISensorClassExtension, ProcessIoControl, ISensorClassExtension::ProcessIoControl
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
req.alt-api: ProcessIoControl
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

# ISensorClassExtension::ProcessIoControl method



## -description
<p>The <a href="sensors.isensorclassextension_processiocontrol">ISensorClassExtension::ProcessControl</a> method sends Windows Portable Devices (WPD) I/O control requests to the sensor class extension for processing.</p>


## -syntax

````
HRESULT ProcessIoControl(
   IWDFIoRequest * pRequest
);
````


## -parameters
<dl>

### -param <i>pRequest</i> 

<dd>
<p>Pointer to the IWDFIoRequest interface that represents the UMDF request object.</p>
</dd>
</dl>

## -returns
<p>This method returns an HRESULT. Possible values include, but are not limited to, one of the following values.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method succeeded.</p><dl>
<dt><b>E_ACCESS_DENIED</b></dt>
</dl><p>No permission. For example, the I/O request sought data for which no permission exists.</p><dl>
<dt><b>E_POINTER</b></dt>
</dl><p>A required pointer argument was <b>NULL</b>.</p><dl>
<dt><b>HRESULT_FROM_WIN32(ERROR_NOT_SUPPORTED)</b></dt>
</dl><p>The request did not contain a WPD IOCTL.</p>

<p> </p>

## -remarks
<p>UMDF sends I/O control requests to sensor drivers through <a href="https://msdn.microsoft.com/library/windows/hardware/ff556854">IQueueCallbackDeviceIoControl::OnDeviceIoControl</a>. We recommend that you call ProcessIoControl to forward all WPD requests to the sensor class extension for processing. You can use the WPD macro IS_WPD_IOCTL to determine whether a given control code is specific to WPD. Clients of the Sensor API and Location API send only WPD IOCTLs, which can always be process by the sensor class extension.</p>

<p>After processing an I/O control request, the sensor class extension uses the driver's callback interface, <a href="https://msdn.microsoft.com/library/windows/hardware/ff545566">ISensorDriver</a>, to provide notifications, as appropriate. WPD requests that the sensor class extension does not handle by default are sent to the driver through <a href="https://msdn.microsoft.com/library/windows/hardware/ff545644">ISensorDriver::OnProcessWpdMessage</a>.</p>

<p>The driver must not complete I/O control requests that it forwards to the sensor class extension.</p>

<p>UMDF sends I/O control requests to sensor drivers through <a href="https://msdn.microsoft.com/library/windows/hardware/ff556854">IQueueCallbackDeviceIoControl::OnDeviceIoControl</a>. We recommend that you call ProcessIoControl to forward all WPD requests to the sensor class extension for processing. You can use the WPD macro IS_WPD_IOCTL to determine whether a given control code is specific to WPD. Clients of the Sensor API and Location API send only WPD IOCTLs, which can always be process by the sensor class extension.</p>

<p>After processing an I/O control request, the sensor class extension uses the driver's callback interface, <a href="https://msdn.microsoft.com/library/windows/hardware/ff545566">ISensorDriver</a>, to provide notifications, as appropriate. WPD requests that the sensor class extension does not handle by default are sent to the driver through <a href="https://msdn.microsoft.com/library/windows/hardware/ff545644">ISensorDriver::OnProcessWpdMessage</a>.</p>

<p>The driver must not complete I/O control requests that it forwards to the sensor class extension.</p>

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