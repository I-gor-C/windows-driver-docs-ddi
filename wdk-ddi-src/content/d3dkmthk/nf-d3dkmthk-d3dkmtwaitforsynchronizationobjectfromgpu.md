---
UID: NF.d3dkmthk.D3DKMTWaitForSynchronizationObjectFromGpu
title: D3DKMTWaitForSynchronizationObjectFromGpu function
author: windows-driver-content
description: D3DKMTWaitForSynchronizationObjectFromGpu waits for a monitored fence to reach a certain value before processing subsequent context commands.
old-location: display\d3dkmtwaitforsynchronizationobjectfromgpu.htm
old-project: display
ms.assetid: 93705446-8B87-46DD-9CFE-DD0473DEE6B6
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: D3DKMTWaitForSynchronizationObjectFromGpu
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
req.alt-api: D3DKMTWaitForSynchronizationObjectFromGpu
req.alt-loc: GDI32.dll,API-MS-Win-DX-D3DKMT-L1-1-1.dll,GDI32.dll,API-MS-Win-DX-D3DKMT-L1-1-2.dll
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
---

# D3DKMTWaitForSynchronizationObjectFromGpu function



## -description
<b>D3DKMTWaitForSynchronizationObjectFromGpu</b> waits for a monitored fence to reach a certain value before processing subsequent context commands.


## -syntax

````
EXTERN_C _Check_return_ NTSTATUS APIENTRY D3DKMTWaitForSynchronizationObjectFromGpu(
  _In_ const D3DKMT_WAITFORSYNCHRONIZATIONOBJECTFROMGPU *pData
);
````


## -parameters

### -param pData [in]

A pointer to a <a href="display.d3dkmt_waitforsynchronizationobjectfromgpu">D3DKMT_WAITFORSYNCHRONIZATIONOBJECTFROMGPU</a> structure that describes the operation.

## -returns
Returns one of the following values:
<dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl>The operation was performed successfully.
<dl>
<dt><b>STATUS_INVALID_PARAMETER </b></dt>
</dl>
         Parameters were validated and determined to be incorrect.

 

This function might also return other <b>NTSTATUS</b> values.

## -remarks
This function semantics are similar to existing <a href="display.d3dkmtwaitforsynchronizationobject2">D3DKMTWaitForSynchronizationObject2</a> call, except that this function also supports monitored fence objects and an array of monitored fence values to wait for.

## -requirements
<table>
<tr>
<th width="30%">
Minimum supported client
</th>
<td width="70%">
Windows 10
</td>
</tr>
<tr>
<th width="30%">
Minimum supported server
</th>
<td width="70%">
Windows Server 2016
</td>
</tr>
<tr>
<th width="30%">
Target platform
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Header
</th>
<td width="70%">
<dl>
<dt>D3dkmthk.h (include D3dkmthk.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library
</th>
<td width="70%">
<dl>
<dt>GDI32.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
DLL
</th>
<td width="70%">
<dl>
<dt>GDI32.dll</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="display.d3dkmt_waitforsynchronizationobjectfromgpu">D3DKMT_WAITFORSYNCHRONIZATIONOBJECTFROMGPU</a>
</dt>
<dt>
<a href="display.d3dkmtwaitforsynchronizationobject">D3DKMTWaitForSynchronizationObject</a>
</dt>
<dt>
<a href="display.d3dkmtwaitforsynchronizationobject2">D3DKMTWaitForSynchronizationObject2</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DKMTWaitForSynchronizationObjectFromGpu function%20 RELEASE:%20(12/6/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
