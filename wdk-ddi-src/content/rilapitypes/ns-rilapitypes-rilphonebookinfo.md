---
UID: NS.rilapitypes.RILPHONEBOOKINFO
title: RILPHONEBOOKINFO
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilphonebookinfo_2.htm
old-project: netvista
ms.assetid: bd302343-c9e3-4d1d-b991-ac19fbdb2da3
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: RILPHONEBOOKINFO, RILPHONEBOOKINFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: rilapitypes.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RILPHONEBOOKINFO
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

# RILPHONEBOOKINFO structure



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. </p>


## -syntax

````
typedef struct _RILPHONEBOOKINFO {
  DWORD  cbSize;
  DWORD  dwParams;
  DWORD  dwUsed;
  DWORD  dwTotal;
  DWORD  dwMaxAddressLength;
  DWORD  dwMaxTextLength;
  DWORD  dwMaxAdditionalNumbers;
  DWORD  dwMaxAdditionalNumberLength;
  DWORD  dwMaxAdditionalNumberTextLength;
  DWORD  dwUsedAdditionalNumberStrings;
  DWORD  dwTotalAdditionalNumberStrings;
  DWORD  dwMaxEmails;
  DWORD  dwMaxEmailAddressLength;
  DWORD  dwMaxGroups;
  DWORD  dwMaxGroupStringLength;
  DWORD  dwUsedGroupStrings;
  DWORD  dwTotalGroupStrings;
  DWORD  dwMaxSecondNameStringLength;
} RILPHONEBOOKINFO, RILPHONEBOOKINFO;
````


## -struct-fields
<dl>

### -field cbSize

<dd></dd>

### -field dwParams

<dd></dd>

### -field dwUsed

<dd></dd>

### -field dwTotal

<dd></dd>

### -field dwMaxAddressLength

<dd></dd>

### -field dwMaxTextLength

<dd></dd>

### -field dwMaxAdditionalNumbers

<dd></dd>

### -field dwMaxAdditionalNumberLength

<dd></dd>

### -field dwMaxAdditionalNumberTextLength

<dd></dd>

### -field dwUsedAdditionalNumberStrings

<dd></dd>

### -field dwTotalAdditionalNumberStrings

<dd></dd>

### -field dwMaxEmails

<dd></dd>

### -field dwMaxEmailAddressLength

<dd></dd>

### -field dwMaxGroups

<dd></dd>

### -field dwMaxGroupStringLength

<dd></dd>

### -field dwUsedGroupStrings

<dd></dd>

### -field dwTotalGroupStrings

<dd></dd>

### -field dwMaxSecondNameStringLength

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