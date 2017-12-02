---
UID: NS.pcivirt._SRIOV_MITIGATED_RANGES_INPUT
title: SRIOV_MITIGATED_RANGES_INPUT
author: windows-driver-content
description: This structure is the input buffer in the IOCTL_SRIOV_QUERY_MITIGATED_RANGES request to get the specific ranges on which intercepts must be placed.
old-location: pci\sriov_mitigated_ranges_input.htm
old-project: PCI
ms.assetid: 40b81630-997f-4427-8d02-5004de6fc943
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: SRIOV_MITIGATED_RANGES_INPUT, SRIOV_MITIGATED_RANGES_INPUT, *PSRIOV_MITIGATED_RANGES_INPUT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: pcivirt.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: SRIOV_MITIGATED_RANGES_INPUT
req.alt-loc: pcivirt.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
---

# SRIOV_MITIGATED_RANGES_INPUT structure



## -description
<p>This structure is the input buffer in the <a href="buses.ioctl_sriov_query_mitigated_ranges">IOCTL_SRIOV_QUERY_MITIGATED_RANGES</a> request to get the specific ranges on which intercepts must be placed.</p>


## -syntax

````
typedef struct _SRIOV_MITIGATED_RANGES_INPUT {
  USHORT  VfIndex;
  UCHAR   BarNumber;
} SRIOV_MITIGATED_RANGES_INPUT, SRIOV_MITIGATED_RANGES_INPUT;
````


## -struct-fields
<dl>

### -field VfIndex

<dd>
<p>Zero-based index of the virtual function from the first virtual function exposed by this physical function.</p>
</dd>

### -field BarNumber

<dd>
<p>The number of BAR of the ranges of memory-mapped I/O space.</p>
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
<dt>Pcivirt.h</dt>
</dl>
</td>
</tr>
</table>