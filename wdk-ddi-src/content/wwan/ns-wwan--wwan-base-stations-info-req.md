---
UID: NS.wwan._WWAN_BASE_STATIONS_INFO_REQ
title: WWAN_BASE_STATIONS_INFO_REQ
author: windows-driver-content
description: The WWAN_BASE_STATIONS_INFO_REQ structure represents the aspects of cellular base stations information that are requested in a base stations information query.
old-location: netvista\wwan_base_stations_info_req.htm
old-project: netvista
ms.assetid: 1948F98B-1F0B-4EB3-A2FF-01DA159B5EEB
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: WWAN_BASE_STATIONS_INFO_REQ, WWAN_BASE_STATIONS_INFO_REQ, *PWWAN_BASE_STATIONS_INFO_REQ
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
req.alt-api: WWAN_BASE_STATIONS_INFO_REQ
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
req.iface: 
req.product: Windows 10 or later.
---

# WWAN_BASE_STATIONS_INFO_REQ structure



## -description
<p>The <b>WWAN_BASE_STATIONS_INFO_REQ</b> structure represents the aspects of cellular base stations information that are requested in a base stations information query.</p>


## -syntax

````
typedef struct _WWAN_BASE_STATIONS_INFO_REQ {
  ULONG MaxGSMCount;
  ULONG MaxUMTSCount;
  ULONG MaxTDSCDMACount;
  ULONG MaxLTECount;
  ULONG MaxCDMACount;
} WWAN_BASE_STATIONS_INFO_REQ, *PWWAN_BASE_STATIONS_INFO_REQ;
````


## -struct-fields
<dl>

### -field <b>MaxGSMCount</b>

<dd>
<p>The maximum number of entries of GSM neighboring cells returned in the GSM network measurement reports of <a href="..\wwan\ns-wwan--wwan-gsm-nmr.md">WWAN_GSM_NMR</a>.</p>
</dd>

### -field <b>MaxUMTSCount</b>

<dd>
<p>The maximum number of entries of UMTS neighboring cells returned in the UMTS measured results list in <a href="..\wwan\ns-wwan--wwan-umts-mrl.md">WWAN_UMTS_MRL</a>.</p>
</dd>

### -field <b>MaxTDSCDMACount</b>

<dd>
<p>The maximum number of entries of TDSCDMA neighboring cells returned in the TDSCDMA measured results list in <a href="..\wwan\ns-wwan--wwan-tdscdma-mrl.md">WWAN_TDSCDMA_MRL</a>.</p>
</dd>

### -field <b>MaxLTECount</b>

<dd>
<p>The maximum number of entries of LTE neighboring cells returned in the LTE measured results list in <a href="..\wwan\ns-wwan--wwan-lte-mrl.md">WWAN_LTE_MRL</a>.</p>
</dd>

### -field <b>MaxCDMACount</b>

<dd>
<p>The maximum number of entries of CDMA cells returned in the CDMA measured results list in <a href="..\wwan\ns-wwan--wwan-cdma-mrl.md">WWAN_CDMA_MRL</a>. This list includes both serving and neighboring cells.</p>
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
<a href="..\ndiswwan\ns-ndiswwan--ndis-wwan-base-stations-info-req.md">NDIS_WWAN_BASE_STATIONS_INFO_REQ</a>
</dt>
<dt>
<a href="..\wwan\ns-wwan--wwan-gsm-nmr.md">WWAN_GSM_NMR</a>
</dt>
<dt>
<a href="..\wwan\ns-wwan--wwan-umts-mrl.md">WWAN_UMTS_MRL</a>
</dt>
<dt>
<a href="..\wwan\ns-wwan--wwan-tdscdma-mrl.md">WWAN_TDSCDMA_MRL</a>
</dt>
<dt>
<a href="..\wwan\ns-wwan--wwan-lte-mrl.md">WWAN_LTE_MRL</a>
</dt>
<dt>
<a href="..\wwan\ns-wwan--wwan-cdma-mrl.md">WWAN_CDMA_MRL</a>
</dt>
<dt>
<a href="https://docs.microsoft.com/windows-hardware/drivers/network/mb-base-stations-information-query-support">MB base stations information query support</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20WWAN_BASE_STATIONS_INFO_REQ structure%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
