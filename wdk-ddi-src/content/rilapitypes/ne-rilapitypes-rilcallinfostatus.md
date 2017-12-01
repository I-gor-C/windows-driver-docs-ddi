---
UID: NE.rilapitypes.RILCALLINFOSTATUS
title: RILCALLINFOSTATUS
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilcallinfostatus_2.htm
old-project: netvista
ms.assetid: 16ecddf7-6c79-4e95-957d-19f27c3e3cf5
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: RIL_WritePhonebookEntry
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: rilapitypes.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RILCALLINFOSTATUS
req.alt-loc: rilapitypes.h
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

# RILCALLINFOSTATUS enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. </p>


## -syntax

````
typedef enum _RILCALLINFOSTATUS { 
  RIL_CPISTAT_NEW_OUTGOING,
  RIL_CPISTAT_NEW_INCOMING,
  RIL_CPISTAT_CONNECTED,
  RIL_CPISTAT_DISCONNECTED,
  RIL_CPISTAT_ONHOLD,
  RIL_CPISTAT_MEDIA,
  RIL_CPISTAT_HANDOVER,
  RIL_CPISTAT_MAX
} RILCALLINFOSTATUS;
````


## -enum-fields
<dl>

### -field <a id="RIL_CPISTAT_NEW_OUTGOING"></a><a id="ril_cpistat_new_outgoing"></a><b>RIL_CPISTAT_NEW_OUTGOING</b>

<dd></dd>

### -field <a id="RIL_CPISTAT_NEW_INCOMING"></a><a id="ril_cpistat_new_incoming"></a><b>RIL_CPISTAT_NEW_INCOMING</b>

<dd></dd>

### -field <a id="RIL_CPISTAT_CONNECTED"></a><a id="ril_cpistat_connected"></a><b>RIL_CPISTAT_CONNECTED</b>

<dd></dd>

### -field <a id="RIL_CPISTAT_DISCONNECTED"></a><a id="ril_cpistat_disconnected"></a><b>RIL_CPISTAT_DISCONNECTED</b>

<dd></dd>

### -field <a id="RIL_CPISTAT_ONHOLD"></a><a id="ril_cpistat_onhold"></a><b>RIL_CPISTAT_ONHOLD</b>

<dd></dd>

### -field <a id="RIL_CPISTAT_MEDIA"></a><a id="ril_cpistat_media"></a><b>RIL_CPISTAT_MEDIA</b>

<dd></dd>

### -field <a id="RIL_CPISTAT_HANDOVER"></a><a id="ril_cpistat_handover"></a><b>RIL_CPISTAT_HANDOVER</b>

<dd></dd>

### -field <a id="RIL_CPISTAT_MAX"></a><a id="ril_cpistat_max"></a><b>RIL_CPISTAT_MAX</b>

<dd></dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Rilapitypes.h</dt>
</dl>
</td>
</tr>
</table>