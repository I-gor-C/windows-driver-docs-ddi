---
UID: NS.wwan._WWAN_SLOT_INFO
title: WWAN_SLOT_INFO
author: windows-driver-content
description: The WWAN_SLOT_INFO structure represents the status of a specific SIM card slot on the modem.
old-location: netvista\wwan_slot_info_status.htm
ms.assetid: F45D253E-E7D7-4600-AF8C-6D4EB096030D
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: netvista
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
ms.keywords: WWAN_SLOT_INFO, WWAN_SLOT_INFO, *PWWAN_SLOT_INFO
req.iface: 
req.product: Windows 10 or later.
---

# WWAN_SLOT_INFO structure



## -description
<p>The <b>WWAN_SLOT_INFO</b> structure represents the status of a specific SIM card slot on the modem.</p>


## -syntax

````
typedef struct _WWAN_SLOT_INFO {
  ULONG               SlotIndex;
  WWAN_UICCSLOT_STATE State;
} WWAN_SLOT_INFO, *PWWAN_SLOT_INFO;
````


## -struct-fields
<dl>

### -field <b>SlotIndex</b>

<dd>
<p>The index of the slot being queried.</p>
</dd>

### -field <b>State</b>

<dd>
<p>The state of the slot being queried, a member of the  <a href="https://msdn.microsoft.com/63A3C2AA-6EBF-469D-933A-C51F5EC31C47">WWAN_UICCSLOT_STATE</a> enumeration that represents a summary of both the slot and the card state.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Windows 10, version 1703</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
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
<a href="https://msdn.microsoft.com/21D9DE55-2A26-467A-B119-8AFD4B47A4FD">NDIS_WWAN_SLOT_INFO</a>
</dt>
<dt>
<a href="netvista.oid_wwan_slot_info_status">OID_WWAN_SLOT_INFO</a>
</dt>
<dt>
<a href="netvista.ndis_status_wwan_slot_info_status">NDIS_STATUS_WWAN_SLOT_INFO</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/63A3C2AA-6EBF-469D-933A-C51F5EC31C47">WWAN_UICCSLOT_STATE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20WWAN_SLOT_INFO structure%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
