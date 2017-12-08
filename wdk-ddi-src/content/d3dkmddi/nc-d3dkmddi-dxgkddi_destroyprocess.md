---
UID: NC.d3dkmddi.DXGKDDI_DESTROYPROCESS
title: DXGKDDI_DESTROYPROCESS
author: windows-driver-content
description: DxgkDdiDestroyProcess destroys a kernel mode driver process object.
old-location: display\dxgkddidestroyprocess.htm
old-project: display
ms.assetid: C5117F9B-876D-4F74-B528-47698666B44B
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: _DD_MULTISAMPLEQUALITYLEVELSDATA, DD_MULTISAMPLEQUALITYLEVELSDATA
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3dkmddi.h
req.include-header: Dispmprt.h
req.target-type: Desktop
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DxgkDdiDestroyProcess
req.alt-loc: dispmprt.h,d3dkmddi.h
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
---

# DXGKDDI_DESTROYPROCESS callback



## -description
<b>DxgkDdiDestroyProcess</b> destroys a kernel mode driver process object.


## -prototype

````
PDXGKDDI_DESTROYPROCESS DxgkDdiDestroyProcess;

NTSTATUS APIENTRY DxgkDdiDestroyProcess(
  _In_ const HANDLE hAdapter,
  _In_ const HANDLE hKmdProcess
)
{ ... }
````


## -parameters

### -param hAdapter [in]

A handle to the display adapter.

### -param hKmdProcess [in]

A handle to the kernel mode driver process.

## -returns

      Returns <b>STATUS_SUCCESS</b> if it succeeds. Otherwise, it returns one of the error codes defined in <b>Ntstatus.h</b>.

## -remarks


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
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Header
</th>
<td width="70%">
<dl>
<dt>Dispmprt.h (include Dispmprt.h); </dt>
<dt>D3dkmddi.h (include D3dkmddi.h)</dt>
</dl>
</td>
</tr>
</table>