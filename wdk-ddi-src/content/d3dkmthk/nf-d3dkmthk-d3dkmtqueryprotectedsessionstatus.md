---
UID : NF:d3dkmthk.D3DKMTQueryProtectedSessionStatus
title : D3DKMTQueryProtectedSessionStatus function
author : windows-driver-content
description : Used to query the status of the protected session.
old-location : display\d3dkmtqueryprotectedsessionstatus.htm
old-project : display
ms.assetid : 787f20a4-51b6-44e3-aefb-2dc529359545
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : d3dkmthk/D3DKMTQueryProtectedSessionStatus, display.d3dkmtqueryprotectedsessionstatus, D3DKMTQueryProtectedSessionStatus method [Display Devices], D3DKMTQueryProtectedSessionStatus
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : function
req.header : d3dkmthk.h
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
req.typenames : D3DKMT_DRIVERVERSION
---


# D3DKMTQueryProtectedSessionStatus function
Used to query the status of the protected session.

## Syntax

````
NTSTATUS  D3DKMTQueryProtectedSessionStatus(
   D3DKMT_QUERYPROTECTEDSESSIONSTATUS  D3dkmt_queryprotectedsessionstatus
);
````

## Parameters

This function has no parameters.

## Return Value

Returns STATUS_SUCCESS if completed successfully.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Windows |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | d3dkmthk.h |
| **Library** |  |
| **IRQL** |  |
| **DDI compliance rules** |  |