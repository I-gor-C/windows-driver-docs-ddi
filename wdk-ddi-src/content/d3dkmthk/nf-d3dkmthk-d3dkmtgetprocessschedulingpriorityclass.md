---
UID: NF.d3dkmthk.D3DKMTGetProcessSchedulingPriorityClass
title: D3DKMTGetProcessSchedulingPriorityClass function
author: windows-driver-content
description: The D3DKMTGetProcessSchedulingPriorityClass function retrieves the scheduling priority for a process.
old-location: display\d3dkmtgetprocessschedulingpriorityclass.htm
old-project: display
ms.assetid: 994df4be-d0ce-4f64-91f5-b5516ce947ec
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: D3DKMTGetProcessSchedulingPriorityClass
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
req.alt-api: D3DKMTGetProcessSchedulingPriorityClass
req.alt-loc: Gdi32.dll,API-MS-Win-dx-d3dkmt-l1-1-0.dll,API-MS-Win-dx-d3dkmt-l1-1-1.dll,API-MS-Win-DX-D3DKMT-L1-1-2.dll
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
---

# D3DKMTGetProcessSchedulingPriorityClass function



## -description
The <b>D3DKMTGetProcessSchedulingPriorityClass</b> function retrieves the scheduling priority for a process.



## -syntax

````
NTSTATUS D3DKMTGetProcessSchedulingPriorityClass(
  _In_  HANDLE                         hProcess,
  _Out_ D3DKMT_SCHEDULINGPRIORITYCLASS *pPriority
);
````


## -parameters

### -param hProcess [in]

A handle to the process for which scheduling priority is set.


### -param pPriority [out]

A pointer to a variable that receives a <a href="display.d3dkmt_schedulingpriorityclass">D3DKMT_SCHEDULINGPRIORITYCLASS</a>-typed value that indicates the priority level for the process.


## -returns
<b>D3DKMTGetProcessSchedulingPriorityClass</b> returns one of the following values:
<dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl>The scheduling priority was successfully retrieved.
<dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl>Parameters were validated and determined to be incorrect.

 

This function might also return other <b>NTSTATUS</b> values.


## -remarks


## -requirements
<table>
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
Version

</th>
<td width="70%">
Available in Windows Vista and later versions of the Windows operating systems.

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
<dt>Gdi32.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
DLL

</th>
<td width="70%">
<dl>
<dt>Gdi32.dll</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="display.d3dkmt_schedulingpriorityclass">D3DKMT_SCHEDULINGPRIORITYCLASS</a>
</dt>
<dt>
<a href="display.d3dkmtsetprocessschedulingpriorityclass">D3DKMTSetProcessSchedulingPriorityClass</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DKMTGetProcessSchedulingPriorityClass function%20 RELEASE:%20(12/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

