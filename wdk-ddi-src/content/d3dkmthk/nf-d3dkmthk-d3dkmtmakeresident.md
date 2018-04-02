---
UID: NF:d3dkmthk.D3DKMTMakeResident
title: D3DKMTMakeResident function
author: windows-driver-content
description: D3DKMTMakeResident is used to add a resource to the device residency list and increment the residency reference count on this allocation.
old-location: display\d3dkmtmakeresident.htm
old-project: display
ms.assetid: 5F4E17CB-3B8B-4BBA-A819-B8E28183F1CB
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: D3DKMTMakeResident, D3DKMTMakeResident function [Display Devices], d3dkmthk/D3DKMTMakeResident, display.d3dkmtmakeresident
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: d3dkmthk.h
req.include-header: D3dkmthk.h
req.target-type: Universal
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
req.lib: GDI32.lib
req.dll: GDI32.dll
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	DllExport
api_location:
-	GDI32.dll
-	API-MS-Win-DX-D3DKMT-L1-1-1.dll
-	GDI32.dll
-	API-MS-Win-DX-D3DKMT-L1-1-2.dll
api_name:
-	D3DKMTMakeResident
product:
- Windows
targetos: Windows
req.typenames: D3DKMT_DRIVERVERSION
---


# D3DKMTMakeResident function
<b>D3DKMTMakeResident</b> is used to add a resource to the device residency list and increment the residency reference count on this allocation.

## Syntax

```
NTSTATUS D3DKMTMakeResident(

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
The operation was performed successfully.

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
 

This function might also return other <b>NTSTATUS</b> values.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 10 Windows Server 2016 |
| **Target Platform** | Universal |
| **Header** | d3dkmthk.h (include D3dkmthk.h) |
| **Library** | GDI32.lib |
| **DLL** | GDI32.dll |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/dn906323">D3DDDI_MAKERESIDENT</a>