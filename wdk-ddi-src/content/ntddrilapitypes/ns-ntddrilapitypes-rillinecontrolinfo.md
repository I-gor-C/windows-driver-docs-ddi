---
UID: NS.NTDDRILAPITYPES.RILLINECONTROLINFO
title: RILLINECONTROLINFO
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rillinecontrolinfo.htm
old-project: NetVista
ms.assetid: 4a3bcbda-58e8-4b40-bcc2-fe7b1e624973
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: RILLINECONTROLINFO, LPRILLINECONTROLINFO, *LPRILLINECONTROLINFO, RILLINECONTROLINFO
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
req.alt-api: RILLINECONTROLINFO
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

# RILLINECONTROLINFO structure



## -description
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.



## -syntax

````
typedef struct _RILLINECONTROLINFO {
  DWORD  cbSize;
  DWORD  dwExecutor;
  BOOL   fPolarityIncluded;
  BOOL   fToggleMode;
  BOOL   fReversePolarity;
  DWORD  dwPowerDenialTime;
} RILLINECONTROLINFO, RILLINECONTROLINFO;
````


## -struct-fields

### -field cbSize


### -field dwExecutor


### -field fPolarityIncluded


### -field fToggleMode


### -field fReversePolarity


### -field dwPowerDenialTime


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