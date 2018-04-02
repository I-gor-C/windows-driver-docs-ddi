---
UID: NF:d3dkmthk.D3DKMTQueryRemoteVidPnSourceFromGdiDisplayName
title: D3DKMTQueryRemoteVidPnSourceFromGdiDisplayName function
author: windows-driver-content
description: Maps a GDI display name to a remote video present network (VidPN) source ID that is needed for a call to the D3DKMTOutputDuplPresent function.
old-location: display\d3dkmtqueryremotevidpnsourcefromgdidisplayname.htm
old-project: display
ms.assetid: 3606d5f4-760f-4ba1-84ea-218b6c2a2e20
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: D3DKMTQueryRemoteVidPnSourceFromGdiDisplayName, D3DKMTQueryRemoteVidPnSourceFromGdiDisplayName callback function [Display Devices], PFND3DKMT_QUERYREMOTEVIDPNSOURCEFROMGDIDISPLAYNAME, d3dkmthk/D3DKMTQueryRemoteVidPnSourceFromGdiDisplayName, display.d3dkmtqueryremotevidpnsourcefromgdidisplayname
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
-	D3DKMTQueryRemoteVidPnSourceFromGdiDisplayName
product: Windows
targetos: Windows
req.typenames: D3DKMT_DRIVERVERSION
---


# D3DKMTQueryRemoteVidPnSourceFromGdiDisplayName function
Maps a GDI display name to a remote video present network (VidPN) source ID that is needed for a call to the <a href="https://msdn.microsoft.com/library/windows/hardware/hh439432">D3DKMTOutputDuplPresent</a> function.

## Syntax

```
NTSTATUS D3DKMTQueryRemoteVidPnSourceFromGdiDisplayName(

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
The mapping was performed successfully.

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


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8 Windows Server 2012 |
| **Target Platform** | Universal |
| **Header** | d3dkmthk.h (include D3dkmthk.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/hh439432">D3DKMTOutputDuplPresent</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/hh406554">D3DKMT_QUERYREMOTEVIDPNSOURCEFROMGDIDISPLAYNAME</a>