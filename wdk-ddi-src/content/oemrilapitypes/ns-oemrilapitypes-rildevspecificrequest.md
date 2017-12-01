---
UID: NS.oemrilapitypes.RILDEVSPECIFICREQUEST
title: RILDEVSPECIFICREQUEST
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rildevspecificrequest.htm
old-project: netvista
ms.assetid: 36e2ae4b-cc2f-4980-95fe-25a38a1c07b1
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: RILDEVSPECIFICREQUEST, RILDEVSPECIFICREQUEST, *LPRILDEVSPECIFICREQUEST
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: oemrilapitypes.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RILDEVSPECIFICREQUEST
req.alt-loc: oemrilapitypes.h
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
req.iface: 
---

# RILDEVSPECIFICREQUEST structure



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.</p>


## -syntax

````
typedef struct _RILDEVSPECIFICREQUEST {
  DWORD   dwCmdId;
  DWORD   dwSize;
  BYTE [] params;
} RILDEVSPECIFICREQUEST, *LPRILDEVSPECIFICREQUEST;
````


## -struct-fields
<dl>

### -field <b>dwCmdId</b>

<dd></dd>

### -field <b>dwSize</b>

<dd></dd>

### -field <b>params</b>

<dd></dd>
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
<dt>Oemrilapitypes.h</dt>
</dl>
</td>
</tr>
</table>