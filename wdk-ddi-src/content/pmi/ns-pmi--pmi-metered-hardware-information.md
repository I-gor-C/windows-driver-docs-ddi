---
UID: NS.pmi._PMI_METERED_HARDWARE_INFORMATION
title: PMI_METERED_HARDWARE_INFORMATION
author: windows-driver-content
description: The PMI_METERED_HARDWARE_INFORMATION structure contains information about one or more power supplies that are monitored by the power meter.
old-location: powermeter\pmi_metered_hardware_information.htm
old-project: powermeter
ms.assetid: 44dcfd41-7f0e-487e-8b08-5f301f17e7c1
ms.author: windowsdriverdev
ms.date: 11/6/2017
ms.keywords: PMI_METERED_HARDWARE_INFORMATION, PMI_METERED_HARDWARE_INFORMATION, *PPMI_METERED_HARDWARE_INFORMATION
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: pmi.h
req.include-header: Pmi.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows 7, Windows Server 2008 R2, and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PMI_METERED_HARDWARE_INFORMATION
req.alt-loc: pmi.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
req.iface: 
---

# PMI_METERED_HARDWARE_INFORMATION structure



## -description
<p>The PMI_METERED_HARDWARE_INFORMATION structure contains information about one or more power supplies that are monitored by the power meter.</p>


## -syntax

````
typedef struct _PMI_METERED_HARDWARE_INFORMATION {
  ULONG MeteredHardwareCount;
  WCHAR MeteredHardware[ANYSIZE_ARRAY];
} PMI_METERED_HARDWARE_INFORMATION, *PPMI_METERED_HARDWARE_INFORMATION;
````


## -struct-fields
<dl>

### -field MeteredHardwareCount

<dd>
<p>A value that specifies the number of device identifiers that are returned in the <b>MeteredHardware</b> member.</p>
</dd>

### -field MeteredHardware

<dd>
<p>A Unicode string that specifies the name of each device that is powered by the circuit on which the power meter provides measurement data. Individual device paths are delimited by a <b>NULL</b> character, and the whole list is terminated with a double <b>NULL</b>. The format of the device name is \\Device\xyz". </p>
<div class="alert"><b>Note</b>  For systemwide power meters, this member returns <b>NULL</b>.</div>
<div> </div>
</dd>
</dl>

## -remarks
<p>The PMI_METERED_HARDWARE_INFORMATION structure is returned through an <a href="..\pmi\ni-pmi-ioctl-pmi-get-capabilities.md">IOCTL_PMI_GET_CAPABILITIES</a> I/O control (IOCTL) query request. The input data for this query request is set to the <a href="..\pmi\ne-pmi-pmi-capabilities-type.md">PMI_CAPABILITIES_TYPE</a> enumerator value of <b>PmiMeteredHardware</b>.</p>

<p>If the query request completes successfully, the request returns a <a href="..\pmi\ns-pmi--pmi-capabilities.md">PMI_CAPABILITIES</a> structure. The <b>Capabilities</b> member of this structure is formatted as a PMI_METERED_HARDWARE_INFORMATION structure.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows 7, Windows Server 2008 R2, and later versions of the Windows operating systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Pmi.h (include Pmi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\pmi\ni-pmi-ioctl-pmi-get-capabilities.md">IOCTL_PMI_GET_CAPABILITIES</a>
</dt>
<dt>
<a href="..\pmi\ns-pmi--pmi-capabilities.md">PMI_CAPABILITIES</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [powermeter\powermeter]:%20PMI_METERED_HARDWARE_INFORMATION structure%20 RELEASE:%20(11/6/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
