---
UID: NS.usbscan._USBSCAN_PIPE_INFORMATION
title: USBSCAN_PIPE_INFORMATION
author: windows-driver-content
description: The USBSCAN_PIPE_INFORMATION structure is used to describe a USB transfer pipe for a still image device. An array of USBSCAN_PIPE_INFORMATION structures is supplied within a USBSCAN_PIPE_CONFIGURATION structure.
old-location: image\usbscan_pipe_information.htm
old-project: image
ms.assetid: a13bec15-67e1-45f9-be90-dee5c555ad64
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: USBSCAN_PIPE_INFORMATION, USBSCAN_PIPE_INFORMATION, *PUSBSCAN_PIPE_INFORMATION
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: usbscan.h
req.include-header: Usbscan.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: USBSCAN_PIPE_INFORMATION
req.alt-loc: usbscan.h
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
req.iface: 
req.product: Windows 10 or later.
---

# USBSCAN_PIPE_INFORMATION structure



## -description
<p>The USBSCAN_PIPE_INFORMATION structure is used to describe a USB transfer pipe for a still image device. An array of USBSCAN_PIPE_INFORMATION structures is supplied within a <a href="..\usbscan\ns-usbscan--usbscan-pipe-configuration.md">USBSCAN_PIPE_CONFIGURATION</a> structure.</p>


## -syntax

````
typedef struct _USBSCAN_PIPE_INFORMATION {
  USHORT        MaximumPacketSize;
  UCHAR         EndpointAddress;
  UCHAR         Interval;
  RAW_PIPE_TYPE PipeType;
} USBSCAN_PIPE_INFORMATION, *PUSBSCAN_PIPE_INFORMATION;
````


## -struct-fields
<dl>

### -field <b>MaximumPacketSize</b>

<dd>
<p>Maximum packet size for the transfer pipe.</p>
</dd>

### -field <b>EndpointAddress</b>

<dd>
<p>The address of the pipe's endpoint. The address is encoded as follows:</p>
<table>
<tr>
<th>Bits</th>
<th>Definition</th>
</tr>
<tr>
<td>
<p>0..3</p>
</td>
<td>
<p>Endpoint number.</p>
</td>
</tr>
<tr>
<td>
<p>4..6</p>
</td>
<td>
<p>Reserved, set to 0.</p>
</td>
</tr>
<tr>
<td>
<p>7</p>
</td>
<td>
<p>Direction, ignored for control endpoints:</p>
<p>0 - OUT endpoint</p>
<p>1 - IN endpoint</p>
</td>
</tr>
</table>
<p> </p>
<p>For more information, see the <i>Universal Serial Bus Specification</i>.</p>
</dd>

### -field <b>Interval</b>

<dd>
<p>Polling interval, in milliseconds, for interrupt pipes. For more information, see the <i>Universal Serial Bus Specification</i>.</p>
</dd>

### -field <b>PipeType</b>

<dd>
<p>A <a href="..\usbscan\ne-usbscan--raw-pipe-type.md">RAW_PIPE_TYPE</a>-typed value identifying the pipe type.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Usbscan.h (include Usbscan.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\usbscan\ns-usbscan--usbscan-pipe-configuration.md">USBSCAN_PIPE_CONFIGURATION</a>
</dt>
<dt>
<a href="..\usbscan\ne-usbscan--raw-pipe-type.md">RAW_PIPE_TYPE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [image\image]:%20USBSCAN_PIPE_INFORMATION structure%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
