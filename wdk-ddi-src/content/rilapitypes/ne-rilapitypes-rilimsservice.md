---
UID: NE.rilapitypes.RILIMSSERVICE
title: RILIMSSERVICE
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilimsservice_2.htm
old-project: netvista
ms.assetid: 9cac61e7-8260-49ef-881d-6430acb622a8
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: RILIMSSERVICE, RILIMSSERVICE
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
req.product: Windows 10 or later.
---

# RILIMSSERVICE enumeration



## -description
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. 


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

### -field RIL_IMS_SERVICE_VOICE


### -field RIL_IMS_SERVICE_VIDEO


### -field RIL_IMS_SERVICE_CUSTOM


### -field RIL_IMS_SERVICE_SUPSVC


### -field RIL_IMS_SERVICE_RCS


### -field RIL_IMS_SERVICE_USSD


### -field RIL_IMS_SERVICE_E_VOICE


### -field RIL_IMS_SERVICE_ALL


## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Header
</th>
<td width="70%">
<dl>
<dt>Rilapitypes.h</dt>
</dl>
</td>
</tr>
</table>