---
UID: NS.RILAPITYPES.RILOPERATORNAMES
title: RILOPERATORNAMES
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\riloperatornames_2.htm
old-project: NetVista
ms.assetid: 5a066e35-1e8c-431e-897f-9d864991b15f
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: RILOPERATORNAMES, RILOPERATORNAMES, *LPRILOPERATORNAMES
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
req.alt-api: RILOPERATORNAMES
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

# RILOPERATORNAMES structure



## -description
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. 



## -syntax

````
typedef struct _RILOPERATORNAMES {
  DWORD                                   cbSize;
  DWORD                                   dwParams;
  DWORD                                   dwSystemType;
  WCHAR [MAXLENGTH_OPERATOR_LONG]         wszLongName;
  WCHAR [MAXLENGTH_OPERATOR_SHORT]        wszShortName;
  WCHAR [MAXLENGTH_OPERATOR_NUMERIC]      wszNumName;
  WCHAR [MAXLENGTH_OPERATOR_COUNTRY_CODE] wszCountryCode;
} RILOPERATORNAMES, RILOPERATORNAMES;
````


## -struct-fields

### -field cbSize


### -field dwParams


### -field dwSystemType


### -field wszLongName


### -field wszShortName


### -field wszNumName


### -field wszCountryCode


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