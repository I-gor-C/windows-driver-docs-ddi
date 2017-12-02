---
UID: NS.rilapitypes.RILUICCFILEPATH
title: RILUICCFILEPATH
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\riluiccfilepath_2.htm
old-project: netvista
ms.assetid: d0321907-0a3c-43cc-97f1-a3a7e9b84311
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: RILUICCFILEPATH, RILUICCFILEPATH
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
req.alt-api: RILUICCFILEPATH
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
req.iface: 
req.product: Windows 10 or later.
---

# RILUICCFILEPATH structure



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. </p>


## -syntax

````
typedef struct _RILUICCFILEPATH {
  HUICCAPP                  hUiccApp;
  DWORD                     dwFilePathLen;
  WORD [MAXLENGTH_UICCPATH] wFilePath;
} RILUICCFILEPATH, RILUICCFILEPATH;
````


## -struct-fields
<dl>

### -field hUiccApp

<dd></dd>

### -field dwFilePathLen

<dd></dd>

### -field wFilePath

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
<dt>Rilapitypes.h</dt>
</dl>
</td>
</tr>
</table>