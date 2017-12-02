---
UID: NE.rilapitypes.RILIMSSERVICE
title: RILIMSSERVICE
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilimsservice_2.htm
old-project: netvista
ms.assetid: 9cac61e7-8260-49ef-881d-6430acb622a8
ms.author: windowsdriverdev
ms.date: 11/30/2017
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
req.alt-api: RILIMSSERVICE
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

# RILIMSSERVICE enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. </p>


## -syntax

````
typedef enum _RILIMSSERVICE { 
  RIL_IMS_SERVICE_VOICE,
  RIL_IMS_SERVICE_VIDEO,
  RIL_IMS_SERVICE_CUSTOM,
  RIL_IMS_SERVICE_SUPSVC,
  RIL_IMS_SERVICE_RCS,
  RIL_IMS_SERVICE_USSD,
  RIL_IMS_SERVICE_E_VOICE,
  RIL_IMS_SERVICE_ALL
} RILIMSSERVICE;
````


## -enum-fields
<dl>

### -field RIL_IMS_SERVICE_VOICE

<dd></dd>

### -field RIL_IMS_SERVICE_VIDEO

<dd></dd>

### -field RIL_IMS_SERVICE_CUSTOM

<dd></dd>

### -field RIL_IMS_SERVICE_SUPSVC

<dd></dd>

### -field RIL_IMS_SERVICE_RCS

<dd></dd>

### -field RIL_IMS_SERVICE_USSD

<dd></dd>

### -field RIL_IMS_SERVICE_E_VOICE

<dd></dd>

### -field RIL_IMS_SERVICE_ALL

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