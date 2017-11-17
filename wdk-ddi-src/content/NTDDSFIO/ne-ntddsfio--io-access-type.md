---
UID: NE.ntddsfio._IO_ACCESS_TYPE
title: IO_ACCESS_TYPE
author: windows-driver-content
description: Defines the access rights for Scheduled File I/O (SFIO).
old-location: kernel\io_access_type.htm
ms.assetid: 9ABFF1E8-50B8-4B59-964D-BA79AB63BFCE
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: kernel
req.header: ntddsfio.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IO_ACCESS_TYPE
req.alt-loc: Ntddsfio.h
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
ms.keywords: SERIALPERF_STATS, SERIALPERF_STATS, *PSERIALPERF_STATS
req.iface: 
---

# IO_ACCESS_TYPE enumeration



## -description
<p>Defines the access rights for Scheduled File I/O (SFIO).</p>


## -syntax

````
typedef enum _IO_ACCESS_TYPE { 
  ReadAccess,
  WriteAccess,
  ModifyAccess
} IO_ACCESS_TYPE;
````


## -enum-fields
<dl>

### -field <a id="ReadAccess"></a><a id="readaccess"></a><a id="READACCESS"></a><b>ReadAccess</b>

<dd>
<p>Indicates that the input/output will be comprised solely of reads.</p>
</dd>

### -field <a id="WriteAccess"></a><a id="writeaccess"></a><a id="WRITEACCESS"></a><b>WriteAccess</b>

<dd>
<p>Indicates that the input/output will be comprised solely of writes.</p>
</dd>

### -field <a id="ModifyAccess"></a><a id="modifyaccess"></a><a id="MODIFYACCESS"></a><b>ModifyAccess</b>

<dd>
<p>Indicates that the input/output will be comprised of reads and writes.</p>
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
<dt>Ntddsfio.h</dt>
</dl>
</td>
</tr>
</table>