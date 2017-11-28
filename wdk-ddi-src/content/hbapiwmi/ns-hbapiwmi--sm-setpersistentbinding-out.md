---
UID: NS.hbapiwmi._SM_SetPersistentBinding_OUT
title: SM_SetPersistentBinding_OUT
author: windows-driver-content
description: The SM_SetPersistentBinding_OUT structure is used to receive output parameters from the SM_SetPersistentBinding method.
old-location: storage\sm_setpersistentbinding_out.htm
old-project: storage
ms.assetid: 42d451ab-51dc-4b59-b6e9-42e02ec1b500
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: SM_SetPersistentBinding_OUT, SM_SetPersistentBinding_OUT, *PSM_SetPersistentBinding_OUT
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
req.alt-api: SM_SetPersistentBinding_OUT
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

# SM_SetPersistentBinding_OUT structure



## -description
<p>The SM_SetPersistentBinding_OUT structure is used to receive output parameters from the SM_SetPersistentBinding method.</p>


## -syntax

````
typedef struct _SM_SetPersistentBinding_OUT {
  ULONG HBAStatus;
  ULONG OutStatusCount;
  ULONG EntryStatus[1];
} SM_SetPersistentBinding_OUT, *PSM_SetPersistentBinding_OUT;
````


## -struct-fields
<dl>

### -field <b>HBAStatus</b>

<dd>
<p>The status of the operation. For a list of allowed values and their descriptions, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff557233">HBA_STATUS</a>.</p>
</dd>

### -field <b>OutStatusCount</b>

<dd>
<p>The number of entries.</p>
</dd>

### -field <b>EntryStatus</b>

<dd>
<p>The status of each entry.</p>
</dd>
</dl>

## -remarks
<p>The WMI tool suite generates a declaration of the SM__SetPersistentBinding_OUT structure in <i>Hbapiwmi.h</i> when it compiles the MS_SM_TargetInformationMethods WMI class.</p>

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