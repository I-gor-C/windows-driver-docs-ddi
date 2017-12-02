---
UID: NS.1394._IRB_REQ_ASYNC_READ
title: IRB_REQ_ASYNC_READ
author: windows-driver-content
description: This structure contains the fields necessary for the 1394 stack to carry out an asynchronous read request.
old-location: ieee\irb_req_async_read.htm
old-project: IEEE
ms.assetid: C88A1F30-FC6B-4EC4-8F10-F507E17CF01D
ms.author: windowsdriverdev
ms.date: 11/29/2017
ms.keywords: IRB_REQ_ASYNC_READ, IRB_REQ_ASYNC_READ
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: 1394.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IRB_REQ_ASYNC_READ
req.alt-loc: 1394.h
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
---

# IRB_REQ_ASYNC_READ structure



## -description
<p>This structure contains the fields necessary for the 1394 stack to carry out an asynchronous read request.</p>


## -syntax

````
typedef struct _IRB_REQ_ASYNC_READ {
  IO_ADDRESS DestinationAddress;
  ULONG      nNumberOfBytesToRead;
  ULONG      nBlockSize;
  ULONG      fulFlags;
  PMDL       Mdl;
  ULONG      ulGeneration;
  UCHAR      chPriority;
  UCHAR      nSpeed;
  UCHAR      tCode;
  UCHAR      Reserved;
  ULONG      ElapsedTime;
} IRB_REQ_ASYNC_READ;
````


## -struct-fields
<dl>

### -field DestinationAddress

<dd>
<p>Specifies the 1394 64-bit destination address for this read operation. The driver only needs to fill in the <b>IA_Destination_Offset</b> member of <b>DestinationAddress</b>; the bus driver fills in the <b>IA_Destination_ID</b> member. See <a href="https://msdn.microsoft.com/library/windows/hardware/ff537346">IO_ADDRESS</a> for the structure description.</p>
</dd>

### -field nNumberOfBytesToRead

<dd>
<p>Specifies the number of bytes to be read from the 1394 node.</p>
</dd>

### -field nBlockSize

<dd>
<p>Specifies the size of each individual block within the data stream that is read as a whole from the 1394 node. If this parameter is zero, the maximum packet size for the device and speed selected is used to issue these read requests, unless raw-mode addressing is used.</p>
<p>

If raw-mode addressing is used, the client driver should set the <b>nBlockSize</b> member to the maximum asynchronous payload size that is supported by the device at the connected speed.

</p>
<p>For more information on raw-mode addressing, see <a href="https://msdn.microsoft.com/93ad0cdf-5ac2-4916-b90e-1e64ca4494b6">Sending Asynchronous I/O Request Packets on the IEEE 1394 Bus.</a>
<div class="alert"><b>Note</b>  In Windows 7 and later versions of Windows, you can specify new values higher speed and  greater sized payloads. For more information, see <a href="buses.device_driver_interface__ddi__changes_in_windows_7#speed#speed">New Flags for Speed and Payload Size</a> and <a href="buses.device_driver_interface__ddi__changes_in_windows_7#ioctl#ioctl">IEEE 1394 IOCTL Changes</a> in Device Driver Interface (DDI) Changes in Windows 7.</div>
<div> </div>
</p>
</dd>

### -field fulFlags

<dd>
<p>Specifies any nondefault settings for this operation. The following flags are provided.</p>
<table>
<tr>
<th>Flag</th>
<th>Description</th>
</tr>
<tr>
<td>
<p> ASYNC_FLAGS_NONINCREMENTING</p>
</td>
<td>
<p>When the bus driver splits the request into blocks, begin the operation for each block at the same address, rather than treating each block as consecutive sections of the device's address space. Used only in asynchronous requests larger than <b>u.AsyncRead.nBlockSize</b> or the maximum packet size for the current speed.</p>
</td>
</tr>
<tr>
<td>
<p>ASYNC_FLAGS_PING</p>
</td>
<td>
<p>The bus driver returns the elapsed time of the operation in <b>u.AsyncRead.ElapsedTime</b>.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field Mdl

<dd>
<p>Points to an MDL that describes the device driver's buffer, which receives data from the 1394 node.</p>
</dd>

### -field ulGeneration

<dd>
<p>Specifies the bus reset generation as known by the device driver that submits this asynchronous request. If the generation count specified does not match the actual generation of the bus, this request is returned with an error of STATUS_INVALID_GENERATION. </p>
</dd>

### -field chPriority

<dd>
<p>Reserved. Drivers must set this to zero.</p>
</dd>

### -field nSpeed

<dd>
<p>Reserved. Drivers must set this to zero.</p>
</dd>

### -field tCode

<dd>
<p>Reserved. Drivers must set this to zero.</p>
</dd>

### -field Reserved

<dd>
<p>Reserved. Drivers must set this to zero.</p>
</dd>

### -field ElapsedTime

<dd>
<p>Elapsed time in nanoseconds. Only valid for flag ASYNC_FLAGS_PING.</p>
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
<dt>1394.h</dt>
</dl>
</td>
</tr>
</table>