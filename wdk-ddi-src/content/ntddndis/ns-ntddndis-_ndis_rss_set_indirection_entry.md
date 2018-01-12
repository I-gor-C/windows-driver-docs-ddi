---
UID: NS:ntddndis._NDIS_RSS_SET_INDIRECTION_ENTRY
title: _NDIS_RSS_SET_INDIRECTION_ENTRY
author: windows-driver-content
description: The NDIS_RSS_SET_INDIRECTION_ENTRY structure represents a command to set a single indirection table entry.
old-location: netvista\ndis_rss_set_indirection_entry.htm
old-project: netvista
ms.assetid: 4430E19F-C603-4C52-8FC8-C36197FD2996
ms.author: windowsdriverdev
ms.date: 1/8/2018
ms.keywords: _NDIS_RSS_SET_INDIRECTION_ENTRY, NDIS_RSS_SET_INDIRECTION_ENTRY, *PNDIS_RSS_SET_INDIRECTION_ENTRY
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntddndis.h
req.include-header: Ndis.h
req.target-type: Windows
req.target-min-winverclnt: Supported in NDIS 6.80 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NDIS_RSS_SET_INDIRECTION_ENTRY
req.alt-loc: Ntddndis.h
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
req.typenames: NDIS_RSS_SET_INDIRECTION_ENTRY, *PNDIS_RSS_SET_INDIRECTION_ENTRY
---

# _NDIS_RSS_SET_INDIRECTION_ENTRY structure



## -description
<p class="CCE_Message">[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.]



## -syntax

````
typedef struct _NDIS_RSS_SET_INDIRECTION_ENTRY {
  NDIS_NIC_SWITCH_ID       SwitchId;
  NDIS_NIC_SWITCH_VPORT_ID VPortId;
  ULONG                    Flags;
  USHORT                   IndirectionTableIndex;
  PROCESSOR_NUMBER         TargetProcessorNumber;
  NDIS_STATUS              EntryStatus;
} NDIS_RSS_SET_INDIRECTION_ENTRY, *PNDIS_RSS_SET_INDIRECTION_ENTRY;
````


## -struct-fields

### -field SwitchId

An NDIS_NIC_SWITCH_ID value that represents the NIC switch where the VPort resides. 

The switch identifier is an integer between zero and the number of switches that the network adapter supports. An NDIS_DEFAULT_SWITCH_ID value indicates the default network adapter switch. 


### -field VPortId

An NDIS_NIC_SWITCH_VPORT_ID value that represents the VPort identifier.


### -field Flags

A <b>ULONG</b> value that contains a bitwise OR of flags. This member qualifies the information in this structure.

Possible flags are as follows:

<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>

### -field NDIS_RSS_SET_INDIRECTION_ENTRY_FLAG_PRIMARY_PROCESSOR

</td>
<td width="60%">
Indicates that the <b>NDIS_RSS_SET_INDIRECTION_ENTRY</b> is referring to the primary processor of the scaling entity (in other words, a VPort in RSSv2 mode). The indirection table is not used.

</td>
</tr>
<tr>

### -field NDIS_RSS_SET_INDIRECTION_ENTRY_FLAG_DEFAULT_PROCESSOR

</td>
<td width="60%">
Indicates that the <b>NDIS_RSS_SET_INDIRECTION_ENTRY</b> is referring to the default processor of the scaling entity (in other words, a VPort in RSSv2 mode). The indirection table is not used.

</td>
</tr>
</table>
 


### -field IndirectionTableIndex

A <b>USHORT</b> value that indicates the indirection table entry being moved.


### -field TargetProcessorNumber

The target processor number.


### -field EntryStatus

An NDIS_STATUS code indicating the status of the move operation for this entry. Because <b>NDIS_RSS_SET_INDIRECTION_ENTRY</b> is used in the context of a Synchronous OID call, the miniport driver cannot return <b>NDIS_STATUS_PENDING</b> for this member.


## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Version

</th>
<td width="70%">
Supported in NDIS 6.80 and later.

</td>
</tr>
<tr>
<th width="30%">
Header

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
<a href="https://msdn.microsoft.com/192CAA41-0D17-4C06-8F13-68EA7C26D023">Receive Side Scaling Version 2 (RSSv2)</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/F59D861C-B7DB-4C28-8842-4FDBAE1B95F1">OID_GEN_RSS_SET_INDIRECTION_TABLE_ENTRIES</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/6BF2E800-90A0-48FC-B702-5AD4EC318A35">Synchronous OID request interface in NDIS 6.80</a>
</dt>
<dt>
<a href="..\ntddndis\ns-ntddndis-_ndis_rss_set_indirection_entries.md">NDIS_RSS_SET_INDIRECTION_ENTRIES</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_RSS_SET_INDIRECTION_ENTRY structure%20 RELEASE:%20(1/8/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

