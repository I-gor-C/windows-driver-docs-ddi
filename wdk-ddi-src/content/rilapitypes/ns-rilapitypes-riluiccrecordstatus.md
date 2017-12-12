---
UID: NS.RILAPITYPES.RILUICCRECORDSTATUS
title: RILUICCRECORDSTATUS
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\riluiccrecordstatus_2.htm
old-project: netvista
ms.assetid: 5f6ff5b1-cd13-4bf6-b4ef-e9b6f4fd54e0
ms.author: windowsdriverdev
ms.date: 12/8/2017
ms.keywords: RILUICCRECORDSTATUS, *LPRILUICCRECORDSTATUS, RILUICCRECORDSTATUS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: rilapitypes.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RILUICCRECORDSTATUS
req.alt-loc: rilapitypes.h
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
req.product: Windows 10 or later.
---

# RILUICCRECORDSTATUS structure



## -description
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. 



## -syntax

````
typedef struct _RILUICCRECORDSTATUS {
  DWORD                                        cbSize;
  DWORD                                        dwParams;
  RILUICCRECORDTYPE                            dwRecordType;
  DWORD                                        dwItemCount;
  DWORD                                        dwSize;
  RILUICCFILELOCKSTATUS [MAXNUM_EFACCESSTYPES] fileLockStatus;
} RILUICCRECORDSTATUS, RILUICCRECORDSTATUS;
````


## -struct-fields

### -field cbSize


### -field dwParams


### -field dwRecordType


### -field dwItemCount


### -field dwSize


### -field fileLockStatus


## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Rilapitypes.h</dt>
</dl>
</td>
</tr>
</table>