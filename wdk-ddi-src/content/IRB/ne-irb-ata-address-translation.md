---
UID: NE.irb.ATA_ADDRESS_TRANSLATION
title: ATA_ADDRESS_TRANSLATION
author: windows-driver-content
description: The ATA_ADDRESS_TRANSLATION enumeration type indicates the type of address translation used during data transfers.Note  The ATA port driver and ATA miniport driver models may be altered or unavailable in the future.
old-location: storage\ata_address_translation.htm
ms.assetid: 72fddd86-6e9f-4e75-af6a-e7f3e1064a8b
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: Storage
req.header: irb.h
req.include-header: Irb.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ATA_ADDRESS_TRANSLATION
req.alt-loc: irb.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: Any level
ms.keywords: WdmlibIoGetAffinityInterrupt
req.iface: 
---

# ATA_ADDRESS_TRANSLATION enumeration



## -description
<p>The ATA_ADDRESS_TRANSLATION enumeration type indicates the type of address translation used during data transfers.</p>


## -syntax

````
typedef enum  { 
  UnknownMode   = 0,
  ChsMode       = 1,
  LbaMode       = 2,
  Lba48BitMode  = 3
} ATA_ADDRESS_TRANSLATION;
````


## -enum-fields
<dl>

### -field <a id="UnknownMode"></a><a id="unknownmode"></a><a id="UNKNOWNMODE"></a><b>UnknownMode</b>

<dd></dd>

### -field <a id="ChsMode"></a><a id="chsmode"></a><a id="CHSMODE"></a><b>ChsMode</b>

<dd>
<p>Indicates that sectors are to be addressed using cylinder/head/sector (CHS) values.</p>
</dd>

### -field <a id="LbaMode"></a><a id="lbamode"></a><a id="LBAMODE"></a><b>LbaMode</b>

<dd>
<p>Indicates that sectors are to be addressed using logical block addressing (LBA) values.</p>
</dd>

### -field <a id="Lba48BitMode"></a><a id="lba48bitmode"></a><a id="LBA48BITMODE"></a><b>Lba48BitMode</b>

<dd>
<p>Indicates support for 48-bit LBAs.</p>
</dd>
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
<dt>Irb.h (include Irb.h)</dt>
</dl>
</td>
</tr>
</table>