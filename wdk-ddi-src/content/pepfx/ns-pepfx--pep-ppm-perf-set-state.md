---
UID: NS.pepfx._PEP_PPM_PERF_SET_STATE
title: PEP_PPM_PERF_SET_STATE
author: windows-driver-content
description: Used in the PEP_NOTIFY_PPM_PERF_SET notification at runtime to set the current operating performance of the processor.  .
old-location: kernel\pep_ppm_perf_set_state.htm
old-project: kernel
ms.assetid: 0d822370-f08b-404d-ad0f-60ea091661d9
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: PEP_PPM_PERF_SET_STATE, PEP_PPM_PERF_SET_STATE, *PPEP_PPM_PERF_SET_STATE
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
req.alt-api: PEP_PPM_PERF_SET_STATE
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
req.iface: 
---

# PEP_PPM_PERF_SET_STATE structure



## -description
<p>Used in the <b>PEP_NOTIFY_PPM_PERF_SET </b>notification at runtime to set the current operating performance of the processor.  </p>


## -syntax

````
typedef struct _PEP_PPM_PERF_SET_STATE {
  UCHAR  MinimumPerformanceState;
  UCHAR  MaximumPerformanceState;
  UCHAR  DesiredPerformanceState;
} PEP_PPM_PERF_SET_STATE, *PPEP_PPM_PERF_SET_STATE;
````


## -struct-fields
<dl>

### -field <b>MinimumPerformanceState</b>

<dd>
<p>On input, the new requested minimum performance state. This state is  defined as the absolute minimum instantaneous performance level at which  the processor may run. The operating system may set this value to any performance value in the range [Lowest Performance, Guaranteed Performance], inclusive. Minimum performance must never be set to a value higher than maximum performance. </p>
</dd>

### -field <b>MaximumPerformanceState</b>

<dd>
<p>On input, the new requested maximum performance state. This state is defined as the absolute maximum instantaneous performance level at which the processor may run. The OS may set Maximum performance to any performance value in the range [Lowest Performance, Highest Performance], inclusive.</p>
</dd>

### -field <b>DesiredPerformanceState</b>

<dd>
<p>On input, the new requested desired performance state. This state is defined as the performance level power manager is requesting from the processor. Desired performance may be set to any performance value in the range [Minimum Performance, Maximum Performance], inclusive. Desired performance may take one of two meanings, depending on whether the desired performance is above or below the guaranteed performance level. 
</p>
<ul>
<li>Below the guaranteed performance level, desired performance expresses the average performance level the platform must provide.  
</li>
<li>Above the guaranteed performance level, the platform must provide the guaranteed performance level. The platform should attempt to provide up to the desired performance level, if current operating conditions allow for it, but it is not required to do so. </li>
</ul>
<p>
 </p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 10, version 1709</p>
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
<dt>Pepfx.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/mt186881">Processor power management (PPM) notifications</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20PEP_PPM_PERF_SET_STATE structure%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
