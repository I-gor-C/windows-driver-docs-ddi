---
UID: NS.hbapiwmi._SM_AddTarget_OUT
title: SM_AddTarget_OUT
author: windows-driver-content
description: The SM_AddTarget_OUT structure is used to receive output parameters from the SM_AddTarget WMI method.
old-location: storage\sm_addtarget_out.htm
ms.assetid: ed4e58cb-6b32-454b-9538-f9f8aa68df4c
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: Storage
req.header: hbapiwmi.h
req.include-header: Hbapiwmi.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: SM_AddTarget_OUT
req.alt-loc: hbapiwmi.h
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
ms.keywords: SM_AddTarget_OUT, SM_AddTarget_OUT, *PSM_AddTarget_OUT
req.iface: 
---

# SM_AddTarget_OUT structure



## -description
<p>The SM_AddTarget_OUT structure is used to receive output parameters from the SM_AddTarget WMI method.</p>


## -syntax

````
typedef struct _SM_AddTarget_OUT {
  ULONG HBAStatus;
} SM_AddTarget_OUT, *PSM_AddTarget_OUT;
````


## -struct-fields
<dl>

### -field <b>HBAStatus</b>

<dd>
<p>The status of the operation. For a list of allowed values and their descriptions, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff557233">HBA_STATUS</a>.</p>
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
<dt>Hbapiwmi.h (include Hbapiwmi.h)</dt>
</dl>
</td>
</tr>
</table>