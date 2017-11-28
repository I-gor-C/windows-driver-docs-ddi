---
UID: NC.iddcx.EVT_IDD_CX_MONITOR_SET_GAMMA_RAMP
title: EVT_IDD_CX_MONITOR_SET_GAMMA_RAMP
author: windows-driver-content
description: EVT_IDD_CX_MONITOR_SET_GAMMA_RAMP is called by the OS to set a gamma ramp on the specified monitor.
old-location: display\evt_idd_cx_monitor_set_gamma_ramp.htm
old-project: display
ms.assetid: 3e0828ee-307a-48fd-a8ea-b469ac6214d0
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: WcsTranslateColors
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: iddcx.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PFN_IDD_CX_MONITOR_SET_GAMMA_RAMP
req.alt-loc: iddcx.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: _requires_same_
req.iface: 
---

# EVT_IDD_CX_MONITOR_SET_GAMMA_RAMP callback



## -description
<p><b>EVT_IDD_CX_MONITOR_SET_GAMMA_RAMP</b> is called by the OS to set a gamma ramp on the specified monitor.</p>


## -prototype

````
EVT_IDD_CX_MONITOR_SET_GAMMA_RAMP EvtIddCxMonitorSetGammaRamp;

NTSTATUS EvtIddCxMonitorSetGammaRamp(
  _In_       IDDCX_MONITOR           MonitorObject,
  _In_ const IDARG_IN_SET_GAMMARAMP* pInArgs
)
{ ... }

typedef EVT_IDD_CX_MONITOR_SET_GAMMA_RAMP PFN_IDD_CX_MONITOR_SET_GAMMA_RAMP;
````


## -parameters
<dl>

### -param <i>MonitorObject</i> [in]

<dd>
<p>
                    
                A handle by the OS to identify the monitor to set a gamma ramp for.</p>
</dd>

### -param <i>pInArgs</i> [in]

<dd>
<p>
                    
                Input arguments used by <b>EVT_IDD_CX_MONITOR_SET_GAMMA_RAMP</b>.</p>
</dd>
</dl>

## -returns
<p>
(NTSTATUS) If the operation is successful, the callback function must return STATUS_SUCCESS, or another status value for which NT_SUCCESS(status) equals TRUE. Otherwise, an appropriate <a href="https://msdn.microsoft.com/7792201b-63bb-4db5-803d-2af02893d505">NTSTATUS</a> error code. 
                    </p>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 10</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2016</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Iddcx.h</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>_requires_same_</p>
</td>
</tr>
</table>