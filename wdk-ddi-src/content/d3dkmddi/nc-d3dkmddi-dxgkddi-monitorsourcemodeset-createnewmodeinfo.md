---
UID: NC.d3dkmddi.DXGKDDI_MONITORSOURCEMODESET_CREATENEWMODEINFO
title: DXGKDDI_MONITORSOURCEMODESET_CREATENEWMODEINFO
author: windows-driver-content
description: The pfnCreateNewModeInfo function returns a pointer to a D3DKMDT_MONITOR_SOURCE_MODE structure that the display miniport driver populates before calling pfnAddMode.
old-location: display\dxgk_monitorsourcemodeset_interface_pfncreatenewmodeinfo.htm
old-project: display
ms.assetid: 314b345c-a40b-418d-a2d8-c7b42e5fd27d
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DD_MULTISAMPLEQUALITYLEVELSDATA, DD_MULTISAMPLEQUALITYLEVELSDATA
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3dkmddi.h
req.include-header: D3dkmddi.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: pfnCreateNewModeInfo
req.alt-loc: d3dkmddi.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
---

# DXGKDDI_MONITORSOURCEMODESET_CREATENEWMODEINFO callback



## -description
<p>The <b>pfnCreateNewModeInfo</b> function returns a pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff546133">D3DKMDT_MONITOR_SOURCE_MODE</a> structure that the display miniport driver populates before calling <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi-monitorsourcemodeset-addmode.md">pfnAddMode</a>.</p>


## -prototype

````
DXGKDDI_MONITORSOURCEMODESET_CREATENEWMODEINFO pfnCreateNewModeInfo;

NTSTATUS APIENTRY pfnCreateNewModeInfo(
  _In_  const D3DKMDT_HMONITORSOURCEMODESET hMonitorSourceModeSet,
  _Out_       D3DKMDT_MONITOR_SOURCE_MODE   **ppNewMonitorSourceModeInfo
)
{ ... }
````


## -parameters
<dl>

### -param <i>hMonitorSourceModeSet</i> [in]

<dd>
<p>[in] A handle to a monitor source mode set object. The display miniport driver previously obtained this handle by calling the <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi-monitor-acquiremonitorsourcemodeset.md">pfnAcquireMonitorSourceModeSet</a> function of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff568433">Monitor interface</a>.</p>
</dd>

### -param <i>ppNewMonitorSourceModeInfo</i> [out]

<dd>
<p>[out] A pointer to a variable that receives a pointer to a newly created D3DKMDT_MONITOR_SOURCE_MODE structure allocated by the VidPN manager.</p>
</dd>
</dl>

## -returns
<p>The <b>pfnCreateNewModeInfo</b> function returns one of the following values.</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The function succeeded.</p><dl>
<dt><b>STATUS_NO_MEMORY</b></dt>
</dl><p>The function failed because it was unable to allocate enough memory.</p>

<p> </p>

## -remarks
<p>After you call <b>pfnCreateNewModeInfo</b> to obtain a D3DKMDT_MONITOR SOURCE_MODE structure, you must do one, but not both, of the following:</p>

<p>Populate the structure and pass it to <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi-monitorsourcemodeset-addmode.md">pfnAddMode</a>.</p>

<p>Release the structure by calling <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi-monitorsourcemodeset-releasemodeinfo.md">pfnReleaseModeInfo</a>.</p>

<p>After you call <b>pfnCreateNewModeInfo</b> to obtain a D3DKMDT_MONITOR SOURCE_MODE structure, you must do one, but not both, of the following:</p>

<p>Populate the structure and pass it to <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi-monitorsourcemodeset-addmode.md">pfnAddMode</a>.</p>

<p>Release the structure by calling <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi-monitorsourcemodeset-releasemodeinfo.md">pfnReleaseModeInfo</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows Vista and later versions of the Windows operating systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3dkmddi.h (include D3dkmddi.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>PASSIVE_LEVEL</p>
</td>
</tr>
</table>