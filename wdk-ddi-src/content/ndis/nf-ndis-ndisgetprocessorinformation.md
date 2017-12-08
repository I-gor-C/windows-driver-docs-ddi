---
UID: NF.ndis.NdisGetProcessorInformation
title: NdisGetProcessorInformation function
author: windows-driver-content
description: The NdisGetProcessorInformation function retrieves information about the CPU topology of the local computer and the set of processors that a miniport driver must use for receive side scaling (RSS).
old-location: netvista\ndisgetprocessorinformation.htm
old-project: netvista
ms.assetid: 2cee5cf4-7dee-49d2-905c-2b9634137ce4
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: NdisGetProcessorInformation
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Universal
req.target-min-winverclnt: Supported in NDIS 6.0 and 6.1. For NDIS 6.20 and later, ise       NdisGetProcessorInformationEx or       NdisGetRssProcessorInformation instead.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdisGetProcessorInformation
req.alt-loc: ndis.lib,ndis.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ndis.lib
req.dll: 
req.irql: PASSIVE_LEVEL
---

# NdisGetProcessorInformation function



## -description
The 
  <b>NdisGetProcessorInformation</b> function retrieves information about the CPU topology of the local
  computer and the set of processors that a miniport driver must use for receive side scaling (RSS).


## -syntax

````
NDIS_STATUS NdisGetProcessorInformation(
  _Inout_ PNDIS_SYSTEM_PROCESSOR_INFO SystemProcessorInfo
);
````


## -parameters

### -param SystemProcessorInfo [in, out]

A pointer to an 
     <a href="netvista.ndis_system_processor_info">
     NDIS_SYSTEM_PROCESSOR_INFO</a> structure that NDIS fills with the information about the CPU topology
     of the system and the RSS processor set.

## -returns
<b>NdisGetProcessorInformation</b> can return one of the following status values:
<dl>
<dt><b>NDIS_STATUS_SUCCESS</b></dt>
</dl>The operation completed successfully.
<dl>
<dt><b>NDIS_STATUS_BUFFER_TOO_SHORT</b></dt>
</dl>The size that was specified in the 
       <b>Header.Size</b> member of the 
       <i>SystemProcessorInfo</i> parameter was too small.

 

## -remarks
NDIS drivers call the 
    <b>NdisGetProcessorInformation</b> function to retrieve information about the processors on the local
    computer.

RSS-capable miniport drivers that support MSI-X call 
    <b>NdisGetProcessorInformation</b> in their 
    <a href="netvista.miniportfilterresourcerequirements">
    MiniportFilterResourceRequirements</a> function. Miniport drivers set the interrupt affinity of the
    allocated MSI-X messages to the RSS processors that are specified in the 
    <b>RssProcessors</b> member of the 
    <i>SystemProcessorInfo</i> parameter.

## -requirements
<table>
<tr>
<th width="30%">
Target platform
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Version
</th>
<td width="70%">
Supported in NDIS 6.0 and 6.1. For NDIS 6.20 and later, ise 
   <a href="netvista.ndisgetprocessorinformationex">
   NdisGetProcessorInformationEx</a> or 
   <a href="netvista.ndisgetrssprocessorinformation">
   NdisGetRssProcessorInformation</a> instead. 
</td>
</tr>
<tr>
<th width="30%">
Header
</th>
<td width="70%">
<dl>
<dt>Ndis.h (include Ndis.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library
</th>
<td width="70%">
<dl>
<dt>Ndis.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL
</th>
<td width="70%">
PASSIVE_LEVEL
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="netvista.miniportfilterresourcerequirements">
   MiniportFilterResourceRequirements</a>
</dt>
<dt>
<a href="netvista.ndis_system_processor_info">NDIS_SYSTEM_PROCESSOR_INFO</a>
</dt>
<dt>
<a href="netvista.ndisgetprocessorinformationex">
   NdisGetProcessorInformationEx</a>
</dt>
<dt>
<a href="netvista.ndisgetrssprocessorinformation">
   NdisGetRssProcessorInformation</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisGetProcessorInformation function%20 RELEASE:%20(12/6/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
