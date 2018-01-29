---
UID : NE:filterpipeline.__MIDL___MIDL_itf_filterpipeline_0000_0000_0004
title : __MIDL___MIDL_itf_filterpipeline_0000_0000_0004
author : windows-driver-content
description : .
old-location : print\expsfontrestriction.htm
old-project : print
ms.assetid : 079BEF8A-514E-42C3-8916-95655C605098
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : __MIDL___MIDL_itf_filterpipeline_0000_0000_0004, Xps_Restricted_Font_PreviewPrint, Xps_Restricted_Font_Editable, filterpipeline/Xps_Restricted_Font_Installable, filterpipeline/Xps_Restricted_Font_NoEmbedding, filterpipeline/Xps_Restricted_Font_Editable, print.expsfontrestriction, Xps_Restricted_Font_NoEmbedding, Xps_Restricted_Font_Installable, EXpsFontRestriction enumeration [Print Devices], EXpsFontRestriction, filterpipeline/Xps_Restricted_Font_PreviewPrint, filterpipeline/EXpsFontRestriction
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : enum
req.header : filterpipeline.h
req.include-header : 
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
req.irql : <= APC_LEVEL
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : EXpsFontRestriction
---

# __MIDL___MIDL_itf_filterpipeline_0000_0000_0004 Enumeration


## Syntax
````
typedef enum __MIDL___MIDL_itf_filterpipeline_0000_0000_0004 { 
  Xps_Restricted_Font_Installable   = 0,
  Xps_Restricted_Font_NoEmbedding   = 0x2,
  Xps_Restricted_Font_PreviewPrint  = 0x4,
  Xps_Restricted_Font_Editable      = 0x8
} EXpsFontRestriction;
````

## Constants

<table>

<tr>
<td>Xps_Restricted_Font_Editable</td>
<td></td>
</tr>

<tr>
<td>Xps_Restricted_Font_Installable</td>
<td></td>
</tr>

<tr>
<td>Xps_Restricted_Font_NoEmbedding</td>
<td></td>
</tr>

<tr>
<td>Xps_Restricted_Font_PreviewPrint</td>
<td></td>
</tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | filterpipeline.h |