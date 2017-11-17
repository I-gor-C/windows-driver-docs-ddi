---
UID: NS.wwan._WWAN_GSM_NMR
title: WWAN_GSM_NMR
author: windows-driver-content
description: The WWAN_GSM_NMR structure represents the network measurement report (NMR) of neighboring GSM cells.
old-location: netvista\wwan_gsm_nmr.htm
ms.assetid: ADEEB57F-79FF-4AA7-84AF-FED413E47057
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
req.alt-api: WWAN_GSM_NMR
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
ms.keywords: WWAN_GSM_NMR, WWAN_GSM_NMR, *PWWAN_GSM_NMR
req.iface: 
req.product: Windows 10 or later.
---

# WWAN_GSM_NMR structure



## -description
<p>The <b>WWAN_GSM_NMR</b> structure represents the network measurement report (NMR) of neighboring GSM cells.</p>


## -syntax

````
typedef struct _WWAN_GSM_NMR {
  ULONG ElementCount;
  BYTE  GSMNmr[ANYSIZE_ARRAY];
} WWAN_GSM_NMR, *PWWAN_GSM_NMR;
````


## -struct-fields
<dl>

### -field <b>ElementCount</b>

<dd>
<p>The count of NMR entries following this member.</p>
</dd>

### -field <b>GSMNmr[ANYSIZE_ARRAY]</b>

<dd>
<p>The array of NMR records, each specified as a <a href="https://msdn.microsoft.com/EF22D5C3-7A3B-4A96-A050-FCB71CA2C149">WWAN_GSM_NMR_INFO</a> structure.</p>
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
<a href="https://msdn.microsoft.com/66460B28-C2B4-4F05-A133-31A753AF9489">WWAN_BASE_STATIONS_INFO</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/EF22D5C3-7A3B-4A96-A050-FCB71CA2C149">WWAN_GSM_NMR_INFO</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/37F6BD26-55F3-4E46-9C39-97A95B6FF5B1">WWAN_GSM_SERVING_CELL_INFO</a>
</dt>
<dt>
<a href="https://docs.microsoft.com/windows-hardware/drivers/network/mb-base-stations-information-query-support">MB base stations information query support</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20WWAN_GSM_NMR structure%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
