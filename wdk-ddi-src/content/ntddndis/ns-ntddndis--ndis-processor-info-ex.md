---
UID: NS.ntddndis._NDIS_PROCESSOR_INFO_EX
title: NDIS_PROCESSOR_INFO_EX
author: windows-driver-content
description: The NDIS_PROCESSOR_INFO_EX structure specifies information about a processor in the local computer.
old-location: netvista\ndis_processor_info_ex.htm
old-project: netvista
ms.assetid: e4f28f30-32bc-4bbc-8e95-f87dfe80229d
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: NDIS_PROCESSOR_INFO_EX, NDIS_PROCESSOR_INFO_EX, *PNDIS_PROCESSOR_INFO_EX
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntddndis.h
req.include-header: Ndis.h
req.target-type: Windows
req.target-min-winverclnt: Supported in NDIS 6.20 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NDIS_PROCESSOR_INFO_EX
req.alt-loc: ntddndis.h
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

# NDIS_PROCESSOR_INFO_EX structure



## -description
<p>The <b>NDIS_PROCESSOR_INFO_EX</b> structure specifies information about a processor in the local
  computer.</p>


## -syntax

````
typedef struct _NDIS_PROCESSOR_INFO_EX {
  PROCESSOR_NUMBER ProcNum;
  ULONG            SocketId;
  ULONG            CoreId;
  ULONG            HyperThreadId;
  USHORT           NodeId;
  USHORT           NodeDistance;
} NDIS_PROCESSOR_INFO_EX, *PNDIS_PROCESSOR_INFO_EX;
````


## -struct-fields
<dl>

### -field <b>ProcNum</b>

<dd>
<p>The processor number that is assigned to the processor.</p>
</dd>

### -field <b>SocketId</b>

<dd>
<p>The socket identifier for the processor. This is the number that is assigned to the motherboard
     socket on the local computer. That is, it is a physical processor identifier. The possible values for
     this member are zero to the number of sockets on the motherboard minus one.</p>
</dd>

### -field <b>CoreId</b>

<dd>
<p>The core ID of the processor. The value is in the range from zero through the number in the 
     <b>NumCoresPerSocket</b> member of the NDIS_SYSTEM_PROCESSOR_INFO_EX structure minus one.</p>
</dd>

### -field <b>HyperThreadId</b>

<dd>
<p>The hyper-threading ID of the processor. The value is in the range from zero through the number in
     the 
     <b>MaxHyperThreadingProcsPerCore</b> member of the NDIS_SYSTEM_PROCESSOR_INFO_EX structure minus
     one.</p>
</dd>

### -field <b>NodeId</b>

<dd>
<p>The node identifier of the processor. This is the number of the NUMA node to which the processor
     belongs. This range of possible values is zero to the number of NUMA nodes on the local computer minus
     one.</p>
</dd>

### -field <b>NodeDistance</b>

<dd>
<p>The node distance of the processor. If the handle at the 
     <i>NdisHandle</i> parameter that the caller passed to the 
     <a href="..\ndis\nf-ndis-ndisgetprocessorinformationex.md">
     NdisGetProcessorInformationEx</a> function is not <b>NULL</b> and is a miniport adapter handle, this member
     contains the distance of the corresponding NIC from this processor's NUMA node. Otherwise, this member
     is zero for miniport drivers or USHORT_MAX (0xffff) for other drivers.</p>
</dd>
</dl>

## -remarks
<p>The NDIS_PROCESSOR_INFO_EX structure is used in the 
    <a href="..\ntddndis\ns-ntddndis--ndis-system-processor-info-ex.md">
    NDIS_SYSTEM_PROCESSOR_INFO_EX</a> structure.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported in NDIS 6.20 and later.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntddndis.h (include Ndis.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566808">NDIS_PROCESSOR_INFO</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567872">NDIS_SYSTEM_PROCESSOR_INFO_EX</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndisgetprocessorinformationex.md">
   NdisGetProcessorInformationEx</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_PROCESSOR_INFO_EX structure%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
