---
UID: NS.pepfx._PEP_PPM_CST_STATES
title: PEP_PPM_CST_STATES
author: windows-driver-content
description: The PEP_PPM_CST_STATES structure specifies the properties of the C states (ACPI processor power states) that are supported for a processor.
old-location: kernel\pep_ppm_cst_states.htm
old-project: kernel
ms.assetid: 4E620796-3065-469E-8E91-8F698F672CAE
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: PEP_PPM_CST_STATES, PEP_PPM_CST_STATES, *PPEP_PPM_CST_STATES
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: pepfx.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Supported starting with Windows 10.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PEP_PPM_CST_STATES
req.alt-loc: pepfx.h
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

# PEP_PPM_CST_STATES structure



## -description
<p>The <b>PEP_PPM_CST_STATES</b> structure specifies the properties of the C states (ACPI processor power states) that are supported for a processor.</p>


## -syntax

````
typedef struct _PEP_PPM_CST_STATES {
  ULONG              Count;
  PPEP_PPM_CST_STATE IdleStates;
} PEP_PPM_CST_STATES, *PPEP_PPM_CST_STATES;
````


## -struct-fields
<dl>

### -field Count

<dd>
<p>The number of elements in the <b>IdleStates</b> array.</p>
</dd>

### -field IdleStates

<dd>
<p>A pointer to an array of <a href="..\pepfx\ns-pepfx--pep-ppm-cst-state.md">PEP_PPM_CST_STATE</a> structures.</p>
</dd>
</dl>

## -remarks
<p>This structure is used by the <a href="kernel.pep_notify_ppm_cst_states">PEP_NOTIFY_PPM_CST_STATES</a> notification. The contents of this structure are obtained from the _CST object that is located in the ACPI namespace for the processor. </p>

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
<dt>Pepfx.h</dt>
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
<a href="..\pepfx\ns-pepfx--pep-ppm-cst-state.md">PEP_PPM_CST_STATE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20PEP_PPM_CST_STATES structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
