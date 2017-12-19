---
UID: NS.NTDDRILAPITYPES.RILEXECUTORCONFIG
title: RILEXECUTORCONFIG
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilexecutorconfig.htm
old-project: NetVista
ms.assetid: d53c3df2-fd75-4008-a740-0afa293e36eb
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: RILEXECUTORCONFIG, *LPRILEXECUTORCONFIG, RILEXECUTORCONFIG, LPRILEXECUTORCONFIG
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntddrilapitypes.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RILEXECUTORCONFIG
req.alt-loc: ntddrilapitypes.h
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

# RILEXECUTORCONFIG structure



## -description
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.



## -syntax

````
typedef struct _RILEXECUTORCONFIG {
  DWORD        cbSize;
  DWORD        dwFlags;
  DWORD        dwNumApps;
  HUICCAPP [2] lphUiccApps;
} RILEXECUTORCONFIG, RILEXECUTORCONFIG;
````


## -struct-fields

### -field cbSize


### -field dwFlags


### -field dwNumApps


### -field lphUiccApps


## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Ntddrilapitypes.h</dt>
</dl>
</td>
</tr>
</table>