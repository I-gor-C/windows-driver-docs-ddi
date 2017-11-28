---
UID: NC.ufxclient.EVT_UFX_DEVICE_PORT_DETECT
title: EVT_UFX_DEVICE_PORT_DETECT
author: windows-driver-content
description: The client driver's implementation to initiate port detection.
old-location: buses\evt_ufx_device_port_detect.htm
old-project: usbref
ms.assetid: EC32BFE8-6E93-4CEF-8EA8-856B0E431FCF
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: UFX_HARDWARE_FAILURE_CONTEXT, UFX_HARDWARE_FAILURE_CONTEXT, *PUFX_HARDWARE_FAILURE_CONTEXT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: ufxclient.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
req.alt-api: PFN_UFX_DEVICE_PORT_DETECT
req.alt-loc: Ufxclient.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# EVT_UFX_DEVICE_PORT_DETECT callback



## -description
<p>The client driver's implementation to initiate port detection</p>


## -prototype

````
EVT_UFX_DEVICE_PORT_DETECT EvtUfxDevicePortDetect;

void EvtUfxDevicePortDetect(
  _In_ UFXDEVICE UfxDevice
)
{ ... }

typedef EVT_UFX_DEVICE_PORT_DETECT PFN_UFX_DEVICE_PORT_DETECT;
````


## -parameters
<dl>

### -param <i>UfxDevice</i> [in]

<dd>
<p>The handle to a  USB device object that the client driver received in a previous call to  the <a href="https://msdn.microsoft.com/library/windows/hardware/mt187951">UfxDeviceCreate</a>.</p>
</dd>
</dl>

## -returns
<p>This callback function does not return a value.</p>

## -remarks
<p>The client driver for the function host controller registers its <i>EVT_UFX_DEVICE_PORT_DETECT</i> implementation with the USB function class extension (UFX) by calling the <a href="https://msdn.microsoft.com/library/windows/hardware/mt187951">UfxDeviceCreate</a> method.</p>

<p>The client driver must indicate completion of port detection by calling the <a href="https://msdn.microsoft.com/library/windows/hardware/mt187962">UfxDevicePortDetectComplete</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/mt187963">UfxDevicePortDetectCompleteEx</a> methods.</p>

<p>The client driver for the function host controller registers its <i>EVT_UFX_DEVICE_PORT_DETECT</i> implementation with the USB function class extension (UFX) by calling the <a href="https://msdn.microsoft.com/library/windows/hardware/mt187951">UfxDeviceCreate</a> method.</p>

<p>The client driver must indicate completion of port detection by calling the <a href="https://msdn.microsoft.com/library/windows/hardware/mt187962">UfxDevicePortDetectComplete</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/mt187963">UfxDevicePortDetectCompleteEx</a> methods.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum KMDF version</p>
</th>
<td width="70%">
<p>1.0</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum UMDF version</p>
</th>
<td width="70%">
<p>2.0</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ufxclient.h</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>PASSIVE_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/mt187951">UfxDeviceCreate</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/mt187952">UfxDeviceEventComplete</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [usbref\buses]:%20EVT_UFX_DEVICE_PORT_DETECT callback function%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
