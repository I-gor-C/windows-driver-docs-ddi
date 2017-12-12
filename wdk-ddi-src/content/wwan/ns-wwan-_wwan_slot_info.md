---
UID: NS.WWAN._WWAN_SLOT_INFO
title: _WWAN_SLOT_INFO
author: windows-driver-content
description: The WWAN_SLOT_INFO structure represents the status of a specific SIM card slot on the modem.
old-location: netvista\wwan_slot_info_status.htm
old-project: netvista
ms.assetid: F45D253E-E7D7-4600-AF8C-6D4EB096030D
ms.author: windowsdriverdev
ms.date: 12/8/2017
ms.keywords: _WWAN_SLOT_INFO, *PWWAN_SLOT_INFO, WWAN_SLOT_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: wwan.h
req.include-header: Wwan.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10, version 1703
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WWAN_SLOT_INFO
req.alt-loc: wwan.h
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
req.product: Windows 10 or later.
---

# _WWAN_SLOT_INFO structure



## -description
The <b>WWAN_SLOT_INFO</b> structure represents the status of a specific SIM card slot on the modem.



## -syntax

````
typedef struct _WWAN_SLOT_INFO {
  ULONG               SlotIndex;
  WWAN_UICCSLOT_STATE State;
} WWAN_SLOT_INFO, *PWWAN_SLOT_INFO;
````


## -struct-fields

### -field SlotIndex

The index of the slot being queried.


### -field State

The state of the slot being queried, a member of the  <a href="netvista.wwan_uiccslot_state">WWAN_UICCSLOT_STATE</a> enumeration that represents a summary of both the slot and the card state.


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
<dt>Wwan.h (include Wwan.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="netvista.ndis_wwan_slot_info_status">NDIS_WWAN_SLOT_INFO</a>
</dt>
<dt>
<a href="netvista.oid_wwan_slot_info_status">OID_WWAN_SLOT_INFO</a>
</dt>
<dt>
<a href="netvista.ndis_status_wwan_slot_info_status">NDIS_STATUS_WWAN_SLOT_INFO</a>
</dt>
<dt>
<a href="netvista.wwan_uiccslot_state">WWAN_UICCSLOT_STATE</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20WWAN_SLOT_INFO structure%20 RELEASE:%20(12/8/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

