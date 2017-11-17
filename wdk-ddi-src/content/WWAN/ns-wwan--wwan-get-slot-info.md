---
UID: NS.wwan._WWAN_GET_SLOT_INFO
title: WWAN_GET_SLOT_INFO
author: windows-driver-content
description: The WWAN_GET_SLOT_INFO structure contains the slot index to specify which slot's status a query request is for.
old-location: netvista\wwan_get_slot_info_status.htm
ms.assetid: 62955CA4-8631-4A85-8E78-5A91A9DA0069
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
req.alt-api: WWAN_GET_SLOT_INFO
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
ms.keywords: WWAN_GET_SLOT_INFO, WWAN_GET_SLOT_INFO, *PWWAN_GET_SLOT_INFO
req.iface: 
req.product: Windows 10 or later.
---

# WWAN_GET_SLOT_INFO structure



## -description
<p>The WWAN_GET_SLOT_INFO structure contains the slot index to specify which slot's status a query request is for.</p>


## -syntax

````
typedef struct _WWAN_GET_SLOT_INFO {
  ULONG SlotIndex;
} WWAN_GET_SLOT_INFO, *PWWAN_GET_SLOT_INFO;
````


## -struct-fields
<dl>

### -field <b>SlotIndex</b>

<dd>
<p>Represents the index of the SIM slot. <b>SlotIndex</b> can be mapped to either a physical or embedded SIM slot and may be expanded to soft SIM in the future.</p>
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
<a href="https://msdn.microsoft.com/214AFAD3-B211-4D66-8CFC-58F8EB407B83">NDIS_WWAN_GET_SLOT_INFO</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20WWAN_GET_SLOT_INFO structure%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
