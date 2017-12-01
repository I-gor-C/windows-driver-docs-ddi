---
UID: NS.usbscan._IO_BLOCK_EX
title: IO_BLOCK_EX
author: windows-driver-content
description: The IO_BLOCK_EX structure is used as a parameter to DeviceIoControl, when the specified I/O control code is IOCTL_SEND_USB_REQUEST.
old-location: image\io_block_ex.htm
old-project: image
ms.assetid: 2474a49b-e275-4b4d-b762-c296b92bab4c
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: IO_BLOCK_EX, IO_BLOCK_EX, *PIO_BLOCK_EX
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
req.alt-api: IO_BLOCK_EX
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

# IO_BLOCK_EX structure



## -description
<p>The IO_BLOCK_EX structure is used as a parameter to <a href="base.deviceiocontrol">DeviceIoControl</a>, when the specified I/O control code is <a href="..\usbscan\ni-usbscan-ioctl-send-usb-request.md">IOCTL_SEND_USB_REQUEST</a>. Values contained in structure members are used to create a USB Device Request (described in the <i>Universal Serial Bus Specification</i>).</p>


## -syntax

````
typedef struct _IO_BLOCK_EX {
  unsigned uOffset;
  unsigned uLength;
  PUCHAR   pbyData;
  unsigned uIndex;
  UCHAR    bRequest;
  UCHAR    bmRequestType;
  UCHAR    fTransferDirectionIn;
} IO_BLOCK_EX, *PIO_BLOCK_EX;
````


## -struct-fields
<dl>

### -field <b>uOffset</b>

<dd>
<p>Used as the <b>Value</b> field of a USB Device Request.</p>
</dd>

### -field <b>uLength</b>

<dd>
<p>Length of the buffer to transfer.</p>
</dd>

### -field <b>pbyData</b>

<dd>
<p>Pointer to a data buffer with a length of <b>uLength</b>.</p>
</dd>

### -field <b>uIndex</b>

<dd>
<p>Used as the <b>Index</b> field of a USB Device Request.</p>
</dd>

### -field <b>bRequest</b>

<dd>
<p>Used as the <b>bRequest</b> field of a USB Device Request.</p>
</dd>

### -field <b>bmRequestType</b>

<dd>
<p>Used as the <b>bmRequestType</b> field of a USB Device Request.</p>
</dd>

### -field <b>fTransferDirectionIn</b>

<dd>
<p><b>TRUE</b> for transfers from device to host; <b>FALSE</b> for transfers from host to device.</p>
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