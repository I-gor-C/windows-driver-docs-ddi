---
UID: NS.bdatypes._BDA_WMDRM_RENEWLICENSE
title: BDA_WMDRM_RENEWLICENSE
author: windows-driver-content
description: .
old-location: stream\bda_wmdrm_renewlicense.htm
old-project: stream
ms.assetid: 73AB73F1-CB9B-46A3-8ECC-19E93210D30E
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: BDA_WMDRM_RENEWLICENSE, BDA_WMDRM_RENEWLICENSE, *PBDA_WMDRM_RENEWLICENSE
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
req.alt-api: BDA_WMDRM_RENEWLICENSE
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

# BDA_WMDRM_RENEWLICENSE structure



## -description
<p></p>


## -syntax

````
typedef struct _BDA_WMDRM_RENEWLICENSE {
  PBDARESULT lResult;
  ULONG      ulDescrambleStatus;
  ULONG      ulXmrLicenseOutputLength;
  BYTE       argbXmrLicenceOutputBuffer[MIN_DIMENSION];
} BDA_WMDRM_RENEWLICENSE, *PBDA_WMDRM_RENEWLICENSE;
````


## -struct-fields
<dl>

### -field lResult

<dd></dd>

### -field ulDescrambleStatus

<dd></dd>

### -field ulXmrLicenseOutputLength

<dd></dd>

### -field argbXmrLicenceOutputBuffer

<dd>
<p>Specifies the license and entitlement token buffer.</p>
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
<dt>Bdatypes.h</dt>
</dl>
</td>
</tr>
</table>