---
UID : NE:ntddrilapitypes.RILMSGCDMAMSGPRIVACY
title : RILMSGCDMAMSGPRIVACY
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\rilmsgcdmamsgprivacy.htm
old-project : netvista
ms.assetid : 491b985f-c228-4f4b-88c1-fd678266dd9d
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : RIL_MSGPRIVACYCLASS_MAX, RIL_MSGPRIVACYCLASS_RESTRICTED, RILMSGCDMAMSGPRIVACY enumeration [Network Drivers Starting with Windows Vista], ntddrilapitypes/RILMSGCDMAMSGPRIVACY, RIL_MSGPRIVACYCLASS_SECRET, ntddrilapitypes/RIL_MSGPRIVACYCLASS_MAX, ntddrilapitypes/RIL_MSGPRIVACYCLASS_SECRET, RILMSGCDMAMSGPRIVACY, RIL_MSGPRIVACYCLASS_CONFIDENTIAL, ntddrilapitypes/RIL_MSGPRIVACYCLASS_CONFIDENTIAL, ntddrilapitypes/RIL_MSGPRIVACYCLASS_RESTRICTED, netvista.rilmsgcdmamsgprivacy
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
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : RILMSGCDMAMSGPRIVACY
---

# RILMSGCDMAMSGPRIVACY Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef enum _RILMSGCDMAMSGPRIVACY { 
  RIL_MSGPRIVACYCLASS_RESTRICTED,
  RIL_MSGPRIVACYCLASS_CONFIDENTIAL,
  RIL_MSGPRIVACYCLASS_SECRET,
  RIL_MSGPRIVACYCLASS_MAX
} RILMSGCDMAMSGPRIVACY;
````

## Constants

<table>

<tr>
<td>RIL_MSGPRIVACYCLASS_CONFIDENTIAL</td>
<td></td>
</tr>

<tr>
<td>RIL_MSGPRIVACYCLASS_MAX</td>
<td></td>
</tr>

<tr>
<td>RIL_MSGPRIVACYCLASS_NOTRESTRICTED</td>
<td></td>
</tr>

<tr>
<td>RIL_MSGPRIVACYCLASS_RESTRICTED</td>
<td></td>
</tr>

<tr>
<td>RIL_MSGPRIVACYCLASS_SECRET</td>
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