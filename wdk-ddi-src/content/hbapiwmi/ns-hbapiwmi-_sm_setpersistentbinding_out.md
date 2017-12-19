---
UID: NS.HBAPIWMI._SM_SETPERSISTENTBINDING_OUT
title: _SM_SetPersistentBinding_OUT
author: windows-driver-content
description: The SM_SetPersistentBinding_OUT structure is used to receive output parameters from the SM_SetPersistentBinding method.
old-location: storage\sm_setpersistentbinding_out.htm
old-project: storage
ms.assetid: 42d451ab-51dc-4b59-b6e9-42e02ec1b500
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: _SM_SetPersistentBinding_OUT, SM_SetPersistentBinding_OUT, PSM_SetPersistentBinding_OUT, *PSM_SetPersistentBinding_OUT
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
---

# _SM_SetPersistentBinding_OUT structure



## -description
The SM_SetPersistentBinding_OUT structure is used to receive output parameters from the SM_SetPersistentBinding method.



## -syntax

````
typedef struct _SM_SetPersistentBinding_OUT {
  ULONG HBAStatus;
  ULONG OutStatusCount;
  ULONG EntryStatus[1];
} SM_SetPersistentBinding_OUT, *PSM_SetPersistentBinding_OUT;
````


## -struct-fields

### -field HBAStatus

The status of the operation. For a list of allowed values and their descriptions, see <a href="storage.hba_status">HBA_STATUS</a>.


### -field OutStatusCount

The number of entries.


### -field EntryStatus

The status of each entry.


## -remarks
The WMI tool suite generates a declaration of the SM__SetPersistentBinding_OUT structure in <i>Hbapiwmi.h</i> when it compiles the MS_SM_TargetInformationMethods WMI class.


## -requirements
<table>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Hbapiwmi.h (include Hbapiwmi.h)</dt>
</dl>
</td>
</tr>
</table>