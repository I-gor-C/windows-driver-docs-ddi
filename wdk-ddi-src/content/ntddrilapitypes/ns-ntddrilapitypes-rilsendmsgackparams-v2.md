---
UID: NS.ntddrilapitypes.RILSENDMSGACKPARAMS_V2
title: RILSENDMSGACKPARAMS_V2
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilsendmsgackparams_v2.htm
old-project: netvista
ms.assetid: 3c05c1a0-339e-447f-b0df-18303ee63f98
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: RILSENDMSGACKPARAMS_V2, RILSENDMSGACKPARAMS_V2, RILSENDMSGACKPARAMS, *LPRILSENDMSGACKPARAMS
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
req.alt-api: RILSENDMSGACKPARAMS_V2
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

# RILSENDMSGACKPARAMS_V2 structure



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.</p>


## -syntax

````
typedef struct _RILSENDMSGACKPARAMS_V2 {
  DWORD            cbSize;
  DWORD            dwExecutor;
  HUICCAPP         hUiccApp;
  DWORD            dwAckID;
  RILMSGACKSTATUS  dwMsgStatus;
  RILSMSFORMAT     dwSmsFormat;
  DWORD            dwOptions;
} RILSENDMSGACKPARAMS_V2, RILSENDMSGACKPARAMS_V2;
````


## -struct-fields
<dl>

### -field cbSize

<dd></dd>

### -field dwExecutor

<dd></dd>

### -field hUiccApp

<dd></dd>

### -field dwAckID

<dd></dd>

### -field dwMsgStatus

<dd></dd>

### -field dwSmsFormat

<dd></dd>

### -field dwOptions

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