---
UID: NC:d3d10umddi.PFND3D10DDI_RESOURCEUPDATESUBRESOURCEUP
title: PFND3D10DDI_RESOURCEUPDATESUBRESOURCEUP
author: windows-driver-content
description: The DefaultConstantBufferUpdateSubresourceUP function updates a destination subresource region that stores constant buffers from a source system-memory region.
old-location: display\defaultconstantbufferupdatesubresourceup.htm
old-project: display
ms.assetid: 80086f1a-75f8-464f-973e-9c1e67725933
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: DefaultConstantBufferUpdateSubresourceUP, DefaultConstantBufferUpdateSubresourceUP callback function [Display Devices], PFND3D10DDI_RESOURCEUPDATESUBRESOURCEUP, UserModeDisplayDriverDx10_Functions_1868c778-0475-4113-8b24-caf7f9822775.xml, d3d10umddi/DefaultConstantBufferUpdateSubresourceUP, display.defaultconstantbufferupdatesubresourceup
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	UserDefined
api_location:
-	d3d10umddi.h
api_name:
-	DefaultConstantBufferUpdateSubresourceUP
product: Windows
targetos: Windows
req.typenames: SETRESULT_INFO, *PSETRESULT_INFO
---


# PFND3D10DDI_RESOURCEUPDATESUBRESOURCEUP callback function
The <i>DefaultConstantBufferUpdateSubresourceUP</i> function updates a destination subresource region that stores constant buffers from a source system-memory region.

## Syntax

```
PFND3D10DDI_RESOURCEUPDATESUBRESOURCEUP Pfnd3d10ddiResourceupdatesubresourceup;

void Pfnd3d10ddiResourceupdatesubresourceup(
   D3D10DDI_HDEVICE,
   D3D10DDI_HRESOURCE,
   UINT,
  CONST D3D10_DDI_BOX *,
  CONST VOID *,
   UINT,
   UINT
)
{...}
```

## Parameters

`D3D10DDI_HDEVICE`



`D3D10DDI_HRESOURCE`



`UINT`



`*`



`*`



`UINT`



`UINT`




## Return Value

None.

The driver can use the <a href="https://msdn.microsoft.com/968b04a7-8869-410c-a6fc-83d57726858f">pfnSetErrorCb</a> callback function to set an error code. For more information about setting error codes, see the following Remarks section.

## Remarks

For more information about <i>DefaultConstantBufferUpdateSubresourceUP</i>, see the Remarks section of the <a href="https://msdn.microsoft.com/3b6177f4-43a1-4461-abfc-5c463b0ba612">ResourceUpdateSubresourceUP</a> function.

The driver should not encounter any error, except for D3DDDIERR_DEVICEREMOVED. Therefore, if the driver passes any error, except for D3DDDIERR_DEVICEREMOVED, in a call to the <a href="https://msdn.microsoft.com/968b04a7-8869-410c-a6fc-83d57726858f">pfnSetErrorCb</a> function, the Direct3D runtime will determine that the error is critical. Even if the device was removed, the driver is not required to return D3DDDIERR_DEVICEREMOVED; however, if device removal interfered with the operation of <i>DefaultConstantBufferUpdateSubresourceUP</i> (which typically should not happen), the driver can return D3DDDIERR_DEVICEREMOVED.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems.  |
| **Target Platform** | Desktop |
| **Header** | d3d10umddi.h (include D3d10umddi.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff541833">D3D10DDI_DEVICEFUNCS</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff541925">D3D10_DDI_BOX</a>



<a href="https://msdn.microsoft.com/3b6177f4-43a1-4461-abfc-5c463b0ba612">ResourceUpdateSubresourceUP</a>



<a href="https://msdn.microsoft.com/968b04a7-8869-410c-a6fc-83d57726858f">pfnSetErrorCb</a>