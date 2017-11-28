---
UID: NS.ndis._NDIS_PROCESSOR_INFO
title: NDIS_PROCESSOR_INFO
author: windows-driver-content
description: The NDIS_PROCESSOR_INFO structure specifies information about a processor in the local computer.
old-location: netvista\ndis_processor_info.htm
old-project: netvista
ms.assetid: 55c7044e-20db-4245-a644-93cbeb9cd512
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: NDIS_PROCESSOR_INFO, NDIS_PROCESSOR_INFO, *PNDIS_PROCESSOR_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Windows
req.target-min-winverclnt: Supported in NDIS 6.0 and 6.1. For NDIS 6.20 and later, use NDIS_PROCESSOR_INFO_EX.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NDIS_PROCESSOR_INFO
req.alt-loc: ndis.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: See Remarks section
req.iface: 
---

# NDIS_PROCESSOR_INFO structure



## -description
<p>The <b>NDIS_PROCESSOR_INFO</b> structure specifies information about a processor in the local
  computer.</p>


## -syntax

````
typedef struct _NDIS_PROCESSOR_INFO {
  ULONG CpuNumber;
  ULONG PhysicalPackageId;
  ULONG CoreId;
  ULONG HyperThreadID;
} NDIS_PROCESSOR_INFO, *PNDIS_PROCESSOR_INFO;
````


## -struct-fields
<dl>

### -field <b>CpuNumber</b>

<dd>
<p>The CPU number that is assigned to the processor. The value is in the range from zero through the
     number of active CPUs minus one.</p>
</dd>

### -field <b>PhysicalPackageId</b>

<dd>
<p>The physical package ID of the processor. The value is in the range from zero through the number
     in the 
     <b>NumPhysicalPackages</b> member of the 
     <a href="..\ndis\ns-ndis--ndis-system-processor-info.md">
     NDIS_SYSTEM_PROCESSOR_INFO</a> structure minus one.</p>
</dd>

### -field <b>CoreId</b>

<dd>
<p>The core ID of the processor. The value is in the range from zero through the number in the 
     <b>NumCoresPerPhysicalPackage</b> member of the NDIS_SYSTEM_PROCESSOR_INFO structure minus one.</p>
</dd>

### -field <b>HyperThreadID</b>

<dd>
<p>The hyper-threading ID of the processor. The value is in the range from zero through the number in
     the 
     <b>MaxHyperThreadingCpusPerCore</b> member of the NDIS_SYSTEM_PROCESSOR_INFO structure minus one.</p>
</dd>
</dl>

## -remarks
<p>The NDIS_PROCESSOR_INFO structure is used in the 
    <a href="..\ndis\ns-ndis--ndis-system-processor-info.md">
    NDIS_SYSTEM_PROCESSOR_INFO</a> structure.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported in NDIS 6.0 and 6.1. For NDIS 6.20 and later, use <a href="https://msdn.microsoft.com/library/windows/hardware/ff566811">NDIS_PROCESSOR_INFO_EX</a>.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ndis.h (include Ndis.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566811">NDIS_PROCESSOR_INFO_EX</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567871">NDIS_SYSTEM_PROCESSOR_INFO</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_PROCESSOR_INFO structure%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
