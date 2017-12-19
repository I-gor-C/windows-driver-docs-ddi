---
UID: NS.WWAN._WWAN_UICC_RESET_INFO
title: _WWAN_UICC_RESET_INFO
author: windows-driver-content
description: The WWAN_UICC_RESET_INFO structure represents the passthrough status of a modem miniport adapter for a UICC smart card.
old-location: netvista\wwan_uicc_reset_info.htm
old-project: NetVista
ms.assetid: 1D53135F-3826-4546-A0AD-34697D186E8A
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: _WWAN_UICC_RESET_INFO, *PWWAN_UICC_RESET_INFO, PWWAN_UICC_RESET_INFO, WWAN_UICC_RESET_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: wwan.h
req.include-header: Wwan.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10, version 1709
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WWAN_UICC_RESET_INFO
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

# _WWAN_UICC_RESET_INFO structure



## -description
The <b>WWAN_UICC_RESET_INFO</b> structure represents the passthrough status of a modem miniport adapter for a UICC smart card.



## -syntax

````
typedef struct _WWAN_UICC_RESET_INFO {
  WWAN_UICC_PASSTHROUGH_STATUS PassThroughStatus;
} WWAN_UICC_RESET_INFO, *PWWAN_UICC_RESET_INFO;
````


## -struct-fields

### -field PassThroughStatus

The passthrough status of the miniport adapter. For more info, see <a href="netvista.wwan_uicc_passthrough_status">WWAN_UICC_PASSTHROUGH_STATUS</a>.


## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Version

</th>
<td width="70%">
Windows 10, version 1709

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
<a href="netvista.ndis_wwan_uicc_reset_info">NDIS_WWAN_UICC_RESET_INFO</a>
</dt>
<dt>
<a href="netvista.wwan_uicc_passthrough_status">WWAN_UICC_PASSTHROUGH_STATUS</a>
</dt>
<dt>
<a href="https://docs.microsoft.com/windows-hardware/drivers/network/mb-uicc-reset-operations">MB UICC reset operations</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [NetVista\netvista]:%20WWAN_UICC_RESET_INFO structure%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

