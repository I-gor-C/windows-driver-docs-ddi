---
UID: NF.wdfusb.WdfUsbTargetDeviceResetPortSynchronously
title: WdfUsbTargetDeviceResetPortSynchronously
author: windows-driver-content
description: The WdfUsbTargetDeviceResetPortSynchronously method resets the USB port that is associated with the specified USB device.
old-location: wdf\wdfusbtargetdeviceresetportsynchronously.htm
ms.assetid: 4f0941ea-ccbb-4345-82c0-ec5d88862b05
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: wdf
req.header: wdfusb.h
req.include-header: Wdfusb.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
req.alt-api: WdfUsbTargetDeviceResetPortSynchronously
req.alt-loc: Wdf01000.sys,Wdf01000.sys.dll,WUDFx02000.dll,WUDFx02000.dll.dll
req.ddi-compliance: DriverCreate, KmdfIrql, KmdfIrql2, UsbKmdfIrql, UsbKmdfIrql2
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Wdf01000.sys (KMDF); 
WUDFx02000.dll (UMDF)
req.dll: 
req.irql: PASSIVE_LEVEL
ms.keywords: WdfUsbTargetDeviceResetPortSynchronously
req.iface: 
req.product: Windows 10 or later.
---

# WdfUsbTargetDeviceResetPortSynchronously function



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]</p>
<p>The <b>WdfUsbTargetDeviceResetPortSynchronously</b> method resets the USB port that is associated with the specified USB device.</p>


## -syntax

````
NTSTATUS WdfUsbTargetDeviceResetPortSynchronously(
  _In_ WDFUSBDEVICE UsbDevice
);
````


## -parameters
<dl>

### -param <i>UsbDevice</i> [in]

<dd>
<p>A handle to a USB device object that was obtained from a previous call to <a href="https://msdn.microsoft.com/library/windows/hardware/hh439428">WdfUsbTargetDeviceCreateWithParameters</a>.</p>
</dd>
</dl>

## -returns
<p><b>WdfUsbTargetDeviceResetPortSynchronously</b> returns the USB I/O target's completion status value if the operation succeeds. Otherwise, this method can return one of the following values:</p><dl>
<dt><b>STATUS_INVALID_DEVICE_REQUEST</b></dt>
</dl><p>The caller's IRQL was invalid.</p>

<p> </p>

<p>This method also might return other <a href="https://msdn.microsoft.com/library/windows/hardware/ff557697">NTSTATUS values</a>.</p>

<p>A bug check occurs if the driver supplies an invalid object handle.

</p>

## -remarks
<p>The <b>WdfUsbTargetDeviceResetPortSynchronously</b> method resets the USB port by sending an <a href="https://msdn.microsoft.com/library/windows/hardware/ff537269">IOCTL_INTERNAL_USB_RESET_PORT</a> request.</p>

<p>Before the framework resets the I/O target's USB port, it cancels all I/O requests that remain in the I/O target's queue. The driver must not send additional I/O requests to the I/O target until <b>WdfUsbTargetDeviceResetPortSynchronously</b> returns.</p>

<p>The driver must call <a href="https://msdn.microsoft.com/library/windows/hardware/ff548680">WdfIoTargetStop</a> before it calls <b>WdfUsbTargetDeviceResetPortSynchronously</b>. After <b>WdfUsbTargetDeviceResetPortSynchronously</b> returns, the driver can call <a href="https://msdn.microsoft.com/library/windows/hardware/ff548677">WdfIoTargetStart</a>.</p>

<p>After a successful reset operation, the bus driver reselects the configuration and any alternate interface settings that the device had before the reset operation occurred.</p>

<p>For more information about the <b>WdfUsbTargetDeviceResetPortSynchronously</b> method and USB I/O targets, see <a href="wdf.usb_i_o_targets">USB I/O Targets</a>.</p>

<p>The following code example resets a specified device's USB port.</p>

<p>The <b>WdfUsbTargetDeviceResetPortSynchronously</b> method resets the USB port by sending an <a href="https://msdn.microsoft.com/library/windows/hardware/ff537269">IOCTL_INTERNAL_USB_RESET_PORT</a> request.</p>

<p>Before the framework resets the I/O target's USB port, it cancels all I/O requests that remain in the I/O target's queue. The driver must not send additional I/O requests to the I/O target until <b>WdfUsbTargetDeviceResetPortSynchronously</b> returns.</p>

<p>The driver must call <a href="https://msdn.microsoft.com/library/windows/hardware/ff548680">WdfIoTargetStop</a> before it calls <b>WdfUsbTargetDeviceResetPortSynchronously</b>. After <b>WdfUsbTargetDeviceResetPortSynchronously</b> returns, the driver can call <a href="https://msdn.microsoft.com/library/windows/hardware/ff548677">WdfIoTargetStart</a>.</p>

<p>After a successful reset operation, the bus driver reselects the configuration and any alternate interface settings that the device had before the reset operation occurred.</p>

<p>For more information about the <b>WdfUsbTargetDeviceResetPortSynchronously</b> method and USB I/O targets, see <a href="wdf.usb_i_o_targets">USB I/O Targets</a>.</p>

<p>The following code example resets a specified device's USB port.</p>

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
<dt>Wdfusb.h (include Wdfusb.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Wdf01000.sys (KMDF); </dt>
<dt>WUDFx02000.dll (UMDF)</dt>
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
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544957">DriverCreate</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff548167">KmdfIrql</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975091">KmdfIrql2</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff554042">UsbKmdfIrql</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh995019">UsbKmdfIrql2</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439428">WdfUsbTargetDeviceCreateWithParameters</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfUsbTargetDeviceResetPortSynchronously method%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
