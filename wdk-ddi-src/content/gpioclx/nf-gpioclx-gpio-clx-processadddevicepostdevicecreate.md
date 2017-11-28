---
UID: NF.gpioclx.GPIO_CLX_ProcessAddDevicePostDeviceCreate
title: GPIO_CLX_ProcessAddDevicePostDeviceCreate
author: windows-driver-content
description: The GPIO_CLX_ProcessAddDevicePostDeviceCreate method passes a framework device object to the GPIO framework extension (GpioClx).
old-location: gpio\gpio_clx_processadddevicepostdevicecreate.htm
old-project: GPIO
ms.assetid: 4B88820F-32B9-4AA2-867A-316A3796BE86
ms.author: windowsdriverdev
ms.date: 11/3/2017
ms.keywords: GPIO_CLX_ProcessAddDevicePostDeviceCreate
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: gpioclx.h
req.include-header: 
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 8.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: GPIO_CLX_ProcessAddDevicePostDeviceCreate
req.alt-loc: Msgpioclxstub.lib,Msgpioclxstub.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Msgpioclxstub.lib
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
---

# GPIO_CLX_ProcessAddDevicePostDeviceCreate function



## -description
<p>The <b>GPIO_CLX_ProcessAddDevicePostDeviceCreate</b> method passes a framework device object to the GPIO framework extension (GpioClx).</p>


## -syntax

````
NTSTATUS GPIO_CLX_ProcessAddDevicePostDeviceCreate(
  _In_ WDFDRIVER Driver,
  _In_ WDFDEVICE Device
);
````


## -parameters
<dl>

### -param <i>Driver</i> [in]

<dd>
<p>A WDFDRIVER handle to the framework driver object for the GPIO controller driver.</p>
</dd>

### -param <i>Device</i> [in]

<dd>
<p>A WDFDEVICE handle to the framework device object that represents the GPIO controller. The caller obtained this handle from the <a href="https://msdn.microsoft.com/library/windows/hardware/ff545926">WdfDeviceCreate</a> call that created the device object.</p>
</dd>
</dl>

## -returns
<p><b>GPIO_CLX_ProcessAddDevicePostDeviceCreate</b> returns STATUS_SUCCESS if the call is successful. Possible return values include the following error codes.</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>The caller is not a registered client of GpioClx.</p><dl>
<dt><b>STATUS_UNSUCCESSFUL</b></dt>
</dl><p>The framework failed to find the device name of the GPIO controller.</p><dl>
<dt><b>STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl><p>Out of memory.</p>

<p> </p>

## -remarks
<p>Your GPIO controller driver must call this method in its <a href="..\wdfdriver\nc-wdfdriver-evt-wdf-driver-device-add.md">EvtDriverDeviceAdd</a> callback function, after the call to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff545926">WdfDeviceCreate</a> method that creates the device object (FDO) that represents the GPIO controller. Otherwise, GpioClx cannot handle I/O requests or process interrupts for the new device object.</p>

<p>For a code example that contains a call to <b>GPIO_CLX_ProcessAddDevicePostDeviceCreate</b>, see <a href="https://msdn.microsoft.com/library/windows/hardware/hh439487">GPIO_CLX_ProcessAddDevicePreDeviceCreate</a>.</p>

<p>Your GPIO controller driver must call this method in its <a href="..\wdfdriver\nc-wdfdriver-evt-wdf-driver-device-add.md">EvtDriverDeviceAdd</a> callback function, after the call to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff545926">WdfDeviceCreate</a> method that creates the device object (FDO) that represents the GPIO controller. Otherwise, GpioClx cannot handle I/O requests or process interrupts for the new device object.</p>

<p>For a code example that contains a call to <b>GPIO_CLX_ProcessAddDevicePostDeviceCreate</b>, see <a href="https://msdn.microsoft.com/library/windows/hardware/hh439487">GPIO_CLX_ProcessAddDevicePreDeviceCreate</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available starting with Windows 8.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Gpioclx.h</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Msgpioclxstub.lib</dt>
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
<a href="..\wdfdriver\nc-wdfdriver-evt-wdf-driver-device-add.md">EvtDriverDeviceAdd</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439487">GPIO_CLX_ProcessAddDevicePreDeviceCreate</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545926">WdfDeviceCreate</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [GPIO\parports]:%20GPIO_CLX_ProcessAddDevicePostDeviceCreate method%20 RELEASE:%20(11/3/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
