---
UID: NS.dxva._DXVA_EncryptProtocolHeader
title: DXVA_EncryptProtocolHeader
author: windows-driver-content
description: The DXVA_EncryptProtocolHeader structure is sent by the host decoder to the accelerator to indicate use of an encryption protocol.
old-location: display\dxva_encryptprotocolheader.htm
ms.assetid: 924da940-f609-4302-b454-87243200808e
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: dxva.h
req.include-header: Dxva.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXVA_EncryptProtocolHeader
req.alt-loc: dxva.h
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
ms.keywords: DXVA_EncryptProtocolHeader, DXVA_EncryptProtocolHeader, *LPDXVA_EncryptProtocolHeader
req.iface: 
---

# DXVA_EncryptProtocolHeader structure



## -description
<p>The DXVA_EncryptProtocolHeader structure is sent by the host decoder to the accelerator to indicate use of an encryption protocol.</p>


## -syntax

````
typedef struct _DXVA_EncryptProtocolHeader {
  DXVA_EncryptProtocolFunc dwFunction;
  DWORD                    ReservedBits[3];
  GUID                     guidEncryptProtocol;
} DXVA_EncryptProtocolHeader, *LPDXVA_EncryptProtocolHeader;
````


## -struct-fields
<dl>

### -field <b>dwFunction</b>

<dd>
<p>Indicates whether encryption is being used and the operation to which encryption applies. The 24 most significant bits of <b>dwFunction</b> indicate that an encryption protocol is being used. These bits must be 0xFFFF00 when sent by the host software decoder, and 0xFFFF08 when sent by the accelerator. The 8 least significant bits of <b>dwFunction</b> contain a <a href="https://msdn.microsoft.com/6db9fa71-7bc2-4eb6-afcb-b16df48f7e8b">bDXVA_Func</a> variable that indicates the operation to which the encryption protocol applies. Currently, the only relevant defined value of <i>bDXVA_Func</i> for use in these bits is 1, which indicates that the encryption protocol applies to compressed picture decoding.</p>
<p>There are only two possible values for <b>dwFunction</b> in this structure: 0xFFFF0001 when sent by a host software decoder, and 0xFFFF0801 when sent by the hardware accelerator.</p>
</dd>

### -field <b>ReservedBits</b>

<dd>
<p>Reserved bits used for packing and alignment. This must be zero.</p>
</dd>

### -field <b>guidEncryptProtocol</b>

<dd>
<p>Contains the GUID associated with the encryption protocol.</p>
</dd>
</dl>

## -remarks
<p>The encryption protocol in use is externally defined and operates as described in <a href="https://msdn.microsoft.com/d5ce9c02-7126-4775-bb87-dae45b93b652">Encryption Support</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Dxva.h (include Dxva.h)</dt>
</dl>
</td>
</tr>
</table>