---
UID: NS.1394._IRB_REQ_GET_CONFIG_ROM
title: IRB_REQ_GET_CONFIG_ROM
author: windows-driver-content
description: This structure contains the fields necessary for the bus driver to carry out a GetConfigRom request.
old-location: ieee\irb_req_get_config_rom.htm
old-project: IEEE
ms.assetid: 9C4EC9CA-3B7F-4611-BB96-A86C0FEDDF25
ms.author: windowsdriverdev
ms.date: 11/29/2017
ms.keywords: IRB_REQ_GET_CONFIG_ROM, IRB_REQ_GET_CONFIG_ROM
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
req.alt-api: IRB_REQ_GET_CONFIG_ROM
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

# IRB_REQ_GET_CONFIG_ROM structure



## -description
<p>This structure contains the fields necessary for the bus driver to carry out a GetConfigRom request.</p>


## -syntax

````
typedef struct _IRB_REQ_GET_CONFIG_ROM {
  ULONG GenerationCount;
  PCROM ConfigRom;
  ULONG UnitDirectoryIndex;
  ULONG UnitDependentDirectoryIndex;
  ULONG VendorLeafIndex;
  ULONG ModelLeafIndex;
} IRB_REQ_GET_CONFIG_ROM;
````


## -struct-fields
<dl>

### -field GenerationCount

<dd>
<p>Receives the generation of the bus for which the contents of this configuration ROM was retrieved.</p>
</dd>

### -field ConfigRom

<dd>
<p>Receives a pointer to a <b>ConfigRom</b> object.</p>
</dd>

### -field UnitDirectoryIndex

<dd>
<p>Receives the index to the node's unit directory in its configuration ROM. This is an index to the <b>Entries</b> array in the <b>u.GetConfigRom.ConfigRom</b> structure.</p>
</dd>

### -field UnitDependentDirectoryIndex

<dd>
<p>Receives the index to the node's unit dependent directory in its configuration ROM. This is an index to the <b>Entries</b> array in the <b>u.GetConfigRom.ConfigRom</b> structure.</p>
</dd>

### -field VendorLeafIndex

<dd>
<p>Receives the index to the node's vendor textual leaf in the configuration ROM. This is an index to the <b>Entries</b> array in the <b>u.GetConfigRom.ConfigRom</b> structure.</p>
</dd>

### -field ModelLeafIndex

<dd>
<p>Receives the index to the node's model textual leaf in the configuration ROM. This is an index to the <b>Entries</b> array in the <b>u.GetConfigRom.ConfigRom</b> structure.</p>
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