---
UID: NS.WDFUSB._WDF_USB_PIPE_INFORMATION
title: _WDF_USB_PIPE_INFORMATION
author: windows-driver-content
description: The WDF_USB_PIPE_INFORMATION structure contains information about a USB pipe and its endpoint.
old-location: wdf\wdf_usb_pipe_information.htm
old-project: wdf
ms.assetid: 05cba67b-c9da-4345-bc6f-09de12a617c1
ms.author: windowsdriverdev
ms.date: 12/7/2017
ms.keywords: _WDF_USB_PIPE_INFORMATION, WDF_USB_PIPE_INFORMATION, *PWDF_USB_PIPE_INFORMATION
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
req.irql: 
req.product: Windows 10 or later.
---

# _WDF_USB_PIPE_INFORMATION structure



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]

The <b>WDF_USB_PIPE_INFORMATION</b> structure contains information about a USB pipe and its endpoint.



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

### -field Size

The size, in bytes, of this structure.


### -field MaximumPacketSize

The maximum packet size, in bytes, that the pipe's endpoint is capable of sending or receiving.

For high-speed isochronous endpoints, the received <b>MaximumPacketSize</b> value includes the number of bytes that can be transferred in additional transactions, if the endpoint supports them.


### -field EndpointAddress

The address of the endpoint on the USB device. For more information about endpoint addresses, see the USB specification.


### -field Interval

The endpoint's polling interval, if the <b>PipeType</b> member is set to <b>WdfUsbPipeTypeInterrupt</b>. For more information about polling intervals, see the USB specification.


### -field SettingIndex

An index value that identifies the alternate setting, within an interface, that the pipe belongs to. For more information about alternate settings, see the USB specification.


### -field PipeType

A <a href="wdf.wdf_usb_pipe_type">WDF_USB_PIPE_TYPE</a>-typed value that specifies the type of pipe.


### -field MaximumTransferSize

This member is not used.  


## -remarks
The <b>WDF_USB_PIPE_INFORMATION</b> structure is filled in by the <a href="wdf.wdfusbtargetpipegetinformation">WdfUsbTargetPipeGetInformation</a>, <a href="wdf.wdfusbinterfacegetconfiguredpipe">WdfUsbInterfaceGetConfiguredPipe</a>, and <a href="wdf.wdfusbinterfacegetendpointinformation">WdfUsbInterfaceGetEndpointInformation</a> methods.

To initialize a <b>WDF_USB_PIPE_INFORMATION</b> structure, your driver should call <a href="wdf.wdf_usb_pipe_information_init">WDF_USB_PIPE_INFORMATION_INIT</a>.

For more information about the <b>MaximumPacketSize</b> member of this structure, see  the Remarks section of <a href="buses.usbd_pipe_information">USBD_PIPE_INFORMATION</a>.

For information on how to transfer data to and from supported isochronous endpoints in a USB device, see <a href="buses.transfer_data_to_isochronous_endpoints">How to Transfer Data to USB Isochronous Endpoints</a>.


## -requirements
<table>
<tr>
<th width="30%">
Minimum KMDF version

</th>
<td width="70%">
1.0

</td>
</tr>
<tr>
<th width="30%">
Minimum UMDF version

</th>
<td width="70%">
2.0

</td>
</tr>
<tr>
<th width="30%">
Header

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
<a href="buses.usbd_pipe_information">USBD_PIPE_INFORMATION</a>
</dt>
<dt>
<a href="wdf.wdf_usb_pipe_information_init">WDF_USB_PIPE_INFORMATION_INIT</a>
</dt>
<dt>
<a href="wdf.wdf_usb_pipe_type">WDF_USB_PIPE_TYPE</a>
</dt>
<dt>
<a href="wdf.wdfusbinterfacegetconfiguredpipe">WdfUsbInterfaceGetConfiguredPipe</a>
</dt>
<dt>
<a href="wdf.wdfusbinterfacegetendpointinformation">WdfUsbInterfaceGetEndpointInformation</a>
</dt>
<dt>
<a href="wdf.wdfusbtargetpipegetinformation">WdfUsbTargetPipeGetInformation</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WDF_USB_PIPE_INFORMATION structure%20 RELEASE:%20(12/7/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

