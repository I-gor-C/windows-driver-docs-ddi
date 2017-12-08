---
UID: NE.nfccx._NFC_CX_DEVICE_MODE
title: NFC_CX_DEVICE_MODE
author: windows-driver-content
description: Specifies device mode flags.
old-location: nfpdrivers\nfc_cx_device_mode.htm
old-project: nfpdrivers
ms.assetid: B9996339-984D-4F6B-BFE9-2F536EC75924
ms.author: windowsdriverdev
ms.date: 11/27/2017
ms.keywords: NPI_REGISTRATION_INSTANCE, NPI_REGISTRATION_INSTANCE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: nfccx.h
req.include-header: Ncidef.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: None supported
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NFC_CX_DEVICE_MODE
req.alt-loc: nfccx.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: Requires same
req.iface: 
---

# NFC_CX_DEVICE_MODE enumeration



## -description
<p>Specifies device mode flags.</p>


## -syntax

````
typedef enum _NFC_CX_DEVICE_MODE { 
  NFC_CX_DEVICE_MODE_NCI  = 0x00000000,
  NFC_CX_DEVICE_MODE_DTA  = 0x00000001,
  NFC_CX_DEVICE_MODE_RAW  = 0x00000002
} NFC_CX_DEVICE_MODE;
````


## -enum-fields
<dl>

### -field NFC_CX_DEVICE_MODE_NCI

<dd>
<p>Enable NCI mode.</p>
</dd>

### -field NFC_CX_DEVICE_MODE_DTA

<dd>
<p>Enable DTA mode.</p>
</dd>

### -field NFC_CX_DEVICE_MODE_RAW

<dd>
<p>Enable RAW mode.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 10</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>None supported</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Nfccx.h (include Ncidef.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?LinkID=785320">Near field communication (NFC) design guide</a></dt>
<dt><a href="https://msdn.microsoft.com/windows/hardware/drivers/nfc/nfc-class-extension-">NFC class extension design guide</a></dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [nfpdrivers\nfpdrivers]:%20NFC_CX_DEVICE_MODE enumeration%20 RELEASE:%20(11/27/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
