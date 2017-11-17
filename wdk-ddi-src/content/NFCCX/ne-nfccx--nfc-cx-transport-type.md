---
UID: NE.nfccx._NFC_CX_TRANSPORT_TYPE
title: NFC_CX_TRANSPORT_TYPE
author: windows-driver-content
description: The NFC_CX_TRANSPORT_TYPE enumeration specifies transport types.
old-location: nfpdrivers\nfc_cx_transport_type.htm
ms.assetid: CC8BEC9A-87F6-4C50-A8FA-ED2A2A5D2934
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: nfpdrivers
req.header: nfccx.h
req.include-header: Ncidef.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: None supported
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NFC_CX_TRANSPORT_TYPE, *PNFC_CX_TRANSPORT_TYPE
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
ms.keywords: NPI_REGISTRATION_INSTANCE, NPI_REGISTRATION_INSTANCE
req.iface: 
---

# NFC_CX_TRANSPORT_TYPE enumeration



## -description
<p>The NFC_CX_TRANSPORT_TYPE enumeration specifies transport types.</p>


## -syntax

````
typedef enum _NFC_CX_TRANSPORT_TYPE { 
  NFC_CX_TRANSPORT_I2C     = 0x00,
  NFC_CX_TRANSPORT_SPI     = 0x01,
  NFC_CX_TRANSPORT_UART    = 0x02,
  NFC_CX_TRANSPORT_CUSTOM  = 0xFF
} NFC_CX_TRANSPORT_TYPE, *PNFC_CX_TRANSPORT_TYPE;
````


## -enum-fields
<dl>

### -field <a id="NFC_CX_TRANSPORT_I2C"></a><a id="nfc_cx_transport_i2c"></a><b>NFC_CX_TRANSPORT_I2C</b>

<dd>
<p>Specifies an Inter-Integrated Circuit (I2C) bus.</p>
</dd>

### -field <a id="NFC_CX_TRANSPORT_SPI"></a><a id="nfc_cx_transport_spi"></a><b>NFC_CX_TRANSPORT_SPI</b>

<dd>
<p>Specifies a Serial Peripheral Interface (SPI).</p>
</dd>

### -field <a id="NFC_CX_TRANSPORT_UART"></a><a id="nfc_cx_transport_uart"></a><b>NFC_CX_TRANSPORT_UART</b>

<dd>
<p>Specifies a Universal Asynchronous Receiver/Transmitter (UART).</p>
</dd>

### -field <a id="NFC_CX_TRANSPORT_CUSTOM"></a><a id="nfc_cx_transport_custom"></a><b>NFC_CX_TRANSPORT_CUSTOM</b>

<dd>
<p>Specifies a custom transport type.</p>
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
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [nfpdrivers\nfpdrivers]:%20NFC_CX_TRANSPORT_TYPE enumeration%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
