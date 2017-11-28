---
UID: NS.1394._CONFIG_ROM
title: CONFIG_ROM
author: windows-driver-content
description: The CONFIG_ROM structure is used to contain the first 24 bytes of an IEEE 1394 device's configuration ROM.
old-location: ieee\config_rom.htm
old-project: IEEE
ms.assetid: 0ab96bc2-a89f-42cf-9ee2-020b47dff4cf
ms.author: windowsdriverdev
ms.date: 10/23/2017
ms.keywords: CONFIG_ROM, CONFIG_ROM, *PCONFIG_ROM
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: 1394.h
req.include-header: 1394.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: CONFIG_ROM
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

# CONFIG_ROM structure



## -description
<p>The CONFIG_ROM structure is used to contain the first 24 bytes of an IEEE 1394 device's configuration ROM.</p>


## -syntax

````
typedef struct _CONFIG_ROM {
  ULONG CR_Info;
  ULONG CR_Signiture;
  ULONG CR_BusInfoBlockCaps;
  ULONG CR_Node_UniqueID[2];
  ULONG CR_Root_Info;
} CONFIG_ROM, *PCONFIG_ROM;
````


## -struct-fields
<dl>

### -field <b>CR_Info</b>

<dd>
<p>Specifies the first 4 bytes of the configuration ROM. </p>
</dd>

### -field <b>CR_Signiture</b>

<dd>
<p>Specifies a signature that will be the same for all 1394 devices.</p>
</dd>

### -field <b>CR_BusInfoBlockCaps</b>

<dd>
<p>Specifies the bus capabilities of the device.</p>
</dd>

### -field <b>CR_Node_UniqueID</b>

<dd>
<p>Specifies the node's 64-bit vendor-assigned unique ID.</p>
</dd>

### -field <b>CR_Root_Info</b>

<dd>
<p>Specifies the first 4 bytes of the root directory information.</p>
</dd>
</dl>

## -remarks
<p>See the <a href="http://go.microsoft.com/fwlink/p/?linkid=8729">IEEE 1394 Trade Association specification</a> website for more details about the layout of the standard configuration ROM.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>1394.h (include 1394.h)</dt>
</dl>
</td>
</tr>
</table>