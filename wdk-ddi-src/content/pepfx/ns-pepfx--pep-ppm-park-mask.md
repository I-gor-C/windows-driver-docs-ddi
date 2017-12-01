---
UID: NS.pepfx._PEP_PPM_PARK_MASK
title: PEP_PPM_PARK_MASK
author: windows-driver-content
description: The PEP_PROCESSOR_PARK_MASK structure contains the current core parking mask.
old-location: kernel\pep_ppm_park_mask.htm
old-project: kernel
ms.assetid: 528576FD-BDB2-4772-9151-A1C855BA953E
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: PEP_PPM_PARK_MASK, PEP_PPM_PARK_MASK, *PPEP_PPM_PARK_MASK
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
req.alt-api: PEP_PPM_PARK_MASK
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

# PEP_PPM_PARK_MASK structure



## -description
<p>The <b>PEP_PROCESSOR_PARK_MASK</b> structure contains the current core parking mask.</p>


## -syntax

````
typedef struct _PEP_PPM_PARK_MASK {
  ULONG                                              Count;
  ULONGLONG                                          EvaluationTime;
  _Field_size_full_(Count) PPEP_PROCESSOR_PARK_STATE Processors;
} PEP_PPM_PARK_MASK, *PPEP_PPM_PARK_MASK;
````


## -struct-fields
<dl>

### -field <b>Count</b>

<dd>
<p>[in] Indicates the number of processors in the <b>Processors</b> array. </p>
</dd>

### -field <b>EvaluationTime</b>

<dd>
<p>[in] The interrupt time of the performance check evaluation that initiated this notification. </p>
</dd>

### -field <b>Processors</b>

<dd>
<p>[in/out] An array of processors in the core parking domain. </p>
<dl class="indent">

### -field <i>On input</i>

<dd>
<p>Indicates the OS parking preference for each processor.</p>
</dd>

### -field <i>On output</i>

<dd>
<p>Returns the PEP parking preference for each processor.</p>
</dd>
</dl>
<p>The Processors array is guaranteed to contain the processors in increasing order by processor index.
</p>
</dd>
</dl>

## -remarks


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
<a href="https://msdn.microsoft.com/library/windows/hardware/mt186768">PEP_NOTIFY_PPM_PARK_MASK notification</a>
</dt>
<dt>
<a href="..\pepfx\ns-pepfx--pep-processor-park-state.md">PEP_PROCESSOR_PARK_STATE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20PEP_PPM_PARK_MASK structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
