---
UID: NS.d3dkmddi._DXGK_QUERYPAGETABLELEVELDESCIN
title: DXGK_QUERYPAGETABLELEVELDESCIN
author: windows-driver-content
description: The DXGK_QUERYPAGETABLELEVELDESCIN structure is used to request page level descriptors from the Dxgkrnl Interface.
old-location: display\dxgk_querypagetableleveldescin.htm
ms.assetid: 1B13BBB1-4184-4166-A61F-CC266D0391BF
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: d3dkmddi.h
req.include-header: D3dkmddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGK_QUERYPAGETABLELEVELDESCIN
req.alt-loc: d3dkmddi.h
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
ms.keywords: DXGK_QUERYPAGETABLELEVELDESCIN, DXGK_QUERYPAGETABLELEVELDESCIN
req.iface: 
---

# DXGK_QUERYPAGETABLELEVELDESCIN structure



## -description
<p>The <b>DXGK_QUERYPAGETABLELEVELDESCIN</b> structure is used to request page level descriptors from the <a href="https://msdn.microsoft.com/library/windows/hardware/ff560940">Dxgkrnl Interface</a>.</p>


## -syntax

````
typedef struct _DXGK_QUERYPAGETABLELEVELDESCIN {
  WORD LevelIndex;
  WORD PhysicalAdapterIndex;
} DXGK_QUERYPAGETABLELEVELDESCIN;
````


## -struct-fields
<dl>

### -field <b>LevelIndex</b>

<dd>
<p>A zero-based physical adapter index (engine ordinal) for which the data is queried.</p>
</dd>

### -field <b>PhysicalAdapterIndex</b>

<dd>
<p>A zero-based page table level index for the information requested.</p>
</dd>
</dl>

## -remarks
<p>To get page table level descriptors Dxgkrnl calls <a href="https://msdn.microsoft.com/f2f4c54c-7413-48e5-a165-d71f35642b6c">DxgkDdiQueryAdapterInfo</a> with the following parameters:</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 10</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2016</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3dkmddi.h (include D3dkmddi.h)</dt>
</dl>
</td>
</tr>
</table>