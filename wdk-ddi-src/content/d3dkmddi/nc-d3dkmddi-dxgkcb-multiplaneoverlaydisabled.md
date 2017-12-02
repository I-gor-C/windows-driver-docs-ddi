---
UID: NC.d3dkmddi.DXGKCB_MULTIPLANEOVERLAYDISABLED
title: DXGKCB_MULTIPLANEOVERLAYDISABLED
author: windows-driver-content
description: This callback allows the kernel mode driver to indicate that the current multiplane overlay configuration is no longer supported on the specified VidPnSourceId.
old-location: display\dxgkcb_multiplaneoverlaydisabled.htm
old-project: display
ms.assetid: EA9FAB26-1EAF-4E67-B240-094BC2B03DEF
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DD_MULTISAMPLEQUALITYLEVELSDATA, DD_MULTISAMPLEQUALITYLEVELSDATA
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3dkmddi.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGKCB_MULTIPLANEOVERLAYDISABLED
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
req.irql: requires_max_(PASSIVE_LEVEL)
req.iface: 
---

# DXGKCB_MULTIPLANEOVERLAYDISABLED callback



## -description
<p>This callback allows the kernel mode driver to indicate that the current multiplane overlay configuration is no longer supported on the specified VidPnSourceId.</p>


## -prototype

````
 APIENTRY DXGKCB_MULTIPLANEOVERLAYDISABLED(
  _In_ const HANDLE hAdapter,
  _In_ const UINT   VidPnSourceId
);
````


## -parameters
<dl>

### -param hAdapter [in]

<dd>
<p>Indicates the adapter on which the current multiplane overlay hardware configuration is no longer supported.</p>
</dd>

### -param VidPnSourceId [in]

<dd>
<p>Indicates the VidPnSourceId on which the current multiplane overlay hardware configuration is no longer supported.</p>
</dd>
</dl>

## -returns
<p>DXGKCB_MULTIPLANEOVERLAYDISABLED returns one of the following values:</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>If the call has been successfully completed.</p>

<p> </p>

## -remarks
<p>This callback will notify the DWM that the current MPO configuration is no longer supported, allowing the DWM to fall back to composition. 

This callback can only be called at passive level.
</p>

<p>This callback can be used in the following scenarios:

</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3dkmddi.h</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>requires_max_(PASSIVE_LEVEL)</p>
</td>
</tr>
</table>