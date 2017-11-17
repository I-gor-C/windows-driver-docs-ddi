---
UID: NS.pmi._PMI_MEASUREMENT_DATA
title: PMI_MEASUREMENT_DATA
author: windows-driver-content
description: The PMI_MEASUREMENT_DATA structure contains the current power measurement that is collected by a power meter.
old-location: powermeter\pmi_measurement_data.htm
ms.assetid: d96e587e-36e2-475a-a139-040034f8e60b
ms.author: windowsdriverdev
ms.date: 10/23/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: powermeter
req.header: pmi.h
req.include-header: Pmi.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows 7, Windows Server 2008 R2, and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PMI_MEASUREMENT_DATA
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
ms.keywords: PMI_MEASUREMENT_DATA, PMI_MEASUREMENT_DATA, *PPMI_MEASUREMENT_DATA
req.iface: 
---

# PMI_MEASUREMENT_DATA structure



## -description
<p>The PMI_MEASUREMENT_DATA structure contains the current power measurement that is collected by a power meter.</p>


## -syntax

````
typedef struct _PMI_MEASUREMENT_DATA {
  ULONG Version;
  ULONG CurrentPower;
} PMI_MEASUREMENT_DATA, *PPMI_MEASUREMENT_DATA;
````


## -struct-fields
<dl>

### -field <b>Version</b>

<dd>
<p>A value that specifies the version of this structure. For Windows 7, Windows Server 2008 R2, and later versions of Windows, this value must be 1.</p>
</dd>

### -field <b>CurrentPower</b>

<dd>
<p>A value, in units of milliwatts (mW), that specifies the current power meter measurement.</p>
</dd>
</dl>

## -remarks
<p>The PMI_MEASUREMENT_DATA structure is returned through an <a href="https://msdn.microsoft.com/library/windows/hardware/ff543845">IOCTL_PMI_GET_MEASUREMENT</a> I/O control (IOCTL) query request. If the query request completes successfully, the request returns a PMI_MEASUREMENT_DATA structure.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543845">IOCTL_PMI_GET_MEASUREMENT</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [powermeter\powermeter]:%20PMI_MEASUREMENT_DATA structure%20 RELEASE:%20(10/23/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
