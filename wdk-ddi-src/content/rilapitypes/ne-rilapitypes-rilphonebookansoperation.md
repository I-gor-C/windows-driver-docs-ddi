---
UID: NE.rilapitypes.RILPHONEBOOKANSOPERATION
title: RILPHONEBOOKANSOPERATION
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilphonebookansoperation_2.htm
old-project: netvista
ms.assetid: ce1d2d09-64a3-40a9-b24b-66edbd34d637
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
req.alt-api: RILPHONEBOOKANSOPERATION
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

# RILPHONEBOOKANSOPERATION enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. </p>


## -syntax

````
typedef enum _RILPHONEBOOKANSOPERATION { 
  RIL_PHONEBOOK_ANSMODIFIED,
  RIL_PHONEBOOK_ANSDELETED,
  RIL_PHONEBOOK_MAX
} RILPHONEBOOKANSOPERATION;
````


## -enum-fields
<dl>

### -field <a id="RIL_PHONEBOOK_ANSMODIFIED"></a><a id="ril_phonebook_ansmodified"></a><b>RIL_PHONEBOOK_ANSMODIFIED</b>

<dd></dd>

### -field <a id="RIL_PHONEBOOK_ANSDELETED"></a><a id="ril_phonebook_ansdeleted"></a><b>RIL_PHONEBOOK_ANSDELETED</b>

<dd></dd>

### -field <a id="RIL_PHONEBOOK_MAX"></a><a id="ril_phonebook_max"></a><b>RIL_PHONEBOOK_MAX</b>

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