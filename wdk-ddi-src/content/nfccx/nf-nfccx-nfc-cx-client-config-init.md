---
UID: NF.nfccx.NFC_CX_CLIENT_CONFIG_INIT
title: NFC_CX_CLIENT_CONFIG_INIT
author: windows-driver-content
description: The NFC_CX_CLIENT_CONFIG_INIT function initializes the NFC_CX_CLIENT_CONFIG structure.
old-location: nfpdrivers\nfc_cx_client_config_init.htm
old-project: nfpdrivers
ms.assetid: 0679406E-091D-4E66-956A-54E3A517BF4C
ms.author: windowsdriverdev
ms.date: 11/27/2017
ms.keywords: NFC_CX_CLIENT_CONFIG_INIT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: nfccx.h
req.include-header: Ncidef.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NFC_CX_CLIENT_CONFIG_INIT
req.alt-loc: nfccxstub.lib,nfccxstub.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Nfccxstub.lib
req.dll: 
req.irql: 
req.iface: 
---

# NFC_CX_CLIENT_CONFIG_INIT function



## -description
<p>The <b>NFC_CX_CLIENT_CONFIG_INIT</b> function initializes the <a href="..\nfccx\ns-nfccx--nfc-cx-client-config.md">NFC_CX_CLIENT_CONFIG</a> structure.</p>


## -syntax

````
FORCEINLINE VOID  NFC_CX_CLIENT_CONFIG_INIT(
  _Out_ PNFC_CX_CLIENT_CONFIG Config,
  _In_  NFC_CX_TRANSPORT_TYPE BusType
);
````


## -parameters
<dl>

### -param <i>Config</i> [out]

<dd>
<p>A pointer to an <a href="..\nfccx\ns-nfccx--nfc-cx-client-config.md">NFC_CX_CLIENT_CONFIG</a> structure. </p>
</dd>

### -param <i>BusType</i> [in]

<dd>
<p>An <a href="..\nfccx\ne-nfccx--nfc-cx-transport-type.md">NFC_CX_TRANSPORT_TYPE</a> enumeration. </p>
</dd>
</dl>

## -returns
<p>This function does not return a value.</p>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
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
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Nfccxstub.lib</dt>
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
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [nfpdrivers\nfpdrivers]:%20NFC_CX_CLIENT_CONFIG_INIT function%20 RELEASE:%20(11/27/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
