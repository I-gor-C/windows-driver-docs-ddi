---
UID : NF:d3dkmthk.D3DKMTUnlock2
title : D3DKMTUnlock2 function
author : windows-driver-content
description : The D3DKMTUnlock2 function unlocks a list of allocations.
old-location : display\d3dkmtunlock2.htm
old-project : display
ms.assetid : DDAA5F5A-4A9C-4E8C-B322-A9B395DC753B
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : D3DKMTUnlock2
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : function
req.header : d3dkmthk.h
req.include-header : D3dkmthk.h
req.target-type : Universal
req.target-min-winverclnt : Windows 10
req.target-min-winversvr : Windows Server 2016
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : D3DKMTUnlock2
req.alt-loc : Gdi32.dll,API-MS-Win-DX-D3DKMT-L1-1-1.dll,API-MS-Win-DX-D3DKMT-L1-1-2.dll
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : Gdi32.lib
req.dll : Gdi32.dll
req.irql : 
req.typenames : D3DKMT_DRIVERVERSION
---


# D3DKMTUnlock2 function
The <b>D3DKMTUnlock2</b> function unlocks a list of allocations.

## Syntax

````
NTSTATUS APIENTRY D3DKMTUnlock2(
  _In_ const D3DKMT_UNLOCK2 *pData
);
````

## Parameters

`D3DKMT_UNLOCK2`




## Return Value

<dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl>The allocations were successfully unlocked.
<dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl>Parameters were validated and determined to be incorrect.

 

This function might also return other <b>NTSTATUS</b> values.


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

## See Also

<dl>
<dt>
<a href="..\d3dkmthk\ns-d3dkmthk-_d3dkmt_unlock2.md">D3DKMT_UNLOCK2</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DKMTUnlock2 function%20 RELEASE:%20(12/29/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>