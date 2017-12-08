---
UID: NS.NDISWWAN._NDIS_WWAN_SLOT_INFO
title: _NDIS_WWAN_SLOT_INFO
author: windows-driver-content
description: The NDIS_WWAN_SLOT_INFO structure represents the information about a slot in the modem of the MB device.
old-location: netvista\ndis_wwan_slot_info_status.htm
old-project: netvista
ms.assetid: 21D9DE55-2A26-467A-B119-8AFD4B47A4FD
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: _NDIS_WWAN_SLOT_INFO, *PNDIS_WWAN_SLOT_INFO, NDIS_WWAN_SLOT_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ndiswwan.h
req.include-header: Ndiswwan.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10, version 1703
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NDIS_WWAN_SLOT_INFO
req.alt-loc: ndiswwan.h
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
---

# _NDIS_WWAN_SLOT_INFO structure



## -description
The <b>NDIS_WWAN_SLOT_INFO</b> structure represents the information about a slot in the modem of the MB device.


## -syntax

````
typedef struct _NDIS_WWAN_SLOT_INFO {
  NDIS_OBJECT_HEADER Header;
  WWAN_STATUS        uStatus;
  WWAN_SLOT_INFO     SlotInfoStatus;
} NDIS_WWAN_SLOT_INFO, *PNDIS_WWAN_SLOT_INFO;
````


## -struct-fields

### -field Header

The header with type, revision, and size information about the <b>NDIS_WWAN_SLOT_INFO</b> structure.
     The MB Service sets the header with the values that are shown in the following table when it sends the
     data structure to the miniport driver for 
     <i>set</i> operations. Miniport drivers must set the header with the same values when they send the data
     structure to the MB service.
     
<table>
<tr>
<th>Header submember</th>
<th>Value</th>
</tr>
<tr>
<td>
Type
</td>
<td>
NDIS_OBJECT_TYPE_DEFAULT
</td>
</tr>
<tr>
<td>
Revision
</td>
<td>
NDIS_WWAN_SLOT_INFO_REVISION_1
</td>
</tr>
<tr>
<td>
Size
</td>
<td>
sizeof(NDIS_WWAN_SLOT_INFO)
</td>
</tr>
</table>
 
For more information about these members, see 
     <a href="netvista.ndis_object_header">NDIS_OBJECT_HEADER</a>.

### -field uStatus

The status of system capability. The following table shows the possible values for
     this member.
     
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
WWAN_STATUS_SUCCESS
</td>
<td>
The operation succeeded.
</td>
</tr>
<tr>
<td>
WWAN_STATUS_BUSY
</td>
<td>
The operation failed because the device was busy. In the absence of any explicit information from the function to clear this condition, the host can use subsequent actions by the function (e.g. notifications or command completions) as a hint to retry the failed operation.
</td>
</tr>
<tr>
<td>
WWAN_STATUS_FAILURE
</td>
<td>
The operation failed.
</td>
</tr>
<tr>
<td>
WWAN_STATUS_INVALID_PARAMETERS
</td>
<td>
The operation failed because of invalid parameters (e.g. slot numbers out of range).
</td>
</tr>
<tr>
<td>
WWAN_STATUS_NOT_INITIALIZED
</td>
<td>
The operation failed because the device is in the process of initializing. Retry the operation
        when the ready-state is not 
        <b>WwanReadyStateOff</b>.
</td>
</tr>
<tr>
<td>
WWAN_STATUS_NO_DEVICE_SUPPORT
</td>
<td>
The operation failed because the device does not support this OID.
</td>
</tr>
</table>
 

### -field SlotInfoStatus

A formatted <a href="netvista.wwan_slot_info_status">WWAN_SLOT_INFO</a> structure which represents the status of a slot in the modem.

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Version
</th>
<td width="70%">
Windows 10, version 1703
</td>
</tr>
<tr>
<th width="30%">
Header
</th>
<td width="70%">
<dl>
<dt>Ndiswwan.h (include Ndiswwan.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="netvista.wwan_slot_info_status">WWAN_SLOT_INFO</a>
</dt>
<dt>
<a href="netvista.oid_wwan_slot_info_status">OID_WWAN_SLOT_INFO</a>
</dt>
<dt>
<a href="netvista.ndis_status_wwan_slot_info_status">NDIS_STATUS_WWAN_SLOT_INFO</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_WWAN_SLOT_INFO structure%20 RELEASE:%20(12/6/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
