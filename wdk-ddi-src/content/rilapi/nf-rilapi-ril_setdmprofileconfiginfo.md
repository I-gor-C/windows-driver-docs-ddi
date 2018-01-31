---
UID : NF:rilapi.RIL_SetDMProfileConfigInfo
title : RIL_SetDMProfileConfigInfo function
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\ril_setdmprofileconfiginfo.htm
old-project : netvista
ms.assetid : 4d2ab950-a045-4b5a-be9b-0b80c442e63d
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : netvista.ril_setdmprofileconfiginfo, RIL_SetDMProfileConfigInfo method [Network Drivers Starting with Windows Vista], rilapi/RIL_SetDMProfileConfigInfo, RIL_SetDMProfileConfigInfo
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
req.typenames : "*PRH_QUERY_CONNECTION_PROPERTIES_OUTPUT_BUFFER, RH_QUERY_CONNECTION_PROPERTIES_OUTPUT_BUFFER"
req.product : Windows 10 or later.
---


# RIL_SetDMProfileConfigInfo function
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax

````
HRESULT  RIL_SetDMProfileConfigInfo(
   HRIL                        hRil,
   LPVOID                      lpContext,
   DWORD                       dwExecutor,
   DWORD                       dwConfigItem,
   const RILDMCONFIGINFOVALUE  rciValue
);
````

## Parameters

`hRil`



`lpContext`



`dwExecutor`



`dwConfigItem`



`rciValue`




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