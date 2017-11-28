---
UID: NS.ntddrilapitypes.RILPHONEBOOKENTRY
title: RILPHONEBOOKENTRY
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilphonebookentry.htm
old-project: netvista
ms.assetid: 2741d992-624a-4fd1-a1b5-57fb39c42f84
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: RILPHONEBOOKENTRY, RILPHONEBOOKENTRY, *LPRILPHONEBOOKENTRY
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
req.alt-api: RILPHONEBOOKENTRY
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

# RILPHONEBOOKENTRY structure



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.</p>


## -syntax

````
typedef struct _RILPHONEBOOKENTRY {
  DWORD       cbSize;
  DWORD       dwParams;
  DWORD       dwIndex;
  RILADDRESS  raAddress;
  WCHAR [256] wszText;
  WCHAR [256] wszSecondName;
  DWORD       dwGroupIdCount;
  DWORD [10]  rgdwGroupId;
  DWORD       dwAdditionalNumCount;
  DWORD       dwAdditionalNumSize;
  DWORD       dwAdditionalNumOffset;
  DWORD       dwEmailCount;
  DWORD       dwEmailSize;
  DWORD       dwEmailOffset;
} RILPHONEBOOKENTRY, RILPHONEBOOKENTRY;
````


## -struct-fields
<dl>

### -field <b>cbSize</b>

<dd></dd>

### -field <b>dwParams</b>

<dd></dd>

### -field <b>dwIndex</b>

<dd></dd>

### -field <b>raAddress</b>

<dd></dd>

### -field <b>wszText</b>

<dd></dd>

### -field <b>wszSecondName</b>

<dd></dd>

### -field <b>dwGroupIdCount</b>

<dd></dd>

### -field <b>rgdwGroupId</b>

<dd></dd>

### -field <b>dwAdditionalNumCount</b>

<dd></dd>

### -field <b>dwAdditionalNumSize</b>

<dd></dd>

### -field <b>dwAdditionalNumOffset</b>

<dd></dd>

### -field <b>dwEmailCount</b>

<dd></dd>

### -field <b>dwEmailSize</b>

<dd></dd>

### -field <b>dwEmailOffset</b>

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