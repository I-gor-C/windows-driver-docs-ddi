---
UID: NS.NTDDRILAPITYPES.RILSENDDTMFPARAMS
title: RILSENDDTMFPARAMS
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilsenddtmfparams.htm
old-project: NetVista
ms.assetid: b08767f9-6b2d-4930-bd02-ebc89f2bdb7d
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: RILSENDDTMFPARAMS, LPRILSENDDTMFPARAMS, *LPRILSENDDTMFPARAMS, RILSENDDTMFPARAMS
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
req.alt-api: RILSENDDTMFPARAMS
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

# RILSENDDTMFPARAMS structure



## -description
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.



## -syntax

````
typedef struct _RILSENDDTMFPARAMS {
  DWORD      dwExecutor;
  char [256] szDTMF;
  DWORD      dwDigitOnTimeMs;
  DWORD      dwDigitOffTimeMs;
} RILSENDDTMFPARAMS, RILSENDDTMFPARAMS;
````


## -struct-fields

### -field dwExecutor


### -field szDTMF


### -field dwDigitOnTimeMs


### -field dwDigitOffTimeMs


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