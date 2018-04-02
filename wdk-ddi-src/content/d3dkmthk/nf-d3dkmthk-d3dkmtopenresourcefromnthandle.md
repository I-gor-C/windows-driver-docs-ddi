---
UID: NF:d3dkmthk.D3DKMTOpenResourceFromNtHandle
title: D3DKMTOpenResourceFromNtHandle function
author: windows-driver-content
description: Opens a shared resource from an NT handle.
old-location: display\d3dkmtopenresourcefromnthandle.htm
old-project: display
ms.assetid: d5a66102-782a-482e-8119-48015820d0c7
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: D3DKMTOpenResourceFromNtHandle, D3DKMTOpenResourceFromNtHandle callback function [Display Devices], PFND3DKMT_OPENRESOURCEFROMNTHANDLE, d3dkmthk/D3DKMTOpenResourceFromNtHandle, display.d3dkmtopenresourcefromnthandle
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: d3dkmthk.h
req.include-header: D3dkmthk.h
req.target-type: Universal
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
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
-	D3dkmthk.h
api_name:
-	D3DKMTOpenResourceFromNtHandle
product: Windows
targetos: Windows
req.typenames: D3DKMT_DRIVERVERSION
---


# D3DKMTOpenResourceFromNtHandle function
Opens a shared resource from an NT handle.

## Syntax

```
NTSTATUS D3DKMTOpenResourceFromNtHandle(

);
```

## Parameters

This function has no parameters.

## Return Value

Returns one of the following values:

<table>
<tr>
<th>Return code</th>
<th>Description</th>
</tr>
<tr>
<td width="40%">
<dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl>
</td>
<td width="60%">
The function completed successfully.

</td>
</tr>
<tr>
<td width="40%">
<dl>
<dt><b>STATUS_INVALID_PARAMETER </b></dt>
</dl>
</td>
<td width="60%">

         Parameters were validated and determined to be incorrect.

</td>
</tr>
</table>
 

This function might also return other NTSTATUS values.

## Remarks

The NT handle to the process, which is used as the <b>hNtHandle</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/hh406496">D3DKMT_OPENRESOURCEFROMNTHANDLE</a> structure, is typically acquired by calling the <a href="https://msdn.microsoft.com/library/windows/hardware/hh780251">D3DKMTShareObjects</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/hh439409">D3DKMTOpenNtHandleFromName</a>  functions.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8 Windows Server 2012 |
| **Target Platform** | Universal |
| **Header** | d3dkmthk.h (include D3dkmthk.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/hh439409">D3DKMTOpenNtHandleFromName</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/hh780251">D3DKMTShareObjects</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/hh406496">D3DKMT_OPENRESOURCEFROMNTHANDLE</a>