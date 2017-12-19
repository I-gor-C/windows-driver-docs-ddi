---
UID: NF.ufxclient.UfxDeviceNotifyReset
title: UfxDeviceNotifyReset function
author: windows-driver-content
description: Notifies UFX about a USB bus reset event.
old-location: buses\ufxdevicenotifyreset.htm
old-project: UsbRef
ms.assetid: FD88E645-7CBB-4998-BEBA-5BBE2FF167FC
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: UfxDeviceNotifyReset
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ufxclient.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: UfxDeviceNotifyReset
req.alt-loc: ufxclient.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: DISPATCH_LEVEL
req.product: Windows 10 or later.
---

# UfxDeviceNotifyReset function



## -description
Notifies UFX about a USB bus reset event.



## -syntax

````
VOID UfxDeviceNotifyReset(
  [in] UFXDEVICE        UfxDevice,
  [in] USB_DEVICE_SPEED DeviceSpeed
);
````


## -parameters

### -param UfxDevice [in]

A handle to a UFX device object that the driver created by calling <a href="buses.ufxdevicecreate">UfxDeviceCreate</a>.


### -param DeviceSpeed [in]

Contains a value of type <a href="buses.usb_device_speed">USB_DEVICE_SPEED</a> that indicates the speed of the device.


## -returns
This method does not return a value.


## -remarks
The client driver calls <b>UfxDeviceNotifyReset</b> when it receives a bus reset event. All non-default endpoints should be disabled and the default endpoint should be reset.  The device moves to the default state.

The client driver typically calls <b>UfxDeviceNotifyReset</b> from its <a href="..\wdfinterrupt\nc-wdfinterrupt-evt_wdf_interrupt_dpc.md">EvtInterruptDpc</a> callback function.  The following example shows how to handle a reset event.


## -requirements
<table>
<tr>
<th width="30%">
Minimum support

</th>
<td width="70%">
Windows 10

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Ufxclient.h</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL

</th>
<td width="70%">
DISPATCH_LEVEL

</td>
</tr>
</table>