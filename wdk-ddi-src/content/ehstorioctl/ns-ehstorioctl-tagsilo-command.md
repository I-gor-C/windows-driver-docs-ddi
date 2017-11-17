---
UID: NS.ehstorioctl.tagSILO_COMMAND
title: tagSILO_COMMAND
author: windows-driver-content
description: This structure describes a storage silo driver command.
old-location: storage\silo_command.htm
ms.assetid: 4d40ac4b-9aca-4be6-8d4f-db94c3daf4e8
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: Storage
req.header: ehstorioctl.h
req.include-header: EhStorIoctl.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: SILO_COMMAND
req.alt-loc: EhStorIoctl.h
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
ms.keywords: tagSILO_COMMAND, SILO_COMMAND, *PSILO_COMMAND
req.iface: 
---

# tagSILO_COMMAND structure



## -description
<p>This structure describes a storage silo driver command.</p>


## -syntax

````
typedef struct tagSILO_COMMAND {
  UCHAR SiloIndex;
  UCHAR Command;
  ULONG cbCommandBuffer;
  UCHAR rgbCommandBuffer[ANYSIZE_ARRAY];
} SILO_COMMAND, *PSILO_COMMAND;
````


## -struct-fields
<dl>

### -field <b>SiloIndex</b>

<dd></dd>

### -field <b>Command</b>

<dd>
<p>This member contains the 1667 command value.</p>
</dd>

### -field <b>cbCommandBuffer</b>

<dd>
<p>This member contains the size of the 1667 command buffer.</p>
</dd>

### -field <b>rgbCommandBuffer</b>

<dd></dd>
</dl>

## -remarks
<p>Together, <b>cbCommandBufferSize</b> and <b>rgbCommandBuffer</b> members indicate the raw data payload for the silo command, and are sent as-is to the device. The structure of the data in this buffer is silo-dependent. The structure is assumed to be shared knowledge between the client issuing this IOCTL and the device firmware implementation of this particular silo.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>EhStorIoctl.h (include EhStorIoctl.h)</dt>
</dl>
</td>
</tr>
</table>