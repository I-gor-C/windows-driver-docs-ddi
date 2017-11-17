---
UID: NS.ntddk._HARDWARE_COUNTER
title: HARDWARE_COUNTER
author: windows-driver-content
description: The HARDWARE_COUNTER structure contains information about a hardware counter.
old-location: kernel\hardware_counter.htm
ms.assetid: 15eeeb07-b71f-4868-8854-6a5034d3f8c6
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: kernel
req.header: ntddk.h
req.include-header: Ntddk.h
req.target-type: Windows
req.target-min-winverclnt: Supported in Windows 7 and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: HARDWARE_COUNTER
req.alt-loc: Ntddk.h
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
ms.keywords: HARDWARE_COUNTER, HARDWARE_COUNTER, *PHARDWARE_COUNTER
req.iface: 
---

# HARDWARE_COUNTER structure



## -description
<p>The <b>HARDWARE_COUNTER</b> structure contains information about a hardware counter. </p>


## -syntax

````
typedef struct _HARDWARE_COUNTER {
  HARDWARE_COUNTER_TYPE Type;
  ULONG                 Reserved;
  ULONG64               Index;
} HARDWARE_COUNTER, *PHARDWARE_COUNTER;
````


## -struct-fields
<dl>

### -field <b>Type</b>

<dd>
<p>Specifies the type of the hardware counter. Set this member to the following <a href="https://msdn.microsoft.com/library/windows/hardware/ff546991">HARDWARE_COUNTER_TYPE</a> enumeration value:</p>
<ul>
<li>
<p><b>PMCCounter</b></p>
</li>
</ul>
</dd>

### -field <b>Reserved</b>

<dd>
<p>Reserved for use by the operating system. Initialize this member to zero. </p>
</dd>

### -field <b>Index</b>

<dd>
<p>Specifies the hardware counter index. Each hardware counter in a performance monitoring unit (PMU) for a processor is identified by an index.</p>
</dd>
</dl>

## -remarks
<p>This structure is used by the <a href="https://msdn.microsoft.com/library/windows/hardware/ff553014">KeQueryHardwareCounterConfiguration</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff553257">KeSetHardwareCounterConfiguration</a> routines. </p>

<p>The <b>Type</b> member specifies the type of hardware counter that is described by the structure. In Windows 7, the only defined hardware counter type is <b>PMCCounter</b>, which is a performance monitor counter. This type of counter is used by thread-profiling applications. </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported in Windows 7 and later versions of Windows. </p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntddk.h (include Ntddk.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546991">HARDWARE_COUNTER_TYPE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553014">KeQueryHardwareCounterConfiguration</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553257">KeSetHardwareCounterConfiguration</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20HARDWARE_COUNTER structure%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
