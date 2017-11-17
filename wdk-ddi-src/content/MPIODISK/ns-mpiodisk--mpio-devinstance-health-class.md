---
UID: NS.mpiodisk._MPIO_DEVINSTANCE_HEALTH_CLASS
title: MPIO_DEVINSTANCE_HEALTH_CLASS
author: windows-driver-content
description: The MPIO_DEVINSTANCE_HEALTH_CLASS structure holds the health information for a instance of a device exposed through the specified path identifiers.
old-location: storage\mpio_devinstance_health_class.htm
ms.assetid: 6d0afab5-4aba-4ebc-a864-85c83cf464d0
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: Storage
req.header: mpiodisk.h
req.include-header: Mpiowmi.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: MPIO_DEVINSTANCE_HEALTH_CLASS
req.alt-loc: mpiodisk.h
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
ms.keywords: MPIO_DEVINSTANCE_HEALTH_CLASS, MPIO_DEVINSTANCE_HEALTH_CLASS, *PMPIO_DEVINSTANCE_HEALTH_CLASS
req.iface: 
---

# MPIO_DEVINSTANCE_HEALTH_CLASS structure



## -description
<p>The MPIO_DEVINSTANCE_HEALTH_CLASS structure holds the health information for a instance of a device exposed through the specified path identifiers.</p>


## -syntax

````
typedef struct _MPIO_DEVINSTANCE_HEALTH_CLASS {
  ULONGLONG PathId;
  ULONGLONG NumberReads;
  ULONGLONG NumberWrites;
  ULONGLONG NumberBytesRead;
  ULONGLONG NumberBytesWritten;
  ULONGLONG NumberRetries;
  ULONGLONG NumberIoErrors;
  ULONGLONG CreateTime;
  ULONGLONG FailTime;
  BOOLEAN   DeviceOffline;
  UCHAR     NumberReadsWrap;
  UCHAR     NumberWritesWrap;
  UCHAR     NumberBytesReadWrap;
  UCHAR     NumberBytesWrittenWrap;
  UCHAR     Pad[3];
} MPIO_DEVINSTANCE_HEALTH_CLASS, *PMPIO_DEVINSTANCE_HEALTH_CLASS;
````


## -struct-fields
<dl>

### -field <b>PathId</b>

<dd>
<p>An unsigned 64-bitfield that returns the path identifier that is associated with this instance of a multi-path disk.</p>
</dd>

### -field <b>NumberReads</b>

<dd>
<p>An unsigned 64-bitfield that specifies the number of read requests that are serviced by the specified path identifier.</p>
</dd>

### -field <b>NumberWrites</b>

<dd>
<p>An unsigned 64-bitfield that specifies the number of write requests that are serviced by the specified path identifier</p>
</dd>

### -field <b>NumberBytesRead</b>

<dd>
<p>An unsigned 64-bitfield that specifies the total number of bytes that are read through the specified path identifier</p>
</dd>

### -field <b>NumberBytesWritten</b>

<dd>
<p>An unsigned 64-bitfield that specifies the total number of bytes that are written through the specified path identifier.</p>
</dd>

### -field <b>NumberRetries</b>

<dd>
<p>An unsigned 64-bitfield that specifies the total number of retries through the specified path identifier.</p>
</dd>

### -field <b>NumberIoErrors</b>

<dd>
<p>An unsigned 64-bitfield that specifies the total number of I/O errors that are encountered through the specified path identifier.</p>
</dd>

### -field <b>CreateTime</b>

<dd>
<p>A 64-bit integer that specifies the system time when this instance was created and exposed.</p>
</dd>

### -field <b>FailTime</b>

<dd>
<p>A 64-bit integer that specifies the system time when the path associated with this path ID was removed.</p>
</dd>

### -field <b>DeviceOffline</b>

<dd>
<p>A Boolean field that indicates whether the path associated with this path ID has been removed.</p>
</dd>

### -field <b>NumberReadsWrap</b>

<dd>
<p>An unsigned character field that specifies the total number of times the <i>NumberReads</i> parameter has rolled around to zero.</p>
</dd>

### -field <b>NumberWritesWrap</b>

<dd>
<p>An unsigned character field that specifies the total number of times the <i>NumberWrites</i> parameter has rolled around to zero.</p>
</dd>

### -field <b>NumberBytesReadWrap</b>

<dd>
<p>An unsigned character field that specifies the total number of times the <i>NumberBytesRead</i> parameter has rolled around to zero.</p>
</dd>

### -field <b>NumberBytesWrittenWrap</b>

<dd>
<p>An unsigned character field that specifies the total number of times the <i>NumberBytesWritten</i> parameter has rolled around to zero.</p>
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
<dt>Mpiodisk.h (include Mpiowmi.h)</dt>
</dl>
</td>
</tr>
</table>