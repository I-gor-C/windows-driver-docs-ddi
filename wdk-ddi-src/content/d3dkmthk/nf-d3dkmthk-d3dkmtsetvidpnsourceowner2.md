---
UID : NF:d3dkmthk.D3DKMTSetVidPnSourceOwner2
title : D3DKMTSetVidPnSourceOwner2 function
author : windows-driver-content
description : Used to set the VidPN source owner.
old-location : display\d3dkmtsetvidpnsourceowner2.htm
old-project : display
ms.assetid : 14ba3307-753f-4dca-8d4d-c87b3fee00a5
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : display.d3dkmtsetvidpnsourceowner2, d3dkmthk/D3DKMTSetVidPnSourceOwner2, D3DKMTSetVidPnSourceOwner2 method [Display Devices], D3DKMTSetVidPnSourceOwner2
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


# D3DKMTSetVidPnSourceOwner2 function
Used to set the VidPN source owner.

## Syntax

````
NTSTATUS  D3DKMTSetVidPnSourceOwner2(
  _In_ const D3DKMT_SETVIDPNSOURCEOWNER2   D3dkmt_setvidpnsourceowner2
);
````

## Parameters

`D3DKMT_SETVIDPNSOURCEOWNER2`

TBD


## Return Value

Returns STATUS_SUCCESS if used successfully.


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