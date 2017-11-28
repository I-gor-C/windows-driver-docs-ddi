---
UID: NS.ntddstor._STORAGE_SPEC_VERSION
title: STORAGE_SPEC_VERSION
author: windows-driver-content
description: Indicates the specification of the storage device.
old-location: storage\storage_spec_version.htm
old-project: storage
ms.assetid: E7E80C4E-C002-4F00-AF7E-6B8DDA337323
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: STORAGE_SPEC_VERSION, STORAGE_SPEC_VERSION, *PSTORAGE_SPEC_VERSION
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntddstor.h
req.include-header: Ntddstor.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: STORAGE_SPEC_VERSION
req.alt-loc: Ntddstor.h
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

# STORAGE_SPEC_VERSION structure



## -description
<p>Indicates the specification of the storage device.</p>


## -syntax

````
typedef union _STORAGE_SPEC_VERSION {
  struct {
    union {
      struct {
        BYTE SubMinor;
        BYTE Minor;
      } DUMMYSTRUCTNAME;
      WORD   AsUshort;
    } MinorVersion;
    WORD  MajorVersion;
  } DUMMYSTRUCTNAME;
  DWORD  AsUlong;
} STORAGE_SPEC_VERSION, *PSTORAGE_SPEC_VERSION;
````


## -struct-fields
<dl>

### -field <b>DUMMYSTRUCTNAME</b>

<dd>
<p>The major and minor version of the storage specification.</p>
<dl>

### -field <b>MinorVersion</b>

<dd>
<p>The minor version of the storage specification.</p>
<dl>

### -field <b>DUMMYSTRUCTNAME</b>

<dd>
<p>The minor and sub-minor version of the storage specification.</p>
<dl>

### -field <b>SubMinor</b>

<dd>
<p>The sub-minor version of the storage specification.</p>
</dd>

### -field <b>Minor</b>

<dd>
<p>The minor version of the storage specification.</p>
</dd>
</dl>
</dd>

### -field <b>AsUshort</b>

<dd>
<p>The combination of the <b>Minor</b> and <b>SubMinor</b> versions of the storage specification.</p>
</dd>
</dl>
</dd>

### -field <b>MajorVersion</b>

<dd>
<p>The major version of the storage specification.</p>
</dd>
</dl>
</dd>

### -field <b>AsUlong</b>

<dd>
<p>The combination of the <b>MajorVersion</b> and <b>MinorVersion</b> versions of the storage specification.</p>
</dd>
</dl>

## -remarks
<p>This union allows for specifying the storage specification version, such as SBC 3, SATA 3.2, and NVMe 1.2.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntddstor.h (include Ntddstor.h)</dt>
</dl>
</td>
</tr>
</table>