---
UID: NE.rilapitypes.RILIMSSERVICE
title: RILIMSSERVICE
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilimsservice_2.htm
old-project: netvista
ms.assetid: 9cac61e7-8260-49ef-881d-6430acb622a8
ms.author: windowsdriverdev
ms.date: 11/22/2017
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

### -field <a id="RIL_IMS_SERVICE_VOICE"></a><a id="ril_ims_service_voice"></a><b>RIL_IMS_SERVICE_VOICE</b>

<dd></dd>

### -field <a id="RIL_IMS_SERVICE_VIDEO"></a><a id="ril_ims_service_video"></a><b>RIL_IMS_SERVICE_VIDEO</b>

<dd></dd>

### -field <a id="RIL_IMS_SERVICE_CUSTOM"></a><a id="ril_ims_service_custom"></a><b>RIL_IMS_SERVICE_CUSTOM</b>

<dd></dd>

### -field <a id="RIL_IMS_SERVICE_SUPSVC"></a><a id="ril_ims_service_supsvc"></a><b>RIL_IMS_SERVICE_SUPSVC</b>

<dd></dd>

### -field <a id="RIL_IMS_SERVICE_RCS"></a><a id="ril_ims_service_rcs"></a><b>RIL_IMS_SERVICE_RCS</b>

<dd></dd>

### -field <a id="RIL_IMS_SERVICE_USSD"></a><a id="ril_ims_service_ussd"></a><b>RIL_IMS_SERVICE_USSD</b>

<dd></dd>

### -field <a id="RIL_IMS_SERVICE_E_VOICE"></a><a id="ril_ims_service_e_voice"></a><b>RIL_IMS_SERVICE_E_VOICE</b>

<dd></dd>

### -field <a id="RIL_IMS_SERVICE_ALL"></a><a id="ril_ims_service_all"></a><b>RIL_IMS_SERVICE_ALL</b>

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