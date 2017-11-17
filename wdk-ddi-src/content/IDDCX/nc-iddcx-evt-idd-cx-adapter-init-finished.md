---
UID: NC.iddcx.EVT_IDD_CX_ADAPTER_INIT_FINISHED
title: EVT_IDD_CX_ADAPTER_INIT_FINISHED
author: windows-driver-content
description: EVT_IDD_CX_ADAPTER_INIT_FINISHED is called by the OS to inform the driver that the adapter initialization has completed.
old-location: display\evt_idd_cx_adapter_init_finished.htm
ms.assetid: cbce9e1b-2f84-4653-8d3d-e5243a1f0eee
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
req.alt-api: PFN_IDD_CX_ADAPTER_INIT_FINISHED
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

# EVT_IDD_CX_ADAPTER_INIT_FINISHED callback



## -description
<p><b>EVT_IDD_CX_ADAPTER_INIT_FINISHED</b> is called by the OS to inform the driver that the adapter initialization has completed.</p>


## -prototype

````
EVT_IDD_CX_ADAPTER_INIT_FINISHED EvtIddCxAdapterInitFinished;

NTSTATUS EvtIddCxAdapterInitFinished(
  _In_       IDDCX_ADAPTER AdapterObject,
  _In_ const               pInArgs
)
{ ... }

typedef EVT_IDD_CX_ADAPTER_INIT_FINISHED PFN_IDD_CX_ADAPTER_INIT_FINISHED;
````


## -parameters
<dl>

### -param <i>AdapterObject</i> [in]

<dd>
<p>
                    
                A handle provided by the driver used by the OS to reference the adapter in a call to the driver.</p>
</dd>

### -param <i>pInArgs</i> [in]

<dd>
<p>
                    
                Input arguments used by <b>EVT_IDD_CX_ADAPTER_COMMIT_MODES</b>.</p>
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