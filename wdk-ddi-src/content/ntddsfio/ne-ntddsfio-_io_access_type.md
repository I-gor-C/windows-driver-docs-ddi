---
UID: NE.ntddsfio._IO_ACCESS_TYPE
title: _IO_ACCESS_TYPE
author: windows-driver-content
description: Defines the access rights for Scheduled File I/O (SFIO).
old-location: kernel\io_access_type.htm
old-project: kernel
ms.assetid: 9ABFF1E8-50B8-4B59-964D-BA79AB63BFCE
ms.author: windowsdriverdev
ms.date: 12/7/2017
ms.keywords: _IO_ACCESS_TYPE, IO_ACCESS_TYPE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
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
---

# _IO_ACCESS_TYPE enumeration



## -description
Defines the access rights for Scheduled File I/O (SFIO).



## -syntax

````
typedef enum _IO_ACCESS_TYPE { 
  ReadAccess,
  WriteAccess,
  ModifyAccess
} IO_ACCESS_TYPE;
````


## -enum-fields

### -field ReadAccess

Indicates that the input/output will be comprised solely of reads.


### -field WriteAccess

Indicates that the input/output will be comprised solely of writes.


### -field ModifyAccess

Indicates that the input/output will be comprised of reads and writes.


## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Ntddsfio.h</dt>
</dl>
</td>
</tr>
</table>