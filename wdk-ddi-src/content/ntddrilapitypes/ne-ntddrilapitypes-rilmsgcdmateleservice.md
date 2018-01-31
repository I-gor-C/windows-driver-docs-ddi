---
UID : NE:ntddrilapitypes.RILMSGCDMATELESERVICE
title : RILMSGCDMATELESERVICE
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\rilmsgcdmateleservice.htm
old-project : netvista
ms.assetid : 01c45c31-2cae-4f9f-a3dc-4a164a3df670
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : ntddrilapitypes/RIL_MSGTELESERVICE_MESSAGING, RIL_MSGTELESERVICE_WAP_OLD, RIL_MSGTELESERVICE_VOICEMAIL_VMN_95, ntddrilapitypes/RIL_MSGTELESERVICE_WAP_CT_MMS, RIL_MSGTELESERVICE_SELFREG, RIL_MSGTELESERVICE_WEMT, RIL_MSGTELESERVICE_WAP, RILMSGCDMATELESERVICE enumeration [Network Drivers Starting with Windows Vista], RIL_MSGTELESERVICE_VOICEMAIL_MWI, ntddrilapitypes/RIL_MSGTELESERVICE_BROADCAST, ntddrilapitypes/RILMSGCDMATELESERVICE, ntddrilapitypes/RIL_MSGTELESERVICE_VOICEMAIL_OLD, ntddrilapitypes/RIL_MSGTELESERVICE_WEMT, RILMSGCDMATELESERVICE, ntddrilapitypes/RIL_MSGTELESERVICE_WAP_OLD, ntddrilapitypes/RIL_MSGTELESERVICE_WAP_CT_OMA, RIL_MSGTELESERVICE_BROADCAST, ntddrilapitypes/RIL_MSGTELESERVICE_BROADCAST_OLD, RIL_MSGTELESERVICE_PAGING, ntddrilapitypes/RIL_MSGTELESERVICE_PAGING, RIL_MSGTELESERVICE_WAP_CT_MMS, ntddrilapitypes/RIL_MSGTELESERVICE_WAP, ntddrilapitypes/RIL_MSGTELESERVICE_SELFREG_OLD, RIL_MSGTELESERVICE_WAP_CT_OMA, ntddrilapitypes/RIL_MSGTELESERVICE_MESSAGING_OLD, RIL_MSGTELESERVICE_BROADCAST_OLD, netvista.rilmsgcdmateleservice, RIL_MSGTELESERVICE_MESSAGING_OLD, ntddrilapitypes/RIL_MSGTELESERVICE_VOICEMAIL_VMN_95, ntddrilapitypes/RIL_MSGTELESERVICE_SELFREG, RIL_MSGTELESERVICE_SELFREG_OLD, RIL_MSGTELESERVICE_VOICEMAIL_OLD, RIL_MSGTELESERVICE_MESSAGING, ntddrilapitypes/RIL_MSGTELESERVICE_VOICEMAIL_MWI
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
req.typenames : RILMSGCDMATELESERVICE
---

# RILMSGCDMATELESERVICE Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef enum _RILMSGCDMATELESERVICE { 
  RIL_MSGTELESERVICE_MESSAGING_OLD,
  RIL_MSGTELESERVICE_VOICEMAIL_OLD,
  RIL_MSGTELESERVICE_WAP_OLD,
  RIL_MSGTELESERVICE_BROADCAST_OLD,
  RIL_MSGTELESERVICE_SELFREG_OLD,
  RIL_MSGTELESERVICE_PAGING,
  RIL_MSGTELESERVICE_MESSAGING,
  RIL_MSGTELESERVICE_WEMT,
  RIL_MSGTELESERVICE_VOICEMAIL_VMN_95,
  RIL_MSGTELESERVICE_VOICEMAIL_MWI,
  RIL_MSGTELESERVICE_WAP,
  RIL_MSGTELESERVICE_WAP_CT_MMS,
  RIL_MSGTELESERVICE_WAP_CT_OMA,
  RIL_MSGTELESERVICE_BROADCAST,
  RIL_MSGTELESERVICE_SELFREG
} RILMSGCDMATELESERVICE;
````

## Constants

<table>

<tr>
<td>RIL_MSGTELESERVICE_BROADCAST</td>
<td></td>
</tr>

<tr>
<td>RIL_MSGTELESERVICE_BROADCAST_OLD</td>
<td></td>
</tr>

<tr>
<td>RIL_MSGTELESERVICE_MESSAGING</td>
<td></td>
</tr>

<tr>
<td>RIL_MSGTELESERVICE_MESSAGING_OLD</td>
<td></td>
</tr>

<tr>
<td>RIL_MSGTELESERVICE_PAGING</td>
<td></td>
</tr>

<tr>
<td>RIL_MSGTELESERVICE_PAGING_OLD</td>
<td></td>
</tr>

<tr>
<td>RIL_MSGTELESERVICE_SELFREG</td>
<td></td>
</tr>

<tr>
<td>RIL_MSGTELESERVICE_SELFREG_OLD</td>
<td></td>
</tr>

<tr>
<td>RIL_MSGTELESERVICE_VOICEMAIL_MWI</td>
<td></td>
</tr>

<tr>
<td>RIL_MSGTELESERVICE_VOICEMAIL_OLD</td>
<td></td>
</tr>

<tr>
<td>RIL_MSGTELESERVICE_VOICEMAIL_VMN_95</td>
<td></td>
</tr>

<tr>
<td>RIL_MSGTELESERVICE_WAP</td>
<td></td>
</tr>

<tr>
<td>RIL_MSGTELESERVICE_WAP_CT_MMS</td>
<td></td>
</tr>

<tr>
<td>RIL_MSGTELESERVICE_WAP_CT_OMA</td>
<td></td>
</tr>

<tr>
<td>RIL_MSGTELESERVICE_WAP_OLD</td>
<td></td>
</tr>

<tr>
<td>RIL_MSGTELESERVICE_WEMT</td>
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