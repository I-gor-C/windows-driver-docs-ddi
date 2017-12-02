---
UID: NS.pcivirt._SRIOV_MITIGATED_RANGE_UPDATE_OUTPUT
title: SRIOV_MITIGATED_RANGE_UPDATE_OUTPUT
author: windows-driver-content
description: This structures is the output buffer received by the IOCTL_SRIOV_MITIGATED_RANGE_UPDATE request that indicates the virtual function (VF) whose memory-mapped I/O space was mitigated.
old-location: pci\sriov_mitigated_range_update_output.htm
old-project: PCI
ms.assetid: bd72ac9a-2985-4f2d-8b72-4039c9d3f896
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: SRIOV_MITIGATED_RANGE_UPDATE_OUTPUT, SRIOV_MITIGATED_RANGE_UPDATE_OUTPUT, *PSRIOV_MITIGATED_RANGE_UPDATE_OUTPUT
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
req.alt-api: SRIOV_MITIGATED_RANGE_UPDATE_OUTPUT
req.alt-loc: Pcivirt.h
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

# SRIOV_MITIGATED_RANGE_UPDATE_OUTPUT structure



## -description
<p>This structures is the output buffer received by the <a href="buses.ioctl_sriov_mitigated_range_update">IOCTL_SRIOV_MITIGATED_RANGE_UPDATE</a> request that indicates the virtual function (VF) whose memory-mapped I/O space
 was mitigated.</p>


## -syntax

````
typedef struct _SRIOV_MITIGATED_RANGE_UPDATE_OUTPUT {
  USHORT  VfIndex;
} SRIOV_MITIGATED_RANGE_UPDATE_OUTPUT, SRIOV_MITIGATED_RANGE_UPDATE_OUTPUT;
````


## -struct-fields
<dl>

### -field VfIndex

<dd>
<p>Zero-based index of the virtual function from the first virtual function exposed by this physical function.</p>
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