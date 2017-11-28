---
UID: NE.ndis.NDIS_PD_COUNTER_TYPE
title: NDIS_PD_COUNTER_TYPE
author: windows-driver-content
description: The NDIS_PD_COUNTER_TYPE enumeration defines types of PacketDirect Provider Interface (PDPI) counters. Its enumeration values are used in the Type member of the NDIS_PD_COUNTER_PARAMETERS structure.
old-location: netvista\ndis_pd_counter_type.htm
old-project: netvista
ms.assetid: 36DA5A61-2DA4-4CD1-8BA5-74444DC002F0
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: RxNameCacheInitialize
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: ndis.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NDIS_PD_COUNTER_TYPE
req.alt-loc: Ndis.h
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

# NDIS_PD_COUNTER_TYPE enumeration



## -description
<p>The <b>NDIS_PD_COUNTER_TYPE</b> enumeration defines types of PacketDirect Provider Interface (PDPI)  counters. Its enumeration values are used in the <b>Type</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/dn931836">NDIS_PD_COUNTER_PARAMETERS</a> structure.</p>


## -syntax

````
typedef enum _NDIS_PD_COUNTER_TYPE { 
  PDCounterTypeUnknown,
  PDCounterTypeReceiveQueue,
  PDCounterTypeTransmitQueue,
  PDCounterTypeReceiveFilter,
  PDCounterTypeMax
} NDIS_PD_COUNTER_TYPE;
````


## -enum-fields
<dl>

### -field <a id="PDCounterTypeUnknown"></a><a id="pdcountertypeunknown"></a><a id="PDCOUNTERTYPEUNKNOWN"></a><b>PDCounterTypeUnknown</b>

<dd>
<p>The counter type is not known.</p>
</dd>

### -field <a id="PDCounterTypeReceiveQueue"></a><a id="pdcountertypereceivequeue"></a><a id="PDCOUNTERTYPERECEIVEQUEUE"></a><b>PDCounterTypeReceiveQueue</b>

<dd>
<p>The counter is a receive queue counter.</p>
</dd>

### -field <a id="PDCounterTypeTransmitQueue"></a><a id="pdcountertypetransmitqueue"></a><a id="PDCOUNTERTYPETRANSMITQUEUE"></a><b>PDCounterTypeTransmitQueue</b>

<dd>
<p>The counter is a transmit queue counter.</p>
</dd>

### -field <a id="PDCounterTypeReceiveFilter"></a><a id="pdcountertypereceivefilter"></a><a id="PDCOUNTERTYPERECEIVEFILTER"></a><b>PDCounterTypeReceiveFilter</b>

<dd>
<p>The counter is a receive filter counter.</p>
</dd>

### -field <a id="PDCounterTypeMax"></a><a id="pdcountertypemax"></a><a id="PDCOUNTERTYPEMAX"></a><b>PDCounterTypeMax</b>

<dd>
<p>The maximum value for this enumeration. This value might change in future versions of NDIS header files and binaries.

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
<p>Windows 10</p>
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
<dt>Ndis.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn931836">NDIS_PD_COUNTER_PARAMETERS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_PD_COUNTER_TYPE enumeration%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
