---
UID : NF:d3dkmthk.D3DKMTOpenProtectedSessionFromNtHandle
title : D3DKMTOpenProtectedSessionFromNtHandle function
author : windows-driver-content
description : Used to open a protected session from the NT handle.
old-location : display\d3dkmtopenprotectedsessionfromnthandle.htm
old-project : display
ms.assetid : 3ebdf120-ecdd-474b-961d-958179cf30e0
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : D3DKMTOpenProtectedSessionFromNtHandle method [Display Devices], d3dkmthk/D3DKMTOpenProtectedSessionFromNtHandle, display.d3dkmtopenprotectedsessionfromnthandle, D3DKMTOpenProtectedSessionFromNtHandle
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


# D3DKMTOpenProtectedSessionFromNtHandle function
Used to open a protected session from the NT handle.

## Syntax

````
NTSTATUS  D3DKMTOpenProtectedSessionFromNtHandle(
  _Inout_ D3DKMT_OPENPROTECTEDSESSIONFROMNTHANDLE  *D3dkmt_openprotectedsessionfromnthandle
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