---
UID: NS.RILAPITYPES.RILIMSFAILURE~R1
title: RILIMSFAILURE
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilimsfailure_2.htm
old-project: netvista
ms.assetid: f9c25e60-8f9e-491f-898a-c79e8790193e
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: RILIMSFAILURE, RILIMSFAILURE, *LPRILIMSFAILURE
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
req.alt-api: RILIMSFAILURE
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

# RILIMSFAILURE structure



## -description
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. 


## -syntax

````
typedef struct _RILIMSFAILURE {
  DWORD                                       cbSize;
  DWORD                                       dwParams;
  DWORD                                       dwExecutor;
  RILIMSFAILUREMESSAGETYPE                    dwMessageType;
  DWORD                                       dwMessageSubType;
  DWORD                                       dwErrorCode;
  WCHAR [MAXLENGTH_SIP_FAILURE_REASON_STRING] wszErrorString;
} RILIMSFAILURE, RILIMSFAILURE;
````


## -struct-fields

### -field cbSize


### -field dwParams


### -field dwExecutor


### -field dwMessageType


### -field dwMessageSubType


### -field dwErrorCode


### -field wszErrorString


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