---
UID : NF:rilapi.RIL_AddCallForwarding
title : RIL_AddCallForwarding function
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\ril_addcallforwarding.htm
old-project : netvista
ms.assetid : 86b08757-bbc0-4f19-8153-c6ecae158cf2
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : rilapi/RIL_AddCallForwarding, RIL_AddCallForwarding, netvista.ril_addcallforwarding, RIL_AddCallForwarding method [Network Drivers Starting with Windows Vista]
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : function
req.header : rilapi.h
req.include-header : 
req.target-type : Windows
req.target-min-winverclnt : Windows 10
req.target-min-winversvr : Windows Server 2016
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
req.typenames : RH_QUERY_CONNECTION_PROPERTIES_OUTPUT_BUFFER, *PRH_QUERY_CONNECTION_PROPERTIES_OUTPUT_BUFFER
req.product : Windows 10 or later.
---


# RIL_AddCallForwarding function
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax

````
HRESULT  RIL_AddCallForwarding(
   HRIL                             hRil,
   LPVOID                           lpContext,
   DWORD                            dwExecutor,
   RILCALLFORWARDINGSETTINGSREASON  dwReason,
   const RILCALLFORWARDINGSETTINGS  lpSettings
);
````

## Parameters

`hRil`



`lpContext`



`dwExecutor`



`dwReason`



`lpSettings`




## Return Value

If this method succeeds, it returns <b xmlns:loc="http://microsoft.com/wdcml/l10n">S_OK</b>. Otherwise, it returns an <b xmlns:loc="http://microsoft.com/wdcml/l10n">HRESULT</b> error code.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Windows |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | rilapi.h |
| **Library** |  |
| **IRQL** |  |
| **DDI compliance rules** |  |