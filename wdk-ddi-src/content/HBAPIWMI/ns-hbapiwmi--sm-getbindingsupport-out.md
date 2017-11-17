---
UID: NS.hbapiwmi._SM_GetBindingSupport_OUT
title: SM_GetBindingSupport_OUT
author: windows-driver-content
description: The SM_GetBindingSupport_OUT structure is used to receive output parameters from the SM_GetBindingSupport method.
old-location: storage\sm_getbindingsupport_out.htm
ms.assetid: 4f45e2ad-19f9-4308-8d63-edf066545e07
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
req.alt-api: SM_GetBindingSupport_OUT
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
ms.keywords: SM_GetBindingSupport_OUT, SM_GetBindingSupport_OUT, *PSM_GetBindingSupport_OUT
req.iface: 
---

# SM_GetBindingSupport_OUT structure



## -description
<p>The SM_GetBindingSupport_OUT structure is used to receive output parameters from the SM_GetBindingSupport method.</p>


## -syntax

````
typedef struct _SM_GetBindingSupport_OUT {
  ULONG HBAStatus;
  ULONG Flags;
} SM_GetBindingSupport_OUT, *PSM_GetBindingSupport_OUT;
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
<p>The WMI tool suite generates a declaration of the SM_GetBindingSupport_OUT structure in <i>Hbapiwmi.h</i> when it compiles the MS_SM_TargetInformationMethods WMI class.</p>

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