---
UID: NS.hbapiwmi._SM_GetBindingCapability_OUT
title: SM_GetBindingCapability_OUT
author: windows-driver-content
description: The SM_GetBindingCapability_OUT structure is used to receive output parameters from the SM_GetBindingCapability method.
old-location: storage\sm_getbindingcapability_out.htm
ms.assetid: 7dfa36be-ab05-478d-b47a-783e599545bf
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
req.alt-api: SM_GetBindingCapability_OUT
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
ms.keywords: SM_GetBindingCapability_OUT, SM_GetBindingCapability_OUT, *PSM_GetBindingCapability_OUT
req.iface: 
---

# SM_GetBindingCapability_OUT structure



## -description
<p>The SM_GetBindingCapability_OUT structure is used to receive output parameters from the SM_GetBindingCapability method.</p>


## -syntax

````
typedef struct _SM_GetBindingCapability_OUT {
  ULONG HBAStatus;
  ULONG Flags;
} SM_GetBindingCapability_OUT, *PSM_GetBindingCapability_OUT;
````


## -struct-fields
<dl>

### -field <b>HBAStatus</b>

<dd>
<p>The status of the operation. For a list of allowed values and their descriptions, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff557233">HBA_STATUS</a>.</p>
</dd>

### -field <b>Flags</b>

<dd>
<p>The HBA_BIND_CAPABILITY binding capabilities.</p>
</dd>
</dl>

## -remarks
<p>The WMI tool suite generates a declaration of the SM_GetBindingCapability_OUT structure in <i>Hbapiwmi.h</i> when it compiles the MS_SM_TargetInformationMethods WMI class.</p>

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