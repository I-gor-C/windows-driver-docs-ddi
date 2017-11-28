---
UID: NS.hbapiwmi._SM_AddLink_OUT
title: SM_AddLink_OUT
author: windows-driver-content
description: The SM_AddLink_OUT structure is used to receive output parameters from the SM_AddLink WMI method.
old-location: storage\sm_addlink_out.htm
old-project: storage
ms.assetid: 1c69b8b0-fe73-4e13-be09-70b99e0e3f32
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: SM_AddLink_OUT, SM_AddLink_OUT, *PSM_AddLink_OUT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: hbapiwmi.h
req.include-header: Hbapiwmi.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: SM_AddLink_OUT
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
req.iface: 
---

# SM_AddLink_OUT structure



## -description
<p>The SM_AddLink_OUT structure is used to receive output parameters from the SM_AddLink WMI method.</p>


## -syntax

````
typedef struct _SM_AddLink_OUT {
  ULONG HBAStatus;
} SM_AddLink_OUT, *PSM_AddLink_OUT;
````


## -struct-fields
<dl>

### -field <b>HBAStatus</b>

<dd>
<p>A value associated with the WMI class qualifier <a href="https://msdn.microsoft.com/library/windows/hardware/ff557233">HBA_STATUS</a> that indicates the result of an HBA query operation.</p>
</dd>
</dl>

## -remarks
<p>The WMI tool suite generates a declaration of the SM_AddLink_OUT structure in <i>Hbapiwmi.h</i> when it compiles the MS_SM_EventControl WMI class.</p>

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