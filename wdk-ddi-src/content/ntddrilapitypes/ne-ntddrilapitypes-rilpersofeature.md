---
UID : NE:ntddrilapitypes.RILPERSOFEATURE
title : RILPERSOFEATURE
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\rilpersofeature.htm
old-project : netvista
ms.assetid : e212ab20-e9b4-4ccc-b0db-a82ca5b59573
ms.author : windowsdriverdev
ms.date : 1/11/2018
ms.keywords : RILPERSOFEATURE, RILPERSOFEATURE
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : enum
req.header : ntddrilapitypes.h
req.include-header : 
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : RILPERSOFEATURE
req.alt-loc : ntddrilapitypes.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : 
req.typenames : RILPERSOFEATURE
---

# RILPERSOFEATURE Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef enum _RILPERSOFEATURE { 
  RIL_PERSOFEATURE_3GPP_NET,
  RIL_PERSOFEATURE_3GPP_NETSUB,
  RIL_PERSOFEATURE_3GPP_SP,
  RIL_PERSOFEATURE_3GPP_CORP,
  RIL_PERSOFEATURE_3GPP_USIM,
  RIL_PERSOFEATURE_3GPP2_NETTYPE1,
  RIL_PERSOFEATURE_3GPP2_NETTYPE2,
  RIL_PERSOFEATURE_3GPP2_HRPD,
  RIL_PERSOFEATURE_3GPP2_SP,
  RIL_PERSOFEATURE_3GPP2_CORP,
  RIL_PERSOFEATURE_3GPP2_UIM,
  RIL_PERSOFEATURE_ALL
} RILPERSOFEATURE;
````

## Constants

<table>

<tr>
<td>RIL_PERSOFEATURE_3GPP_CORP</td>
<td></td>
</tr>

<tr>
<td>RIL_PERSOFEATURE_3GPP_NET</td>
<td></td>
</tr>

<tr>
<td>RIL_PERSOFEATURE_3GPP_NETSUB</td>
<td></td>
</tr>

<tr>
<td>RIL_PERSOFEATURE_3GPP_SP</td>
<td></td>
</tr>

<tr>
<td>RIL_PERSOFEATURE_3GPP_USIM</td>
<td></td>
</tr>

<tr>
<td>RIL_PERSOFEATURE_3GPP2_CORP</td>
<td></td>
</tr>

<tr>
<td>RIL_PERSOFEATURE_3GPP2_HRPD</td>
<td></td>
</tr>

<tr>
<td>RIL_PERSOFEATURE_3GPP2_NETTYPE1</td>
<td></td>
</tr>

<tr>
<td>RIL_PERSOFEATURE_3GPP2_NETTYPE2</td>
<td></td>
</tr>

<tr>
<td>RIL_PERSOFEATURE_3GPP2_SP</td>
<td></td>
</tr>

<tr>
<td>RIL_PERSOFEATURE_3GPP2_UIM</td>
<td></td>
</tr>

<tr>
<td>RIL_PERSOFEATURE_ALL</td>
<td></td>
</tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ntddrilapitypes.h |