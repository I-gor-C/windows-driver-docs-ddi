---
UID : NE:filterpipeline.__MIDL___MIDL_itf_filterpipeline_0000_0000_0002
title : __MIDL___MIDL_itf_filterpipeline_0000_0000_0002
author : windows-driver-content
description : The EXpsFontOptions enumeration describes the font options for an XPS part.
old-location : print\expsfontoptions.htm
old-project : print
ms.assetid : 3a92b219-91ee-4c11-b5c1-8e2e0cbff406
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : Font_Obfusticate, filterpipeline_252cd44a-7a00-40fb-9245-364c1453e2ef.xml, EXpsFontOptions enumeration [Print Devices], __MIDL___MIDL_itf_filterpipeline_0000_0000_0002, filterpipeline/Font_Obfusticate, print.expsfontoptions, filterpipeline/EXpsFontOptions, Font_Normal, filterpipeline/Font_Normal, EXpsFontOptions
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : enum
req.header : filterpipeline.h
req.include-header : Filterpipeline.h
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : Filterpipeline.idl
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : NtosKrnl.exe
req.dll : 
req.irql : "<= APC_LEVEL"
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : EXpsFontOptions
---

# __MIDL___MIDL_itf_filterpipeline_0000_0000_0002 Enumeration
The EXpsFontOptions enumeration describes the font options for an XPS part.

## Syntax
````
typedef enum  { 
  Font_Normal,
  Font_Obfusticate
} EXpsFontOptions;
````

## Constants

<table>

<tr>
<td>Font_Normal</td>
<td>The font code is human-readable.</td>
</tr>

<tr>
<td>Font_Obfusticate</td>
<td>The font code is obfusticated (that is, the internal structure of the font is scrambled in such a way to prevent someone from understaning how the structure works).</td>
</tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | filterpipeline.h (include Filterpipeline.h) |