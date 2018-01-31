---
UID : NE:rilapitypes.RILCALLINFOSTATUS
title : RILCALLINFOSTATUS
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\rilcallinfostatus_2.htm
old-project : netvista
ms.assetid : 16ecddf7-6c79-4e95-957d-19f27c3e3cf5
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : rilapitypes/RIL_CPISTAT_MAX, RIL_CPISTAT_ONHOLD, rilapitypes/RIL_CPISTAT_MEDIA, RIL_CPISTAT_NEW_OUTGOING, RIL_CPISTAT_CONNECTED, rilapitypes/RIL_CPISTAT_CONNECTED, RIL_CPISTAT_MAX, rilapitypes/RIL_CPISTAT_NEW_OUTGOING, RILCALLINFOSTATUS, RIL_CPISTAT_DISCONNECTED, rilapitypes/RILCALLINFOSTATUS, rilapitypes/RIL_CPISTAT_DISCONNECTED, rilapitypes/RIL_CPISTAT_ONHOLD, rilapitypes/RIL_CPISTAT_HANDOVER, netvista.rilcallinfostatus_2, RIL_CPISTAT_MEDIA, RIL_CPISTAT_NEW_INCOMING, RIL_CPISTAT_HANDOVER, rilapitypes/RIL_CPISTAT_NEW_INCOMING, RILCALLINFOSTATUS enumeration [Network Drivers Starting with Windows Vista]
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : enum
req.header : rilapitypes.h
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
req.lib : NtosKrnl.exe
req.dll : 
req.irql : 
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : RILCALLINFOSTATUS
req.product : Windows 10 or later.
---

# RILCALLINFOSTATUS Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef enum _RILCALLINFOSTATUS { 
  RIL_CPISTAT_NEW_OUTGOING,
  RIL_CPISTAT_NEW_INCOMING,
  RIL_CPISTAT_CONNECTED,
  RIL_CPISTAT_DISCONNECTED,
  RIL_CPISTAT_ONHOLD,
  RIL_CPISTAT_MEDIA,
  RIL_CPISTAT_HANDOVER,
  RIL_CPISTAT_MAX
} RILCALLINFOSTATUS;
````

## Constants

<table>

<tr>
<td>RIL_CPISTAT_CONNECTED</td>
<td></td>
</tr>

<tr>
<td>RIL_CPISTAT_DISCONNECTED</td>
<td></td>
</tr>

<tr>
<td>RIL_CPISTAT_HANDOVER</td>
<td></td>
</tr>

<tr>
<td>RIL_CPISTAT_MAX</td>
<td></td>
</tr>

<tr>
<td>RIL_CPISTAT_MEDIA</td>
<td></td>
</tr>

<tr>
<td>RIL_CPISTAT_NEW_INCOMING</td>
<td></td>
</tr>

<tr>
<td>RIL_CPISTAT_NEW_OUTGOING</td>
<td></td>
</tr>

<tr>
<td>RIL_CPISTAT_ONHOLD</td>
<td></td>
</tr>

<tr>
<td>RIL_CPISTAT_UNKNOWN</td>
<td></td>
</tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | rilapitypes.h |