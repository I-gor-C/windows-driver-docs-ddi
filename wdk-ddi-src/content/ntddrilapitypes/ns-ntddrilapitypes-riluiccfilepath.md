---
UID: NS.NTDDRILAPITYPES.RILUICCFILEPATH
title: RILUICCFILEPATH
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\riluiccfilepath.htm
old-project: netvista
ms.assetid: 65c46391-f0ef-4618-ac26-86f41e04e688
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: RILUICCFILEPATH, *LPRILUICCFILEPATH, RILUICCFILEPATH
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
req.alt-api: RILUICCFILEPATH
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

# RILUICCFILEPATH structure



## -description
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.


## -syntax

````
typedef struct _RILUICCFILEPATH {
  HUICCAPP  hUiccApp;
  DWORD     dwFilePathLen;
  WORD [8]  wFilePath;
} RILUICCFILEPATH, RILUICCFILEPATH;
````


## -struct-fields

### -field hUiccApp


### -field dwFilePathLen


### -field wFilePath


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