---
UID: NE.d3dkmdt._D3DKMDT_MONITOR_CONNECTIVITY_CHECKS
title: D3DKMDT_MONITOR_CONNECTIVITY_CHECKS
author: windows-driver-content
description: The D3DKMDT_MONITOR_CONNECTIVITY_CHECKS enumerated type indicates whether the DxgkDdiCommitVidPn function should verify that certain video outputs have connected monitors.
old-location: display\d3dkmdt_monitor_connectivity_checks.htm
ms.assetid: 8a32fef1-e404-478d-8b99-064ed456e37c
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: display
req.header: d3dkmdt.h
req.include-header: D3dkmdt.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DKMDT_MONITOR_CONNECTIVITY_CHECKS
req.alt-loc: d3dkmdt.h
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
ms.keywords: DXGK_CHECK_MULTIPLANE_OVERLAY_SUPPORT_RETURN_INFO, DXGK_CHECK_MULTIPLANE_OVERLAY_SUPPORT_RETURN_INFO
req.iface: 
---

# D3DKMDT_MONITOR_CONNECTIVITY_CHECKS enumeration



## -description
<p>The D3DKMDT_MONITOR_CONNECTIVITY_CHECKS enumerated type indicates whether the <a href="https://msdn.microsoft.com/979b86e9-f3ff-4022-8c00-b6afc2b1f747">DxgkDdiCommitVidPn</a> function should verify that certain video outputs have connected monitors.</p>


## -syntax

````
typedef enum _D3DKMDT_MONITOR_CONNECTIVITY_CHECKS { 
  D3DKMDT_MCC_UNINITIALIZED  = 0,
  D3DKMDT_MCC_IGNORE         = 1,
  D3DKMDT_MCC_ENFORCE        = 2
} D3DKMDT_MONITOR_CONNECTIVITY_CHECKS;
````


## -enum-fields
<dl>

### -field <a id="D3DKMDT_MCC_UNINITIALIZED"></a><a id="d3dkmdt_mcc_uninitialized"></a><b>D3DKMDT_MCC_UNINITIALIZED</b>

<dd>
<p>Indicates that a variable of type D3DKMDT_MONITOR_CONNECTIVITY_CHECKS has not yet been assigned a meaningful value.</p>
</dd>

### -field <a id="D3DKMDT_MCC_IGNORE"></a><a id="d3dkmdt_mcc_ignore"></a><b>D3DKMDT_MCC_IGNORE</b>

<dd>
<p>Indicates that <b>DxgkDdiCommitVidPn</b> does not need to verify that monitors are connected.</p>
</dd>

### -field <a id="D3DKMDT_MCC_ENFORCE"></a><a id="d3dkmdt_mcc_enforce"></a><b>D3DKMDT_MCC_ENFORCE</b>

<dd>
<p>Indicates that <b>DxgkDdiCommitVidPn</b> must verify that monitors are connected.</p>
</dd>
</dl>

## -remarks
<p>The <b>MonitorConnectivityChecks</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff557552">DXGKARG_COMMITVIDPN</a> structure is a D3DKMDT_MONITOR_CONNECTIVITY_CHECKS value.</p>

<p>The <b>MonitorConnectivityChecks</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff557552">DXGKARG_COMMITVIDPN</a> structure is a D3DKMDT_MONITOR_CONNECTIVITY_CHECKS value.</p>

<p>The <b>MonitorConnectivityChecks</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff557552">DXGKARG_COMMITVIDPN</a> structure is a D3DKMDT_MONITOR_CONNECTIVITY_CHECKS value.</p>

## -requirements
<table>
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
<dt>D3dkmdt.h (include D3dkmdt.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/979b86e9-f3ff-4022-8c00-b6afc2b1f747">DxgkDdiCommitVidPn</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DKMDT_MONITOR_CONNECTIVITY_CHECKS enumeration%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
