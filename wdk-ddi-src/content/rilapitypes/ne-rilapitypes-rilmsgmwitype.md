---
UID: NE.rilapitypes.RILMSGMWITYPE
title: RILMSGMWITYPE
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilmsgmwitype_2.htm
old-project: netvista
ms.assetid: 55f06d11-60b7-4dc0-8f78-eb9901d49d1a
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
req.alt-api: RILMSGMWITYPE
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

# RILMSGMWITYPE enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. </p>


## -syntax

````
typedef enum _RILMSGMWITYPE { 
  RIL_MSGMWITYPE_VOICEMAIL,
  RIL_MSGMWITYPE_VIDEOMAIL,
  RIL_MSGMWITYPE_FAX,
  RIL_MSGMWITYPE_PAGER,
  RIL_MSGMWITYPE_MULTIMEDIA,
  RIL_MSGMWITYPE_TEXT,
  RIL_MSGMWITYPE_MAX
} RILMSGMWITYPE;
````


## -enum-fields
<dl>

### -field <a id="RIL_MSGMWITYPE_VOICEMAIL"></a><a id="ril_msgmwitype_voicemail"></a><b>RIL_MSGMWITYPE_VOICEMAIL</b>

<dd></dd>

### -field <a id="RIL_MSGMWITYPE_VIDEOMAIL"></a><a id="ril_msgmwitype_videomail"></a><b>RIL_MSGMWITYPE_VIDEOMAIL</b>

<dd></dd>

### -field <a id="RIL_MSGMWITYPE_FAX"></a><a id="ril_msgmwitype_fax"></a><b>RIL_MSGMWITYPE_FAX</b>

<dd></dd>

### -field <a id="RIL_MSGMWITYPE_PAGER"></a><a id="ril_msgmwitype_pager"></a><b>RIL_MSGMWITYPE_PAGER</b>

<dd></dd>

### -field <a id="RIL_MSGMWITYPE_MULTIMEDIA"></a><a id="ril_msgmwitype_multimedia"></a><b>RIL_MSGMWITYPE_MULTIMEDIA</b>

<dd></dd>

### -field <a id="RIL_MSGMWITYPE_TEXT"></a><a id="ril_msgmwitype_text"></a><b>RIL_MSGMWITYPE_TEXT</b>

<dd></dd>

### -field <a id="RIL_MSGMWITYPE_MAX"></a><a id="ril_msgmwitype_max"></a><b>RIL_MSGMWITYPE_MAX</b>

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