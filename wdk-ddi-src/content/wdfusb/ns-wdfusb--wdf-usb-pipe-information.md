---
UID: NS.wdfusb._WDF_USB_PIPE_INFORMATION
title: WDF_USB_PIPE_INFORMATION
author: windows-driver-content
description: The WDF_USB_PIPE_INFORMATION structure contains information about a USB pipe and its endpoint.
old-location: wdf\wdf_usb_pipe_information.htm
old-project: wdf
ms.assetid: 05cba67b-c9da-4345-bc6f-09de12a617c1
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: WDF_USB_PIPE_INFORMATION, WDF_USB_PIPE_INFORMATION, *PWDF_USB_PIPE_INFORMATION
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: wdfusb.h
req.include-header: Wdfusb.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
req.alt-api: WDF_USB_PIPE_INFORMATION
req.alt-loc: wdfusb.h
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

# WDF_USB_PIPE_INFORMATION structure



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]</p>
<p>The <b>WDF_USB_PIPE_INFORMATION</b> structure contains information about a USB pipe and its endpoint.</p>


## -syntax

````
typedef struct _WDF_USB_PIPE_INFORMATION {
  ULONG             Size;
  ULONG             MaximumPacketSize;
  UCHAR             EndpointAddress;
  UCHAR             Interval;
  UCHAR             SettingIndex;
  WDF_USB_PIPE_TYPE PipeType;
  ULONG             MaximumTransferSize;
} WDF_USB_PIPE_INFORMATION, *PWDF_USB_PIPE_INFORMATION;
````


## -struct-fields
<dl>

### -field <b>Size</b>

<dd>
<p>The size, in bytes, of this structure.</p>
</dd>

### -field <b>MaximumPacketSize</b>

<dd>
<p>The maximum packet size, in bytes, that the pipe's endpoint is capable of sending or receiving.</p>
<p>For high-speed isochronous endpoints, the received <b>MaximumPacketSize</b> value includes the number of bytes that can be transferred in additional transactions, if the endpoint supports them.</p>
</dd>

### -field <b>EndpointAddress</b>

<dd>
<p>The address of the endpoint on the USB device. For more information about endpoint addresses, see the USB specification.</p>
</dd>

### -field <b>Interval</b>

<dd>
<p>The endpoint's polling interval, if the <b>PipeType</b> member is set to <b>WdfUsbPipeTypeInterrupt</b>. For more information about polling intervals, see the USB specification.</p>
</dd>

### -field <b>SettingIndex</b>

<dd>
<p>An index value that identifies the alternate setting, within an interface, that the pipe belongs to. For more information about alternate settings, see the USB specification.</p>
</dd>

### -field <b>PipeType</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff553047">WDF_USB_PIPE_TYPE</a>-typed value that specifies the type of pipe.</p>
</dd>

### -field <b>MaximumTransferSize</b>

<dd>
<p>This member is not used.  </p>
</dd>
</dl>

## -remarks
<p>The <b>WDF_USB_PIPE_INFORMATION</b> structure is filled in by the <a href="https://msdn.microsoft.com/library/windows/hardware/ff551142">WdfUsbTargetPipeGetInformation</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff550057">WdfUsbInterfaceGetConfiguredPipe</a>, and <a href="https://msdn.microsoft.com/library/windows/hardware/ff550063">WdfUsbInterfaceGetEndpointInformation</a> methods.</p>

<p>To initialize a <b>WDF_USB_PIPE_INFORMATION</b> structure, your driver should call <a href="https://msdn.microsoft.com/library/windows/hardware/ff553040">WDF_USB_PIPE_INFORMATION_INIT</a>.</p>

<p>For more information about the <b>MaximumPacketSize</b> member of this structure, see  the Remarks section of <a href="https://msdn.microsoft.com/library/windows/hardware/ff539114">USBD_PIPE_INFORMATION</a>.</p>

<p>For information on how to transfer data to and from supported isochronous endpoints in a USB device, see <a href="https://msdn.microsoft.com/library/windows/hardware/hh406225">How to Transfer Data to USB Isochronous Endpoints</a>.</p>

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
<dt>Wdfusb.h (include Wdfusb.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff539114">USBD_PIPE_INFORMATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553040">WDF_USB_PIPE_INFORMATION_INIT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553047">WDF_USB_PIPE_TYPE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550057">WdfUsbInterfaceGetConfiguredPipe</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550063">WdfUsbInterfaceGetEndpointInformation</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551142">WdfUsbTargetPipeGetInformation</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WDF_USB_PIPE_INFORMATION structure%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
