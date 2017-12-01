---
UID: NC.wdm.PO_FX_COMPONENT_PERF_STATE_CALLBACK
title: PO_FX_COMPONENT_PERF_STATE_CALLBACK
author: windows-driver-content
description: The ComponentPerfStateCallback callback routine notifies the driver that its request to change the performance state of a component is complete.
old-location: kernel\componentperfstatecallback.htm
old-project: kernel
ms.assetid: A54376E6-FBA2-4A27-83C7-8E3B6F2B2A05
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: WDI_TYPE_PMK_NAME, WDI_TYPE_PMK_NAME, *PWDI_TYPE_PMK_NAME
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: wdm.h
req.include-header: 
req.target-type: Desktop
req.target-min-winverclnt: Supported starting with Windows 10.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ComponentPerfStateCallback
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
req.irql: Called at IRQL <= DISPATCH_LEVEL.
req.iface: 
req.product: Windows 10 or later.
---

# PO_FX_COMPONENT_PERF_STATE_CALLBACK callback



## -description
<p>The <i>ComponentPerfStateCallback</i> callback routine notifies the driver that its request to change the performance state of a component is complete.</p>


## -prototype

````
PO_FX_COMPONENT_PERF_STATE_CALLBACK ComponentPerfStateCallback;

VOID CALLBACK ComponentPerfStateCallback(
  _In_ PVOID   Context,
  _In_ ULONG   Component,
  _In_ BOOLEAN Succeeded,
  _In_ PVOID   RequestContext
)
{ ... }
````


## -parameters
<dl>

### -param <i>Context</i> [in]

<dd>
<p>A pointer to the device context. The device driver uses this context to store information about the current power state of the device. The device driver specified this pointer in the <b>DeviceContext</b> member of the <a href="kernel.po_fx_device">PO_FX_DEVICE</a> structure that the driver used to register the device with the power management framework (PoFx). This context is opaque to PoFx.</p>
</dd>

### -param <i>Component</i> [in]

<dd>
<p>Specifies the index that identifies the component. This parameter is an index into the <b>Components</b> array in the <b>PO_FX_DEVICE</b> structure that the device driver used to register the device with PoFx. If the <b>Components</b> array contains N elements, component indexes range from 0 to N–1.</p>
</dd>

### -param <i>Succeeded</i> [in]

<dd>
<p>If TRUE, the platform extension plug-in (PEP) succeeded the performance state change. If FALSE, the PEP failed the performance state change. For more information, see the Remarks section.</p>
</dd>

### -param <i>RequestContext</i> [in]

<dd>
<p>Pointer to the optional driver or device context that was specified by the <i>Context</i> parameter of the <a href="..\wdm\nf-wdm-pofxissuecomponentperfstatechange.md">PoFxIssueComponentPerfStateChange</a> or <a href="..\wdm\nf-wdm-pofxissuecomponentperfstatechangemultiple.md">PoFxIssueComponentPerfStateChangeMultiple</a> routine.</p>
</dd>
</dl>

## -returns
<p>None.</p>

## -remarks
<p>When a device driver requests a performance state change by calling the  <a href="..\wdm\nf-wdm-pofxissuecomponentperfstatechange.md">PoFxIssueComponentPerfStateChange</a> or <a href="..\wdm\nf-wdm-pofxissuecomponentperfstatechangemultiple.md">PoFxIssueComponentPerfStateChangeMultiple</a> routine, PoFx calls the <i>ComponentPerfStateCallback</i>  routine to notify the driver when the request is complete. </p>

<p>To specify a <i>ComponentPerfStateCallback</i> routine, use the <i>ComponentPerfStateCallback</i> parameter of the <a href="..\wdm\nf-wdm-pofxregistercomponentperfstates.md">PoFxRegisterComponentPerfStates</a> routine when the driver registers for performance state management by PoFx. The <i>ComponentPerfStateCallback</i> routine may be the same for all components and all devices.</p>

<p>If <i>Succeeded</i> is TRUE, the driver should perform whatever work is necessary to change the performance state in the hardware. If <i>Succeeded</i> is FALSE, the driver may choose to do nothing or retry the request with the same performance state or an alternate performance state.  
</p>

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
<p>Supported starting with Windows 10.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdm.h</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>Called at IRQL &lt;= DISPATCH_LEVEL.</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdm\nf-wdm-pofxregisterdevice.md">PoFxRegisterDevice</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-pofxissuecomponentperfstatechange.md">PoFxIssueComponentPerfStateChange</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-pofxissuecomponentperfstatechangemultiple.md">PoFxIssueComponentPerfStateChangeMultiple</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20ComponentPerfStateCallback routine%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
