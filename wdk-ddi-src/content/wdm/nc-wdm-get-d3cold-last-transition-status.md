---
UID: NC.wdm.GET_D3COLD_LAST_TRANSITION_STATUS
title: GET_D3COLD_LAST_TRANSITION_STATUS
author: windows-driver-content
description: The GetLastTransitionStatus routine enables the driver for a device to query whether the most recent transition to the D3hot substate was followed by a transition to the D3cold substate.
old-location: kernel\getlasttransitionstatus.htm
old-project: kernel
ms.assetid: 2ED5A28B-8668-411D-9462-8D6ED2F08B35
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: WDI_TYPE_PMK_NAME, WDI_TYPE_PMK_NAME, *PWDI_TYPE_PMK_NAME
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: wdm.h
req.include-header: Wdm.h
req.target-type: Desktop
req.target-min-winverclnt: Available starting with Windows 8.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: GetLastTransitionStatus
req.alt-loc: Wdm.h
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
req.product: Windows 10 or later.
---

# GET_D3COLD_LAST_TRANSITION_STATUS callback



## -description
<p>The <i>GetLastTransitionStatus</i> routine enables the driver for a device to query whether the most recent transition to the D3hot substate was followed by a transition to the D3cold substate.</p>


## -prototype

````
GET_D3COLD_LAST_TRANSITION_STATUS GetLastTransitionStatus;

VOID GetLastTransitionStatus(
  _In_opt_ PVOID                          Context,
  _Out_    PD3COLD_LAST_TRANSITION_STATUS LastTransitionStatus
)
{ ... }
````


## -parameters
<dl>

### -param <i>Context</i> [in, optional]

<dd>
<p>A pointer to interface-specific context information. The caller sets this parameter to the value of the <b>Context</b> member of the <a href="..\wdm\ns-wdm--d3cold-support-interface.md">D3COLD_SUPPORT_INTERFACE</a> structure for the interface.</p>
</dd>

### -param <i>LastTransitionStatus</i> [out]

<dd>
<p>A pointer to a variable into which the routine writes one of the following <a href="..\wdm\ne-wdm--d3cold-last-transition-status.md">D3COLD_LAST_TRANSITION_STATUS</a> enumeration values:</p>
<ul>
<li><b>LastDStateTransitionStatusUnknown</b></li>
<li><b>LastDStateTransitionD3hot</b></li>
<li><b>LastDStateTransitionD3cold</b></li>
</ul>
<p> The <b>LastDStateTransitionD3cold</b> value indicates that the most recent transition to D3hot was followed by a transition to D3cold. For more information, see Remarks.</p>
</dd>
</dl>

## -returns
<p>None.</p>

## -remarks
<p>This routine tries to get the information needed to answer the caller's query from the parent bus driver and platform firmware. If this information is not available, the routine writes the value <b>LastDStateTransitionStatusUnknown</b> to the location pointed to by <i>the LastTransitionStatus</i> parameter.</p>

<p>For more information, see <a href="..\wdm\ne-wdm--d3cold-last-transition-status.md">D3COLD_LAST_TRANSITION_STATUS</a>.</p>

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
<p>Available starting with Windows 8.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdm.h (include Wdm.h)</dt>
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

## -see-also
<dl>
<dt>
<a href="..\wdm\ne-wdm--d3cold-last-transition-status.md">D3COLD_LAST_TRANSITION_STATUS</a>
</dt>
<dt>
<a href="..\wdm\ns-wdm--d3cold-support-interface.md">D3COLD_SUPPORT_INTERFACE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20GET_D3COLD_LAST_TRANSITION_STATUS routine%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
