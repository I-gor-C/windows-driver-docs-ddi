---
UID: NF:wdfhwaccess.WDF_WRITE_PORT_BUFFER_UCHAR
title: WDF_WRITE_PORT_BUFFER_UCHAR function
author: windows-driver-content
description: The WDF_WRITE_PORT_BUFFER_UCHAR function writes a number of bytes from a buffer to the specified port.
old-location: wdf\wdf_write_port_buffer_uchar.htm
old-project: wdf
ms.assetid: 744189F3-07D1-42F2-986C-70BEBE760123
ms.author: windowsdriverdev
ms.date: 12/29/2017
ms.keywords: WDF_WRITE_PORT_BUFFER_UCHAR
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdfhwaccess.h
req.include-header: 
req.target-type: Universal
req.target-min-winverclnt: Windows 8.1
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 2.0
req.alt-api: WDF_WRITE_PORT_BUFFER_UCHAR
req.alt-loc: Wdfhwaccess.h
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
req.typenames: *PWDF_FILE_INFORMATION_CLASS, WDF_FILE_INFORMATION_CLASS
req.product: Windows 10 or later.
---

# WDF_WRITE_PORT_BUFFER_UCHAR function



## -description
<p class="CCE_Message">[Applies to UMDF only]

The <b>WDF_WRITE_PORT_BUFFER_UCHAR</b> function writes a number of bytes from a buffer to the specified port.




## -syntax

````
void WDF_WRITE_PORT_BUFFER_UCHAR(
  _In_ WDFDEVICE Device,
  _In_ PUCHAR    Port,
  _In_ PUCHAR    Buffer,
  _In_ ULONG     Count 
);
````


## -parameters

### -param Device [in]

A handle to a framework device object.


### -param Port [in]

A pointer to the port, which must be a mapped memory range in I/O space.



### -param Buffer [in]

A pointer to a buffer from which an array of UCHAR values is to be written.


### -param Count  [in]

Specifies the number of bytes to be written to the buffer.


## -returns
This function does not return a value.


## -remarks
The size of the buffer must be large enough to contain at least the specified number of bytes.


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Minimum support

</th>
<td width="70%">
Windows 8.1

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
<dt>Wdfhwaccess.h</dt>
</dl>
</td>
</tr>
</table>