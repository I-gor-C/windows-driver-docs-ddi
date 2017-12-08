---
UID: NS.PEPFX._PEP_PROCESSOR_PERF_STATE
title: _PEP_PROCESSOR_PERF_STATE
author: windows-driver-content
description: Use in the PEP_NOTIFY_PPM_QUERY_DISCRETE_PERF_STATES  notification. This structure describes the properties of a single performance state.  .
old-location: kernel\pep_processor_perf_state.htm
old-project: kernel
ms.assetid: 46231ac0-2c34-4154-8b3e-f34c40cbff4a
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: _PEP_PROCESSOR_PERF_STATE, *PPEP_PROCESSOR_PERF_STATE, PEP_PROCESSOR_PERF_STATE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: pepfx.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10, version 1709
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PEP_PROCESSOR_PERF_STATE
req.alt-loc: Pepfx.h
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
---

# _PEP_PROCESSOR_PERF_STATE structure



## -description
Use in the <b>PEP_NOTIFY_PPM_QUERY_DISCRETE_PERF_STATES</b>  notification. This structure describes the properties of a single performance state.  


## -syntax

````
typedef struct _PEP_PROCESSOR_PERF_STATE {
  ULONG     Performance;
  ULONG     Frequency;
  ULONG [4] Reserved;
} PEP_PROCESSOR_PERF_STATE, PEP_PROCESSOR_PERF_STATE;
````


## -struct-fields

### -field Performance

On output, the performance level (on the scale returned by the <a href="kernel.pep_query_component_perf_capabilities">PEP_QUERY_COMPONENT_PERF_CAPABILITIES</a> notification) of this performance state.

### -field Frequency

On output, the frequency (in MHz) of this performance state. 

### -field Reserved

Reserved.

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Minimum supported client
</th>
<td width="70%">
Windows 10, version 1709
</td>
</tr>
<tr>
<th width="30%">
Minimum supported server
</th>
<td width="70%">
Windows Server 2016
</td>
</tr>
<tr>
<th width="30%">
Header
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
<a href="kernel._pep_ppm_query_discrete_perf_states">PEP_PPM_QUERY_DISCRETE_PERF_STATES</a>
</dt>
<dt>
<a href="kernel.processor_power_management__ppm__notifications">Processor power management (PPM) notifications</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20PEP_PROCESSOR_PERF_STATE structure%20 RELEASE:%20(12/6/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
