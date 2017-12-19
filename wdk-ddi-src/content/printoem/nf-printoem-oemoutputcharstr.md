---
UID: NF.printoem.OEMOutputCharStr
title: OEMOutputCharStr function
author: windows-driver-content
description: OEMOutputCharStr function
old-location: print\oemoutputcharstr.htm
old-project: print
ms.assetid: ac23ec89-b455-4bfd-93a5-2294d8b8ffc2
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: OEMOutputCharStr
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: printoem.h
req.include-header: Printoem.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: OEMOutputCharStr
req.alt-loc: printoem.h
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

# OEMOutputCharStr function



## -description

## -syntax

````
VOID APIENTRY OEMOutputCharStr(
       PDEVOBJ                pdevobj,
       PUNIFONTOBJ            pUFObj,
       DWORD                  dwType,
       DWORD                  dwCount,
  _In_ _reads_(dwCount) PVOID pGlyph
);
````


## -parameters

### -param pdevobj 


### -param pUFObj 


### -param dwType 


### -param dwCount 


### -param pGlyph [in]


## -returns
This function does not return a value.

This function is obsolete for Windows XP and later. It is supported only for earlier Unidrv plug-ins. Use <a href="print.iprintoemuni_outputcharstr">IPrintOemUni::OutputCharStr</a>.


## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Printoem.h (include Printoem.h)</dt>
</dl>
</td>
</tr>
</table>