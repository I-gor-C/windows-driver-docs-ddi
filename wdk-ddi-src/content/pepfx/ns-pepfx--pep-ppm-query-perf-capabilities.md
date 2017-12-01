---
UID: NS.pepfx._PEP_PPM_QUERY_PERF_CAPABILITIES
title: PEP_PPM_QUERY_PERF_CAPABILITIES
author: windows-driver-content
description: The PEP_PPM_QUERY_PERF_CAPABILITIES structure describes the performance capabilities of the processors in the specified processor performance domain.
old-location: kernel\pep_ppm_query_perf_capabilities.htm
old-project: kernel
ms.assetid: 562EA523-A74D-4D46-8C01-12C745106F86
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: PEP_PPM_QUERY_PERF_CAPABILITIES, PEP_PPM_QUERY_PERF_CAPABILITIES, *PPEP_PPM_QUERY_PERF_CAPABILITIES
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
req.alt-api: PEP_PPM_QUERY_PERF_CAPABILITIES
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

# PEP_PPM_QUERY_PERF_CAPABILITIES structure



## -description
<p>The <b>PEP_PPM_QUERY_PERF_CAPABILITIES</b> structure describes the performance capabilities of the processors in the specified processor performance domain.</p>


## -syntax

````
typedef struct _PEP_PPM_QUERY_PERF_CAPABILITIES {
  ULONG HighestPerformance;
  ULONG NominalPerformance;
  ULONG LowestNonlinearPerformance;
  ULONG LowestPerformance;
  ULONG DomainId;
  ULONG DomainMembers;
} PEP_PPM_QUERY_PERF_CAPABILITIES, *PPEP_PPM_QUERY_PERF_CAPABILITIES;
````


## -struct-fields
<dl>

### -field <b>HighestPerformance</b>

<dd>
<p>[out] The highest performance level in platform-specific units. For more information, see Remarks.</p>
</dd>

### -field <b>NominalPerformance</b>

<dd>
<p>[out] The nominal performance level in platform-specific units. For more information, see Remarks.</p>
</dd>

### -field <b>LowestNonlinearPerformance</b>

<dd>
<p>[out] The lowest nonlinear performance level in platform-specific units. For more information, see Remarks.</p>
</dd>

### -field <b>LowestPerformance</b>

<dd>
<p>[out] The lowest performance level in platform-specific units. For more information, see Remarks.</p>
</dd>

### -field <b>DomainId</b>

<dd>
<p>[out] The domain ID of the processor performance domain.</p>
</dd>

### -field <b>DomainMembers</b>

<dd>
<p>[out] The number of processors in this performance domain.</p>
</dd>
</dl>

## -remarks
<p>This structure is used by the <a href="kernel.pep_notify_ppm_query_perf_capabilities">PEP_NOTIFY_PPM_QUERY_PERF_CAPABILITIES</a> notification. All six members contain output values that the platform extension plug-in (PEP) writes to the structure in response to this notification.</p>

<p>Processor performance levels are specified in platform-specific units. For example, a hardware platform might use a metric such as the processor clock frequency to provide a rough approximation to the amount of processing work that is being done. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/mt629132">Platform Performance Thresholds</a>.</p>

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
<a href="kernel.pep_notify_ppm_query_perf_capabilities">PEP_NOTIFY_PPM_QUERY_PERF_CAPABILITIES</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/mt629132">Platform Performance Thresholds</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20PEP_PPM_QUERY_PERF_CAPABILITIES structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
