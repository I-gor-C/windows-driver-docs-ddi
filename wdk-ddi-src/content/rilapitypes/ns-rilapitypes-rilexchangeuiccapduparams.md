---
UID: NS:rilapitypes.RILEXCHANGEUICCAPDUPARAMS
title: RILEXCHANGEUICCAPDUPARAMS
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilexchangeuiccapduparams_2.htm
old-project: netvista
ms.assetid: 0bbdfb04-70a9-4ded-9947-6f082940cfa0
ms.author: windowsdriverdev
ms.date: 1/8/2018
ms.keywords: RILEXCHANGEUICCAPDUPARAMS, *LPRILEXCHANGEUICCAPDUPARAMS, RILEXCHANGEUICCAPDUPARAMS
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
req.alt-api: RILEXCHANGEUICCAPDUPARAMS
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
req.typenames: *LPRILEXCHANGEUICCAPDUPARAMS, RILEXCHANGEUICCAPDUPARAMS
req.product: Windows 10 or later.
---

# RILEXCHANGEUICCAPDUPARAMS structure



## -description
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. 



## -syntax

````
typedef struct _RILEXCHANGEUICCAPDUPARAMS {
  DWORD    dwSlotIndex;
  DWORD    dwChannelId;
  DWORD    dwAPDULength;
  BYTE [1] bAPDU;
} RILEXCHANGEUICCAPDUPARAMS, RILEXCHANGEUICCAPDUPARAMS;
````


## -struct-fields

### -field dwSlotIndex


### -field dwChannelId


### -field dwAPDULength


### -field bAPDU


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