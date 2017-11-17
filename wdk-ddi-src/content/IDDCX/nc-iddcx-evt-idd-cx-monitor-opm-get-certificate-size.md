---
UID: NC.iddcx.EVT_IDD_CX_MONITOR_OPM_GET_CERTIFICATE_SIZE
title: EVT_IDD_CX_MONITOR_OPM_GET_CERTIFICATE_SIZE
author: windows-driver-content
description: EVT_IDD_CX_MONITOR_OPM_GET_CERTIFICATE_SIZE is called by the OS to get the size of an OPM certificate.
old-location: display\evt_idd_cx_monitor_opm_get_certificate_size.htm
ms.assetid: f5293625-19eb-4df9-9934-1e1990b7d608
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
req.alt-api: PFN_IDD_CX_MONITOR_OPM_GET_CERTIFICATE_SIZE
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

# EVT_IDD_CX_MONITOR_OPM_GET_CERTIFICATE_SIZE callback



## -description
<p><b>EVT_IDD_CX_MONITOR_OPM_GET_CERTIFICATE_SIZE</b> is called by the OS to get the size of an OPM certificate.</p>


## -prototype

````
EVT_IDD_CX_MONITOR_OPM_GET_CERTIFICATE_SIZE EvtIddCxMonitorOpmGetCertificateSize;

NTSTATUS EvtIddCxMonitorOpmGetCertificateSize(
  _In_        IDDCX_ADAPTER                       AdapterObject,
  _In_  const IDARG_IN_OPM_GET_CERTIFICATE_SIZE*  pInArgs,
  _Out_       IDARG_OUT_OPM_GET_CERTIFICATE_SIZE* pOutArgs
)
{ ... }

typedef EVT_IDD_CX_MONITOR_OPM_GET_CERTIFICATE_SIZE PFN_IDD_CX_MONITOR_OPM_GET_CERTIFICATE_SIZE;
````


## -parameters
<dl>

### -param <i>AdapterObject</i> [in]

<dd>
<p>
                    
                The object for the adapter that the OPM certificate size will be gotten for.</p>
</dd>

### -param <i>pInArgs</i> [in]

<dd>
<p>
                    
                Input arguments used by <b>EVT_IDD_CX_MONITOR_OPM_GET_CERTIFICATE_SIZE</b>.</p>
</dd>

### -param <i>pOutArgs</i> [out]

<dd>
<p>
                    
                Output arguments returned by <b>EVT_IDD_CX_MONITOR_OPM_GET_CERTIFICATE_SIZE</b>.</p>
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