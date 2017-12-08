---
UID: NI.nfcsedev.IOCTL_NFCSE_GET_ROUTING_TABLE
title: IOCTL_NFCSE_GET_ROUTING_TABLE
author: windows-driver-content
description: Returns information regarding the current configuration of listen mode routing table.
old-location: nfpdrivers\ioctl_nfcse_get_routing_table.htm
old-project: nfpdrivers
ms.assetid: 838D31E8-1835-47C7-8201-93910610F5EC
ms.author: windowsdriverdev
ms.date: 11/27/2017
ms.keywords: NFCRM_SET_RADIO_STATE, NFCRM_SET_RADIO_STATE, *PNFCRM_SET_RADIO_STATE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: ioctl
req.header: nfcsedev.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IOCTL_NFCSE_GET_ROUTING_TABLE
req.alt-loc: nfcsedev.h
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

# IOCTL_NFCSE_GET_ROUTING_TABLE IOCTL



## -description
<p>Returns information regarding the current configuration of listen mode routing table. Note that the caller must allocate an output buffer large enough to hold information regarding all the entries that are present in the current listen mode routing table, i.e. Total number of routing entries x Size of routing table entry, otherwise the driver should return a STATUS_BUFFER_OVERFLOW error code to the client with NumberOfEntries field containing the number of routing table entries configured. The routing table entry is of type SECURE_ELEMENT_ROUTING_TABLE_ENTRY. Note: The driver shouldn’t return entry routing NFC-DEP to DH as part of the routing table returned in the output buffer even though the entry is present in the NFCC routing table.

</p>


## -ioctlparameters

### -input-buffer
<p>None</p>

### -input-buffer-length
<p>None</p>

<p>None</p>

### -output-buffer
<p>
<a href="..\nfcsedev\ns-nfcsedev--secure-element-routing-table.md"> SECURE_ELEMENT_ROUTING_TABLE</a> containing all currently configured routing entries.
</p>

<p>
<a href="..\nfcsedev\ns-nfcsedev--secure-element-routing-table.md"> SECURE_ELEMENT_ROUTING_TABLE</a> containing all currently configured routing entries.
</p>

<p>
<a href="..\nfcsedev\ns-nfcsedev--secure-element-routing-table.md"> SECURE_ELEMENT_ROUTING_TABLE</a> containing all currently configured routing entries.
</p>

### -output-buffer-length
<p>sizeof(SECURE_ELEMENT_ROUTING_TABLE)</p>

<p>sizeof(SECURE_ELEMENT_ROUTING_TABLE)</p>

<p>sizeof(SECURE_ELEMENT_ROUTING_TABLE)</p>

<p>sizeof(SECURE_ELEMENT_ROUTING_TABLE)</p>

### -in-out-buffer

<text></text>

### -inout-buffer-length

<text></text>

### -status-block
I/O Status block
<p><b>Irp-&gt;IoStatus.Status</b> is set to <b>STATUS_SUCCESS</b> if the request is successful. Possible error codes are:</p>

<p> </p>

<p><b>Irp-&gt;IoStatus.Status</b> is set to <b>STATUS_SUCCESS</b> if the request is successful. Possible error codes are:</p>

<p> </p>

<p><b>Irp-&gt;IoStatus.Status</b> is set to <b>STATUS_SUCCESS</b> if the request is successful. Possible error codes are:</p>

<p> </p>

<p><b>Irp-&gt;IoStatus.Status</b> is set to <b>STATUS_SUCCESS</b> if the request is successful. Possible error codes are:</p>

<p> </p>

<p><b>Irp-&gt;IoStatus.Status</b> is set to <b>STATUS_SUCCESS</b> if the request is successful. Possible error codes are:</p>

<p> </p>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Nfcsedev.h</dt>
</dl>
</td>
</tr>
</table>