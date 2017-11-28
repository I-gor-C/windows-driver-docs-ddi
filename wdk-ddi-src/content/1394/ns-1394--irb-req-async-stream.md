---
UID: NS.1394._IRB_REQ_ASYNC_STREAM
title: IRB_REQ_ASYNC_STREAM
author: windows-driver-content
description: This structure contains the fields necessary for the 1394 bus driver to carry out an asynchronous write request.
old-location: ieee\irb_req_async_stream.htm
old-project: IEEE
ms.assetid: 9E4958B0-066F-4485-AFF2-3AE499AF3E64
ms.author: windowsdriverdev
ms.date: 10/23/2017
ms.keywords: IRB_REQ_ASYNC_STREAM, IRB_REQ_ASYNC_STREAM
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
req.alt-api: IRB_REQ_ASYNC_STREAM
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

# IRB_REQ_ASYNC_STREAM structure



## -description
<p>This structure contains the fields necessary for the 1394 bus driver to carry out an asynchronous write request.</p>


## -syntax

````
typedef struct _IRB_REQ_ASYNC_STREAM {
  ULONG nNumberOfBytesToStream;
  ULONG fulFlags;
  PMDL  Mdl;
  ULONG ulTag;
  ULONG nChannel;
  ULONG ulSynch;
  ULONG Reserved;
  UCHAR nSpeed;
} IRB_REQ_ASYNC_STREAM;
````


## -struct-fields
<dl>

### -field <b>nNumberOfBytesToStream</b>

<dd>
<p>Specifies the number of bytes to write.</p>
</dd>

### -field <b>fulFlags</b>

<dd>
<p>Reserved. Drivers must set this to zero.</p>
</dd>

### -field <b>Mdl</b>

<dd>
<p>Specifies the source buffer.</p>
</dd>

### -field <b>ulTag</b>

<dd>
<p>Specifies the Tag field for any packets generated from this request.</p>
</dd>

### -field <b>nChannel</b>

<dd>
<p>Specifies the channel to which the data will be written.</p>
</dd>

### -field <b>ulSynch</b>

<dd>
<p>Specifies the Sy field for any packets generated from this request.</p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>Reserved. Drivers must set this to zero.</p>
</dd>

### -field <b>nSpeed</b>

<dd>
<p>Specifies the transfer rate. The possible speed values are SPEED_FLAGS_xxx, where xxx is the (approximate) transfer rate in megabits per second. Existing hardware currently supports transfer rates of 100, 200, and 400 Mb/sec.</p>
<table>
<tr>
<th>Transfer Rate</th>
<th>Description</th>
</tr>
<tr>
<td>
<p>SPEED_FLAGS_100</p>
</td>
<td>
<p>100 Mb/s</p>
</td>
</tr>
<tr>
<td>
<p>SPEED_FLAGS_200</p>
</td>
<td>
<p>200 Mb/s</p>
</td>
</tr>
<tr>
<td>
<p>SPEED_FLAGS_400</p>
</td>
<td>
<p>400 Mb/s</p>
</td>
</tr>
</table>
<p> </p>
<div class="alert"><b>Note</b>  In Windows 7 and later versions of Windows, you can specify new values higher speed and  greater sized payloads. For more information, see <a href="buses.device_driver_interface__ddi__changes_in_windows_7#speed#speed">New Flags for Speed and Payload Size</a> and <a href="buses.device_driver_interface__ddi__changes_in_windows_7#ioctl#ioctl">IEEE 1394 IOCTL Changes</a> in Device Driver Interface (DDI) Changes in Windows 7.</div>
<div> </div>
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