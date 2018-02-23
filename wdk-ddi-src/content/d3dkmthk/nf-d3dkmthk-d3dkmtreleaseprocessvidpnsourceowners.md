---
UID: NF:d3dkmthk.D3DKMTReleaseProcessVidPnSourceOwners
title: D3DKMTReleaseProcessVidPnSourceOwners function
author: windows-driver-content
description: The D3DKMTReleaseProcessVidPnSourceOwners function releases the video present network source owners for a process.
old-location: display\d3dkmtreleaseprocessvidpnsourceowners.htm
old-project: display
ms.assetid: 65fa0654-25b5-4ead-ac9e-0eb0f404259a
ms.author: windowsdriverdev
ms.date: 2/20/2018
ms.keywords: OpenGL_Functions_8c1e2870-c803-4ca4-99f1-8f39a00983c8.xml, D3DKMTReleaseProcessVidPnSourceOwners, d3dkmthk/D3DKMTReleaseProcessVidPnSourceOwners, display.d3dkmtreleaseprocessvidpnsourceowners, D3DKMTReleaseProcessVidPnSourceOwners function [Display Devices]
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: d3dkmthk.h
req.include-header: D3dkmthk.h
req.target-type: Universal
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
req.lib: Gdi32.lib
req.dll: Gdi32.dll
req.irql: 
topictype:
-	APIRef
-	kbSyntax
apitype:
-	DllExport
apilocation:
-	Gdi32.dll
-	API-MS-Win-dx-d3dkmt-l1-1-0.dll
-	API-MS-Win-dx-d3dkmt-l1-1-1.dll
-	API-MS-Win-DX-D3DKMT-L1-1-2.dll
apiname:
-	D3DKMTReleaseProcessVidPnSourceOwners
product: Windows
targetos: Windows
req.typenames: D3DKMT_DRIVERVERSION
---


# D3DKMTReleaseProcessVidPnSourceOwners function
The <b>D3DKMTReleaseProcessVidPnSourceOwners</b> function releases the video present network source owners for a process.

## Syntax

````
NTSTATUS APIENTRY D3DKMTReleaseProcessVidPnSourceOwners(
  _In_ HANDLE hProcess
);
````

## Parameters

This function has no parameters.

## Return Value

<b>D3DKMTReleaseProcessVidPnSourceOwners</b> returns one of the following values:

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
The video present network source owners for a process were successfully released.

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
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems.  |
| **Target Platform** | Universal |
| **Header** | d3dkmthk.h (include D3dkmthk.h) |
| **Library** | Gdi32.lib |
| **DLL** | Gdi32.dll |