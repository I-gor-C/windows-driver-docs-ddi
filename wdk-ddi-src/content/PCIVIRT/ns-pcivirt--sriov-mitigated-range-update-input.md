---
UID: NS.pcivirt._SRIOV_MITIGATED_RANGE_UPDATE_INPUT
title: SRIOV_MITIGATED_RANGE_UPDATE_INPUT
author: windows-driver-content
description: This structure is used as an input buffer to the IOCTL_SRIOV_MITIGATED_RANGE_UPDATE request to indicate the virtual function (VF) whose memory-mapped I/O space that must be mitigated.
old-location: pci\sriov_mitigated_range_update_input.htm
ms.assetid: ae4936ac-9794-4854-81ec-2139b3ce4c3c
ms.author: windowsdriverdev
ms.date: 10/23/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: PCI
req.header: pcivirt.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: SRIOV_MITIGATED_RANGE_UPDATE_INPUT
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
ms.keywords: SRIOV_MITIGATED_RANGE_UPDATE_INPUT, SRIOV_MITIGATED_RANGE_UPDATE_INPUT, *PSRIOV_MITIGATED_RANGE_UPDATE_INPUT
req.iface: 
---

# SRIOV_MITIGATED_RANGE_UPDATE_INPUT structure



## -description
<p>This structure is used as an input buffer to the <a href="buses.ioctl_sriov_mitigated_range_update">IOCTL_SRIOV_MITIGATED_RANGE_UPDATE</a> request to indicate the virtual function (VF) whose memory-mapped I/O space that must be mitigated. </p>


## -syntax

````
typedef struct _SRIOV_MITIGATED_RANGE_UPDATE_INPUT {
  USHORT  VfIndex;
} SRIOV_MITIGATED_RANGE_UPDATE_INPUT, SRIOV_MITIGATED_RANGE_UPDATE_INPUT;
````


## -struct-fields
<dl>

### -field <b>VfIndex</b>

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