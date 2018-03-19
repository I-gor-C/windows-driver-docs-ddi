---
UID: NF:d3dkmthk.D3DKMTGetSharedResourceAdapterLuid
title: D3DKMTGetSharedResourceAdapterLuid function
author: windows-driver-content
description: Maps a shared resource to a locally unique identifier (LUID) that identifies the graphics adapter that the resource was created on.
old-location: display\d3dkmtgetsharedresourceadapterluid.htm
old-project: display
ms.assetid: 880bf5bd-eadc-480f-a10c-f6d57f670857
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: D3DKMTGetSharedResourceAdapterLuid, D3DKMTGetSharedResourceAdapterLuid function [Display Devices], d3dkmthk/D3DKMTGetSharedResourceAdapterLuid, display.d3dkmtgetsharedresourceadapterluid
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
-	API-MS-Win-dx-d3dkmt-l1-1-0.dll
-	API-MS-Win-dx-d3dkmt-l1-1-1.dll
-	API-MS-Win-DX-D3DKMT-L1-1-2.dll
api_name:
-	D3DKMTGetSharedResourceAdapterLuid
product: Windows
targetos: Windows
req.typenames: D3DKMT_DRIVERVERSION
---


# D3DKMTGetSharedResourceAdapterLuid function
Maps a shared resource to a locally unique identifier (LUID) that identifies the graphics adapter that the resource was created on.

## Syntax

````
EXTERN_C _Check_return_ NTSTATUS APIENTRY D3DKMTGetSharedResourceAdapterLuid(
  _Inout_ D3DKMT_GETSHAREDRESOURCEADAPTERLUID *pLuid
);
````

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
The mapping was performed successfully.

</td>
</tr>
<tr>
<td width="40%">
<dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
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
| **Windows version** | Windows 8 Windows Server 2012 |
| **Target Platform** | Universal |
| **Header** | d3dkmthk.h (include D3dkmthk.h) |
| **Library** | GDI32.lib |
| **DLL** | GDI32.dll |

## See Also

<a href="..\d3dkmthk\ns-d3dkmthk-_d3dkmt_getsharedresourceadapterluid.md">D3DKMT_GETSHAREDRESOURCEADAPTERLUID</a>