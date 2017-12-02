---
UID: NS.bdatypes._BDA_WMDRM_KEYINFOLIST
title: BDA_WMDRM_KEYINFOLIST
author: windows-driver-content
description: .
old-location: stream\bda_wmdrm_keyinfolist.htm
old-project: stream
ms.assetid: 0A151425-C22F-4201-855F-FF6FECE611D7
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: BDA_WMDRM_KEYINFOLIST, BDA_WMDRM_KEYINFOLIST, *PBDA_WMDRM_KEYINFOLIST
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: bdatypes.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: BDA_WMDRM_KEYINFOLIST
req.alt-loc: Bdatypes.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
---

# BDA_WMDRM_KEYINFOLIST structure



## -description
<p></p>


## -syntax

````
typedef struct _BDA_WMDRM_KEYINFOLIST {
  PBDARESULT lResult;
  ULONG      ulKeyuuidBufferLen;
  GUID       argKeyuuidBuffer[MIN_DIMENSION];
} BDA_WMDRM_KEYINFOLIST, *PBDA_WMDRM_KEYINFOLIST;
````


## -struct-fields
<dl>

### -field lResult

<dd></dd>

### -field ulKeyuuidBufferLen

<dd></dd>

### -field argKeyuuidBuffer

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
<dt>Bdatypes.h</dt>
</dl>
</td>
</tr>
</table>