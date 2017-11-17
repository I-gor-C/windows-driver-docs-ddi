---
UID: NS.irb._IDE_LBA_RANGE
title: IDE_LBA_RANGE
author: windows-driver-content
description: The IDE_LBA_RANGE structure is used by the port driver to provide the miniport driver with a range of logical blocks.Note  The ATA port driver and ATA miniport driver models may be altered or unavailable in the future.
old-location: storage\ide_lba_range.htm
ms.assetid: 2d823d9c-7328-44e2-9ba2-22967471ef68
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: Storage
req.header: irb.h
req.include-header: Irb.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IDE_LBA_RANGE
req.alt-loc: irb.h
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
ms.keywords: IDE_LBA_RANGE, IDE_LBA_RANGE, *PIDE_LBA_RANGE
req.iface: 
---

# IDE_LBA_RANGE structure



## -description
<p>The IDE_LBA_RANGE structure is used by the port driver to provide the miniport driver with a range of logical blocks.</p>


## -syntax

````
typedef struct _IDE_LBA_RANGE {
  ULONGLONG StartSector  :48;
  ULONGLONG SectorCount  :16;
} IDE_LBA_RANGE, *PIDE_LBA_RANGE;
````


## -struct-fields
<dl>

### -field <b>StartSector</b>

<dd>
<p>Contains the starting sector of the LBA range.</p>
</dd>

### -field <b>SectorCount</b>

<dd>
<p>Contains the sector count of the LBA range.</p>
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
<dt>Irb.h (include Irb.h)</dt>
</dl>
</td>
</tr>
</table>