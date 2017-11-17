---
UID: NS.usbioctl._USB_PIPE_INFO
title: USB_PIPE_INFO
author: windows-driver-content
description: The USB_PIPE_INFO structure is used in conjunction with the USB_NODE_CONNECTION_INFORMATION_EX structure and the IOCTL_USB_GET_NODE_CONNECTION_INFORMATION_EX request to obtain information about a connection and its associated pipes.
old-location: buses\usb_pipe_info.htm
ms.assetid: 9da16cd4-bd5f-4713-83ce-4302f6807476
ms.author: windowsdriverdev
ms.date: 11/3/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: usbref
req.header: usbioctl.h
req.include-header: Usbioctl.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: USB_PIPE_INFO
req.alt-loc: usbioctl.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <=DISPATCH_LEVEL
ms.keywords: USB_PIPE_INFO, USB_PIPE_INFO, *PUSB_PIPE_INFO
req.iface: 
req.product: Windows 10 or later.
---

# USB_PIPE_INFO structure



## -description
<p>The <b>USB_PIPE_INFO</b> structure is used in conjunction with the <a href="https://msdn.microsoft.com/library/windows/hardware/ff540094">USB_NODE_CONNECTION_INFORMATION_EX</a> structure and the <a href="https://msdn.microsoft.com/library/windows/hardware/ff537321">IOCTL_USB_GET_NODE_CONNECTION_INFORMATION_EX</a> request to obtain information about a connection and its associated pipes.</p>


## -syntax

````
typedef struct _USB_PIPE_INFO {
  USB_ENDPOINT_DESCRIPTOR EndpointDescriptor;
  ULONG                   ScheduleOffset;
} USB_PIPE_INFO, *PUSB_PIPE_INFO;
````


## -struct-fields
<dl>

### -field <b>EndpointDescriptor</b>

<dd>
<p>Describes the endpoint descriptor. For more information about the endpoint descriptor, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff539317">USB_ENDPOINT_DESCRIPTOR</a>.</p>
</dd>

### -field <b>ScheduleOffset</b>

<dd>
<p>Indicates the schedule offset assigned to the endpoint for this pipe. See the remarks section for a discussion of the range of values that this member can take. </p>
</dd>
</dl>

## -remarks
<p>The USB specification labels isochronous and interrupt transfers as "periodic," because certain periods of transmission time are set aside for these types of transfers. The port driver further divides these periods into "schedule offsets" and distributes the available offsets between those endpoints that are doing periodic transfers. The number of offsets that are available depends on the period. The following table lists the offset values that are available for each period.
</p>

<p>1</p>

<p>0</p>

<p>2</p>

<p>0 to 1</p>

<p>4</p>

<p>0 to 3</p>

<p>8</p>

<p>0 to 7</p>

<p>16</p>

<p>0 to 15 </p>

<p>32</p>

<p>0 to 31</p>

<p> </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Usbioctl.h (include Usbioctl.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff537321">IOCTL_USB_GET_NODE_CONNECTION_INFORMATION_EX</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff539317">USB_ENDPOINT_DESCRIPTOR</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff540160">USB Structures</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [usbref\buses]:%20USB_PIPE_INFO structure%20 RELEASE:%20(11/3/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
