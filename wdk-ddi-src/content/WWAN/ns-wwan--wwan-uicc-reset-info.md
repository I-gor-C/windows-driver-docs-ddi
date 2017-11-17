---
UID: NS.wwan._WWAN_UICC_RESET_INFO
title: WWAN_UICC_RESET_INFO
author: windows-driver-content
description: The WWAN_UICC_RESET_INFO structure represents the passthrough status of a modem miniport adapter for a UICC smart card.
old-location: netvista\wwan_uicc_reset_info.htm
ms.assetid: 1D53135F-3826-4546-A0AD-34697D186E8A
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: netvista
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
ms.keywords: WWAN_UICC_RESET_INFO, WWAN_UICC_RESET_INFO, *PWWAN_UICC_RESET_INFO
req.iface: 
req.product: Windows 10 or later.
---

# WWAN_UICC_RESET_INFO structure



## -description
<p>The <b>WWAN_UICC_RESET_INFO</b> structure represents the passthrough status of a modem miniport adapter for a UICC smart card.</p>


## -syntax

````
typedef struct _WWAN_UICC_RESET_INFO {
  WWAN_UICC_PASSTHROUGH_STATUS PassThroughStatus;
} WWAN_UICC_RESET_INFO, *PWWAN_UICC_RESET_INFO;
````


## -struct-fields
<dl>

### -field <b>PassThroughStatus</b>

<dd>
<p>The passthrough status of the miniport adapter. For more info, see <a href="https://msdn.microsoft.com/93D35A64-8394-41C2-BFB8-C8DE93619E75">WWAN_UICC_PASSTHROUGH_STATUS</a>.</p>
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
<p>Windows 10, version 1709</p>
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
<a href="https://msdn.microsoft.com/9CBAFC44-187A-41ED-9405-1208167AC75D">NDIS_WWAN_UICC_RESET_INFO</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/93D35A64-8394-41C2-BFB8-C8DE93619E75">WWAN_UICC_PASSTHROUGH_STATUS</a>
</dt>
<dt>
<a href="https://docs.microsoft.com/windows-hardware/drivers/network/mb-uicc-reset-operations">MB UICC reset operations</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20WWAN_UICC_RESET_INFO structure%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
