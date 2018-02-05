---
UID : NF:d3dkmthk.D3DKMTSetDeviceLostSupport
title : D3DKMTSetDeviceLostSupport function
author : windows-driver-content
description : Used to indicate that the device has lost support.
old-location : display\d3dkmtsetdevicelostsupport.htm
old-project : display
ms.assetid : 9b7469cb-d489-4428-8167-91b26e1fa348
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : display.d3dkmtsetdevicelostsupport, D3DKMTSetDeviceLostSupport method [Display Devices], D3DKMTSetDeviceLostSupport, d3dkmthk/D3DKMTSetDeviceLostSupport
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


# D3DKMTSetDeviceLostSupport function
Used to indicate that the device has lost support.

## Syntax

````
NTSTATUS  D3DKMTSetDeviceLostSupport(
  _In_ D3DKMT_SETDEVICELOSTSUPPORT  *D3dkmt_setdevicelostsupport
);
````

## Parameters

This function has no parameters.

## Return Value

Returns STATUS_SUCCESS if completed successfully.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 10 Windows 10 |
| **Target Platform** | Windows |
| **Header** | d3dkmthk.h |
| **Library** | NtosKrnl.exe |