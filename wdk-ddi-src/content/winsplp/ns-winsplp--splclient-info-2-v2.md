---
UID: NS.winsplp._SPLCLIENT_INFO_2_V2
title: SPLCLIENT_INFO_2_V2
author: windows-driver-content
description: TBD.
old-location: print\splclient_info_2_winxp.htm
ms.assetid: 48BD760E-6017-49B2-854F-7F48671974F3
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: print
req.header: winsplp.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: SPLCLIENT_INFO_2_WINXP
req.alt-loc: Winsplp.h
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
ms.keywords: SPLCLIENT_INFO_2_V2, SPLCLIENT_INFO_2_WINXP
req.iface: 
req.product: Windows 10 or later.
---

# SPLCLIENT_INFO_2_V2 structure



## -description
<p>TBD</p>


## -syntax

````
typedef struct _SPLCLIENT_INFO_2_V2 {
#ifdef _WIN64
  DWORD64  hSplPrinter;
#else 
  DWORD32  hSplPrinter;
#endif 
} SPLCLIENT_INFO_2_WINXP;
````


## -struct-fields
<dl>

### -field <b>hSplPrinter</b>

<dd>
<p>Specifies the server-side handle to be used for direct calls.</p>
</dd>

### -field <b>hSplPrinter</b>

<dd>
<p>Specifies the server-side handle to be used for direct calls.</p>
</dd>
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
<dt>Winsplp.h</dt>
</dl>
</td>
</tr>
</table>