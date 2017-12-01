---
UID: NS.hidpi._HIDP_UNKNOWN_TOKEN
title: HIDP_UNKNOWN_TOKEN
author: windows-driver-content
description: The HIDP_UNKNOWN_TOKEN structure contains information about a global item that the HID parser did not recognize.
old-location: hid\hidp_unknown_token.htm
old-project: hid
ms.assetid: 6c9e0477-1698-41bf-9ce6-43e7e8741425
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: HIDP_UNKNOWN_TOKEN, HIDP_UNKNOWN_TOKEN, *PHIDP_UNKNOWN_TOKEN
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: hidpi.h
req.include-header: Hidpi.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: HIDP_UNKNOWN_TOKEN
req.alt-loc: hidpi.h
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

# HIDP_UNKNOWN_TOKEN structure



## -description
<p>The HIDP_UNKNOWN_TOKEN structure contains information about a global item that the HID parser did not recognize.</p>


## -syntax

````
typedef struct _HIDP_UNKNOWN_TOKEN {
  UCHAR Token;
  UCHAR Reserved[3];
  ULONG BitField;
} HIDP_UNKNOWN_TOKEN, *PHIDP_UNKNOWN_TOKEN;
````


## -struct-fields
<dl>

### -field <b>Token</b>

<dd>
<p>Specifies the one-byte prefix of a global item.</p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>Reserved for internal system use.</p>
</dd>

### -field <b>BitField</b>

<dd>
<p>Specifies the data part of the global item.</p>
</dd>
</dl>

## -remarks
<p>HIDP_UNKNOWN_TOKEN is designed to be used with the <a href="..\hidpi\ns-hidpi--hidp-extended-attributes.md">HIDP_EXTENDED_ATTRIBUTES</a> structure. <a href="..\hidpi\nf-hidpi-hidp-getextendedattributes.md">HidP_GetExtendedAttributes</a> returns a HIDP_EXTENDED_ATTRIBUTES structure, which contains a variable length array of <b>HIDP_UNKNOWN_TOKEN</b> structures.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Hidpi.h (include Hidpi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\hidpi\ns-hidpi--hidp-extended-attributes.md">HIDP_EXTENDED_ATTRIBUTES</a>
</dt>
<dt>
<a href="..\hidpi\nf-hidpi-hidp-getextendedattributes.md">HidP_GetExtendedAttributes</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [hid\hid]:%20HIDP_UNKNOWN_TOKEN structure%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
