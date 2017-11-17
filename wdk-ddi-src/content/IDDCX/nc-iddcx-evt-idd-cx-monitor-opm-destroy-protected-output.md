---
UID: NC.iddcx.EVT_IDD_CX_MONITOR_OPM_DESTROY_PROTECTED_OUTPUT
title: EVT_IDD_CX_MONITOR_OPM_DESTROY_PROTECTED_OUTPUT
author: windows-driver-content
description: EVT_IDD_CX_MONITOR_OPM_DESTROY_PROTECTED_OUTPUT is called by the OS to destroy an OPM protected output context.
old-location: display\evt_idd_cx_monitor_opm_destroy_protected_output.htm
ms.assetid: 86bd815f-b413-4680-9679-8778a47a0e27
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: callback
ms.prod: windows-hardware
ms.technology: display
req.header: iddcx.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PFN_IDD_CX_MONITOR_OPM_DESTROY_PROTECTED_OUTPUT
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
ms.keywords: WcsTranslateColors
req.iface: 
---

# EVT_IDD_CX_MONITOR_OPM_DESTROY_PROTECTED_OUTPUT callback



## -description
<p><b>EVT_IDD_CX_MONITOR_OPM_DESTROY_PROTECTED_OUTPUT</b> is called by the OS to destroy an OPM protected output context.</p>


## -prototype

````
EVT_IDD_CX_MONITOR_OPM_DESTROY_PROTECTED_OUTPUT EvtIddCxMonitorOpmDestroyProtectedOutput;

NTSTATUS EvtIddCxMonitorOpmDestroyProtectedOutput(
  _In_ IDDCX_OPMCTX OpmCxtObject
)
{ ... }

typedef EVT_IDD_CX_MONITOR_OPM_DESTROY_PROTECTED_OUTPUT PFN_IDD_CX_MONITOR_OPM_DESTROY_PROTECTED_OUTPUT;
````


## -parameters
<dl>

### -param <i>OpmCxtObject</i> [in]

<dd>
<p>
                    
                The object for the OPM context that will be destroyed.</p>
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