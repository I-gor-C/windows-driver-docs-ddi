---
UID: NS.ntddrilapitypes.RILEXECUTORRFSTATE
title: RILEXECUTORRFSTATE
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilexecutorrfstate.htm
old-project: netvista
ms.assetid: b56f71c3-3c24-4f6b-ba50-203e17374c81
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: RILEXECUTORRFSTATE, RILEXECUTORRFSTATE, *LPRILEXECUTORRFSTATE
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
req.alt-api: RILEXECUTORRFSTATE
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
req.iface: 
---

# RILEXECUTORRFSTATE structure



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.</p>


## -syntax

````
typedef struct _RILEXECUTORRFSTATE {
  DWORD  cbSize;
  DWORD  dwParams;
  DWORD  dwExecutor;
  BOOL   fExecutorRFState;
} RILEXECUTORRFSTATE, RILEXECUTORRFSTATE;
````


## -struct-fields
<dl>

### -field <b>cbSize</b>

<dd></dd>

### -field <b>dwParams</b>

<dd></dd>

### -field <b>dwExecutor</b>

<dd></dd>

### -field <b>fExecutorRFState</b>

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
<dt>Ntddrilapitypes.h</dt>
</dl>
</td>
</tr>
</table>