---
UID : NE:rilapitypes.RILSERVICEPROVISIONINGSTATUS
title : RILSERVICEPROVISIONINGSTATUS
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\rilserviceprovisioningstatus_2.htm
old-project : netvista
ms.assetid : 044d89f7-6167-4e85-b4b4-d706a1499480
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : RIL_SVCPROV_TEMPMODERESTRICTED, RIL_SVCPROV_MAX, rilapitypes/RIL_SVCPROV_MAX, RIL_SVCPROV_TEMPMODEALLOWED, rilapitypes/RIL_SVCPROV_TEMPMODEALLOWED, rilapitypes/RIL_SVCPROV_NOTPROVISIONED, RIL_SVCPROV_PROVISIONED, rilapitypes/RILSERVICEPROVISIONINGSTATUS, rilapitypes/RIL_SVCPROV_TEMPMODERESTRICTED, RILSERVICEPROVISIONINGSTATUS, RILSERVICEPROVISIONINGSTATUS enumeration [Network Drivers Starting with Windows Vista], netvista.rilserviceprovisioningstatus_2, rilapitypes/RIL_SVCPROV_PROVISIONED, RIL_SVCPROV_NOTPROVISIONED
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
req.typenames : RILSERVICEPROVISIONINGSTATUS
req.product : Windows 10 or later.
---

# RILSERVICEPROVISIONINGSTATUS Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef enum _RILSERVICEPROVISIONINGSTATUS { 
  RIL_SVCPROV_NOTPROVISIONED,
  RIL_SVCPROV_PROVISIONED,
  RIL_SVCPROV_TEMPMODERESTRICTED,
  RIL_SVCPROV_TEMPMODEALLOWED,
  RIL_SVCPROV_MAX
} RILSERVICEPROVISIONINGSTATUS;
````

## Constants

<table>

<tr>
<td>RIL_SVCPROV_MAX</td>
<td></td>
</tr>

<tr>
<td>RIL_SVCPROV_NOTPROVISIONED</td>
<td></td>
</tr>

<tr>
<td>RIL_SVCPROV_PROVISIONED</td>
<td></td>
</tr>

<tr>
<td>RIL_SVCPROV_TEMPMODEALLOWED</td>
<td></td>
</tr>

<tr>
<td>RIL_SVCPROV_TEMPMODERESTRICTED</td>
<td></td>
</tr>

<tr>
<td>RIL_SVCPROV_UNKNOWN</td>
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