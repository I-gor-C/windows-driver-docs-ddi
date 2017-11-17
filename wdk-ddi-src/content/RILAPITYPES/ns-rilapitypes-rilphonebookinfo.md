---
UID: NS.rilapitypes.RILPHONEBOOKINFO
title: RILPHONEBOOKINFO
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilphonebookinfo_2.htm
ms.assetid: bd302343-c9e3-4d1d-b991-ac19fbdb2da3
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: netvista
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
ms.keywords: RILPHONEBOOKINFO, RILPHONEBOOKINFO
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

### -field <b>cbSize</b>

<dd></dd>

### -field <b>dwParams</b>

<dd></dd>

### -field <b>dwUsed</b>

<dd></dd>

### -field <b>dwTotal</b>

<dd></dd>

### -field <b>dwMaxAddressLength</b>

<dd></dd>

### -field <b>dwMaxTextLength</b>

<dd></dd>

### -field <b>dwMaxAdditionalNumbers</b>

<dd></dd>

### -field <b>dwMaxAdditionalNumberLength</b>

<dd></dd>

### -field <b>dwMaxAdditionalNumberTextLength</b>

<dd></dd>

### -field <b>dwUsedAdditionalNumberStrings</b>

<dd></dd>

### -field <b>dwTotalAdditionalNumberStrings</b>

<dd></dd>

### -field <b>dwMaxEmails</b>

<dd></dd>

### -field <b>dwMaxEmailAddressLength</b>

<dd></dd>

### -field <b>dwMaxGroups</b>

<dd></dd>

### -field <b>dwMaxGroupStringLength</b>

<dd></dd>

### -field <b>dwUsedGroupStrings</b>

<dd></dd>

### -field <b>dwTotalGroupStrings</b>

<dd></dd>

### -field <b>dwMaxSecondNameStringLength</b>

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