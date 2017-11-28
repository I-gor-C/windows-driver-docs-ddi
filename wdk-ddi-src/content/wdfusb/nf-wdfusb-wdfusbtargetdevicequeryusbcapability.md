---
UID: NF.wdfusb.WdfUsbTargetDeviceQueryUsbCapability
title: WdfUsbTargetDeviceQueryUsbCapability
author: windows-driver-content
description: The WdfUsbTargetDeviceQueryUsbCapability method determines whether the host controller and USB driver stack support a specific capability.
old-location: wdf\wdfusbtargetdevicequeryusbcapability.htm
old-project: wdf
ms.assetid: B6C3E94F-AFC9-45EC-91F1-F0E3586DBDA1
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: WdfUsbTargetDeviceQueryUsbCapability
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdfusb.h
req.include-header: Wdfusb.h
req.target-type: Universal
req.target-min-winverclnt: Windows Vista
req.target-min-winversvr: 
req.kmdf-ver: 1.11
req.umdf-ver: 2.0
req.alt-api: WdfUsbTargetDeviceQueryUsbCapability
req.alt-loc: Wdf01000.sys,Wdf01000.sys.dll,WUDFx02000.dll,WUDFx02000.dll.dll
req.ddi-compliance: DriverCreate
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
req.iface: 
req.product: Windows 10 or later.
---

# WdfUsbTargetDeviceQueryUsbCapability function



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]</p>
<p>
   The <b>WdfUsbTargetDeviceQueryUsbCapability</b> method determines whether the host controller and USB driver stack support a specific capability.</p>


## -syntax

````
NTSTATUS WdfUsbTargetDeviceQueryUsbCapability(
  _In_            WDFUSBDEVICE UsbDevice,
  _In_      const PGUID        *CapabilityType,
  _In_            ULONG        CapabilityBufferLength,
  _Out_opt_       PVOID        CapabilityBuffer,
  _Out_opt_       PULONG       ResultLength
);
````


## -parameters
<dl>

### -param <i>UsbDevice</i> [in]

<dd>
<p>A handle to a USB device object.</p>
</dd>

### -param <i>CapabilityType</i> [in]

<dd>
<p>A pointer to a GUID that represents the capability about which the client driver wants to retrieve information. The possible  <i>PGUID</i>  values are  as follows:</p>
<ul>
<li>GUID_USB_CAPABILITY_CHAINED_MDLS</li>
<li>GUID_USB_CAPABILITY_STATIC_STREAMS</li>
<li>GUID_USB_CAPABILITY_SELECTIVE_SUSPEND</li>
<li>GUID_USB_CAPABILITY_FUNCTION_SUSPEND

</li>
<li>GUID_USB_CAPABILITY_DEVICE_CONNECTION_HIGH_SPEED_COMPATIBLE</li>
<li>GUID_USB_CAPABILITY_DEVICE_CONNECTION_SUPER_SPEED_COMPATIBLE</li>
</ul>
<p>See more information in Remarks.</p>
</dd>

### -param <i>CapabilityBufferLength</i> [in]

<dd>
<p>Length, in bytes, of the buffer pointed to by <i>CapabilityBuffer</i>.</p>
</dd>

### -param <i>CapabilityBuffer</i> [out, optional]

<dd>
<p>A pointer to a caller-allocated buffer to receive the requested USB capability. This parameter is optional. If 
                       <i>CapabilityBufferLength</i> is zero, this parameter must be NULL. Similarly, if <i>CapabilityBufferLength</i> is nonzero, this parameter must be supplied. This parameter corresponds to the <i>OutputBuffer</i> parameter of the <a href="https://msdn.microsoft.com/library/windows/hardware/hh406230">USBD_QueryUsbCapability</a> routine.</p>
</dd>

### -param <i>ResultLength</i> [out, optional]

<dd>
<p>A pointer to a location containing the size, in bytes, of the returned capability. This parameter is optional.</p>
</dd>
</dl>

## -returns
<p><b>WdfUsbTargetDeviceQueryUsbCapability</b> returns STATUS_SUCCESS if the operation succeeds. Otherwise, this method can return one of the following values:</p><dl>
<dt><b>STATUS_INVALID_DEVICE_STATE</b></dt>
</dl><p>The USB device object handle is not valid.</p><dl>
<dt><b>STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl><p>Insufficient memory was available.</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>The caller passed an invalid parameter value.</p><dl>
<dt><b>STATUS_NOT_IMPLEMENTED</b></dt>
</dl><p>The specified capability is not supported by the underlying USB driver stack.</p><dl>
<dt><b>STATUS_NOT_SUPPORTED</b></dt>
</dl><p>The specified capability is not supported by the host controller hardware.</p>

<p> </p>

<p>This method also might return other <a href="https://msdn.microsoft.com/library/windows/hardware/ff557697">NTSTATUS values</a>.</p>

## -remarks
<p>Before calling <b>WdfUsbTargetDeviceQueryUsbCapability</b>, the driver must call  <a href="https://msdn.microsoft.com/library/windows/hardware/hh439428">WdfUsbTargetDeviceCreateWithParameters</a> to register with the underlying USB driver stack.</p>

<p><b>WdfUsbTargetDeviceQueryUsbCapability</b> must be called after the driver's <a href="..\wdfdevice\nc-wdfdevice-evt-wdf-device-prepare-hardware.md">EvtDevicePrepareHardware</a> callback function has been called. </p>

<p>The following table describes the USB-specific capabilities that a KMDF-based USB client driver can query through a <b>WdfUsbTargetDeviceQueryUsbCapability</b> call. </p>

<p>The new USB driver stack in Windows 8 is capable of accepting a chained MDL (see <a href="https://msdn.microsoft.com/library/windows/hardware/ff554414">MDL</a>) from the a KMDF-based USB client driver.</p>

<p> For more information about the chained MDLs capability in the USB driver stack, see <a href="https://msdn.microsoft.com/library/windows/hardware/hh450848">How to Send Chained MDLs</a>.  </p>

<p>This GUID applies to KMDF drivers only.</p>

<p> Whereas USB 2.0 and earlier supports sending only a single data stream through a bulk endpoint, USB 3.0 permits sending and receiving multiple data streams through a bulk endpoint. 
</p>

<p>For more information about opening streams, see <a href="https://msdn.microsoft.com/library/windows/hardware/hh450846">How to Open and Close Static Streams in a USB Bulk Endpoint</a>.</p>

<p>This GUID applies to KMDF drivers only.</p>

<p>The Universal Serial Bus (USB) 3.0 specification defines a new feature called function suspend. The feature enables an individual function of a composite device to enter a low-power state, independently of other functions. </p>

<p>For more information about function suspend, see <a href="buses.how-to__implement_remote_and_function_wake_support">How to Implement Function Suspend in a Composite Driver</a>.</p>

<p>This GUID applies to KMDF drivers only.</p>

<p>For information about selective suspend, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff540144">USB Selective Suspend</a>.</p>

<p>This GUID applies to KMDF drivers only.</p>

<p>Determines whether the bus is operating at high-speed or higher. </p>

<p>This GUID applies to KMDF and UMDF drivers.</p>

<p>Determines whether the bus is operating at SuperSpeed or higher.</p>

<p>This GUID applies to KMDF and UMDF drivers.</p>

<p> </p>

<p>Before calling <b>WdfUsbTargetDeviceQueryUsbCapability</b>, the driver must call  <a href="https://msdn.microsoft.com/library/windows/hardware/hh439428">WdfUsbTargetDeviceCreateWithParameters</a> to register with the underlying USB driver stack.</p>

<p><b>WdfUsbTargetDeviceQueryUsbCapability</b> must be called after the driver's <a href="..\wdfdevice\nc-wdfdevice-evt-wdf-device-prepare-hardware.md">EvtDevicePrepareHardware</a> callback function has been called. </p>

<p>The following table describes the USB-specific capabilities that a KMDF-based USB client driver can query through a <b>WdfUsbTargetDeviceQueryUsbCapability</b> call. </p>

<p>The new USB driver stack in Windows 8 is capable of accepting a chained MDL (see <a href="https://msdn.microsoft.com/library/windows/hardware/ff554414">MDL</a>) from the a KMDF-based USB client driver.</p>

<p> For more information about the chained MDLs capability in the USB driver stack, see <a href="https://msdn.microsoft.com/library/windows/hardware/hh450848">How to Send Chained MDLs</a>.  </p>

<p>This GUID applies to KMDF drivers only.</p>

<p> Whereas USB 2.0 and earlier supports sending only a single data stream through a bulk endpoint, USB 3.0 permits sending and receiving multiple data streams through a bulk endpoint. 
</p>

<p>For more information about opening streams, see <a href="https://msdn.microsoft.com/library/windows/hardware/hh450846">How to Open and Close Static Streams in a USB Bulk Endpoint</a>.</p>

<p>This GUID applies to KMDF drivers only.</p>

<p>The Universal Serial Bus (USB) 3.0 specification defines a new feature called function suspend. The feature enables an individual function of a composite device to enter a low-power state, independently of other functions. </p>

<p>For more information about function suspend, see <a href="buses.how-to__implement_remote_and_function_wake_support">How to Implement Function Suspend in a Composite Driver</a>.</p>

<p>This GUID applies to KMDF drivers only.</p>

<p>For information about selective suspend, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff540144">USB Selective Suspend</a>.</p>

<p>This GUID applies to KMDF drivers only.</p>

<p>Determines whether the bus is operating at high-speed or higher. </p>

<p>This GUID applies to KMDF and UMDF drivers.</p>

<p>Determines whether the bus is operating at SuperSpeed or higher.</p>

<p>This GUID applies to KMDF and UMDF drivers.</p>

<p> </p>

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
<p>Minimum support</p>
</th>
<td width="70%">
<p>Windows Vista</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum KMDF version</p>
</th>
<td width="70%">
<p>1.11</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544957">DriverCreate</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh406230">USBD_QueryUsbCapability</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550100">WdfUsbTargetDeviceRetrieveInformation</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfUsbTargetDeviceQueryUsbCapability method%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
