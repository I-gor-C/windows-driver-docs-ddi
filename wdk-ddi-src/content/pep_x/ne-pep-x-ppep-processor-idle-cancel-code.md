---
UID: NE.pep_x.PPEP_PROCESSOR_IDLE_CANCEL_CODE
title: PPEP_PROCESSOR_IDLE_CANCEL_CODE
author: windows-driver-content
description: The PEP_PROCESSOR_IDLE_CANCEL_CODE enumeration values indicate reasons why a processor cannot enter an idle state that was previously selected by the platform extension plug-in (PEP).
old-location: kernel\pep_processor_idle_cancel_code.htm
old-project: kernel
ms.assetid: 6112360C-B74F-4A77-8DE5-3EF1AAF49533
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: PO_FX_CORE_DEVICE, PO_FX_CORE_DEVICE, *PPO_FX_CORE_DEVICE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: pep_x.h
req.include-header: Pepfx.h
req.target-type: Windows
req.target-min-winverclnt: Supported starting with Windows 10.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PEP_PROCESSOR_IDLE_CANCEL_CODE
req.alt-loc: pep_x.h
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
---

# PPEP_PROCESSOR_IDLE_CANCEL_CODE enumeration



## -description
<p>The <b>PEP_PROCESSOR_IDLE_CANCEL_CODE</b> enumeration values indicate reasons why a processor cannot enter an idle state that was previously selected by the platform extension plug-in (PEP).</p>


## -syntax

````
typedef enum _PEP_PROCESSOR_IDLE_CANCEL_CODE { 
  PepIdleCancelWorkPending            = 0,
  PepIdleCancelDependencyCheckFailed,
  PepIdleCancelNoCState,
  PepIdleCancelMax
} PEP_PROCESSOR_IDLE_CANCEL_CODE;
````


## -enum-fields
<dl>

### -field <a id="PepIdleCancelWorkPending"></a><a id="pepidlecancelworkpending"></a><a id="PEPIDLECANCELWORKPENDING"></a><b>PepIdleCancelWorkPending</b>

<dd>
<p>The processor has pending work that prevents it from entering the selected idle state.</p>
</dd>

### -field <a id="PepIdleCancelDependencyCheckFailed"></a><a id="pepidlecanceldependencycheckfailed"></a><a id="PEPIDLECANCELDEPENDENCYCHECKFAILED"></a><b>PepIdleCancelDependencyCheckFailed</b>

<dd>
<p>The processor can enter the selected idle state only after one or more secondary processors have entered their corresponding idle states, but not all of these secondary processors have entered the correct idle states.</p>
</dd>

### -field <a id="PepIdleCancelNoCState"></a><a id="pepidlecancelnocstate"></a><a id="PEPIDLECANCELNOCSTATE"></a><b>PepIdleCancelNoCState</b>

<dd>
<p>The selected idle state corresponds to a C-state that is not supported. The PEP previously received a <a href="kernel.pep_notify_ppm_cst_states">PEP_NOTIFY_PPM_CST_STATES</a> notification that supplied a list of the supported C-states for this processor.</p>
</dd>

### -field <a id="PepIdleCancelMax"></a><a id="pepidlecancelmax"></a><a id="PEPIDLECANCELMAX"></a><b>PepIdleCancelMax</b>

<dd>
<p>Reserved for use by the operating system.</p>
</dd>
</dl>

## -remarks
<p>The <b>CancelCode</b> member of the <a href="..\pep_x\ns-pep-x--pep-ppm-idle-cancel.md">PEP_PPM_IDLE_CANCEL</a> structure contains a <b>PEP_PROCESSOR_IDLE_CANCEL_CODE</b> enumeration value.</p>

## -requirements
<table>
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
<dt>Pep_x.h (include Pepfx.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="kernel.pep_notify_ppm_cst_states">PEP_NOTIFY_PPM_CST_STATES</a>
</dt>
<dt>
<a href="..\pep_x\ns-pep-x--pep-ppm-idle-cancel.md">PEP_PPM_IDLE_CANCEL</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20PEP_PROCESSOR_IDLE_CANCEL_CODE enumeration%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
