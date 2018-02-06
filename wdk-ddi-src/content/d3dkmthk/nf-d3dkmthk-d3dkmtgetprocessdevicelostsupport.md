---
UID: NF:d3dkmthk.D3DKMTGetProcessDeviceLostSupport
title: D3DKMTGetProcessDeviceLostSupport function
author: windows-driver-content
description: Used to get the indicated process.
old-location: display\d3dkmtgetprocessdevicelostsupport.htm
old-project: display
ms.assetid: 7127b6ff-164b-4645-a602-3969f87a47d0
ms.author: windowsdriverdev
ms.date: 12/29/2017
ms.keywords: d3dkmthk/D3DKMTGetProcessDeviceLostSupport, display.d3dkmtgetprocessdevicelostsupport, D3DKMTGetProcessDeviceLostSupport, D3DKMTGetProcessDeviceLostSupport method [Display Devices]
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: d3dkmthk.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.exe
req.dll: 
req.irql: 
topictype:
-	APIRef
-	kbSyntax
apitype:
-	HeaderDef
apilocation:
-	d3dkmthk.h
apiname:
-	D3DKMTGetProcessDeviceLostSupport
product: Windows
targetos: Windows
req.typenames: D3DKMT_DRIVERVERSION
---


# D3DKMTGetProcessDeviceLostSupport function
Used to get the indicated process.

## Syntax

````
NTSTATUS  D3DKMTGetProcessDeviceLostSupport(
  _Inout_ D3DKMT_GETPROCESSDEVICELOSTSUPPORT  *D3dkmt_getprocessdevicelostsupport
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