---
UID: NC.d3dkmddi.DXGKCB_QUERYMONITORINTERFACE
title: DXGKCB_QUERYMONITORINTERFACE
author: windows-driver-content
description: The DxgkCbQueryMonitorInterface function returns a pointer to a DXGK_MONITOR_INTERFACE structure.
old-location: display\dxgkcbquerymonitorinterface.htm
old-project: display
ms.assetid: 0c23e72d-3eb9-4511-a386-1dcc2f4910b7
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DD_MULTISAMPLEQUALITYLEVELSDATA, DD_MULTISAMPLEQUALITYLEVELSDATA
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3dkmddi.h
req.include-header: Dispmprt.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DxgkCbQueryMonitorInterface
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
req.irql: <= APC_LEVEL
req.iface: 
---

# DXGKCB_QUERYMONITORINTERFACE callback



## -description
<p>The <b>DxgkCbQueryMonitorInterface</b> function returns a pointer to a <a href="..\d3dkmddi\ns-d3dkmddi--dxgk-monitor-interface.md">DXGK_MONITOR_INTERFACE</a> structure. The structure contains pointers to functions that the display miniport driver can call to obtain other interfaces that provide access to monitor descriptors, modes, and frequency ranges.</p>


## -prototype

````
DXGKCB_QUERYMONITORINTERFACE DxgkCbQueryMonitorInterface;

NTSTATUS APIENTRY DxgkCbQueryMonitorInterface(
  _In_  const HANDLE                         hAdapter,
  _In_  const DXGK_MONITOR_INTERFACE_VERSION MonitorInterfaceVersion,
  _Out_ const DXGK_MONITOR_INTERFACE         **ppMonitorInterface
)
{ ... }
````


## -parameters
<dl>

### -param hAdapter [in]

<dd>
<p>[in] A handle that represents a display adapter. The VidPN manager provided this handle to the display miniport driver in a call to <a href="display.dxgkddirecommendfunctionalvidpn">DxgkDdiRecommendFunctionalVidPn</a>, <a href="display.dxgkddiissupportedvidpn">DxgkDdiIsSupportedVidPn</a>, <a href="display.dxgkddienumvidpncofuncmodality">DxgkDdiEnumVidPnCofuncModality</a>, or <a href="display.dxgkddicommitvidpn">DxgkDdiCommitVidPn</a>.</p>
</dd>

### -param MonitorInterfaceVersion [in]

<dd>
<p>[in] A value from the <a href="..\d3dkmddi\ne-d3dkmddi--dxgk-monitor-interface-version.md">DXGK_MONITOR_INTERFACE_VERSION</a> enumeration that specifies the version of the monitor interface being requested.</p>
</dd>

### -param ppMonitorInterface [out]

<dd>
<p>[out] A pointer to a variable that receives a pointer to the <a href="..\d3dkmddi\ns-d3dkmddi--dxgk-monitor-interface.md">DXGK_MONITOR_INTERFACE</a> structure.</p>
</dd>
</dl>

## -returns
<p><b>DxgkCbQueryMonitorInterface</b> returns STATUS_SUCCESS if it succeeds. Otherwise, it returns one of the error codes defined in <i>Ntstatus.</i>h. </p>

<p>The following code example shows how to acquire the monitor-management interface from the Microsoft DirectX graphics kernel subsystem (<i>Dxgkrnl.sys</i>) and use the monitor-management interface to retrieve the monitor-frequency-range-set object.</p>

## -remarks


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
<dt>D3dkmddi.h (include Dispmprt.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;= APC_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="display.monitor_interface">Monitor Interface</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGKCB_QUERYMONITORINTERFACE callback function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
