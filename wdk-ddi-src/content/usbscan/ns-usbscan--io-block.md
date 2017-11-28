---
UID: NS.usbscan._IO_BLOCK
title: IO_BLOCK
author: windows-driver-content
description: The IO_BLOCK structure is used as a parameter to DeviceIoControl, when the specified I/O control code is IOCTL_READ_REGISTERS or IOCTL_WRITE_REGISTERS.
old-location: image\io_block.htm
old-project: image
ms.assetid: aa1ccffc-c742-415d-8b72-fef247dff03c
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: IO_BLOCK, IO_BLOCK, *PIO_BLOCK
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
req.alt-api: IO_BLOCK
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

# IO_BLOCK structure



## -description
<p>The IO_BLOCK structure is used as a parameter to <a href="base.deviceiocontrol">DeviceIoControl</a>, when the specified I/O control code is <a href="https://msdn.microsoft.com/library/windows/hardware/ff542869">IOCTL_READ_REGISTERS</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff542920">IOCTL_WRITE_REGISTERS</a>. Values contained in structure members are used to create a USB Device Request (described in the <i>Universal Serial Bus Specification</i>).</p>


## -syntax

````
typedef struct _IO_BLOCK {
  unsigned uOffset;
  unsigned uLength;
  PUCHAR   pbyData;
  unsigned uIndex;
} IO_BLOCK, *PIO_BLOCK;
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