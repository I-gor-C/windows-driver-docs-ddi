---
UID : NF:d3dkmthk.D3DKMTWaitForVerticalBlankEvent2
title : D3DKMTWaitForVerticalBlankEvent2 function
author : windows-driver-content
description : Waits for specified wait objects, including a vertical blank event, to occur and then returns. Supported starting with Windows 8.
old-location : display\d3dkmtwaitforverticalblankevent2.htm
old-project : display
ms.assetid : 71a48c1f-1eca-4f3e-a085-99ffc207a7e0
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : D3DKMTWaitForVerticalBlankEvent2
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : function
req.header : d3dkmthk.h
req.include-header : D3dkmthk.h
req.target-type : Universal
req.target-min-winverclnt : Windows 8
req.target-min-winversvr : Windows Server 2012
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : D3DKMTWaitForVerticalBlankEvent2
req.alt-loc : D3dkmthk.h
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
req.typenames : D3DKMT_DRIVERVERSION
---


# D3DKMTWaitForVerticalBlankEvent2 function
Waits for specified wait objects, including a vertical blank event, to occur and then returns. Supported starting with Windows 8.

## Syntax

````
EXTERN_C _Check_return_ NTSTATUS APIENTRY D3DKMTWaitForVerticalBlankEvent2(
  _In_ const D3DKMT_WAITFORVERTICALBLANKEVENT2 *pWait
);
````

## Parameters

`D3DKMT_WAITFORVERTICALBLANKEVENT2`




## Return Value

Returns one of the following values:
<dl>
<dt><b>STATUS_WAIT_0 </b></dt>
</dl>The vertical blank event caused the wait object to return.
<dl>
<dt>STATUS_WAIT_1–STATUS_WAIT_8</dt>
</dl>The number of the user-mode event that caused the wait object to return.
<dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl>Parameters were validated and determined to be incorrect.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Universal |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | d3dkmthk.h (include D3dkmthk.h) |
| **Library** |  |
| **IRQL** |  |
| **DDI compliance rules** |  |