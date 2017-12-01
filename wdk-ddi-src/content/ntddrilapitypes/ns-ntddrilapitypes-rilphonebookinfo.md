---
UID: NS.ntddrilapitypes.RILPHONEBOOKINFO
title: RILPHONEBOOKINFO
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilphonebookinfo.htm
old-project: netvista
ms.assetid: 626bfc9b-6d84-4b8c-89eb-c635d0cb61f0
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: RILPHONEBOOKINFO, RILPHONEBOOKINFO, *LPRILPHONEBOOKINFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntddrilapitypes.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RILPHONEBOOKINFO
req.alt-loc: ntddrilapitypes.h
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
---

# RILPHONEBOOKINFO structure



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.</p>


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
<dt>Ntddrilapitypes.h</dt>
</dl>
</td>
</tr>
</table>