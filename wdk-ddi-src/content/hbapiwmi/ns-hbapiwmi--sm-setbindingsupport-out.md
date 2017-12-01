---
UID: NS.hbapiwmi._SM_SetBindingSupport_OUT
title: SM_SetBindingSupport_OUT
author: windows-driver-content
description: The SM_SetBindingSupport_OUT structure is used to receive output parameters from the SM_SetBindingSupport method.
old-location: storage\sm_setbindingsupport_out.htm
old-project: storage
ms.assetid: b0902b79-25ee-45e6-944e-de9e69ce43ec
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: SM_SetBindingSupport_OUT, SM_SetBindingSupport_OUT, *PSM_SetBindingSupport_OUT
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
req.alt-api: SM_SetBindingSupport_OUT
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

# SM_SetBindingSupport_OUT structure



## -description
<p>The SM_SetBindingSupport_OUT structure is used to receive output parameters from the SM_SetBindingSupport method.</p>


## -syntax

````
typedef struct _SM_SetBindingSupport_OUT {
  ULONG HBAStatus;
} SM_SetBindingSupport_OUT, *PSM_SetBindingSupport_OUT;
````


## -struct-fields
<dl>

### -field <b>HBAStatus</b>

<dd>
<p>The status of the operation. For a list of allowed values and their descriptions, see <a href="storage.hba_status">HBA_STATUS</a>.</p>
</dd>
</dl>

## -remarks
<p>The WMI tool suite generates a declaration of the SM_SetBindingSupport_OUT structure in <i>Hbapiwmi.h</i> when it compiles the MS_SM_TargetInformationMethods WMI class.</p>

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