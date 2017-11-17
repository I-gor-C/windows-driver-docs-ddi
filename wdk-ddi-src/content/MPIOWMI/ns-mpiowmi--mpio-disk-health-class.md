---
UID: NS.mpiowmi._MPIO_DISK_HEALTH_CLASS
title: MPIO_DISK_HEALTH_CLASS
author: windows-driver-content
description: The MPIO_DISK_HEALTH_CLASS structure contains the health information for a multi-path disk.
old-location: storage\mpio_disk_health_class.htm
ms.assetid: 07b04bad-9d52-4a32-8834-48cd5803844c
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: Storage
req.header: mpiowmi.h
req.include-header: Mpiowmi.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: MPIO_DISK_HEALTH_CLASS
req.alt-loc: mpiowmi.h
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
ms.keywords: MPIO_DISK_HEALTH_CLASS, MPIO_DISK_HEALTH_CLASS, *PMPIO_DISK_HEALTH_CLASS
req.iface: 
---

# MPIO_DISK_HEALTH_CLASS structure



## -description
<p>The MPIO_DISK_HEALTH_CLASS structure contains the health information for a multi-path disk.</p>


## -syntax

````
typedef struct _MPIO_DISK_HEALTH_CLASS {
  WCHAR     Name[63 + 1];
  ULONGLONG NumberReads;
  ULONGLONG NumberWrites;
  ULONGLONG NumberBytesRead;
  ULONGLONG NumberBytesWritten;
  ULONGLONG NumberRetries;
  ULONGLONG NumberIoErrors;
  ULONGLONG CreateTime;
  ULONGLONG PathFailures;
  ULONGLONG FailTime;
  BOOLEAN   DeviceOffline;
  UCHAR     NumberReadsWrap;
  UCHAR     NumberWritesWrap;
  UCHAR     NumberBytesReadWrap;
  UCHAR     NumberBytesWrittenWrap;
  UCHAR     Pad[3];
} MPIO_DISK_HEALTH_CLASS, *PMPIO_DISK_HEALTH_CLASS;
````


## -struct-fields
<dl>

### -field <b>Name</b>

<dd>
<p>The name of this multi-path disk.</p>
</dd>

### -field <b>NumberReads</b>

<dd>
<p>An unsigned 64-bitfield that specifies the number of read requests that are serviced by this multi-path disk.</p>
</dd>

### -field <b>NumberWrites</b>

<dd>
<p>An unsigned 64-bitfield that specifies the number of write requests that are serviced by this multi-path disk.</p>
</dd>

### -field <b>NumberBytesRead</b>

<dd>
<p>An unsigned 64-bitfield that specifies the total number of bytes that are read from this multi-path disk.</p>
</dd>

### -field <b>NumberBytesWritten</b>

<dd>
<p>An unsigned 64-bitfield that specifies the total number of bytes that are written to this multi-path disk.</p>
</dd>

### -field <b>NumberRetries</b>

<dd>
<p>An unsigned 64-bitfield that specifies the total number of retries for this multi-path disk.</p>
</dd>

### -field <b>NumberIoErrors</b>

<dd>
<p>An unsigned 64-bitfield that specifies the total number of I/O errors that are encountered by this multi-path disk.</p>
</dd>

### -field <b>CreateTime</b>

<dd>
<p>A 64-bit integer that specifies the system time when the health packet was created for this multi-path disk.</p>
</dd>

### -field <b>PathFailures</b>

<dd>
<p>A 64-bit integer that specifies the total number of path failures for this multi-path disk.</p>
</dd>

### -field <b>FailTime</b>

<dd>
<p>A 64-bit integer that specifies the system time when this multi-path disk went offline or failed.</p>
</dd>

### -field <b>DeviceOffline</b>

<dd>
<p>A Boolean field that indicates whether the multi-path disk is offline or has failed.</p>
</dd>

### -field <b>NumberReadsWrap</b>

<dd>
<p>An unsigned character field that specifies the total number of times that the <i>NumberReads</i> parameter has rolled around to zero.</p>
</dd>

### -field <b>NumberWritesWrap</b>

<dd>
<p>An unsigned character field that specifies the total number of times the <i>NumberWrites</i> parameter has rolled around to zero.</p>
</dd>

### -field <b>NumberBytesReadWrap</b>

<dd>
<p>An unsigned character field that specifies the total number of times that the <i>NumberBytesRead</i> parameter has rolled around to zero.</p>
</dd>

### -field <b>NumberBytesWrittenWrap</b>

<dd>
<p>An unsigned character field that specifies the total number of times that the <i>NumberBytesWritten</i> parameter has rolled around to zero.</p>
</dd>

### -field <b>Pad</b>

<dd>
<p>Should be zero.</p>
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
<dt>Mpiowmi.h (include Mpiowmi.h)</dt>
</dl>
</td>
</tr>
</table>