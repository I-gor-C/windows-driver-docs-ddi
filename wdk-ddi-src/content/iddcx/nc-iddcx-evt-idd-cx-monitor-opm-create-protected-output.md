---
UID: NC.iddcx.EVT_IDD_CX_MONITOR_OPM_CREATE_PROTECTED_OUTPUT
title: EVT_IDD_CX_MONITOR_OPM_CREATE_PROTECTED_OUTPUT
author: windows-driver-content
description: EVT_IDD_CX_MONITOR_OPM_CREATE_PROTECTED_OUTPUT is called by the OS to create an OPM protected output context.
old-location: display\evt_idd_cx_monitor_opm_create_protected_output.htm
old-project: display
ms.assetid: 16c6fda5-c2e1-4ee4-80f7-e970b1da0e01
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
req.alt-api: PFN_IDD_CX_MONITOR_OPM_CREATE_PROTECTED_OUTPUT
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

# EVT_IDD_CX_MONITOR_OPM_CREATE_PROTECTED_OUTPUT callback



## -description
<p><b>EVT_IDD_CX_MONITOR_OPM_CREATE_PROTECTED_OUTPUT</b> is called by the OS to create an OPM protected output context.</p>


## -prototype

````
EVT_IDD_CX_MONITOR_OPM_CREATE_PROTECTED_OUTPUT EvtIddCxMonitorOpmCreateProtectedOutput;

NTSTATUS EvtIddCxMonitorOpmCreateProtectedOutput(
  _In_       IDDCX_MONITOR                         MonitorObject,
  _In_       IDDCX_OPMCTX                          OpmCxtObject,
  _In_ const IDARG_IN_OPM_CREATE_PROTECTED_OUTPUT* pInArgs
)
{ ... }

typedef EVT_IDD_CX_MONITOR_OPM_CREATE_PROTECTED_OUTPUT PFN_IDD_CX_MONITOR_OPM_CREATE_PROTECTED_OUTPUT;
````


## -parameters
<dl>

### -param MonitorObject [in]

<dd>
<p>
                    
                A handle used by the OS to identify the monitor that the OPM context should be created on.</p>
</dd>

### -param OpmCxtObject [in]

<dd>
<p>
                    
                A context used by the OS to identify the OPM context the call is for.</p>
</dd>

### -param pInArgs [in]

<dd>
<p>
                    
                Input arguments used by <b>EVT_IDD_CX_MONITOR_OPM CREATE_PROTECTED_OUTPUT</b>.</p>
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