---
UID: NE.rilapitypes.RILMSGPROTOCOLID
title: RILMSGPROTOCOLID
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilmsgprotocolid_2.htm
old-project: netvista
ms.assetid: a4dc4bc4-f636-46be-b99c-12d2bf4a577f
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
req.alt-api: RILMSGPROTOCOLID
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

# RILMSGPROTOCOLID enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. </p>


## -syntax

````
typedef enum _RILMSGPROTOCOLID { 
  RIL_MSGPROTOCOL_SMETOSME,
  RIL_MSGPROTOCOL_IMPLICIT,
  RIL_MSGPROTOCOL_TELEX,
  RIL_MSGPROTOCOL_TELEFAX_GROUP3,
  RIL_MSGPROTOCOL_TELEFAX_GROUP4,
  RIL_MSGPROTOCOL_VOICEPHONE,
  RIL_MSGPROTOCOL_ERMES,
  RIL_MSGPROTOCOL_PAGING,
  RIL_MSGPROTOCOL_VIDEOTEX,
  RIL_MSGPROTOCOL_TELETEX,
  RIL_MSGPROTOCOL_TELETEX_PSPDN,
  RIL_MSGPROTOCOL_TELETEX_CSPDN,
  RIL_MSGPROTOCOL_TELETEX_PSTN,
  RIL_MSGPROTOCOL_TELETEX_ISDN,
  RIL_MSGPROTOCOL_UCI,
  RIL_MSGPROTOCOL_MSGHANDLING,
  RIL_MSGPROTOCOL_X400,
  RIL_MSGPROTOCOL_EMAIL,
  RIL_MSGPROTOCOL_SCSPECIFIC1,
  RIL_MSGPROTOCOL_SCSPECIFIC2,
  RIL_MSGPROTOCOL_SCSPECIFIC3,
  RIL_MSGPROTOCOL_SCSPECIFIC4,
  RIL_MSGPROTOCOL_SCSPECIFIC5,
  RIL_MSGPROTOCOL_SCSPECIFIC6,
  RIL_MSGPROTOCOL_SCSPECIFIC7,
  RIL_MSGPROTOCOL_GSMSTATION,
  RIL_MSGPROTOCOL_SM_TYPE0,
  RIL_MSGPROTOCOL_RSM_TYPE1,
  RIL_MSGPROTOCOL_RSM_TYPE2,
  RIL_MSGPROTOCOL_RSM_TYPE3,
  RIL_MSGPROTOCOL_RSM_TYPE4,
  RIL_MSGPROTOCOL_RSM_TYPE5,
  RIL_MSGPROTOCOL_RSM_TYPE6,
  RIL_MSGPROTOCOL_RSM_TYPE7,
  RIL_MSGPROTOCOL_RETURNCALL,
  RIL_MSGPROTOCOL_ME_DOWNLOAD,
  RIL_MSGPROTOCOL_DEPERSONALIZATION,
  RIL_MSGPROTOCOL_UICC_DOWNLOAD,
  RIL_MSGPROTOCOL_MAX
} RILMSGPROTOCOLID;
````


## -enum-fields
<dl>

### -field RIL_MSGPROTOCOL_SMETOSME

<dd></dd>

### -field RIL_MSGPROTOCOL_IMPLICIT

<dd></dd>

### -field RIL_MSGPROTOCOL_TELEX

<dd></dd>

### -field RIL_MSGPROTOCOL_TELEFAX_GROUP3

<dd></dd>

### -field RIL_MSGPROTOCOL_TELEFAX_GROUP4

<dd></dd>

### -field RIL_MSGPROTOCOL_VOICEPHONE

<dd></dd>

### -field RIL_MSGPROTOCOL_ERMES

<dd></dd>

### -field RIL_MSGPROTOCOL_PAGING

<dd></dd>

### -field RIL_MSGPROTOCOL_VIDEOTEX

<dd></dd>

### -field RIL_MSGPROTOCOL_TELETEX

<dd></dd>

### -field RIL_MSGPROTOCOL_TELETEX_PSPDN

<dd></dd>

### -field RIL_MSGPROTOCOL_TELETEX_CSPDN

<dd></dd>

### -field RIL_MSGPROTOCOL_TELETEX_PSTN

<dd></dd>

### -field RIL_MSGPROTOCOL_TELETEX_ISDN

<dd></dd>

### -field RIL_MSGPROTOCOL_UCI

<dd></dd>

### -field RIL_MSGPROTOCOL_MSGHANDLING

<dd></dd>

### -field RIL_MSGPROTOCOL_X400

<dd></dd>

### -field RIL_MSGPROTOCOL_EMAIL

<dd></dd>

### -field RIL_MSGPROTOCOL_SCSPECIFIC1

<dd></dd>

### -field RIL_MSGPROTOCOL_SCSPECIFIC2

<dd></dd>

### -field RIL_MSGPROTOCOL_SCSPECIFIC3

<dd></dd>

### -field RIL_MSGPROTOCOL_SCSPECIFIC4

<dd></dd>

### -field RIL_MSGPROTOCOL_SCSPECIFIC5

<dd></dd>

### -field RIL_MSGPROTOCOL_SCSPECIFIC6

<dd></dd>

### -field RIL_MSGPROTOCOL_SCSPECIFIC7

<dd></dd>

### -field RIL_MSGPROTOCOL_GSMSTATION

<dd></dd>

### -field RIL_MSGPROTOCOL_SM_TYPE0

<dd></dd>

### -field RIL_MSGPROTOCOL_RSM_TYPE1

<dd></dd>

### -field RIL_MSGPROTOCOL_RSM_TYPE2

<dd></dd>

### -field RIL_MSGPROTOCOL_RSM_TYPE3

<dd></dd>

### -field RIL_MSGPROTOCOL_RSM_TYPE4

<dd></dd>

### -field RIL_MSGPROTOCOL_RSM_TYPE5

<dd></dd>

### -field RIL_MSGPROTOCOL_RSM_TYPE6

<dd></dd>

### -field RIL_MSGPROTOCOL_RSM_TYPE7

<dd></dd>

### -field RIL_MSGPROTOCOL_RETURNCALL

<dd></dd>

### -field RIL_MSGPROTOCOL_ME_DOWNLOAD

<dd></dd>

### -field RIL_MSGPROTOCOL_DEPERSONALIZATION

<dd></dd>

### -field RIL_MSGPROTOCOL_UICC_DOWNLOAD

<dd></dd>

### -field RIL_MSGPROTOCOL_MAX

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