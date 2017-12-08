---
UID: NS.WWAN._WWAN_UMTS_MRL
title: _WWAN_UMTS_MRL
author: windows-driver-content
description: The WWAN_UMTS_MRL structure contains the measured results list (MRL) of neighboring UMTS cells.
old-location: netvista\wwan_umts_mrl.htm
old-project: netvista
ms.assetid: B62F63EB-747A-4672-9A79-5065A8BC04D1
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: _WWAN_UMTS_MRL, WWAN_UMTS_MRL, *PWWAN_UMTS_MRL
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
req.alt-api: WWAN_UMTS_MRL
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

# _WWAN_UMTS_MRL structure



## -description
The <b>WWAN_UMTS_MRL</b> structure contains the measured results list (MRL) of neighboring UMTS cells.


## -syntax

````
typedef struct _WWAN_UMTS_MRL {
  ULONG ElementCount;
  BYTE  UMTSMrl[ANYSIZE_ARRAY];
} WWAN_UMTS_MRL, *PWWAN_UMTS_MRL;
````


## -struct-fields

### -field ElementCount

The count of MRL entries following this member.

### -field UMTSMrl[ANYSIZE_ARRAY]

The array of MRL records, each specified as a <a href="netvista.wwan_umts_mrl_info">WWAN_UMTS_MRL_INFO</a> structure.

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
<a href="netvista.wwan_base_stations_info">WWAN_BASE_STATIONS_INFO</a>
</dt>
<dt>
<a href="netvista.wwan_umts_mrl_info">WWAN_UMTS_MRL_INFO</a>
</dt>
<dt>
<a href="netvista.wwan_umts_serving_cell_info">WWAN_UMTS_SERVING_CELL_INFO</a>
</dt>
<dt>
<a href="https://docs.microsoft.com/windows-hardware/drivers/network/mb-base-stations-information-query-support">MB base stations information query support</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20WWAN_UMTS_MRL structure%20 RELEASE:%20(12/6/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
